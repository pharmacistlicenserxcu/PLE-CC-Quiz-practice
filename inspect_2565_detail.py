import sys
import io
import re
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

src = r'C:\Users\thana\Downloads\_CC1 Product Contents (1).md'
with open(src, 'r', encoding='utf-8') as f:
    text = f.read()

# Let's inspect Year 2565 in detail
# Start of 2565 to Start of 2564
start_2565 = text.find('# 2565')
end_2565 = text.find('# 🫠 2564')
p2565 = text[start_2565:end_2565]

print(f"2565 length: {len(p2565)}")
lines = [l.strip() for l in p2565.splitlines() if l.strip()]
print("First 25 lines of 2565:")
for l in lines[:25]:
    print(" ", l)

# Count questions in 2565
q_nums = re.findall(r'(?:^|\n)(\d+)\\\.\s+(.*?)(?=\n[ก-จa-e]\.|\n\d+\\\.|$)', p2565)
print(f"Numbered questions found in 2565: {len(q_nums)}")
for q in q_nums[:5]:
    print("  Q:", q[0], q[1][:60])
