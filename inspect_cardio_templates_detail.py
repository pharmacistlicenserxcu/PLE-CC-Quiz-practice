import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['2. Cardiovascular']
rows = list(ws.iter_rows(values_only=True))

valid_rows = []
for idx, r in enumerate(rows[2:], 3):
    if not any(x is not None for x in r):
        continue
    c1 = str(r[3]) if r[3] else ''
    c2 = str(r[4]) if r[4] else ''
    q_text = str(r[1]) if r[1] else ''
    
    if c1 in ['Diltiazem 30 mg TID', 'Amlodipine 5 mg OD', 'Hydrochlorothiazide 25 mg OD', 'Bisoprolol 5 mg OD', 'Aspirin 81 mg OD'] and \
       c2 in ['Warfarin 3 mg OD (target INR 2-3)', 'Losartan 50 mg OD', 'Atorvastatin 20 mg OD', 'Spironolactone 25 mg OD', 'Sacubitril/Valsartan 49/51 mg BID']:
        continue
    if len(q_text.strip()) < 10 and not any(k in q_text.lower() for k in ['bp', 'hr', 'ecg', 'ckd', 'htn']):
        continue
    valid_rows.append((idx, r))

# Collect rows with templates
template_items = []
for orig_idx, r in valid_rows:
    exp = str(r[9]) if len(r) > 9 and r[9] else ''
    if any(k in exp for k in ['ไม่ใช่คำตอบที่ถูกต้องสำหรับภาวะ', 'ไม่ใช่คำตอบที่ถูกต้อง', 'ไม่ตรงกับบริบท', 'ไม่ถูกต้องตามหลักการรักษา']):
        template_items.append((orig_idx, r[0], str(r[1])[:80], r[3], r[4], r[5], r[6], r[7], r[8], r[11], r[15]))

print(f"Total template items to rewrite: {len(template_items)}")
for t in template_items[:5]:
    print(f"\nRow {t[0]} (Q{t[1]}): {t[2]}")
    print(f"  C1: {t[3]} | C2: {t[4]} | C3: {t[5]} | C4: {t[6]} | C5: {t[7]}")
    print(f"  Ans: {t[8]} | Subtopic: {t[9]} | Source: {t[10]}")
