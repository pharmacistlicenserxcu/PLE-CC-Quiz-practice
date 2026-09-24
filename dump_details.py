import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('pulmo_part2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k, v in data.items():
    print("="*60)
    print(f"ID: {k} | Ans: {v.get('ans')} | Note: {v.get('note')}")
    print(f"Q: {v.get('q_text')}")
    for i in range(1, 6):
        c = v.get(f'c{i}')
        if c:
            print(f"  c{i}: {c}")
    print(f"Exp: {v.get('exp')[:200]}...")
