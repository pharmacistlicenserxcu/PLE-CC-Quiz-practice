# -*- coding: utf-8 -*-
"""
batch_replace_pearls_engine.py
Systematically processes tabs in Google Sheets:
1. Identifies rows containing the generic template:
   '• First-line Therapy: จำ first-line drug of choice...'
2. Generates authentic, question-specific and drug-specific pearls using exam_pearls_kb.py
3. Replaces the generic bullet points cleanly in Col J
4. Ensures strict zero-asterisk formatting
5. Updates Google Sheets in batches of 50-100 rows
"""
import sys, os, time, re
import gspread
from google.oauth2.service_account import Credentials

sys.stdout.reconfigure(encoding='utf-8')
sys.path.append('c:/Users/thana/Desktop/PLE-CC/scratch')
from exam_pearls_kb import get_high_yield_exam_pearls

CREDS_FILE = 'c:/Users/thana/Desktop/PLE-CC/gemini-sheets-editor-497118-060a7f15daf9.json'
SPREADSHEET_ID = '1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w'
TARGET_SNIPPET = 'First-line Therapy: จำ first-line drug of choice'

def clean_asterisks(text):
    if not text:
        return ""
    return text.replace('**', '').replace('* ', '• ')

def build_new_explanation(old_exp, ans_text, subtopic, track, q_text):
    if TARGET_SNIPPET not in old_exp:
        return clean_asterisks(old_exp)
        
    pearl_pos = old_exp.find('📌 จุดจำก่อนสอบ:')
    if pearl_pos != -1:
        base_exp = old_exp[:pearl_pos].rstrip()
    else:
        first_line_pos = old_exp.find('• First-line Therapy:')
        if first_line_pos != -1:
            base_exp = old_exp[:first_line_pos].rstrip()
        else:
            base_exp = old_exp
            
    pearl = get_high_yield_exam_pearls('', ans_text, subtopic, track, q_text)
    new_exp = f"{base_exp}\n\n📌 จุดจำก่อนสอบ:\n{pearl}"
    return clean_asterisks(new_exp).strip()

def process_worksheet(ws, doc_title=""):
    print(f"\n==========================================")
    print(f"Processing worksheet: '{ws.title}'")
    print(f"==========================================")
    
    all_vals = ws.get_all_values()
    if len(all_vals) <= 2:
        print("  Sheet has <= 2 rows. Skipping.")
        return 0
        
    # Check headers
    headers = all_vals[1]
    total_rows = len(all_vals)
    print(f"  Total rows in sheet: {total_rows}")
    
    # Identify generic rows
    generic_indices = []
    for r_idx in range(2, total_rows):
        row = all_vals[r_idx]
        exp = row[9] if len(row) > 9 else ''
        if TARGET_SNIPPET in exp:
            generic_indices.append(r_idx)
            
    print(f"  Found {len(generic_indices)} rows with generic template out of {total_rows - 2} questions.")
    if not generic_indices:
        print("  Zero generic templates found! Everything is clean.")
        return 0
        
    # Process in batches
    BATCH_SIZE = 80
    num_updated = 0
    
    for start_i in range(0, len(generic_indices), BATCH_SIZE):
        batch_slice = generic_indices[start_i : start_i + BATCH_SIZE]
        min_row = min(batch_slice) + 1 # 1-indexed
        max_row = max(batch_slice) + 1
        
        # Read the range
        range_str = f"A{min_row}:P{max_row}"
        chunk_vals = ws.get(range_str)
        
        chunk_modified = 0
        for rel_idx, abs_row_idx in enumerate(range(min_row - 1, max_row)):
            row_data = chunk_vals[rel_idx]
            exp = row_data[9] if len(row_data) > 9 else ''
            
            if TARGET_SNIPPET in exp:
                q_text = row_data[1] if len(row_data) > 1 else ''
                opts = [
                    row_data[3] if len(row_data) > 3 else '',
                    row_data[4] if len(row_data) > 4 else '',
                    row_data[5] if len(row_data) > 5 else '',
                    row_data[6] if len(row_data) > 6 else '',
                    row_data[7] if len(row_data) > 7 else ''
                ]
                ans_key = row_data[8] if len(row_data) > 8 else ''
                sub = row_data[11] if len(row_data) > 11 else ''
                trk = row_data[12] if len(row_data) > 12 else ''
                
                ans_text = ''
                try:
                    ans_idx = int(ans_key) - 1
                    if 0 <= ans_idx < len(opts):
                        ans_text = opts[ans_idx]
                except:
                    ans_text = ''
                    
                new_exp = build_new_explanation(exp, ans_text, sub, trk, q_text)
                
                while len(row_data) < 16:
                    row_data.append('')
                row_data[9] = new_exp
                chunk_vals[rel_idx] = row_data
                chunk_modified += 1
                num_updated += 1
                
        if chunk_modified > 0:
            print(f"  Uploading batch {range_str} ({chunk_modified} rows updated)...")
            ws.update(chunk_vals, range_str)
            time.sleep(1.0) # rate limit politeness
            
    print(f"  [COMPLETED] Worksheet '{ws.title}': successfully updated {num_updated} rows.")
    return num_updated

if __name__ == '__main__':
    target_tab = sys.argv[1] if len(sys.argv) > 1 else None
    
    print("Connecting to Google Sheets...")
    gc = gspread.authorize(Credentials.from_service_account_file(CREDS_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets']))
    sh = gc.open_by_key(SPREADSHEET_ID)
    
    SKIP_SHEETS = ['สารบัญ', '🔍 รวมข้อสอบ & กรองข้อมูล', 'User_Profiles', 'Community_Chat', 'Report_Quiz_Issues']
    
    if target_tab and target_tab != 'ALL':
        ws = sh.worksheet(target_tab)
        process_worksheet(ws)
    else:
        # Process all sheets
        all_worksheets = [ws for ws in sh.worksheets() if ws.title not in SKIP_SHEETS]
        print(f"Found {len(all_worksheets)} worksheets to inspect and clean.")
        total_sheets_updated = 0
        total_rows_updated = 0
        
        for ws in all_worksheets:
            try:
                cnt = process_worksheet(ws)
                if cnt > 0:
                    total_sheets_updated += 1
                    total_rows_updated += cnt
                time.sleep(1.5)
            except Exception as e:
                print(f"  [ERROR] on sheet '{ws.title}': {e}")
                time.sleep(3.0)
                
        print(f"\n==========================================")
        print(f"GLOBAL BATCH REPLACE FINISHED!")
        print(f"Updated {total_rows_updated} rows across {total_sheets_updated} worksheets.")
        print(f"==========================================")

