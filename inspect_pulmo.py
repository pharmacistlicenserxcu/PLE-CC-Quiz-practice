import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('pulmo_part2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k, v in data.items():
    ans = v.get('ans')
    q = v.get('q_text', '').replace('\n', ' ')[:90]
    print(f"ID {k} | Ans: {ans} | Q: {q}")
    for i in range(1, 6):
        c_val = v.get(f'c{i}')
        if c_val:
            print(f"  c{i}: {c_val}")
