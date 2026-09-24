import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['2. Cardiovascular']
rows = list(ws.iter_rows(values_only=True))

print("=== Checking rows that were excluded ===")
excluded_reasons = {}
for idx, r in enumerate(rows[2:], 3):
    if not any(x is not None for x in r):
        continue
    c1 = str(r[3]).strip() if r[3] else ''
    c2 = str(r[4]).strip() if r[4] else ''
    q_text = str(r[1]).strip() if r[1] else ''

    reason = None
    if c1 in ['Diltiazem 30 mg TID', 'Amlodipine 5 mg OD', 'Hydrochlorothiazide 25 mg OD', 'Bisoprolol 5 mg OD', 'Aspirin 81 mg OD'] and \
       c2 in ['Warfarin 3 mg OD (target INR 2-3)', 'Warfarin 3 mg OD (target INR 2.0-3.0)', 'Losartan 50 mg OD', 'Atorvastatin 20 mg OD', 'Spironolactone 25 mg OD', 'Sacubitril/Valsartan 49/51 mg BID']:
        reason = 'Dummy C1/C2 repetition'
    elif len(q_text) < 10 and not any(k in q_text.lower() for k in ['bp', 'hr', 'ecg', 'ckd', 'htn']):
        reason = 'Short text (<10 chars)'
    
    if reason:
        excluded_reasons[reason] = excluded_reasons.get(reason, 0) + 1
        if excluded_reasons[reason] <= 3:
            print(f"Reason: {reason} | Row {idx}: Q: {q_text[:50]} | C1: {c1[:30]}")

print("Excluded counts:", excluded_reasons)
