import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['2. Cardiovascular']
rows = list(ws.iter_rows(values_only=True))

print("=== Scanning 2. Cardiovascular for Real vs Corrupted Rows ===")
real_count = 0
corrupted_count = 0

for i, r in enumerate(rows[2:], 3):
    if not any(x is not None for x in r):
        continue
    q_no = r[0]
    q_text = str(r[1]) if r[1] else ''
    c1 = str(r[3]) if r[3] else ''
    c2 = str(r[4]) if r[4] else ''
    
    # Check dummy repetitive pattern like C1='Diltiazem 30 mg TID' or 'Amlodipine 5 mg OD'
    is_corrupted = False
    if c1 in ['Diltiazem 30 mg TID', 'Amlodipine 5 mg OD', 'Hydrochlorothiazide 25 mg OD', 'Bisoprolol 5 mg OD', 'Aspirin 81 mg OD']:
        if len(q_text) < 30 or any(w in q_text.lower() for w in ['thala', 'isolator', 'amitiptyline', 'สิว', 'micromoles', 'metformin', 'furosemide']):
            is_corrupted = True
    
    if is_corrupted:
        corrupted_count += 1
    else:
        real_count += 1

print(f"Total non-empty rows: {real_count + corrupted_count}")
print(f"Likely Real Questions: {real_count}")
print(f"Corrupted/Dummy Rows: {corrupted_count}")
