import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)

product_sheets = [
    '1. Titrations', '2. Chromatography', '3. Spectroscopy & Optics', '4. Preformulation & GMP',
    '5. Pharmaceutical Calc', '6. Solid Dosage Forms', '7. Liquid & Semisolids',
    '8. Biopharm & Drug Release', '9. Sterile & Special Forms', '10. Biotech Products',
    '11. Herbal Products', '12. Food Products & QA', '13. Medicinal Chemistry'
]

print(f"{'Sheet':<30} | {'Total Non-Empty':<16} | {'Asterisks (**)':<14} | {'Template Distractors'}")
print("-" * 85)

for s in product_sheets:
    ws = wb[s]
    rows = list(ws.iter_rows(values_only=True))
    non_empty = [r for r in rows[2:] if any(x is not None for x in r)]
    
    asterisk_count = 0
    template_count = 0
    
    for r in non_empty:
        exp = str(r[9]) if len(r) > 9 and r[9] else ''
        if '**' in exp or '*' in exp:
            asterisk_count += 1
        if 'ไม่ใช่คำตอบที่ถูกต้อง' in exp or 'ไม่ตรงกับบริบท' in exp or 'ไม่ถูกต้องตามหลักการรักษา' in exp:
            template_count += 1
            
    print(f"{s:<30} | {len(non_empty):<16} | {asterisk_count:<14} | {template_count}")
