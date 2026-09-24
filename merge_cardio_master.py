import json
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load base extracted questions
with open('cardio_valid_extracted.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total base cardio items: {len(items)}")

# Load all 5 distractor parts
distractors_all = {}
for p in range(1, 6):
    with open(f'distractors_cardio_part{p}.json', 'r', encoding='utf-8') as f:
        part_data = json.load(f)
        print(f"Part {p}: {len(part_data)} questions mapped")
        for k, v in part_data.items():
            distractors_all[str(k)] = v.get('distractors', {})

print(f"Total distractor keys merged: {len(distractors_all)}")

thai_letters = ['ก', 'ข', 'ค', 'ง', 'จ']

def clean_asterisks(text):
    if not text:
        return text
    return str(text).replace('**', '').replace('*', '').strip()

# Update explanations in items
updated_count = 0
for i, item in enumerate(items):
    key_str = str(i)
    if key_str in distractors_all:
        d_map = distractors_all[key_str]
        orig_exp = item['exp']
        
        # Build pristine distractor text
        distractor_lines = []
        for letter in thai_letters:
            if letter in d_map:
                d_reason = clean_asterisks(d_map[letter])
                # Find choice text
                choice_idx = thai_letters.index(letter) + 1
                c_text = clean_asterisks(item.get(f'c{choice_idx}', ''))
                # format clean line
                distractor_lines.append(f"• ข้อ {letter}. ({c_text}): {d_reason}")
                
        if distractor_lines:
            new_distractor_block = "\n".join(distractor_lines)
            
            # Replace the old "🔍 ข้ออื่นผิดเพราะอะไร:" section if present
            if "🔍 ข้ออื่นผิดเพราะอะไร:" in orig_exp:
                # split before and after
                parts = orig_exp.split("🔍 ข้ออื่นผิดเพราะอะไร:")
                before = parts[0].strip()
                after_part = parts[1]
                
                # find where the next section starts (📖 Guideline หรือ 📌 จุดจำก่อนสอบ)
                next_marker = None
                for marker in ["📖 Guideline", "📌 จุดจำก่อนสอบ"]:
                    if marker in after_part:
                        if next_marker is None or after_part.find(marker) < after_part.find(next_marker):
                            next_marker = marker
                
                if next_marker:
                    split_next = after_part.split(next_marker, 1)
                    after = next_marker + split_next[1]
                else:
                    after = ""
                    
                new_exp = f"{before}\n\n🔍 ข้ออื่นผิดเพราะอะไร:\n{new_distractor_block}\n\n{after}".strip()
            else:
                new_exp = f"{orig_exp}\n\n🔍 ข้ออื่นผิดเพราะอะไร:\n{new_distractor_block}".strip()
                
            item['exp'] = clean_asterisks(new_exp)
            updated_count += 1
    else:
        item['exp'] = clean_asterisks(item['exp'])

print(f"Total explanations updated with authentic distractors: {updated_count}")

# Verify zero asterisks across all items
total_asterisks = 0
for it in items:
    for field in ['q_text', 'c1', 'c2', 'c3', 'c4', 'c5', 'exp', 'subtopic']:
        val = str(it.get(field, ''))
        if '**' in val or '*' in val:
            total_asterisks += 1

print(f"Total asterisks in dataset after merge: {total_asterisks}")

with open('cardio_master_pristine.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Saved to cardio_master_pristine.json")
