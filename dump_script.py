import json

data = json.load(open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\derm_part1.json', encoding='utf-8'))
with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\questions_dump.txt', 'w', encoding='utf-8') as f:
    for k, v in data.items():
        idx_val = v.get("idx")
        ans_val = v.get("ans")
        note_val = v.get("note")
        q_val = v.get("q_text")
        f.write(f"=== KEY: {k} | idx: {idx_val} | ans: {ans_val} | note: {note_val} ===\n")
        f.write(f"Q: {q_val}\n")
        for opt in ['c1', 'c2', 'c3', 'c4', 'c5']:
            f.write(f"  {opt}: {v.get(opt)}\n")
        f.write("\n")
print("Dumped successfully")
