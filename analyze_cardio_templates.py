import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['2. Cardiovascular']
rows = list(ws.iter_rows(values_only=True))

template_rows = []
for i, r in enumerate(rows[2:], 3):
    exp = str(r[9]) if len(r) > 9 and r[9] else ''
    if any(k in exp for k in ['ไม่ใช่คำตอบที่ถูกต้องสำหรับภาวะ', 'ไม่ใช่คำตอบที่ถูกต้อง', 'ไม่ตรงกับบริบท', 'ไม่ถูกต้องตามหลักการรักษา']):
        template_rows.append((i, r[0], str(r[1])[:50], r[15]))

print(f"Total template distractor rows in Cardio: {len(template_rows)}")
print("Sample rows:")
for tr in template_rows[:10]:
    print(f"Row {tr[0]}: Q{tr[1]} | {tr[2]} | Source: {tr[3]}")
