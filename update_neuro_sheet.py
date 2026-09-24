import openpyxl
from openpyxl.styles import Font, PatternFill, Alignment, Border, Side
import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load master pristine neurologic questions
with open('neuro_master_pristine.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Loaded {len(items)} pristine Neuro items.")

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx')
sheet_name = '9. Neurologic'
if sheet_name not in wb.sheetnames:
    print(f"Error: {sheet_name} not found in workbook!")
    sys.exit(1)

ws = wb[sheet_name]

# Ensure banner in Row 1
ws['A1'] = '=HYPERLINK("#gid=0", "🏠 กลับสู่หน้าแรก (Go to Home Page)")'
ws['A1'].font = Font(name='Bai Jamjuree', size=11, bold=True, color='0D47A1')
ws['A1'].alignment = Alignment(horizontal='center', vertical='center')
ws['A1'].fill = PatternFill(start_color='E3F2FD', end_color='E3F2FD', fill_type='solid')
ws.row_dimensions[1].height = 35

# Keep headers in Row 2
# Clear all rows from Row 3 to max_row
max_r = ws.max_row
print(f"Current max_row in sheet: {max_r}")

for row in ws.iter_rows(min_row=3, max_row=max_r):
    for cell in row:
        cell.value = None

thin_border = Border(
    left=Side(style='thin', color='E0E0E0'),
    right=Side(style='thin', color='E0E0E0'),
    top=Side(style='thin', color='E0E0E0'),
    bottom=Side(style='thin', color='E0E0E0')
)

font_regular = Font(name='Bai Jamjuree', size=10)
font_bold = Font(name='Bai Jamjuree', size=10, bold=True)
align_left = Alignment(horizontal='left', vertical='top', wrap_text=True)
align_center = Alignment(horizontal='center', vertical='top')

col_keys = [
    'idx', 'q_text', 'q_pic', 'c1', 'c2', 'c3', 'c4', 'c5', 
    'ans', 'exp', 'ans_pic', 'subtopic', 'category', 'note', 'type', 'year_set'
]

asterisk_count = 0
template_count = 0
template_keywords = ['ไม่ใช่คำตอบที่ถูกต้องสำหรับภาวะ', 'ไม่ใช่คำตอบที่ถูกต้อง', 'ไม่ตรงกับบริบท', 'ไม่ถูกต้องตามหลักการรักษา']

for i, item in enumerate(items):
    row_num = i + 3
    for col_idx, key in enumerate(col_keys, start=1):
        val = item.get(key, '')
        if val is None:
            val = ''
        
        # Verify 0 asterisks
        if isinstance(val, str):
            if '*' in val:
                asterisk_count += val.count('*')
                val = val.replace('**', '').replace('*', '')
            
            if key == 'exp':
                for kw in template_keywords:
                    if kw in val:
                        template_count += 1
                        break

        cell = ws.cell(row=row_num, column=col_idx, value=val)
        cell.border = thin_border
        
        if key in ['idx', 'ans', 'subtopic', 'category', 'type', 'year_set']:
            cell.font = font_bold if key in ['idx', 'ans'] else font_regular
            cell.alignment = align_center
        else:
            cell.font = font_regular
            cell.alignment = align_left

print(f"Successfully wrote {len(items)} rows to '{sheet_name}'.")
print(f"Asterisks found and cleaned: {asterisk_count}")
print(f"Residual template phrases detected: {template_count}")

# Save workbook
wb.save('PLE CC QUIZ.xlsx')
print("Successfully saved PLE CC QUIZ.xlsx!")
