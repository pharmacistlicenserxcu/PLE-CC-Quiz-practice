# -*- coding: utf-8 -*-
"""
=============================================================================
  🚀 PLE-CC Quiz Practice -- Offline Database Compiler (v2.0 Clean Edition)
=============================================================================
Source Sheet: 1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w
Output: quiz-data-offline.js
Features:
- Pure clean text for Questions and Choices (NO HTML spans, highlights, or colors).
- Standardized math & comparison symbols (≥, ≤, →, ±).
- Strips student recollection tags and leak banners.
- Clean image resolution (strictly eliminates 'Medium', 'Easy', 'Hard', and placeholders).
- Re-routes questions from '16. Others & Toxic' to their true disease/subject categories.
- High-yield structured clinical & pharmaceutical rationale formatting.
=============================================================================
"""

import os, sys, json, re, zipfile, io, time
from google.oauth2 import service_account
from googleapiclient.discovery import build

sys.stdout.reconfigure(encoding='utf-8')
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from scratch.master_cleaner import clean_text_advanced, clean_image_field, clean_explanation_field, classify_question_precise
from scratch.quality_overhaul_engine import DISTRACTOR_POOLS
from scratch.subtopic_classifier import determine_standard_subtopic
from scratch.advanced_explanation_builder import build_advanced_clinical_explanation

CREDS_FILE = 'C:/Users/thana/Desktop/PLE-CC/gemini-sheets-editor-497118-060a7f15daf9.json'
SPREADSHEET_ID = '1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w'
OUTPUT_JS = os.path.join(os.path.dirname(__file__), 'quiz-data-offline.js')
IMAGES_DIR = os.path.join(os.path.dirname(__file__), 'images')

print("=" * 65)
print("  📝 PLE-CC Quiz Practice -- Offline Database Compiler (v2.0 Clean)")
print(f"  Target Sheet: {SPREADSHEET_ID}")
print("=" * 65)

creds = service_account.Credentials.from_service_account_file(
    CREDS_FILE, scopes=[
        'https://www.googleapis.com/auth/spreadsheets.readonly',
        'https://www.googleapis.com/auth/drive.readonly'
    ]
)

service = build('sheets', 'v4', credentials=creds)
drive_service = build('drive', 'v3', credentials=creds)

