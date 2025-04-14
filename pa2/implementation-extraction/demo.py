# A demo script that allows us to test the retriever
from db_handler import DbHandler

db = DbHandler()

query = 'r'
model_name = 'sentence-transformers/LaBSE'
table_name = 'crawldb.page_segment'

print(db.query_db_cosine(query, model_name, table_name))