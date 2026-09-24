# -*- coding: utf-8 -*-
"""
Analysis of the 35 items in psych_part2.json
Indices: 35, 37, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 57, 58, 59, 61, 62, 63, 65, 66, 67, 69, 70, 71, 73, 74, 75, 76
Total: 35 items
"""

import json

# Let's inspect each item's q_text, choices c1..c5, and ans index
with open('psych_part2.json', encoding='utf-8') as f:
    d = json.load(f)

for k in d:
    item = d[k]
    ans_idx = int(item['ans'])
    choices = [item['c1'], item['c2'], item['c3'], item['c4'], item['c5']]
    print(f"Key: {k}, AnsIdx: {ans_idx}")
    print(f"  Ans text: {choices[ans_idx-1]}")
    for i, c in enumerate(choices, 1):
        letter = ['ก', 'ข', 'ค', 'ง', 'จ'][i-1]
        is_ans = " [CORRECT]" if i == ans_idx else ""
        print(f"  {letter}: {c[:60]}{is_ans}")
    print()
