import json
import sys

with open('psych_part2.json', encoding='utf-8') as f:
    d = json.load(f)

for k, v in d.items():
    print(f"KEY: {k} | ANS: {v['ans']}")
    print(f"  Q: {v['q_text'][:120]}")
    print(f"  c1: {v['c1']}")
    print(f"  c2: {v['c2']}")
    print(f"  c3: {v['c3']}")
    print(f"  c4: {v['c4']}")
    print(f"  c5: {v['c5']}")
    print()
