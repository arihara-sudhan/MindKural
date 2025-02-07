import json

def read_corpus(file_path="corpus.json"):
    with open(file_path, 'r', encoding="utf-8") as file:
        data = json.load(file)
    return [f"{kural['Number']}. {kural['Translation']}" for kural in data["kural"]]