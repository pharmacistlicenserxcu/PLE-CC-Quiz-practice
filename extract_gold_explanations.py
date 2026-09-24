# -*- coding: utf-8 -*-
"""
extract_gold_explanations.py
Extracts handcrafted clinical explanations from refinement_scripts.
"""
import sys, json, os, re

sys.stdout.reconfigure(encoding='utf-8')

handcrafted = {}

def extract_from_file(file_path):
    if not os.path.exists(file_path): 
        print("Not found:", file_path)
        return
    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()
    pattern = re.compile(r'exp_(\d+)\s*=\s*"""([\s\S]*?)"""')
    for m in pattern.finditer(content):
        row_id = int(m.group(1))
        exp_text = m.group(2).strip()
        handcrafted[row_id] = exp_text

extract_from_file(r'PLE CC Quiz/scripts/refinement_scripts/refine_musculo_rows84_95.py')
extract_from_file(r'PLE CC Quiz/scripts/refinement_scripts/refine_musculo_rows96_107.py')
extract_from_file(r'PLE CC Quiz/scripts/refinement_scripts/refine_musculo_rows108_120.py')

print(f"Total handcrafted explanations loaded: {len(handcrafted)}")
with open(r'PLE CC Quiz/handcrafted_explanations.json', 'w', encoding='utf-8') as f:
    json.dump(handcrafted, f, ensure_ascii=False, indent=2)
print("Saved to PLE CC Quiz/handcrafted_explanations.json successfully!")
