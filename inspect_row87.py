import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['2. Cardiovascular']
rows = list(ws.iter_rows(values_only=True))

for r_idx in [86]: # Row 87 (0-indexed 86)
    r = rows[r_idx]
    print(f"Row {r_idx+1}:")
    print("Q:", r[1])
    print("C1:", r[3], "| C2:", r[4], "| C3:", r[5], "| C4:", r[6], "| C5:", r[7])
    print("Ans:", r[8])
    print("Exp:\n", r[9])
    print("Source:", r[15])
