import psycopg2
from threading import Lock
from transformers import AutoTokenizer, AutoModel
import torch
from sentence_transformers import SentenceTransformer
from helper import Helper
import torch.nn.functional as F
import requests
import re

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

    # query using cosine distance
    def query_db_cosine(self, query, model_name, table_name):
        """
        The query_db_cosine function retrieves the top 5 most similar sentences from a pgvector database based on cosine distance.

        Parameters
        - query (str): The input text query to be searched.
        - model_name (str): The name of the model to be used for encoding the query.
        - table_name (str): The name of the table containing the stored sentence embeddings
        """
        if model_name == 'labse':
            model = SentenceTransformer('sentence-transformers/LaBSE')
            query_embedding = model.encode(query).tolist()
        elif model_name in ['sloberta', 'openai']:
            if model_name == 'sloberta':
                model_id = 'EMBEDDIA/sloberta'
            else:
                model_id = 'Xenova/text-embedding-ada-002'

            tokenizer = AutoTokenizer.from_pretrained(model_id)
            model = AutoModel.from_pretrained(model_id)

            inputs = tokenizer(query, return_tensors="pt", truncation=True, padding=True, max_length=512)
            with torch.no_grad():
                outputs = model(**inputs)

            token_embeddings = outputs.last_hidden_state
            attention_mask = inputs['attention_mask'].unsqueeze(-1).expand(token_embeddings.size()).float()

            sum_embeddings = torch.sum(token_embeddings * attention_mask, dim=1)
            sum_mask = attention_mask.sum(dim=1)
            mean_embeddings = sum_embeddings / sum_mask

            # Normalize only if you're storing normalized vectors in DB
            query_embedding = F.normalize(mean_embeddings, p=2, dim=1)[0].tolist()

        else:
            raise ValueError(f"Unsupported model type: {model_name}")

        cur = self.conn.cursor()
        # execute the query to fetch the top 5 most similar sentences based on cosine distance
        cur.execute(
            'SELECT page_id, page_segment, 1 - (embedding <=> %s::vector) AS similarity '
            'FROM ' + table_name + ' ORDER BY similarity DESC LIMIT 5',
            (query_embedding,)  # pass the embedding twice, once for ordering and once for calculation
        )
        result = cur.fetchall()
        cur.close()
        return result
