import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['2. Cardiovascular']
rows = list(ws.iter_rows(values_only=True))

for r_idx in [62, 63, 64]: # Row 63, 64, 65 (0-indexed 62, 63, 64)
    r = rows[r_idx]
    print(f"\n=== Row {r_idx+1} ===")
    print("Q:", r[1])
    print("C1:", r[3])
    print("C2:", r[4])
    print("C3:", r[5])
    print("C4:", r[6])
    print("C5:", r[7])
    print("Ans:", r[8])
    print("Exp:\n", r[9])
    print("Source:", r[15])
