import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['3. Spectroscopy & Optics']
rows = list(ws.iter_rows(values_only=True))

for row_idx in [3, 4]: # Row 4 and Row 5 (0-indexed 3 and 4)
    r = rows[row_idx]
    print(f"\n=== Row {row_idx+1} ===")
    print("ข้อที่:", r[0])
    print("คำถาม:", r[1])
    print("ตัวเลือก 1:", r[3])
    print("ตัวเลือก 2:", r[4])
    print("ตัวเลือก 3:", r[5])
    print("ตัวเลือก 4:", r[6])
    print("ตัวเลือก 5:", r[7])
    print("เฉลย:", r[8])
    print("คำอธิบายเฉลย:\n", r[9])
    print("Filter หมวด:", r[11])
    print("หมายเหตุ:", r[13])
    print("ประเภทข้อสอบ:", r[14])
    print("ปี / เลขชุด:", r[15])
