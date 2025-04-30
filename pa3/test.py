from rag import ask_question, ask_question_with_context
from helper import Helper

helper = Helper()
config = helper.get_config()
similarity_metric = config['MODEL']['SIMILARITY_METRIC']
model_name = config['MODEL']['LANGUAGE_MODEL']
context_size = config['MODEL']['CONTEXT_SIZE']

with open("test_questions.txt", "r") as file:
    questions = file.read().split("\n")

with open("test_answers.txt", "a") as file:
    file.write(f"Language model: {model_name}\n")
    file.write(f"Context size: {context_size}\n\n")
    file.write("No context:\n")
    for q in questions:
        answer = ask_question(q)
        file.write(answer + "\n")
    file.write("\n")
    file.write("With context:")
    for q in questions:
        answer = ask_question_with_context(q)
        file.write(answer + "\n")
    file.write("\n-----------------------------\n")