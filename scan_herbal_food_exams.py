import sys
import io
import re
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

src = r'C:\Users\thana\Downloads\_CC1 Product Contents (1).md'
with open(src, 'r', encoding='utf-8') as f:
    text = f.read()

print("File loaded, length:", len(text))

# Let's search for keywords related to herbal, extraction, traditional medicine
herbal_keywords = [
    'สมุนไพร', 'ขมิ้น', 'ฟ้าทะลายโจร', 'รางจืด', 'เถาวัลย์เปรียง', 'กัญชา',
    'บัวบก', 'พญายอ', 'มะระขี้นก', 'สารสกัด', 'maceration', 'percolation',
    'soxhlet', 'decoction', 'tincture', 'บัญชียาสมุนไพร', 'น้ำมันหอมระเหย',
    'curcumin', 'andrographolide', 'THC', 'CBD', 'capsaicin', 'แคปซูลขมิ้น'
]

# Let's search for food, nutrition, QA, adulteration, contaminants
food_keywords = [
    'อาหาร', 'อาหารเสริม', 'ผลิตภัณฑ์เสริมอาหาร', 'สารปนเปื้อน', 'วัตถุกันเสีย',
    'benzoic', 'sorbic', 'aflatoxin', 'โลหะหนัก', 'ตะกั่ว', 'สารหนู',
    'ฟอร์มาลิน', 'บอแรกซ์', 'สารกันบูด', 'สารฟอกขาว', 'sodium hydrosulfite',
    'อย.', 'ฉลากอาหาร', 'GHP', 'HACCP', 'CODEX', 'วิตามินรวม'
]

# Let's find blocks in the exam section (before line 11672, or before '# แบ่งงาน')
exam_text = text[:text.find('# แบ่งงาน')]
print("Exam section length:", len(exam_text))

# Let's search for questions containing herbal keywords
herbal_found = []
food_found = []

# Split exam_text into roughly questions or examine lines
# In the md file, questions are preceded by headers or 'ข้อ'
lines = exam_text.splitlines()
print(f"Total lines in exam part: {len(lines)}")

# We can search year by year
year_sections = [
    ('2567', 46, 25507),
    ('2566', 25507, 43413),
    ('2565', 43413, 75497),
    ('2564', 75497, 189447),
    ('2563', 189447, 230632),
    ('2562', 230632, 299915),
    ('2561', 299915, 377372),
    ('2560', 377372, 379116),
    ('2559', 379116, 390689),
    ('2558', 390689, len(exam_text))
]

for yr, s, e in year_sections:
    chunk = exam_text[s:e]
    for hk in herbal_keywords:
        if hk in chunk:
            count = chunk.count(hk)
            herbal_found.append((yr, hk, count))
    for fk in food_keywords:
        if fk in chunk:
            count = chunk.count(fk)
            food_found.append((yr, fk, count))

print("\nHerbal matches by year:")
for yr, hk, cnt in herbal_found[:20]:
    print(f"  Year {yr}: {hk} ({cnt} times)")

print("\nFood matches by year:")
for yr, fk, cnt in food_found[:20]:
    print(f"  Year {yr}: {fk} ({cnt} times)")
