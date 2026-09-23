# -*- coding: utf-8 -*-
"""
=============================================================================
  🚀 PLE-CC Quiz Practice -- Offline Database Compiler
=============================================================================
  Source Sheet: 1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w
  Output: quiz-data-offline.js
=============================================================================
"""

import os, sys, json, re, zipfile, io
from google.oauth2 import service_account
from googleapiclient.discovery import build

sys.stdout.reconfigure(encoding='utf-8')

CREDS_FILE = 'C:/Users/thana/Desktop/PLE-CC/gemini-sheets-editor-497118-060a7f15daf9.json'
SPREADSHEET_ID = '1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w'
OUTPUT_JS = os.path.join(os.path.dirname(__file__), 'quiz-data-offline.js')
IMAGES_DIR = os.path.join(os.path.dirname(__file__), 'images')

print("=" * 65)
print("  📝 PLE-CC Quiz Practice -- Offline Database Compiler")
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

                d_xml = z.read(d_path).decode('utf-8')
                d_root = ET.fromstring(d_xml)

                for anchor in d_root:
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

                    media_file = media_map[embed_id]
                    if media_file in z.namelist():
                        ext = os.path.splitext(media_file)[1]
                        clean_sheet = re.sub(r'[^a-zA-Z0-9_]', '_', sheet_name)
                        out_fname = f"quiz_{clean_sheet}_r{row_idx}_c{col_idx}{ext}"
                        out_path = os.path.join(IMAGES_DIR, out_fname)
                        with open(out_path, 'wb') as out_f:
                            out_f.write(z.read(media_file))
                        rel_path = f"images/{out_fname}"
                        extracted_map[(sheet_name, row_idx, col_idx)] = rel_path
                        print(f"     Found in-cell image: [{sheet_name}] Row {row_idx} Col {col_idx} -> {rel_path}")

        print(f"  ✅ Extracted {len(extracted_map)} in-cell images.")
    except Exception as e:
        print(f"  ℹ️ Image extraction info: {e}")
    return extracted_map

