import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('pulmo_part2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k, v in data.items():
    first_exp = v.get('exp', '').split('\n')[0]
    note = v.get('note', '')
    ans = v.get('ans')
    print(f"[{k}] ans={ans} | note={note} | {first_exp}")
