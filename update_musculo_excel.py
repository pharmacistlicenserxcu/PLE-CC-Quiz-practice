# -*- coding: utf-8 -*-
"""
update_musculo_excel.py
Writes the master 217 pristine questions directly into '1. Musculoskeleton' in PLE CC QUIZ.xlsx.
Preserves Row 1 (Home banner) and Row 2 (Headers).
Replaces data rows starting at Row 3.
Zero asterisks, zero generic distractors.
"""
import sys, io, json, openpyxl

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# 1. Load pristine items
with open('master_musculo_217_pristine.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Loaded {len(items)} pristine items.")

# 2. Open workbook
wb_path = 'PLE CC QUIZ.xlsx'
wb = openpyxl.load_workbook(wb_path)

if '1. Musculoskeleton' not in wb.sheetnames:
    print("Error: '1. Musculoskeleton' sheet not found!")
    sys.exit(1)

ws = wb['1. Musculoskeleton']

# Clear existing rows from row 3 downwards
max_row = ws.max_row
if max_row and max_row >= 3:
    print(f"Clearing rows 3 to {max_row}...")
    ws.delete_rows(3, max_row - 2)

# Write items starting at row 3
print(f"Writing {len(items)} pristine rows starting at Row 3...")
for idx, it in enumerate(items):
    row_num = idx + 3
    c = it['choices']
    
    ws.cell(row=row_num, column=1, value=idx + 1)                 # A: ข้อที่
    ws.cell(row=row_num, column=2, value=it['question'])            # B: คำถาม
    ws.cell(row=row_num, column=3, value=it.get('img_q', ''))       # C: รูปถาม
    ws.cell(row=row_num, column=4, value=c[0] if len(c) > 0 else '')# D: ตัวเลือก 1
    ws.cell(row=row_num, column=5, value=c[1] if len(c) > 1 else '')# E: ตัวเลือก 2
    ws.cell(row=row_num, column=6, value=c[2] if len(c) > 2 else '')# F: ตัวเลือก 3
    ws.cell(row=row_num, column=7, value=c[3] if len(c) > 3 else '')# G: ตัวเลือก 4
    ws.cell(row=row_num, column=8, value=c[4] if len(c) > 4 else '')# H: ตัวเลือก 5
    ws.cell(row=row_num, column=9, value=int(it['ans']))            # I: เฉลย (ตัวเลข 1-5)
    ws.cell(row=row_num, column=10, value=it['explanation'])        # J: คำอธิบายเฉลย
    ws.cell(row=row_num, column=11, value=it.get('img_exp', ''))    # K: รูปเฉลย
    ws.cell(row=row_num, column=12, value=it.get('topic', 'Musculoskeletal')) # L: Filter หมวด/Subtopic
    ws.cell(row=row_num, column=13, value=it.get('domain', 'Clinic'))         # M: Product / Clinic
    ws.cell(row=row_num, column=14, value=it.get('subtopic', ''))             # N: หมายเหตุ
    ws.cell(row=row_num, column=15, value=it.get('source_type', ''))          # O: ประเภทข้อสอบ
    ws.cell(row=row_num, column=16, value=it.get('year', ''))                 # P: ปี / เลขชุด

# Save workbook
wb.save(wb_path)
print(f"Successfully saved {wb_path} with {len(items)} pristine rows in '1. Musculoskeleton'!")
