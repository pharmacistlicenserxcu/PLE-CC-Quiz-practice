# -*- coding: utf-8 -*-
import json
import sys

sys.stdout.reconfigure(encoding='utf-8')
with open('pulmo_items_fixed.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for idx in range(71, 80):
    it = items[idx]
    print(f"=== IDX {idx} ===")
    print("Q:", it.get('q_text', ''))
    for i in range(1, 6):
        print(f"  c{i}: {it.get(f'c{i}')}")
    print("Ans:", it.get('ans'))
