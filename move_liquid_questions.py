import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx')
ws_solid = wb['6. Solid Dosage Forms']
ws_liquid = wb['7. Liquid & Semisolids']

solid_rows = list(ws_solid.iter_rows(values_only=True))
liquid_rows = list(ws_liquid.iter_rows(values_only=True))

print(f"Initial 6. Solid Dosage Forms data rows: {len(solid_rows)-2}")
print(f"Initial 7. Liquid & Semisolids data rows: {len(liquid_rows)-2}")

# Identify misplaced rows in Solid Dosage Forms
misplaced_rows = []
stay_rows = []

for idx, r in enumerate(solid_rows[2:], 3):
    if not any(x is not None for x in r):
        continue
    q_text = str(r[1]) if r[1] else ''
    if any(k in q_text.lower() for k in ['suspension', 'ย้ำน้ำ', 'ยาน้ำ', 'cream', 'ครีม', 'ointment', 'syrup', 'emulsion']):
        misplaced_rows.append(r)
    else:
        stay_rows.append(r)

print(f"Found {len(misplaced_rows)} misplaced rows to move from Solid to Liquid.")
print(f"Solid rows remaining: {len(stay_rows)}")

# Prepare Liquid rows: keep existing non-empty rows + add misplaced_rows
existing_liquid_rows = [r for r in liquid_rows[2:] if any(x is not None for x in r)]
all_liquid_rows = existing_liquid_rows + misplaced_rows

print(f"Total rows for 7. Liquid & Semisolids will be: {len(all_liquid_rows)}")

font_regular = Font(name='Bai Jamjuree', size=10)
align_left = Alignment(horizontal='left', vertical='top', wrap_text=True)
align_center = Alignment(horizontal='center', vertical='top')

# 1. Rewrite 6. Solid Dosage Forms
# Clear from row 3 to max_row
for r in ws_solid.iter_rows(min_row=3, max_row=ws_solid.max_row):
    for c in r:
        c.value = None

for idx, r in enumerate(stay_rows, 1):
    row_num = idx + 2
    ws_solid.cell(row=row_num, column=1, value=idx).alignment = align_center
    ws_solid.cell(row=row_num, column=1).font = font_regular
    for col_idx in range(2, 17):
        val = r[col_idx-1] if len(r) >= col_idx else None
        cell = ws_solid.cell(row=row_num, column=col_idx, value=val)
        cell.font = font_regular
        if col_idx in [3, 9, 11, 13, 15, 16]:
            cell.alignment = align_center
        else:
            cell.alignment = align_left

# 2. Rewrite 7. Liquid & Semisolids
for r in ws_liquid.iter_rows(min_row=3, max_row=ws_liquid.max_row):
    for c in r:
        c.value = None

for idx, r in enumerate(all_liquid_rows, 1):
    row_num = idx + 2
    ws_liquid.cell(row=row_num, column=1, value=idx).alignment = align_center
    ws_liquid.cell(row=row_num, column=1).font = font_regular
    for col_idx in range(2, 17):
        val = r[col_idx-1] if len(r) >= col_idx else None
        cell = ws_liquid.cell(row=row_num, column=col_idx, value=val)
        cell.font = font_regular
        if col_idx in [3, 9, 11, 13, 15, 16]:
            cell.alignment = align_center
        else:
            cell.alignment = align_left

wb.save('PLE CC QUIZ.xlsx')
print("Successfully moved 15 questions from Solid to Liquid & Semisolids!")
