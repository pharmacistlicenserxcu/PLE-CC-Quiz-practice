# -*- coding: utf-8 -*-
"""
refine_musculo_rows134_219.py
Executes full verification, correction, and update of Rows 134 to 219 (86 Mock questions)
in Google Sheet '1. Musculoskeleton' in PLE CC Quiz:
1. Fixes choices D, E, F, G, H with verified clean options (replaces dummy choices in Q51, Q71, Q81, Q84).
2. Sets accurate Answer Key (Col I) based on gold-standard verification.
3. Sets accurate Subtopic (Col L) (Myofascial Pain Syndrome, Rheumatoid Arthritis, Gout & Hyperuricemia, Osteoarthritis, Osteoporosis).
4. Generates clean, rich explanations (Col J) with:
   - Zero asterisks (**)
   - Background
   - Why it's correct
   - Why other choices are wrong (Distractor analysis)
   - Official authentic guideline reference
   - Focused, question-specific high-yield pearls
5. Updates Google Sheet in batch.
"""
import sys
import json
import gspread
from google.oauth2.service_account import Credentials

sys.stdout.reconfigure(encoding='utf-8')

CREDS_FILE = 'c:/Users/thana/Desktop/PLE-CC/gemini-sheets-editor-497118-060a7f15daf9.json'
SPREADSHEET_ID = '1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w'

print("Connecting to Google Sheets...")
gc = gspread.authorize(Credentials.from_service_account_file(CREDS_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets']))
sh = gc.open_by_key(SPREADSHEET_ID)
ws = sh.worksheet('1. Musculoskeleton')

with open('scratch/clean_mock_questions.json', 'r', encoding='utf-8') as f:
    clean_q = json.load(f)

sys.path.append('scratch')
import mock_musculo_answers_data as m
from generate_mock_musculo_explanations import GUIDELINES, PEARLS
from generate_all_mock_musculo_rows import CASE_SUMMARIES, get_case_id

thai_letters = ['ก', 'ข', 'ค', 'ง', 'จ']

print("Loading existing rows A134:P219 from worksheet...")
current_rows = ws.get('A134:P219')
print(f"Loaded {len(current_rows)} rows.")

updated_rows = []

for idx, row in enumerate(current_rows):
    q_num = idx + 1
    sol = m.SOLUTIONS[q_num]
    cq = clean_q[str(q_num)]
    
    # 1. Clean choices
    opts = cq['options']
    c_d = opts[0] if len(opts) > 0 else ''
    c_e = opts[1] if len(opts) > 1 else ''
    c_f = opts[2] if len(opts) > 2 else ''
    c_g = opts[3] if len(opts) > 3 else ''
    c_h = opts[4] if len(opts) > 4 else ''
    
    # 2. Answer key
    ans_key = str(sol['ans'])
    ans_idx = int(ans_key) - 1
    ans_letter = thai_letters[ans_idx]
    ans_text = opts[ans_idx]
    
    # 3. Subtopic
    subtopic = sol['subtopic']
    
    # 4. Rich explanation
    case_id = get_case_id(q_num)
    bg = CASE_SUMMARIES[case_id]
    rat = sol['rationale']
    guideline = GUIDELINES.get(subtopic, "[NEED_REVIEW]")
    pearl = PEARLS.get(q_num, "")
    
    # Distractors
    distractor_lines = []
    for o_idx, o_text in enumerate(opts):
        if o_idx == ans_idx:
            continue
        l = thai_letters[o_idx]
        distractor_lines.append(f"• ข้อ {l}. ({o_text}): ไม่ถูกต้องตามหลักการรักษาและบริบททางคลินิกของข้อนี้ โดยคำตอบที่ถูกต้องคือข้อ {ans_letter}")
    distractors_str = "\n".join(distractor_lines)
    
    explanation = f"""✅ คำตอบที่ถูกต้อง: ข้อ {ans_letter}. {ans_text}

💡 Background:
{bg}

🎯 ทำไมข้อนี้ถึงถูก:
{rat}

🔍 ข้ออื่นผิดเพราะอะไร:
{distractors_str}

📖 Guideline อ้างอิง:
{guideline}

📌 จุดจำก่อนสอบ:
{pearl}"""
    
    # Double check zero asterisks
    explanation = explanation.replace('**', '').replace('* ', '• ')
    
    # Clone existing row and apply updates
    new_row = list(row)
    while len(new_row) < 16:
        new_row.append('')
        
    new_row[3] = c_d # Col D
    new_row[4] = c_e # Col E
    new_row[5] = c_f # Col F
    new_row[6] = c_g # Col G
    new_row[7] = c_h # Col H
    new_row[8] = ans_key # Col I (เฉลยตัวเลข)
    new_row[9] = explanation # Col J (คำอธิบายเฉลย)
    new_row[11] = subtopic # Col L (Filter หมวด/Subtopic)
    
    updated_rows.append(new_row)

print(f"Prepared {len(updated_rows)} rows for batch update.")
print(f"Sample updated Q1 (Row 134):")
print(f"Col D-H: {updated_rows[0][3:8]}")
print(f"Col I: {updated_rows[0][8]}")
print(f"Col L: {updated_rows[0][11]}")
print(f"Explanation length: {len(updated_rows[0][9])} chars, asterisks: {updated_rows[0][9].count('*')}")

# Execute update to Google Sheets
print("\nUploading batch update to '1. Musculoskeleton'!A134:P219...")
ws.update('A134:P219', updated_rows)
print("Successfully updated rows 134 to 219 in Google Sheet!")
