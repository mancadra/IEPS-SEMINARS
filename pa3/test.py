from rag import ask_question, ask_question_with_context
from helper import Helper
from pathvalidate import sanitize_filename
import zlib

helper = Helper()
config = helper.get_config()
similarity_metric = config['MODEL']['SIMILARITY_METRIC']
model_name = config['MODEL']['LANGUAGE_MODEL']
context_size = config['MODEL']['CONTEXT_SIZE']

with open("test_questions4.txt", "r", encoding="utf8") as file:
    text = file.read()
    questions = text.split("\n")
    questions = list(filter(lambda x : (not ('#' in x)) and x != "", questions))
    hash = zlib.crc32(text.encode('utf-8'))

filename = sanitize_filename(f"{model_name}_{context_size}c_{abs(hash % 10**5)}.txt")

with open(filename, "a", encoding="utf8") as file:
    file.write(f"Language model: {model_name}\n")
    file.write(f"Context size: {context_size}\n")
    
    for q in questions:
        file.write("\n- - - - - - - - - - - - - - -\n")
        file.write(f"Question: {q}\n\n")
        answer = ask_question(q)
        file.write("No context:\n" + answer + "\n\n")
        answer = ask_question_with_context(q)
        file.write("With context:\n" + answer + "\n\n")

    file.write("\n")
    file.write("\n-----------------------------\n")
