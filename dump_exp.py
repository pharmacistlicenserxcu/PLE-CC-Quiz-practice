import json

with open('immuno_part2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('dump_exp.txt', 'w', encoding='utf-8') as out:
    for k, q in data.items():
        out.write(f"=== KEY {k}: {q.get('q_text', '')[:60]} ===\n")
        out.write(f"ans: {q.get('ans')}\n")
        out.write(f"exp: {q.get('exp', '')}\n\n")
print("Done writing dump_exp.txt")
