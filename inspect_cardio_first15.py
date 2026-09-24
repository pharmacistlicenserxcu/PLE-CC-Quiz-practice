import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['2. Cardiovascular']
rows = list(ws.iter_rows(values_only=True))

print("=== Checking first 15 rows of 2. Cardiovascular ===")
for i in range(2, min(len(rows), 17)):
    r = rows[i]
    print(f"\n--- Row {i+1} (Q{r[0]}) ---")
    print("Q:", str(r[1])[:80])
    print("C1:", r[3], "| C2:", r[4], "| C3:", r[5], "| C4:", r[6], "| C5:", r[7])
    print("Ans:", r[8])
    print("Exp:", str(r[9])[:150])
    print("Subtopic:", r[11], "| Source:", r[15])
