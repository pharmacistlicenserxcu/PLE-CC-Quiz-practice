import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
product_sheets = [
    '1. Titrations', '2. Chromatography', '3. Spectroscopy & Optics', '4. Preformulation & GMP',
    '5. Pharmaceutical Calc', '6. Solid Dosage Forms', '7. Liquid & Semisolids',
    '8. Biopharm & Drug Release', '9. Sterile & Special Forms', '10. Biotech Products',
    '11. Herbal Products', '12. Food Products & QA', '13. Medicinal Chemistry',
    '1. Pharmacy Laws & Ethics'
]

print(f"{'Sheet':<30} | {'Total Qs Now':<14} | {'Banner Status'}")
print("-" * 65)
total_prod = 0
for s in product_sheets:
    ws = wb[s]
    rows = list(ws.iter_rows(values_only=True))
    non_empty = [r for r in rows[2:] if any(x is not None for x in r)]
    total_prod += len(non_empty)
    banner_val = str(rows[0][0]) if rows and rows[0] and rows[0][0] else ''
    banner = '✅ OK' if 'HYPERLINK' in banner_val else '❌ Missing'
    print(f"{s:<30} | {len(non_empty):<14} | {banner}")

print("-" * 65)
print(f"Total questions across Product & Law tabs: {total_prod}")
