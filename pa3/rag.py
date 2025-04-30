import dspy
import db_handler
import helper

helper = helper.Helper()
config = helper.get_config()
db = db_handler.DbHandler()
similarity_metric = config['MODEL']['SIMILARITY_METRIC']
model_name = config['MODEL']['LANGUAGE_MODEL']
table_name = 'crawldb.page_segment'

def query_database(query):
    return db.query_similarity(query, table_name, similarity_metric)

class RAG(dspy.Module):
    def __init__(self):
        self.respond = dspy.ChainOfThought('context, question -> answer: str')

    def forward(self, question):
        context = query_database(question)
        return self.respond(context=context, question=question)

lm = dspy.LM(f"ollama_chat/{model_name}", api_base='http://localhost:11434', api_key='')
dspy.configure(lm=lm)

naive_rag = dspy.ChainOfThought('question -> answer: str')
rag = RAG()

def ask_question(question):
    return naive_rag(question=question).answer
    
def ask_question_with_context(question):
    return rag(question=question).answer
