import sys
import io
import re
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

src = r'C:\Users\thana\Downloads\_CC1 Product Contents (1).md'
with open(src, 'r', encoding='utf-8') as f:
    text = f.read()

print("File length:", len(text))

# Let's inspect sections from year 2567 down to 2558
# In 2567, questions were in:
# Phần 1: ข้อสอบ (Questions)
# Phần 2: เฉลยข้อสอบ (Answer)

# Let's see how each year is structured
year_markers = [
    ('2567', r'# 2567\b', r'# 🤯 2566\b'),
    ('2566', r'# 🤯 2566\b', r'# 2565\b'),
    ('2565', r'# 2565\b', r'# 🫠 2564\b'),
    ('2564', r'# 🫠 2564\b', r'# 💚 2563\b'),
    ('2563', r'# 💚 2563\b', r'# 2562\b'),
    ('2562', r'# 2562\b', r'# 🫥 2561\b'),
    ('2561', r'# 🫥 2561\b', r'# 2560\b'),
    ('2560', r'# 2560\b', r'# 2559\b'),
    ('2559', r'# 2559\b', r'# 😘 2558\b'),
    ('2558', r'# 😘 2558\b', r'# แบ่งงาน\b')
]

for yr, start_pat, end_pat in year_markers:
    m_start = re.search(start_pat, text)
    m_end = re.search(end_pat, text)
    if m_start and m_end:
        chunk = text[m_start.start():m_end.start()]
        # find image markers like ![][image12] or similar
        images = re.findall(r'!\[.*?\]\[(.*?)\]', chunk)
        print(f"Year {yr}: length = {len(chunk)}, images = {len(images)}")
    else:
        print(f"Year {yr}: NOT FOUND (start={bool(m_start)}, end={bool(m_end)})")
