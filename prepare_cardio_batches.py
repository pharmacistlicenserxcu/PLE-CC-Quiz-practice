import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('cardio_valid_extracted.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total valid items: {len(items)}")

# Count template items
template_indices = []
for i, item in enumerate(items):
    exp = item['exp']
    if any(k in exp for k in ['ไม่ใช่คำตอบที่ถูกต้องสำหรับภาวะ', 'ไม่ใช่คำตอบที่ถูกต้อง', 'ไม่ตรงกับบริบท', 'ไม่ถูกต้องตามหลักการรักษา']):
        template_indices.append(i)

print(f"Total items needing distractor overhaul: {len(template_indices)}")

# Split into 5 parts for subagents
part_size = (len(template_indices) + 4) // 5
parts = []
for p in range(5):
    idx_slice = template_indices[p*part_size : (p+1)*part_size]
    part_items = []
    for idx in idx_slice:
        it = items[idx]
        part_items.append({
            'cardio_idx': idx,
            'orig_row': it['orig_row'],
            'q_no': it['q_no'],
            'q_text': it['q_text'],
            'c1': it['c1'],
            'c2': it['c2'],
            'c3': it['c3'],
            'c4': it['c4'],
            'c5': it['c5'],
            'ans': it['ans'],
            'subtopic': it['subtopic'],
            'exam_year': it['exam_year']
        })
    parts.append(part_items)
    with open(f'cardio_part{p+1}.json', 'w', encoding='utf-8') as pf:
        json.dump(part_items, pf, ensure_ascii=False, indent=2)
    print(f"Part {p+1}: {len(part_items)} items saved to cardio_part{p+1}.json")
