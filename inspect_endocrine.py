import openpyxl
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['4. Endocrine']
rows = list(ws.iter_rows(values_only=True))

print(f"Total rows in 4. Endocrine: {len(rows)}")
print("Row 1 (Banner):", rows[0][:4])
print("Row 2 (Headers):", rows[1][:8])

non_empty = [r for r in rows[2:] if any(x is not None for x in r)]
print(f"Total non-empty data rows: {len(non_empty)}")

# Check subtopics and templates
subtopics = {}
sources = {}
templates = 0
asterisks = 0

for r in non_empty:
    st = str(r[11]) if len(r) > 11 and r[11] else 'Uncategorized'
    src = str(r[15]) if len(r) > 15 and r[15] else 'Unknown'
    subtopics[st] = subtopics.get(st, 0) + 1
    sources[src] = sources.get(src, 0) + 1
    exp = str(r[9]) if len(r) > 9 and r[9] else ''
    if '**' in exp or '*' in exp:
        asterisks += 1
    if any(k in exp for k in ['ไม่ใช่คำตอบที่ถูกต้องสำหรับภาวะ', 'ไม่ใช่คำตอบที่ถูกต้อง', 'ไม่ตรงกับบริบท', 'ไม่ถูกต้องตามหลักการรักษา']):
        templates += 1

print("\nSubtopics breakdown:")
for st, cnt in sorted(subtopics.items(), key=lambda x: -x[1])[:10]:
    print(f"  - {st}: {cnt}")

print("\nSources breakdown:")
for s, cnt in sorted(sources.items(), key=lambda x: -x[1])[:10]:
    print(f"  - {s}: {cnt}")

print(f"\nQuality stats: Asterisks = {asterisks}, Templates needing rewrite = {templates}")

# Print first 5 rows
print("\nFirst 5 rows preview:")
for i in range(min(5, len(non_empty))):
    r = non_empty[i]
    print(f"Row {i+3}: Q{r[0]} | {str(r[1])[:60]} | Ans: {r[8]} | Sub: {r[11]} | Src: {r[15]}")
