import json
import sys
import io

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

with open('parsed_new_product_questions.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

print(f"Total extracted: {len(items)}")

# Sample questions from 11. Herbal Products, 12. Food Products & QA, 1. Titrations, 9. Sterile
sample_tabs = ['11. Herbal Products', '12. Food Products & QA', '1. Titrations', '9. Sterile & Special Forms', '2. Chromatography']

for t in sample_tabs:
    t_items = [it for it in items if it['target_tab'] == t]
    print(f"\n=== Sample from {t} (Total: {len(t_items)}) ===")
    for it in t_items[:3]:
        print(f"[{it['year']} ข้อ {it['q_num']}] Q: {it['q_text'][:70]}")
        print(f"   Img: {it['q_img']}")
        print(f"   ก: {it['c1'][:25]} | ข: {it['c2'][:25]} | ค: {it['c3'][:25]} | Ans: {it['ans']}")
