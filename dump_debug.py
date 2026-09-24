import json

with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\hemato_part1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\debug_hemato.txt', 'w', encoding='utf-8') as out:
    for k, v in data.items():
        out.write(f"=== KEY: {k} (idx: {v.get('idx')}) ans: {v.get('ans')} ===\n")
        out.write(f"Q: {v.get('q_text')}\n")
        for i in range(1, 6):
            out.write(f"  c{i}: {v.get(f'c{i}')}\n")
        exp_first = v.get('exp', '').split('\n')[0] if v.get('exp') else ''
        out.write(f"EXP: {exp_first}\n\n")

print("Done writing debug_hemato.txt")
