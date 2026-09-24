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

print(f"{'Sheet':<28} | {'Qs':<6} | {'Sample Sources'}")
print("-" * 80)
total_prod_qs = 0
for s in product_sheets:
    ws = wb[s]
    rows = list(ws.iter_rows(values_only=True))
    q_rows = [r for r in rows[2:] if r[0] is not None or (len(r) > 1 and r[1] is not None)]
    total_prod_qs += len(q_rows)
    sources = []
    for r in q_rows:
        src_info = []
        for col_idx in [15, 14, 13]:
            if len(r) > col_idx and r[col_idx]:
                src_info.append(str(r[col_idx]).strip())
        if src_info:
            sources.append(" / ".join(src_info))
    unique_sources = list(dict.fromkeys(sources))
    sample = "; ".join(unique_sources[:2])
    print(f"{s:<28} | {len(q_rows):<6} | {sample[:60]}")

print("-" * 80)
print(f"Total Product Questions currently in workbook: {total_prod_qs}")
