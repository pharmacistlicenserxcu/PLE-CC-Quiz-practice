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
    
    # Filter corrupted
    if c1 in ['Diltiazem 30 mg TID', 'Amlodipine 5 mg OD', 'Hydrochlorothiazide 25 mg OD', 'Bisoprolol 5 mg OD', 'Aspirin 81 mg OD'] and \
       c2 in ['Warfarin 3 mg OD (target INR 2-3)', 'Losartan 50 mg OD', 'Atorvastatin 20 mg OD', 'Spironolactone 25 mg OD', 'Sacubitril/Valsartan 49/51 mg BID']:
        continue
    if len(q_text.strip()) < 10 and not any(k in q_text.lower() for k in ['bp', 'hr', 'ecg', 'ckd', 'htn']):
        continue
    valid_rows.append(r)

print(f"Total valid Cardio rows: {len(valid_rows)}")

# Check subtopics and sources
subtopics = {}
sources = {}
templates = 0
asterisks = 0

for r in valid_rows:
    st = str(r[11]) if r[11] else 'Uncategorized'
    src = str(r[15]) if len(r) > 15 and r[15] else 'Unknown'
    subtopics[st] = subtopics.get(st, 0) + 1
    sources[src] = sources.get(src, 0) + 1
    exp = str(r[9]) if len(r) > 9 and r[9] else ''
    if '**' in exp or '*' in exp:
        asterisks += 1
    if any(k in exp for k in ['ไม่ใช่คำตอบที่ถูกต้องสำหรับภาวะ', 'ไม่ใช่คำตอบที่ถูกต้อง', 'ไม่ตรงกับบริบท', 'ไม่ถูกต้องตามหลักการรักษา']):
        templates += 1

print("\nSubtopics breakdown:")
for st, count in sorted(subtopics.items(), key=lambda x: -x[1])[:10]:
    print(f"  - {st}: {count}")

print("\nSources breakdown:")
for src, count in sorted(sources.items(), key=lambda x: -x[1])[:10]:
    print(f"  - {src}: {count}")

print(f"\nQuality stats: Asterisks = {asterisks}, Templates needing rewrite = {templates}")