def main():
    images_map = extract_in_cell_images()

    print("\n  📊 Fetching spreadsheet metadata...")
    meta = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
    sheet_names = [s['properties']['title'] for s in meta['sheets']]

    offline_categories = []
    offline_questions = {}
    all_questions_list = []
    total_q_count = 0

    for s_name in sheet_names:
        if s_name.startswith('Log_') or s_name.startswith('Report_') or s_name.startswith('Eval_') or s_name == 'สารบัญ':
            continue

        print(f"  -> Reading sheet: '{s_name}'...")
        res = service.spreadsheets().values().get(
            spreadsheetId=SPREADSHEET_ID,
            range=f"'{s_name}'!A3:O"
        ).execute()

        rows = res.get('values', [])
        questions = []
        track_guess = 'Clinic'

        for idx, row in enumerate(rows):
            row_num = idx + 3
            # Pad row up to 15 columns
            while len(row) < 15:
                row.append('')

            first_col = str(row[0] or '').strip()
            # Detect whether column A is item number
            if first_col.isdigit() or len(rows) > 0 and len(row) >= 15 and (first_col.isdigit() or len(first_col) <= 4):
                offset = 1
                item_no = int(first_col) if first_col.isdigit() else len(questions) + 1
            else:
                offset = 0
                item_no = len(questions) + 1

            q_text = str(row[offset + 0] or '').strip()
            q_img  = str(row[offset + 1] or '').strip()
            c1     = str(row[offset + 2] or '').strip()
            c2     = str(row[offset + 3] or '').strip()
            c3     = str(row[offset + 4] or '').strip()
            c4     = str(row[offset + 5] or '').strip()
            c5     = str(row[offset + 6] or '').strip()
            ans_raw = str(row[offset + 7] or '').strip()
            explanation = str(row[offset + 8] or '').strip()
            ans_img = str(row[offset + 9] or '').strip()
            subtopic = str(row[offset + 10] or '').strip() or s_name
            track    = str(row[offset + 11] or 'Clinic').strip()
            note     = str(row[offset + 12] or '').strip()
            exam_type = str(row[offset + 13] or 'ข้อสอบทั่วไป').strip() or 'ข้อสอบทั่วไป'

            if not q_text and not c1:
                continue

            # Answer key parsing (supports 1, 2, 3, 4, 5 or ก, ข, ค, ง, จ or A, B, C, D, E)
            ans_key = 1
            ans_map = {'ก': 1, 'ข': 2, 'ค': 3, 'ง': 4, 'จ': 5, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5}
            if ans_raw.lower() in ans_map:
                ans_key = ans_map[ans_raw.lower()]
            else:
                try:
                    ans_key = int(re.search(r'\d+', ans_raw).group(0))
                except Exception:
                    ans_key = 1

            # In-cell image resolution
            if not q_img and (s_name, row_num, offset + 1) in images_map:
                q_img = images_map[(s_name, row_num, offset + 1)]
            if not ans_img and (s_name, row_num, offset + 9) in images_map:
                ans_img = images_map[(s_name, row_num, offset + 9)]

            choices = [c1, c2, c3, c4]
            if c5:
                choices.append(c5)

            if track:
                track_guess = track

            q_obj = {
                'id': f"{s_name}::{row_num}",
                'itemNo': item_no,
                'category': s_name,
                'subtopic': subtopic,
                'track': track or 'Clinic',
                'question': q_text,
                'questionImage': q_img,
                'choices': choices,
                'answer': ans_key,
                'explanation': explanation,
                'answerImage': ans_img,
                'note': note,
                'examType': exam_type
            }
            questions.append(q_obj)
            all_questions_list.append(q_obj)

        if questions:
            offline_questions[s_name] = questions
            total_q_count += len(questions)
            offline_categories.append({
                'name': s_name,
                'count': len(questions),
                'track': track_guess
            })
            print(f"     [OK] {len(questions)} questions extracted (Track: {track_guess})")

    # Group all questions by track
    questions_by_track = {
        'all': all_questions_list,
        'clinic': [q for q in all_questions_list if 'clinic' in q.get('track', '').lower()],
        'product': [q for q in all_questions_list if 'product' in q.get('track', '').lower() or 'prod' in q.get('track', '').lower()],
        'sap': [q for q in all_questions_list if 'sap' in q.get('track', '').lower() or 'สังคม' in q.get('track', '').lower()]
    }

    # Generate quiz-data-offline.js
    print(f"\n  💾 Writing to {OUTPUT_JS}...")
    with open(OUTPUT_JS, 'w', encoding='utf-8') as f:
        f.write("/**\n")
        f.write(" * 📝 PLE-CC Quiz Practice -- Auto-compiled Offline Database\n")
        f.write(f" * Total Questions: {total_q_count} across {len(offline_categories)} Categories\n")
        f.write(" */\n\n")
        f.write("window.QUIZ_GOOGLE_SHEET_ID = " + json.dumps(SPREADSHEET_ID) + ";\n")
        f.write("window.QUIZ_GAS_SCRIPT_ID = '1LB8brFu49jQwb5xR3WeeyW2Su_M8e1X2XX3mxD6sxlO7yVwWpDPwG-tS';\n")
        f.write("window.QUIZ_GAS_WEBAPP_URL = 'https://script.google.com/macros/s/AKfycby14F6sdMW67mOv2D6EzRW3NMP6rVnzUHKWjwr_8i10y3NWTOrQPvqmmy6p9LIITNrM/exec';\n\n")
        f.write("window.QUIZ_OFFLINE_CATEGORIES = " + json.dumps(offline_categories, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("window.QUIZ_OFFLINE_QUESTIONS = " + json.dumps(offline_questions, ensure_ascii=False, indent=2) + ";\n\n")
        f.write("window.QUIZ_OFFLINE_BY_TRACK = " + json.dumps(questions_by_track, ensure_ascii=False) + ";\n")

    print(f"\n  🎉 Compilation Complete! Extracted {total_q_count} questions successfully.")

if __name__ == '__main__':
    main()
