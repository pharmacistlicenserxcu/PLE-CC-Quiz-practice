# -*- coding: utf-8 -*-
import sys, io, json, os

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('past_65_bad.json', 'r', encoding='utf-8') as f:
    past = json.load(f)

# Split into 3 parts: 22, 22, 21
p1 = past[:22]
p2 = past[22:44]
p3 = past[44:]

with open('past_part1.json', 'w', encoding='utf-8') as f:
    json.dump(p1, f, ensure_ascii=False, indent=2)

with open('past_part2.json', 'w', encoding='utf-8') as f:
    json.dump(p2, f, ensure_ascii=False, indent=2)

with open('past_part3.json', 'w', encoding='utf-8') as f:
    json.dump(p3, f, ensure_ascii=False, indent=2)

print(f"Past split: {len(p1)}, {len(p2)}, {len(p3)}")

with open('mock_86_for_batch.json', 'r', encoding='utf-8') as f:
    mock = json.load(f)

# Split into 4 parts: 22, 22, 21, 21
m1 = mock[:22]
m2 = mock[22:44]
m3 = mock[44:65]
m4 = mock[65:]

with open('mock_part1.json', 'w', encoding='utf-8') as f:
    json.dump(m1, f, ensure_ascii=False, indent=2)

with open('mock_part2.json', 'w', encoding='utf-8') as f:
    json.dump(m2, f, ensure_ascii=False, indent=2)

with open('mock_part3.json', 'w', encoding='utf-8') as f:
    json.dump(m3, f, ensure_ascii=False, indent=2)

with open('mock_part4.json', 'w', encoding='utf-8') as f:
    json.dump(m4, f, ensure_ascii=False, indent=2)

print(f"Mock split: {len(m1)}, {len(m2)}, {len(m3)}, {len(m4)}")
