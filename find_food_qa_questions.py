import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
print("=== Scanning 16. Others & Toxic for Food and QA questions ===")
ws = wb['16. Others & Toxic']
rows = list(ws.iter_rows(values_only=True))

food_qa_rows = []
for idx, r in enumerate(rows[2:], 3):
    q_text = str(r[1]) if r[1] else ''
    sub = str(r[11]) if len(r) > 11 and r[11] else ''
    cat = str(r[12]) if len(r) > 12 and r[12] else ''
    
    if any(k in q_text for k in ['อาหารเสริม', 'ผลิตภัณฑ์เสริมอาหาร', 'สารปนเปื้อน', 'วัตถุกันเสีย', 'benzoic', 'sorbic', 'aflatoxin', 'ฟอร์มาลิน', 'บอแรกซ์', 'สารกันบูด', 'สารฟอกขาว', 'sodium hydrosulfite', 'ฉลากอาหาร', 'GHP', 'HACCP', 'CODEX', 'มาตรฐานอาหาร', 'วิตามินรวม']):
        food_qa_rows.append((idx, r[0], q_text[:70], r[8], sub))

print(f"Total Food & QA questions found in 16. Others & Toxic: {len(food_qa_rows)}")
for f in food_qa_rows[:15]:
    print(f"Row {f[0]} (Q{f[1]}): {f[2]} | Ans: {f[3]} | Sub: {f[4]}")