def extract_in_cell_images():
    os.makedirs(IMAGES_DIR, exist_ok=True)
    extracted_map = {}
    try:
        print("  🖼️ Checking for in-cell images in Google Sheets...")
        req = drive_service.files().export_media(
            fileId=SPREADSHEET_ID,
            mimeType='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet'
        )
        xlsx_bytes = req.execute()
        import xml.etree.ElementTree as ET
        with zipfile.ZipFile(io.BytesIO(xlsx_bytes)) as z:
            if 'xl/workbook.xml' not in z.namelist() or 'xl/_rels/workbook.xml.rels' not in z.namelist():
                return extracted_map

            wb_xml = z.read('xl/workbook.xml').decode('utf-8')
            root = ET.fromstring(wb_xml)
            sheets_map = {}
            for elem in root.findall('.//{http://schemas.openxmlformats.org/spreadsheetml/2006/main}sheet'):
                name = elem.attrib['name']
                r_id = elem.attrib['{http://schemas.openxmlformats.org/officeDocument/2006/relationships}id']
                sheets_map[r_id] = name

            wb_rels = z.read('xl/_rels/workbook.xml.rels').decode('utf-8')
            rels_root = ET.fromstring(wb_rels)
            sheet_files_map = {}
            for elem in rels_root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                r_id = elem.attrib['Id']
                target = elem.attrib['Target']
                if r_id in sheets_map:
                    sheet_files_map[target] = sheets_map[r_id]

            drawing_to_sheet = {}
            for name in z.namelist():
                if name.startswith('xl/worksheets/_rels/'):
                    sheet_xml = 'worksheets/' + name.replace('xl/worksheets/_rels/', '').replace('.rels', '')
                    sheet_name = sheet_files_map.get(sheet_xml)
                    if not sheet_name: continue
                    rels_content = z.read(name).decode('utf-8')
                    r_elem = ET.fromstring(rels_content)
                    for rel in r_elem.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                        target = rel.attrib.get('Target', '')
                        if 'drawing' in target:
                            d_name = os.path.basename(target)
                            drawing_to_sheet[d_name] = sheet_name

            for d_name, sheet_name in drawing_to_sheet.items():
                d_path = f'xl/drawings/{d_name}'
                d_rels_path = f'xl/drawings/_rels/{d_name}.rels'
                if d_path not in z.namelist() or d_rels_path not in z.namelist():
                    continue

                d_rels_content = z.read(d_rels_path).decode('utf-8')
                d_rels_root = ET.fromstring(d_rels_content)
                media_map = {}
                for rel in d_rels_root.findall('{http://schemas.openxmlformats.org/package/2006/relationships}Relationship'):
                    r_id = rel.attrib['Id']
                    target = rel.attrib['Target']
                    media_map[r_id] = 'xl/' + target.replace('../', '')

                drawing_xml = z.read(d_path).decode('utf-8')
                draw_root = ET.fromstring(drawing_xml)
                for anchor in draw_root.findall('.//{http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}twoCellAnchor') + \
                              draw_root.findall('.//{http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}oneCellAnchor'):
                    from_elem = anchor.find('{http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}from')
                    if from_elem is None: continue
                    col_elem = from_elem.find('{http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}col')
                    row_elem = from_elem.find('{http://schemas.openxmlformats.org/drawingml/2006/spreadsheetDrawing}row')
                    if col_elem is None or row_elem is None: continue
                    col_idx = int(col_elem.text)
                    row_idx = int(row_elem.text) + 1

                    blip = anchor.find('.//{http://schemas.openxmlformats.org/drawingml/2006/main}blip')
                    if blip is None: continue
                    embed_id = blip.attrib.get('{http://schemas.openxmlformats.org/officeDocument/2006/relationships}embed')
                    if not embed_id or embed_id not in media_map: continue

                    img_zip_path = media_map[embed_id]
                    if img_zip_path in z.namelist():
                        img_data = z.read(img_zip_path)
                        ext = os.path.splitext(img_zip_path)[1]
                        safe_sheet = re.sub(r'[^\w\-_\. ]', '_', sheet_name)
                        out_fname = f"{safe_sheet}_r{row_idx}_c{col_idx}{ext}"
                        out_fpath = os.path.join(IMAGES_DIR, out_fname)
                        with open(out_fpath, 'wb') as img_out:
                            img_out.write(img_data)
                        extracted_map[(sheet_name, row_idx, col_idx)] = f"images/{out_fname}"
        print(f"     [OK] Extracted {len(extracted_map)} embedded images.")
    except Exception as e:
        print(f"     [WARN] In-cell image extraction skipped: {e}")
    return extracted_map

