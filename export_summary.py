import json

with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\gi_part1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\q_summary.txt', 'w', encoding='utf-8') as f:
    for k, v in data.items():
        f.write(f"=== ID: {k} | idx: {v.get('idx')} | ans: {v.get('ans')} | topic: {v.get('subtopic')} ===\n")
        f.write(f"Q: {v.get('q_text')}\n")
        f.write(f"ก: {v.get('c1')}\n")
        f.write(f"ข: {v.get('c2')}\n")
        f.write(f"ค: {v.get('c3')}\n")
        f.write(f"ง: {v.get('c4')}\n")
        f.write(f"จ: {v.get('c5')}\n")
        f.write(f"Current exp: {v.get('exp')[:150]}...\n\n")

print("Done exporting summary")
