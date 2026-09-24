import openpyxl
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['2. Cardiovascular']
rows = list(ws.iter_rows(values_only=True))

# Header is row 2 (index 1)
headers = rows[1]

# Let's inspect all non-empty rows and categorize
valid_rows = []
corrupted_rows = []

dummy_c1_list = [
    'Diltiazem 30 mg TID', 'Amlodipine 5 mg OD', 'Hydrochlorothiazide 25 mg OD',
    'Bisoprolol 5 mg OD', 'Aspirin 81 mg OD'
]

for idx, r in enumerate(rows[2:], 3):
    if not any(x is not None for x in r):
        continue
    q_no = r[0]
    q_text = str(r[1]) if r[1] else ''
    c1 = str(r[3]) if r[3] else ''
    c2 = str(r[4]) if r[4] else ''
    c3 = str(r[5]) if r[5] else ''
    c4 = str(r[6]) if r[6] else ''
    c5 = str(r[7]) if r[7] else ''
    ans = r[8]
    exp = str(r[9]) if r[9] else ''
    subtopic = str(r[11]) if r[11] else ''
    source = str(r[15]) if len(r) > 15 and r[15] else ''

    # Check if corrupted
    # Characteristics of corrupted rows:
    # 1. C1 is one of the repeated dummy strings AND Q is fragmented or belongs to other topics
    # 2. Or Q text is obviously a choice fragment like 'amitiptyline', 'เพิ่ม amlodipine', '200 micromoles per litre' with dummy C1-C5
    is_corrupted = False
    if c1 in dummy_c1_list and c2 in ['Warfarin 3 mg OD (target INR 2-3)', 'Losartan 50 mg OD', 'Atorvastatin 20 mg OD', 'Spironolactone 25 mg OD', 'Sacubitril/Valsartan 49/51 mg BID']:
        is_corrupted = True
    elif len(q_text.strip()) < 10 and not any(k in q_text.lower() for k in ['bp', 'hr', 'ecg', 'ckd', 'htn']):
        is_corrupted = True

    if is_corrupted:
        corrupted_rows.append((idx, q_no, q_text[:60], c1[:30]))
    else:
        valid_rows.append((idx, r))

print(f"Total rows inspected: {len(rows)-2}")
print(f"Valid questions: {len(valid_rows)}")
print(f"Corrupted rows identified: {len(corrupted_rows)}")
print("\nSample corrupted rows (first 10):")
for cr in corrupted_rows[:10]:
    print(f"Row {cr[0]}: Q{cr[1]} | Q: {cr[2]} | C1: {cr[3]}")
print("\nSample corrupted rows (last 10):")
for cr in corrupted_rows[-10:]:
    print(f"Row {cr[0]}: Q{cr[1]} | Q: {cr[2]} | C1: {cr[3]}")
