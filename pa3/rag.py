import dspy

# Integration point for PA2
def query_database(query):
    return "banana"

class RAG(dspy.Module):
    def __init__(self):
        self.respond = dspy.ChainOfThought('context, question -> answer: str')

    def forward(self, question):
        context = query_database(question)
        return self.respond(context=context, question=question)

lm = dspy.LM('ollama_chat/llama3.2:1b', api_base='http://localhost:11434', api_key='')
dspy.configure(lm=lm)

naive_rag = dspy.ChainOfThought('question -> answer: str')
rag = RAG()

def ask_question(question):
    return naive_rag(question=question).answer
    
def ask_question_with_context(question):
    return rag(question=question).answer
