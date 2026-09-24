import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)

clinic_sheets = [
    '1. Musculoskeleton', '2. Cardiovascular', '3. Dermatologic', '4. Endocrine',
    '5. Gastrointestinal', '6. Hematologic', '7. Immunologic', '8. Infectious diseases',
    '9. Neurologic', '10. Psychiatric', '11. Pulmonary', '12. GynaecologicGenitourinary',
    '13. Eye disorder', '14. Oncologic', '15. Renal', '16. Others & Toxic',
    '17. Herbal Medicine', '18. Clinical Nutrition'
]

print(f"{'Sheet':<30} | {'Total Qs':<10} | {'Asterisks':<10} | {'Template Distractors':<22} | {'Status'}")
print("-" * 90)

for s in clinic_sheets:
    ws = wb[s]
    rows = list(ws.iter_rows(values_only=True))
    non_empty = [r for r in rows[2:] if any(x is not None for x in r)]
    
    ast = 0
    tmpl = 0
    for r in non_empty:
        exp = str(r[9]) if len(r) > 9 and r[9] else ''
        if '**' in exp or '*' in exp:
            ast += 1
        if any(k in exp for k in ['ไม่ใช่คำตอบที่ถูกต้องสำหรับภาวะ', 'ไม่ใช่คำตอบที่ถูกต้อง', 'ไม่ตรงกับบริบท', 'ไม่ถูกต้องตามหลักการรักษา']):
            tmpl += 1
            
    if ast == 0 and tmpl == 0 and len(non_empty) > 0:
        status = '✅ เสร็จสมบูรณ์ 100%'
    else:
        status = f'⚠️ รอ Overhaul ({tmpl} ข้อ)'
    print(f"{s:<30} | {len(non_empty):<10} | {ast:<10} | {tmpl:<22} | {status}")
