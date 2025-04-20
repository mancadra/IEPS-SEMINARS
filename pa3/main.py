# main.py

from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
import uvicorn
from pathlib import Path
from rag import ask_question, ask_question_with_context

app = FastAPI()

class QuestionRequest(BaseModel):
    question: str
    use_rag: bool

class AnswerResponse(BaseModel):
    answer: str

@app.post("/question", response_model=AnswerResponse)
async def answer_question(request: QuestionRequest):
    if request.use_rag:
        answer = ask_question_with_context(question=request.question)
    else:
        answer = ask_question(question=request.question)
    return AnswerResponse(answer=answer)

@app.get("/", response_class=HTMLResponse)
async def get_form():
    html_path = Path("templates/index.html")
    return HTMLResponse(content=html_path.read_text(), status_code=200)

if __name__ == "__main__":
    uvicorn.run("main:app", host="127.0.0.1", port=8000, reload=True)

