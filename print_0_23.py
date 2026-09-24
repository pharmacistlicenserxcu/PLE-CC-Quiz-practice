import json
import sys

sys.stdout.reconfigure(encoding='utf-8')

with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\hemato_part1.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

for k in range(24):
    v = data[str(k)]
    print(f"KEY {k}: ans {v['ans']} | Q: {v['q_text'][:60].replace(chr(10), ' ')}")
    lines = v.get('exp', '').split('\n')
    print("  AnsLine:", lines[0] if lines else '')
    for l_idx, l in enumerate(lines):
        if 'ทำไมข้อนี้ถึงถูก' in l and l_idx+1 < len(lines):
            print("  Why:", lines[l_idx+1][:100])
