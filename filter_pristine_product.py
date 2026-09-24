import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('parsed_new_product_questions.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Filter quality:
# 1. Question must not start with 'ตอบข้อ' or 'คำอธิบาย'
# 2. Must have at least 2 non-empty choices
# 3. Question length >= 20 characters
valid_product_items = []
for it in items:
    q = it['q_text']
    if any(q.startswith(bad) for bad in ['ตอบข้อ', 'คำอธิบาย', 'เหตุผล', 'เฉลย:']):
        continue
    # count valid choices
    valid_c = [it.get(f'c{i}', '').strip() for i in range(1, 6) if it.get(f'c{i}', '').strip()]
    if len(valid_c) < 2:
        continue
    if len(q) < 20:
        continue
    valid_product_items.append(it)

print(f"Total extracted: {len(items)}")
print(f"Pristine high-quality questions ready to ingest: {len(valid_product_items)}")

tab_counts = {}
for q in valid_product_items:
    tab_counts[q['target_tab']] = tab_counts.get(q['target_tab'], 0) + 1

print("\nBreakdown of Pristine Questions by Target Tab:")
for t, cnt in sorted(tab_counts.items(), key=lambda x: -x[1]):
    print(f"  - {t:<30}: {cnt} questions")

with open('valid_product_ready_to_ingest.json', 'w', encoding='utf-8') as f:
    json.dump(valid_product_items, f, ensure_ascii=False, indent=2)

print("Saved to valid_product_ready_to_ingest.json")
