import psycopg2
from transformers import AutoTokenizer, AutoModel, DistilBertTokenizer, DistilBertModel
from sentence_transformers import SentenceTransformer
from helper import Helper
import embeddings

helper = Helper()
config = helper.get_config()

class DbHandler:
    def __init__(self, dbname=config['DATABASE']['DB_NAME'], user=config['DATABASE']['USER'], password=config['DATABASE']['PASSWORD'], host=config['DATABASE']['HOST'], port=config['DATABASE']['PORT']):
        self.conn_details = {
            'dbname': dbname,
            'user': user,
            'password': password,
            'host': host,
            'port': port,
        }
        self.conn = psycopg2.connect(**self.conn_details)
        self.conn.autocommit = True


    def get_html_content(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT html_content FROM crawldb.page WHERE id=%s", (id,))
        result = cur.fetchone()
        if result is None: return result
        else: return result[0]


    def get_url(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT url FROM crawldb.page WHERE id=%s", (id,))
        result = cur.fetchone()
        if result is None: return result
        else: return result[0]

    
    def update_cleaned_content(self, page_id, cleaned_content):
        """Update the database with cleaned content"""
        cur = self.conn.cursor()
        cur.execute("""
            UPDATE crawldb.page 
            SET cleaned_content = %s 
            WHERE id = %s
            """, (cleaned_content, page_id))
        self.conn.commit()
        return cur.rowcount


    def get_cleaned_content(self, id):
        cur = self.conn.cursor()
        cur.execute("SELECT cleaned_content FROM crawldb.page WHERE id=%s", (id,))
        result = cur.fetchone()
        if result is None: return result
        else: return result[0]


    def clear_page_segment(self):
        cur = self.conn.cursor()
        cur.execute("TRUNCATE TABLE crawldb.page_segment RESTART IDENTITY CASCADE;")


    def insert_page_segment(self, page_id, page_segment, embedding):
        cur = self.conn.cursor()
        cur.execute("""
            INSERT INTO crawldb.page_segment 
            (page_id, page_segment, embedding) 
            VALUES (%s, %s, %s)
            """, (page_id, page_segment, embedding))
        self.conn.commit()
        return cur.rowcount


    def create_segment_index(self):
        cur = self.conn.cursor()
        cur.execute('CREATE INDEX ON crawldb.page_segment USING hnsw (embedding vector_cosine_ops) WITH (m = 16, ef_construction = 64);')


    def query_similarity(self, query, table_name, similarity_metric):
        """
        The query_similarity function retrieves the top 5 most similar segments, and their page_id from a pgvector database based on a given similarity_metric.

        Parameters
        - query (str): The input text query to be searched.
        - table_name (str): The name of the table containing the stored sentence embeddings
        - similarity metric (str): The name of the used metric to calculate the similarity with
        """
        model_name = config['MODEL']['MODEL_NAME']
        if model_name == 'labse':
            model = SentenceTransformer('sentence-transformers/LaBSE')
            query_embedding = model.encode(query).tolist()
        elif model_name == 'distilbert':
            model_id = 'distilbert-base-uncased'
            tokenizer = DistilBertTokenizer.from_pretrained(model_id)
            model = DistilBertModel.from_pretrained(model_id)
            query_embedding = embeddings.calculate_embedding(model, tokenizer, query)
        elif model_name in ['sloberta', 'openai', 'croslo']:
            if model_name == 'sloberta':
                model_id = 'EMBEDDIA/sloberta'
            elif model_name == 'croslo':
                model_id = 'EMBEDDIA/crosloengual-bert'
            else:
                model_id = 'Xenova/text-embedding-ada-002'

            tokenizer = AutoTokenizer.from_pretrained(model_id)
            model = AutoModel.from_pretrained(model_id)
            query_embedding = embeddings.calculate_embedding(model, tokenizer, query)
        else:
            raise ValueError(f"Unsupported model type: {model_name}")

        metric_ops = {
            'cosine': ('<=>', '1 - (embedding %s %s::vector)'),
            'L1': ('<->', '-1 * (embedding %s %s::vector)'),
            'inner_product': ('<#>', '(embedding %s %s::vector) * -1')
        }

        op, template = metric_ops[similarity_metric]
        similarity_expr = template % (op, '%s')

        # Execute query
        with self.conn.cursor() as cur:
            cur.execute(
                f'SELECT page_id, page_segment, {similarity_expr} AS similarity '
                f'FROM {table_name} ORDER BY similarity DESC LIMIT 5',
                (query_embedding,)
            )
            return cur.fetchall()
