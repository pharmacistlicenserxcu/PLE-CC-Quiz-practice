import sys
import io
import re
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

src = r'C:\Users\thana\Downloads\_CC1 Product Contents (1).md'
with open(src, 'r', encoding='utf-8') as f:
    text = f.read()

print("File loaded, total length:", len(text))

# Let's inspect the 13 Product Groups listed in the markdown file
# Lines 11693-11720:
# Product Group 1: Titrations
# Product Group 2: Chromatography
# Product Group 3: Spectroscopy & Optics
# Product Group 4: Preformulation & GMP
# Product Group 5: Pharmaceutical Calc
# Product Group 6: Solid Dosage Forms
# Product Group 7: Liquid & Semisolids
# Product Group 8: Biopharm & Drug Release
# Product Group 9: Sterile & Special Forms
# Product Group 10: Biotech Products
# Product Group 11: Herbal Products
# Product Group 12: Food Products & QA
# Product Group 13: Medicinal Chemistry

# Let's inspect Year 2567 questions and their topics
q_2567 = text[46:8404]
questions_2567 = re.findall(r'### \*\*ข้อ (\d+)\*\*(.*?)(?=### \*\*ข้อ \d+\*\*|$)', q_2567, re.DOTALL)
print(f"\nTotal questions in 2567: {len(questions_2567)}")

for q_num, content in questions_2567[:15]:
    lines = [l.strip() for l in content.strip().splitlines() if l.strip()]
    q_title = lines[0] if lines else ''
    print(f"2567 Q{q_num}: {q_title[:80]}")
