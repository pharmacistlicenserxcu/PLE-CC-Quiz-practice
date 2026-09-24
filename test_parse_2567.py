import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

src = r'C:\Users\thana\Downloads\_CC1 Product Contents (1).md'
with open(src, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect 2567 section carefully
p2567 = text[46:25507]

# Questions are in "ส่วนที่ 1: ข้อสอบ (Questions)"
# Answers are in "ส่วนที่ 2: เฉลยข้อสอบ (Answer)"
parts = p2567.split('ส่วนที่ 2: เฉลยข้อสอบ (Answer)')
q_part = parts[0]
ans_part = parts[1] if len(parts) > 1 else ''

print(f"2567 Q part len: {len(q_part)}, Ans part len: {len(ans_part)}")

# Find all questions in q_part
q_blocks = re.findall(r'### \*\*ข้อ (\d+)\*\*(.*?)(?=### \*\*ข้อ \d+\*\*|$)', q_part, re.DOTALL)
print(f"Total questions found in 2567: {len(q_blocks)}")

for q_num, content in q_blocks[:5]:
    print(f"\n--- Q{q_num} ---")
    lines = [l.strip() for l in content.strip().splitlines() if l.strip()]
    for l in lines[:6]:
        print(" ", l)

# Find all answers in ans_part
ans_blocks = re.findall(r'### \*\*เฉลยข้อที่\s*(\d+).*?\*\*(.*?)(?=### \*\*เฉลยข้อที่|$)', ans_part, re.DOTALL)
print(f"\nTotal answers found in 2567: {len(ans_blocks)}")
for a_num, content in ans_blocks[:3]:
    print(f"\n--- Ans {a_num} ---")
    lines = [l.strip() for l in content.strip().splitlines() if l.strip()]
    for l in lines[:6]:
        print(" ", l)
