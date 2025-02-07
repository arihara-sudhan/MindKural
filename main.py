from fastapi import FastAPI, WebSocket
from fastapi.middleware.cors import CORSMiddleware
import json
from utils.langchain_setup import get_qa_chain
from pydantic import BaseModel
import re

app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], 
    allow_credentials=True,
    allow_methods=["*"], 
    allow_headers=["*"],
)

qa_chain = get_qa_chain()
class QuestionRequest(BaseModel):
    question: str
    chat_history: list

def extract_matches(numbers):
    if not numbers:
        return []
    with open("data/corpus.json", "r", encoding="utf-8") as kural_file:
        data = json.load(kural_file)

    matches = [
        [kural["Line1"], kural["Line2"], kural["ari"]]
        for kural in data["kural"] if kural["Number"] in numbers
    ]
    return matches

def extract_numbers(response):
    match = re.search(r"Kural:\s*(\d+)", response)
    if match:
        numbers = [
            int(n.strip()) for n in match.group(1).split(',') 
            if n.strip().isdigit()
        ]
        return numbers
    return []

@app.post("/ask/")
async def ask_question(request: QuestionRequest):
    question = request.question
    chat_history = request.chat_history
    response = qa_chain({"question": question, "chat_history": chat_history})
    numbers = extract_numbers(response["answer"])
    matches = extract_matches(numbers)
    answer = response["answer"].strip()
    print(answer, "ANSWER")
    return {"answer": answer, "matches": matches}
