# -*- coding: utf-8 -*-
import sys, io, openpyxl

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx')
ws = wb['1. Musculoskeleton']

# 1. Set Row 1 banner properly
ws.cell(1, 1).value = '=HYPERLINK("#gid=0", "🏠 กลับสู่หน้าแรก (Go to Home Page)")'

# 2. Fix HLA-B*58:01 to HLA-B58:01 in all cells
fixed_cells = 0
for r in range(1, ws.max_row + 1):
    for c in range(1, 17):
        val = ws.cell(r, c).value
        if val and isinstance(val, str) and '*' in val:
            ws.cell(r, c).value = val.replace('HLA-B*58:01', 'HLA-B58:01').replace('*', '')
            fixed_cells += 1

print(f"Fixed {fixed_cells} cells containing asterisks.")
wb.save('PLE CC QUIZ.xlsx')
print("Saved clean workbook.")
