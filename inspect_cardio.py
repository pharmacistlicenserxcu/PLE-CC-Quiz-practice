import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['2. Cardiovascular']
rows = list(ws.iter_rows(values_only=True))

print(f"Total rows in 2. Cardiovascular: {len(rows)}")
print("Row 1 (Banner):", rows[0][:4])
print("Row 2 (Headers):", rows[1][:8])

non_empty = [i for i, r in enumerate(rows[2:], 3) if any(x is not None for x in r)]
print(f"Total non-empty data rows: {len(non_empty)}")

# Check sample questions
for r_idx in [2, 3, 4, 10, 50, 100, 150, 200, 250, 300]:
    if r_idx < len(rows):
        r = rows[r_idx]
        print(f"\nRow {r_idx+1}: Q{r[0]} | {str(r[1])[:60]} | Ans: {r[8]} | Subtopic: {r[11]} | Source: {r[15]}")
