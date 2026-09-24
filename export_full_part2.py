import json
import sys

with open('psych_part2.json', encoding='utf-8') as f:
    d = json.load(f)

with open('full_part2_questions.txt', 'w', encoding='utf-8') as out:
    for k, v in d.items():
        ans_idx = v.get('ans', 1)
        choices = {1: 'ก', 2: 'ข', 3: 'ค', 4: 'ง', 5: 'จ'}
        correct_letter = choices.get(ans_idx, 'ก')
        
        out.write(f"=== KEY: {k} | ANS: {ans_idx} ({correct_letter}) ===\n")
        out.write(f"Q: {v.get('q_text')}\n")
        out.write(f"ก: {v.get('c1')}\n")
        out.write(f"ข: {v.get('c2')}\n")
        out.write(f"ค: {v.get('c3')}\n")
        out.write(f"ง: {v.get('c4')}\n")
        out.write(f"จ: {v.get('c5')}\n")
        out.write(f"Note: {v.get('note')}\n")
        out.write(f"Exp:\n{v.get('exp')}\n")
        out.write("="*60 + "\n\n")

print("Done writing full_part2_questions.txt")
