import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['17. Herbal Medicine']
rows = list(ws.iter_rows(values_only=True))

for i, r in enumerate(rows[2:], 3):
    q_text = str(r[1]) if r[1] else ''
    cat = str(r[12]) if len(r) > 12 and r[12] else ''
    subtopic = str(r[11]) if len(r) > 11 and r[11] else ''
    # Check if questions are about formulation, extraction, standard, QA
    if any(k in q_text for k in ['สกัด', 'สารสกัด', 'มาตรฐาน', 'assay', 'TLC', 'ควบคุมคุณภาพ', 'ตำรับ', 'รูปยาสมุนไพร', 'น้ำมัน', 'แคปซูล', 'ชง']):
        print(f"Row {i}: {q_text[:70]} | Cat: {cat} | Sub: {subtopic}")
