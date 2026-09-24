import openpyxl
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['4. Endocrine']
rows = list(ws.iter_rows(values_only=True))

def clean_text(s):
    if not s:
        return ""
    s = str(s).replace('**', '').replace('*', '').replace('_x001E_', '')
    s = s.replace('เชื%อ', 'เชื้อ').replace('ขึ%น', 'ขึ้น').replace('นี%', 'นี้')
    return s.strip()

items = []
template_indices = []

for idx, r in enumerate(rows[2:], 3):
    if not any(x is not None for x in r):
        continue
    q_no = r[0]
    q_text = clean_text(r[1])
    q_img = r[2]
    c1 = clean_text(r[3])
    c2 = clean_text(r[4])
    c3 = clean_text(r[5])
    c4 = clean_text(r[6])
    c5 = clean_text(r[7])
    ans = r[8]
    exp = clean_text(r[9])
    exp_img = r[10]
    subtopic = clean_text(r[11]) if len(r) > 11 and r[11] else 'Diabetes mellitus'
    cat = clean_text(r[12]) if len(r) > 12 and r[12] else 'Clinic'
    note = clean_text(r[13]) if len(r) > 13 and r[13] else ''
    q_type = clean_text(r[14]) if len(r) > 14 and r[14] else ''
    exam_year = clean_text(r[15]) if len(r) > 15 and r[15] else ''

    item = {
        'row_idx': idx,
        'q_no': q_no,
        'q_text': q_text,
        'q_img': q_img,
        'c1': c1,
        'c2': c2,
        'c3': c3,
        'c4': c4,
        'c5': c5,
        'ans': ans,
        'exp': exp,
        'exp_img': exp_img,
        'subtopic': subtopic,
        'cat': cat,
        'note': note,
        'q_type': q_type,
        'exam_year': exam_year
    }
    items.append(item)
    
    if any(k in exp for k in ['ไม่ใช่คำตอบที่ถูกต้องสำหรับภาวะ', 'ไม่ใช่คำตอบที่ถูกต้อง', 'ไม่ตรงกับบริบท', 'ไม่ถูกต้องตามหลักการรักษา']):
        template_indices.append(len(items) - 1)

print(f"Total extracted endocrine items: {len(items)}")
print(f"Total items needing distractor overhaul: {len(template_indices)}")

# Split template items into 4 batches for subagents
batch_size = (len(template_indices) + 3) // 4
for b in range(4):
    b_indices = template_indices[b*batch_size : (b+1)*batch_size]
    b_items = []
    for idx_in_items in b_indices:
        it = items[idx_in_items]
        b_items.append({
            'endo_idx': idx_in_items,
            'row_idx': it['row_idx'],
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
    with open(f'endo_part{b+1}.json', 'w', encoding='utf-8') as f:
        json.dump(b_items, f, ensure_ascii=False, indent=2)
    print(f"Batch {b+1}: {len(b_items)} items saved to endo_part{b+1}.json")

with open('endocrine_base_items.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Saved endocrine_base_items.json")
