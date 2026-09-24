import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['17. Herbal Medicine']
rows = list(ws.iter_rows(values_only=True))

print(f"Total rows in 17. Herbal Medicine: {len(rows)-2}")

product_herbal_rows = []
for idx, r in enumerate(rows[2:], 3):
    q_text = str(r[1]) if r[1] else ''
    cat = str(r[12]) if len(r) > 12 and r[12] else ''
    sub = str(r[11]) if len(r) > 11 and r[11] else ''
    
    # Check if question is Product focused (formulation, extraction, standardization, QA, pharmacopoeia)
    is_prod = False
    if cat.lower() == 'product':
        is_prod = True
    elif any(k in q_text for k in ['สารสกัด', 'maceration', 'percolation', 'soxhlet', 'THP', 'TLC', 'Thai Herbal Pharmacopoeia', 'สารสำคัญ', 'สกัดด้วย', 'ควบคุมคุณภาพ', 'มาตรฐาน', 'ตั้งตำรับ', 'ความชื้น', 'ash', 'LOD', 'น้ำมันหอมระเหย']):
        is_prod = True
        
    if is_prod:
        product_herbal_rows.append((idx, r[0], q_text[:70], cat, sub))

print(f"Total Herbal Product questions found inside 17. Herbal Medicine: {len(product_herbal_rows)}")
for p in product_herbal_rows[:15]:
    print(f"Row {p[0]} (Q{p[1]}): {p[2]} | Cat: {p[3]} | Sub: {p[4]}")
