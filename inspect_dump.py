import json

with open('dump.json', 'r') as f:
    data = json.load(f)

for item in data[:5]:
    print("---")
    print("Filename:", item["original_file"])
    print("Slug:", item["slug"])
    print(item["text"][:300]) # first 300 chars
