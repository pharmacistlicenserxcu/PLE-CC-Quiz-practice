import openpyxl
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
product_sheets = [
    '1. Titrations', '2. Chromatography', '3. Spectroscopy & Optics', '4. Preformulation & GMP',
    '5. Pharmaceutical Calc', '6. Solid Dosage Forms', '7. Liquid & Semisolids',
    '8. Biopharm & Drug Release', '9. Sterile & Special Forms', '10. Biotech Products',
    '11. Herbal Products', '12. Food Products & QA', '13. Medicinal Chemistry'
]

year_counts = {}
sheet_details = {}

for s in product_sheets:
    ws = wb[s]
    rows = list(ws.iter_rows(values_only=True))
    q_rows = [r for r in rows[2:] if r[0] is not None or (len(r) > 1 and r[1] is not None)]
    sheet_details[s] = {'total': len(q_rows), 'years': {}}
    for r in q_rows:
        src = str(r[15]) if len(r) > 15 and r[15] else ''
        cat = str(r[14]) if len(r) > 14 and r[14] else ''
        note = str(r[13]) if len(r) > 13 and r[13] else ''
        filter_col = str(r[11]) if len(r) > 11 and r[11] else ''
        full_info = f"{src} {cat} {note} {filter_col}"
        
        # detect year
        years_found = re.findall(r'25[56][0-9]', full_info)
        if years_found:
            y = years_found[0]
        elif 'Mock' in full_info:
            y = 'Mock'
        elif 'Practice' in full_info or 'แบบฝึกหัด' in full_info:
            y = 'Practice/RxCU'
        else:
            y = 'Unknown'
            
        sheet_details[s]['years'][y] = sheet_details[s]['years'].get(y, 0) + 1
        year_counts[y] = year_counts.get(y, 0) + 1

print("=== OVERALL YEARS IN PRODUCT TABS ===")
for y, c in sorted(year_counts.items()):
    print(f"Year {y}: {c} questions")

print("\n=== BREAKDOWN BY PRODUCT TAB ===")
for s, data in sheet_details.items():
    print(f"\n{s} (Total: {data['total']}):")
    for y, c in sorted(data['years'].items()):
        print(f"  - {y}: {c}")
