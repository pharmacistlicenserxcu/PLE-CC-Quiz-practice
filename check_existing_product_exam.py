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

print("=== Checking if 2567 Q1 & Q2 already exist in any Product tab ===")
found = []
for s in product_sheets:
    ws = wb[s]
    rows = list(ws.iter_rows(values_only=True))
    for idx, r in enumerate(rows[2:], 3):
        q_text = str(r[1]) if r[1] else ''
        if 'specific rotation' in q_text.lower() or 'polarimetry' in str(r).lower():
            found.append((s, idx, q_text[:80], r[8], r[13], r[14], r[15]))

for f in found:
    print(f[0], f"Row {f[1]}:", f[2], "| Ans:", f[3], "| Source:", f[5], f[6])

print(f"Total found matching specific rotation/polarimetry: {len(found)}")