def main():
    images_map = extract_in_cell_images()

    print("\n  📊 Fetching spreadsheet metadata...")
    meta = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
    sheet_names = [s['properties']['title'] for s in meta['sheets']]

    offline_questions = {}
    total_q_count = 0

    SYSTEM_SHEETS = {'สารบัญ', 'User_Profiles', 'Community_Chat', 'Report_Quiz_Issues', 'Log_Quiz_Results', 'Template', '🔍 รวมข้อสอบ & กรองข้อมูล'}
    
    # Initialize all target category buckets
    for s in sheet_names:
        if s not in SYSTEM_SHEETS and not s.startswith(('Log_', 'Report_', 'Eval_', 'User_', 'Community_', '🔍')):
            offline_questions[s] = []

    for s_name in sheet_names:
        if s_name in SYSTEM_SHEETS or s_name.startswith(('Log_', 'Report_', 'Eval_', 'User_', 'Community_', '🔍')):
            continue

        print(f"  -> Reading sheet: '{s_name}'...")
        try:
            val_res = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=f"'{s_name}'!A3:P").execute()
            rows = val_res.get('values', [])
        except Exception as e:
            print(f"     [WARN] values.get failed for '{s_name}': {e}")
            continue

        for idx, r in enumerate(rows):
            row_num = idx + 3
            while len(r) < 16:
                r.append('')

            q_num_raw = str(r[0] or '').strip()
            q_text_raw = str(r[1] or '').strip()
            q_img_raw = str(r[2] or '').strip()
            c1_raw = str(r[3] or '').strip()
            c2_raw = str(r[4] or '').strip()
            c3_raw = str(r[5] or '').strip()
            c4_raw = str(r[6] or '').strip()
            c5_raw = str(r[7] or '').strip()
            ans_raw = str(r[8] or '').strip()
            exp_raw = str(r[9] or '').strip()
            ans_img_raw = str(r[10] or '').strip()
            subtopic_raw = str(r[11] or '').strip()
            track_raw = str(r[12] or '').strip()
            note_raw = str(r[13] or '').strip()
            exam_type = str(r[14] or '').strip()
            exam_year = str(r[15] or '').strip()

            # Strict Exam Set Code Mapping (GEMINI.md Rule 2):
            # 'เล่มม่วง' / 'Pharma Plus' -> 'ชุด 1' / 'Mock'
            if re.search(r'เล่มม่วง|pharma\s*plus|pharmaplus', exam_year, re.IGNORECASE):
                exam_year = 'ชุด 1'
                if not exam_type or exam_type == 'ข้อสอบจริง':
                    exam_type = 'Mock'
            if re.search(r'เล่มม่วง|pharma\s*plus|pharmaplus', exam_type, re.IGNORECASE):
                exam_type = 'Mock'
                if not exam_year:
                    exam_year = 'ชุด 1'

            note_raw = re.sub(r'Pharma\s*Plus\s*(?:Fight\s*for\s*Pharmacy\s*License)?', 'ชุด 1', note_raw, flags=re.IGNORECASE)
            note_raw = re.sub(r'เล่มม่วง', 'ชุด 1', note_raw, flags=re.IGNORECASE)

            if not q_text_raw and not c1_raw:
                continue
            if q_text_raw == 'คำถาม' or 'กลับหน้าแรก' in q_text_raw or 'กลับสู่หน้าแรก' in q_text_raw:
                continue

            # 1. Clean Question Text (Pure plain text with proper math symbols)
            q_clean = clean_text_advanced(q_text_raw, is_choice=False)
            if not q_clean:
                q_clean = f"แบบทดสอบความรู้ทางเภสัชกรรม ข้อที่ {idx+1}"

            # 2. Determine True Category & Subtopic
            if s_name == '16. Others & Toxic':
                target_sheet, target_sub, target_track = classify_question_precise(q_clean)
            else:
                target_sheet = s_name
                target_sub = subtopic_raw or determine_standard_subtopic(s_name, q_clean, subtopic_raw)
                target_track = track_raw or ('Product' if any(p in s_name for p in ['Titration', 'Chromatography', 'Spectroscopy', 'Preformulation', 'Calc', 'Solid', 'Liquid', 'Biopharm', 'Sterile', 'Biotech', 'Chemistry', 'Herbal', 'Food']) else ('SAP' if any(s in s_name for s in ['Laws', 'Administration', 'Research']) else 'Clinic'))

            # In Musculoskeleton, strictly normalize subtopic
            if 'musculo' in target_sheet.lower():
                st_low = target_sub.lower()
                if 'gout' in st_low or 'เกาต์' in st_low:
                    target_sub = 'Gout'
                elif 'osteoarthritis' in st_low or 'ข้อเสื่อม' in st_low or 'ข้อเข่า' in st_low or st_low == 'oa':
                    target_sub = 'OA'
                elif 'osteoporosis' in st_low or 'กระดูกพรุน' in st_low or 'กระดูกบาง' in st_low:
                    target_sub = 'Osteoporosis'
                elif 'rheumatoid' in st_low or 'รูมาตอยด์' in st_low or st_low == 'ra':
                    target_sub = 'RA'
                elif not target_sub or target_sub == target_sheet:
                    target_sub = 'OA'

            # 3. Clean Images (Remove Medium/Easy/Hard)
            q_img = clean_image_field(q_img_raw)
            ans_img = clean_image_field(ans_img_raw)
            if not q_img and (s_name, row_num, 1) in images_map:
                q_img = images_map[(s_name, row_num, 1)]
            if not ans_img and (s_name, row_num, 9) in images_map:
                ans_img = images_map[(s_name, row_num, 9)]

            # 4. Standardize Answer (1-5)
            ans_map = {'ก': 1, 'ข': 2, 'ค': 3, 'ง': 4, 'จ': 5, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
            ans_num = ans_map.get(ans_raw.lower())
            if not ans_num:
                m = re.search(r'[1-5]', ans_raw)
                ans_num = int(m.group(0)) if m else 1

            # 5. Clean Choices (Pure single-line text, math symbols standardized)
            raw_choices = [c1_raw, c2_raw, c3_raw, c4_raw, c5_raw]
            choices = [clean_text_advanced(c, is_choice=True) for c in raw_choices]
            
            # Distractor guarantee if blank/dummy or mismatched antidote in non-toxic sheet
            if target_sheet != '16. Others & Toxic' and any(k in c.lower() for c in choices for k in ['sodium thiosulfate', 'dimercaprol', 'calcium disodium edta']):
                choices = ['', '', '', '', '']
                
            pool = DISTRACTOR_POOLS.get(target_sheet, DISTRACTOR_POOLS.get(s_name, DISTRACTOR_POOLS['1. Musculoskeleton']))
            pool_idx = (idx * 3) % len(pool)
            invalid_dummies = {'', 'ไม่มีข้อใดถูกต้อง', 'ถูกทุกข้อที่กล่าวมาข้างต้น', 'ข้อมูลไม่เพียงพอในการสรุปผล', '-', 'Osteoarthritis / Gout', 'Cardiovascular', 'Infectious diseases', 'General Therapeutics'}
            for c_i in range(5):
                if choices[c_i] in invalid_dummies or len(choices[c_i]) < 2:
                    candidate = pool[(pool_idx + c_i) % len(pool)]
                    offset = 1
                    while candidate in choices:
                        candidate = pool[(pool_idx + c_i + offset) % len(pool)]
                        offset += 1
                    choices[c_i] = candidate

            # 6. Format Explanation for Web Display
            choice_letters = ['ก', 'ข', 'ค', 'ง', 'จ']
            ans_letter = choice_letters[ans_num - 1]
            ans_text = choices[ans_num - 1]
            exp_html = build_advanced_clinical_explanation(
                raw_exp=exp_raw,
                choices=choices,
                ans_num=ans_num,
                subtopic=target_sub,
                track=target_track,
                q_text=q_clean,
                for_web=True
            )


            # Format question with clean line breaks
            q_html = q_clean.replace('\n', '<br>')

            item_no = int(q_num_raw) if q_num_raw.isdigit() else len(offline_questions.get(target_sheet, [])) + 1

            q_obj = {
                'id': f"{s_name}::{row_num}",
                'itemNo': item_no,
                'category': target_sheet,
                'subtopic': target_sub,
                'track': target_track,
                'question': q_html,
                'questionImage': q_img,
                'choices': choices,
                'answer': ans_num,
                'explanation': exp_html,
                'answerImage': ans_img,
                'note': note_raw.replace('\n', '<br>'),
                'examType': exam_type,
                'examYear': exam_year
            }

            if target_sheet not in offline_questions:
                offline_questions[target_sheet] = []
            offline_questions[target_sheet].append(q_obj)
            total_q_count += 1

    # Build offline categories list
    offline_categories = []
    track_order = {'Clinic': 1, 'Product': 2, 'SAP': 3}
    for cat_name, q_list in offline_questions.items():
        if not q_list: continue
        cat_track = q_list[0]['track'] if q_list else 'Clinic'
        offline_categories.append({
            'name': cat_name,
            'count': len(q_list),
            'track': cat_track
        })

    # Sort categories nicely: Clinic first, Product second, SAP third
    offline_categories.sort(key=lambda x: (track_order.get(x['track'], 4), x['name']))

    print(f"\n  💾 Writing to {OUTPUT_JS}...")
    with open(OUTPUT_JS, 'w', encoding='utf-8') as f:
        f.write("/**\n")
        f.write(" * 📝 PLE-CC Quiz Practice -- Auto-compiled Offline Database (v2.0 Clean Edition)\n")
        f.write(f" * Total Questions: {total_q_count} across {len(offline_categories)} Categories\n")
        f.write(f" * Build Timestamp: {time_str()}\n")
        f.write(" */\n\n")
        f.write(f'window.QUIZ_GOOGLE_SHEET_ID = "{SPREADSHEET_ID}";\n')
        f.write("window.QUIZ_GAS_SCRIPT_ID = '1LB8brFu49jQwb5xR3WeeyW2Su_M8e1X2XX3mxD6sxlO7yVwWpDPwG-tS';\n")
        f.write("window.QUIZ_GAS_WEBAPP_URL = 'https://script.google.com/macros/s/AKfycby14F6sdMW67mOv2D6EzRW3NMP6rVnzUHKWjwr_8i10y3NWTOrQPvqmmy6p9LIITNrM/exec';\n\n")
        f.write("window.QUIZ_OFFLINE_CATEGORIES = ")
        f.write(json.dumps(offline_categories, ensure_ascii=False, indent=2))
        f.write(";\n\n")
        f.write("window.QUIZ_OFFLINE_QUESTIONS = ")
        f.write(json.dumps(offline_questions, ensure_ascii=False, indent=2))
        f.write(";\n")

    print(f"\n  🎉 Compilation Complete! Extracted {total_q_count} clean questions across {len(offline_categories)} categories successfully.\n")

def time_str():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    main()
