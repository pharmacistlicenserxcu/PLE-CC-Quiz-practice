import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['2. Cardiovascular']
rows = list(ws.iter_rows(values_only=True))

print("=== Checking Row 201 (Row 199) and nearby ===")
for i in range(195, 210):
    r = rows[i]
    print(f"Row {i+1}: Q{r[0]} | Q_text: {str(r[1])[:50]} | C1: {str(r[3])[:30]} | C2: {str(r[4])[:30]} | Ans: {r[8]} | Exp: {str(r[9])[:40]}")

print("\n=== Checking Row 245 to 260 ===")
for i in range(245, 260):
    r = rows[i]
    print(f"Row {i+1}: Q{r[0]} | Q_text: {str(r[1])[:50]} | C1: {str(r[3])[:30]} | C2: {str(r[4])[:30]} | Ans: {r[8]} | Exp: {str(r[9])[:40]}")
