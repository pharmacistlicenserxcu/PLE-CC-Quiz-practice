import json
import sys

with open('psych_part2.json', encoding='utf-8') as f:
    data = json.load(f)

with open('summary_part2.txt', 'w', encoding='utf-8') as out:
    for k, v in data.items():
        out.write(f"=== KEY: {k} (ans: {v.get('ans')}) ===\n")
        out.write(f"Q: {v.get('q_text')}\n")
        out.write(f"c1: {v.get('c1')}\n")
        out.write(f"c2: {v.get('c2')}\n")
        out.write(f"c3: {v.get('c3')}\n")
        out.write(f"c4: {v.get('c4')}\n")
        out.write(f"c5: {v.get('c5')}\n")
        out.write(f"note: {v.get('note')}\n")
        exp = v.get('exp', '')
        first_few = '\n'.join(exp.split('\n')[:8])
        out.write(f"exp_start:\n{first_few}\n")
        out.write("-" * 50 + "\n\n")

print("Done writing summary_part2.txt")
