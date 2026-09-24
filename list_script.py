import json

with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\neuro_part2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\all_questions_list.txt', 'w', encoding='utf-8') as out:
    for k in range(32, 62):
        sk = str(k)
        v = data[sk]
        out.write(f"=== {sk} (ans: {v['ans']}) ===\n")
        out.write(f"Q: {v['q_text']}\n")
        for i in range(1, 6):
            out.write(f"  {i}: {v[f'c{i}']}\n")
        out.write("\n")

print("Wrote all_questions_list.txt")
