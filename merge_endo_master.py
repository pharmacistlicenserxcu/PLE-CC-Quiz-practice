import json
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load base endocrine items
with open('endocrine_base_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total base endocrine items: {len(items)}")

# Load all 4 distractor parts
distractors_all = {}
for p in range(1, 5):
    with open(f'distractors_endo_part{p}.json', 'r', encoding='utf-8') as f:
        part_data = json.load(f)
        print(f"Part {p}: {len(part_data)} questions mapped")
        for k, v in part_data.items():
            distractors_all[str(k)] = v.get('distractors', {})

print(f"Total distractor keys loaded: {len(distractors_all)}")

thai_letters = ['ก', 'ข', 'ค', 'ง', 'จ']

def clean_asterisks(text):
    if not text:
        return text
    return str(text).replace('**', '').replace('*', '').strip()

updated_count = 0
for i, item in enumerate(items):
    key_str = str(i)
    orig_exp = item.get('exp', '')
    
    if key_str in distractors_all:
        d_map = distractors_all[key_str]
        
        # Build pristine distractor text
        distractor_lines = []
        for letter in thai_letters:
            if letter in d_map:
                d_reason = clean_asterisks(d_map[letter])
                choice_idx = thai_letters.index(letter) + 1
                c_text = clean_asterisks(item.get(f'c{choice_idx}', ''))
                distractor_lines.append(f"• ข้อ {letter}. ({c_text}): {d_reason}")
                
        if distractor_lines:
            new_distractor_block = "\n".join(distractor_lines)
            
            if "🔍 ข้ออื่นผิดเพราะอะไร:" in orig_exp:
                parts = orig_exp.split("🔍 ข้ออื่นผิดเพราะอะไร:")
                before = parts[0].strip()
                after_part = parts[1]
                
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
            item['exp'] = clean_asterisks(orig_exp)
    else:
        item['exp'] = clean_asterisks(orig_exp)

print(f"Total explanations updated with authentic distractors: {updated_count}")

# Verify zero asterisks across all items
total_asterisks = 0
for it in items:
    for field in ['q_text', 'c1', 'c2', 'c3', 'c4', 'c5', 'exp', 'subtopic']:
        val = str(it.get(field, ''))
        if '**' in val or '*' in val:
            total_asterisks += 1

print(f"Total asterisks in dataset after merge: {total_asterisks}")

with open('endo_master_pristine.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Saved to endo_master_pristine.json")
