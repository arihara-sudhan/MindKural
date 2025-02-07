import json

with open("input.json", "r", encoding="utf-8") as ip_file:
    ip_data = json.load(ip_file)

with open("corpus.json", "r", encoding="utf-8") as corpus_file:
    corpus_data = json.load(corpus_file)

vilakkam_map = {int(item["kural"]): item["vilakkam"] for item in ip_data}

for kural in corpus_data["kural"]:
    kural.pop("sp", None)
    number = kural["Number"]
    if number in vilakkam_map:
        kural["ari"] = vilakkam_map[number]

with open("corpus.json", "w", encoding="utf-8") as corpus_file:
    json.dump(corpus_data, corpus_file, ensure_ascii=False, indent=2)

print("MOVED!")
