import sys
import io
import re
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

src = r'C:\Users\thana\Downloads\_CC1 Product Contents (1).md'
with open(src, 'r', encoding='utf-8') as f:
    text = f.read()

print("File loaded, total length:", len(text))

# Find the end of questions (start of section 11672: # แบ่งงาน)
split_idx = text.find('# แบ่งงาน')
if split_idx == -1:
    split_idx = len(text)
exam_text = text[:split_idx]

# Pattern to locate year headers: # 2567, # 🤯 2566, # 2565, # 🫠 2564, # 💚 2563, # 2562, # 🫥 2561, # 2560, # 2559, # 😘 2558
year_patterns = [
    ('2567', r'# 2567\b'),
    ('2566', r'# 🤯 2566\b'),
    ('2565', r'# 2565\b'),
    ('2564', r'# 🫠 2564\b'),
    ('2563', r'# 💚 2563\b'),
    ('2562', r'# 2562\b'),
    ('2561', r'# 🫥 2561\b'),
    ('2560', r'# 2560\b'),
    ('2559', r'# 2559\b'),
    ('2558', r'# 😘 2558\b')
]

year_spans = []
for idx, (yr, pat) in enumerate(year_patterns):
    m = re.search(pat, exam_text)
    if m:
        year_spans.append((yr, m.start()))

year_spans.sort(key=lambda x: x[1])

print(f"Detected {len(year_spans)} year blocks:")
for i in range(len(year_spans)):
    yr, start_pos = year_spans[i]
    end_pos = year_spans[i+1][1] if i+1 < len(year_spans) else len(exam_text)
    print(f"Year {yr}: pos {start_pos} to {end_pos} (length: {end_pos - start_pos})")
