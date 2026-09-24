import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['2. Cardiovascular']
rows = list(ws.iter_rows(values_only=True))

corrupted_choices = []
for idx, r in enumerate(rows[2:], 3):
    c1 = str(r[3]) if r[3] else ''
    c2 = str(r[4]) if r[4] else ''
    c3 = str(r[5]) if r[5] else ''
    # Check if multiple choices are bundled into C1 like "a) ... b) ... c) ..."
    if any(k in c1 for k in ['b)', 'ข.', '2.', 'B.', 'b.']) and len(c1) > 20:
        corrupted_choices.append((idx, r[0], str(r[1])[:50], c1[:60], c2[:40]))

print(f"Total bundled choice rows in Cardio: {len(corrupted_choices)}")
for cc in corrupted_choices[:10]:
    print(f"Row {cc[0]} (Q{cc[1]}): {cc[2]}")
    print(f"   C1: {cc[3]}")
    print(f"   C2: {cc[4]}")
