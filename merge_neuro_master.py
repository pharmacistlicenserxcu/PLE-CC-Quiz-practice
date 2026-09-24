import json
import glob
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load base neuro items
with open('neuro_base_items.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total base Neuro items: {len(items)}")

# Load all distractors_neuro_part*.json
distractor_files = sorted(glob.glob('distractors_neuro_part*.json'))
all_distractors = {}
for df in distractor_files:
    with open(df, 'r', encoding='utf-8') as f:
        data = json.load(f)
        all_distractors.update(data)
        print(f"{df}: {len(data)} questions loaded")

print(f"Total distractor keys loaded: {len(all_distractors)}")

choices_letters = ['ก', 'ข', 'ค', 'ง', 'จ']

def build_distractor_block(distractors_dict, ans_letter):
    lines = ["🔍 ข้ออื่นผิดเพราะอะไร:"]
    for ltr in choices_letters:
        if ltr == ans_letter:
            continue
        reason = distractors_dict.get(ltr, '').strip()
        reason = reason.replace('**', '').replace('*', '')
        if reason:
            if reason.startswith(f"ข้อ {ltr}."):
                lines.append(f"- {reason}")
            elif reason.startswith(f"{ltr}."):
                lines.append(f"- ข้อ {reason}")
            elif reason.startswith(f"ข้อ {ltr}"):
                lines.append(f"- {reason}")
            else:
                lines.append(f"- ข้อ {ltr}. {reason}")
    return "\n".join(lines)

updated_count = 0
for str_idx, dist_data in all_distractors.items():
    idx = int(str_idx)
    if idx >= len(items):
        continue
    
    item = items[idx]
    ans_letter = item.get('ans', '').strip()
    
    dist_map = dist_data.get('distractors', {})
    if not dist_map:
        dist_map = {k: v for k, v in dist_data.items() if k in choices_letters}
        
    new_distractor_block = build_distractor_block(dist_map, ans_letter)
    
    curr_exp = item.get('exp', '')
    if "🔍 ข้ออื่นผิดเพราะอะไร:" in curr_exp:
        parts = curr_exp.split("🔍 ข้ออื่นผิดเพราะอะไร:")
        before = parts[0].strip()
        after = parts[1]
        
        after_block = ""
        for tag in ["📖 Guideline", "📌 จุดจำ", "💡 Background", "🎯 ทำไมข้อนี้ถึงถูก"]:
            if tag in after:
                after_block = after[after.find(tag):].strip()
                break
                
        if after_block:
            new_exp = f"{before}\n\n{new_distractor_block}\n\n{after_block}"
        else:
            new_exp = f"{before}\n\n{new_distractor_block}"
    else:
        new_exp = f"{curr_exp}\n\n{new_distractor_block}"
        
    item['exp'] = new_exp
    updated_count += 1

asterisk_count = 0
for item in items:
    for k, v in item.items():
        if isinstance(v, str):
            if '*' in v:
                asterisk_count += v.count('*')
                item[k] = v.replace('**', '').replace('*', '')

print(f"Total explanations updated with authentic distractors: {updated_count}")
print(f"Total asterisks in dataset after merge: {asterisk_count}")

with open('neuro_master_pristine.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Saved to neuro_master_pristine.json")
