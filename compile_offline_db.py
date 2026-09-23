# -*- coding: utf-8 -*-
"""
=============================================================================
  🚀 PLE-CC Quiz Practice -- Offline Database Compiler (Rich Text Support)
=============================================================================
  Source Sheet: 1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w
  Output: quiz-data-offline.js
  Features:
  - Extracts rich text formatting: Bold, Italic, Font Colors from Google Sheet.
  - Subtopic normalization: OA, RA, Osteoporosis, Gout in Musculoskeletal.
  - Dynamic Exam Type extraction from Column O.
  - Clinical Guideline Note extraction from Column N.
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

def cell_to_html(cell):
    """Converts a Google Sheet cell (with rich text runs, formatting, and markdown) into HTML."""
    if not cell:
        return ''
    val = cell.get('formattedValue', '')
    if not val:
        return ''
    
    runs = cell.get('textFormatRuns', [])
    cell_fmt = cell.get('userEnteredFormat', {}).get('textFormat', {})

    if not runs:
        b = cell_fmt.get('bold', False)
        it = cell_fmt.get('italic', False)
        c = cell_fmt.get('foregroundColor', {})
        sp = []
        if b: sp.append('font-weight:bold')
        if it: sp.append('font-style:italic')
        if c:
            r = int(c.get('red', 0) * 255)
            g = int(c.get('green', 0) * 255)
            bl = int(c.get('blue', 0) * 255)
            if (r, g, bl) not in [(0, 0, 0), (255, 255, 255)]:
                sp.append(f'color:rgb({r},{g},{bl})')
        
        # Parse markdown bold and italic
        v = val.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;')
        v = re.sub(r'\*\*(.+?)\*\*', r'<b>\1</b>', v)
        v = re.sub(r'(?<!\*)\*([^*]+?)\*(?!\*)', r'<i>\1</i>', v)
        v = v.replace('\n', '<br>')
        if sp:
            return f'<span style="{"; ".join(sp)}">{v}</span>'
        return v

    slices = []
    run_starts = [r.get('startIndex', 0) for r in runs]
    run_starts.append(len(val))

    for i in range(len(runs)):
        start = run_starts[i]
        end = run_starts[i + 1]
        chunk = val[start:end]
        fmt = runs[i].get('format', {})
        b = fmt.get('bold', False)
        it = fmt.get('italic', False)
        c = fmt.get('foregroundColor', {})
        sp = []
        if b: sp.append('font-weight:bold')
        if it: sp.append('font-style:italic')
        if c:
            r = int(c.get('red', 0) * 255)
            g = int(c.get('green', 0) * 255)
            bl = int(c.get('blue', 0) * 255)
            if (r, g, bl) not in [(0, 0, 0), (255, 255, 255)]:
                sp.append(f'color:rgb({r},{g},{bl})')
        
        ch = chunk.replace('&', '&amp;').replace('<', '&lt;').replace('>', '&gt;').replace('\n', '<br>')
        if sp:
            slices.append(f'<span style="{"; ".join(sp)}">{ch}</span>')
        else:
            slices.append(ch)

    return ''.join(slices)

def main():
    images_map = extract_in_cell_images()

    print("\n  📊 Fetching spreadsheet metadata...")
    meta = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
    sheet_names = [s['properties']['title'] for s in meta['sheets']]

    offline_categories = []
    offline_questions = {}
    total_q_count = 0

    SYSTEM_SHEETS = {'สารบัญ', 'User_Profiles', 'Community_Chat', 'Report_Quiz_Issues', 'Log_Quiz_Results', 'Template', '🔍 รวมข้อสอบ & กรองข้อมูล'}
    for s_name in sheet_names:
        if s_name in SYSTEM_SHEETS or s_name.startswith(('Log_', 'Report_', 'Eval_', 'User_', 'Community_', '🔍')):
            continue

        print(f"  -> Reading sheet: '{s_name}' (with rich text gridData)...")
        try:
            res = service.spreadsheets().get(
                spreadsheetId=SPREADSHEET_ID,
                ranges=[f"'{s_name}'!A3:P"],
                includeGridData=True
            ).execute()
            sheet_obj = res['sheets'][0]
            data_obj = sheet_obj['data'][0]
            row_data = data_obj.get('rowData', [])
        except Exception as e:
            print(f"     [WARN] Fallback values.get for '{s_name}': {e}")
            val_res = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=f"'{s_name}'!A3:P").execute()
            raw_rows = val_res.get('values', [])
            row_data = []
            for r in raw_rows:
                cells = [{'formattedValue': str(x)} for x in r]
                row_data.append({'values': cells})

        questions = []
        track_guess = 'Clinic'

        for idx, r_obj in enumerate(row_data):
            row_num = idx + 3
            cells = r_obj.get('values', [])
            while len(cells) < 16:
                cells.append({})

            def get_plain(col_i):
                if col_i < len(cells):
                    return str(cells[col_i].get('formattedValue', '') or '').strip()
                return ''

            def get_html(col_i):
                if col_i < len(cells):
                    return cell_to_html(cells[col_i]).strip()
                return ''

            first_col = get_plain(0)
            if first_col.isdigit() or (len(cells) >= 16 and len(first_col) <= 4 and first_col.isdigit()):
                offset = 1
                item_no = int(first_col) if first_col.isdigit() else len(questions) + 1
            else:
                offset = 0
                item_no = len(questions) + 1

            q_text_html = get_html(offset + 0)
            q_text_plain = get_plain(offset + 0)
            q_img = get_plain(offset + 1)
            c1 = get_html(offset + 2)
            c2 = get_html(offset + 3)
            c3 = get_html(offset + 4)
            c4 = get_html(offset + 5)
            c5 = get_html(offset + 6)
            ans_raw = get_plain(offset + 7)
            exp_html = get_html(offset + 8)
            ans_img = get_plain(offset + 9)
            subtopic = get_plain(offset + 10) or s_name
            track = get_plain(offset + 11) or 'Clinic'
            note_html = get_html(offset + 12)
            exam_type = get_plain(offset + 13)
            exam_year = get_plain(offset + 14)

            if not q_text_plain and not c1:
                continue
            if 'คำถาม' in q_text_plain or 'กลับหน้าแรก' in q_text_plain:
                continue

            def sanitize_choice_str(val):
                if not val: return ''
                v = re.sub(r'<\s*br\s*/?\s*>', ' ', str(val), flags=re.IGNORECASE)
                v = re.sub(r'---', '', v)
                return re.sub(r'\s+', ' ', v).strip()

            c1 = sanitize_choice_str(c1)
            c2 = sanitize_choice_str(c2)
            c3 = sanitize_choice_str(c3)
            c4 = sanitize_choice_str(c4)
            c5 = sanitize_choice_str(c5)

            # In Musculoskeleton, ensure subtopic is strictly OA, RA, Osteoporosis, or Gout
            if 'musculo' in s_name.lower():
                st_low = subtopic.lower()
                if 'gout' in st_low or 'เกาต์' in st_low:
                    subtopic = 'Gout'
                elif 'osteoarthritis' in st_low or 'ข้อเสื่อม' in st_low or 'ข้อเข่า' in st_low or st_low == 'oa':
                    subtopic = 'OA'
                elif 'osteoporosis' in st_low or 'กระดูกพรุน' in st_low or 'กระดูกบาง' in st_low:
                    subtopic = 'Osteoporosis'
                elif 'rheumatoid' in st_low or 'รูมาตอยด์' in st_low or st_low == 'ra':
                    subtopic = 'RA'
                elif not subtopic or subtopic == s_name:
                    subtopic = 'OA'

            # Answer key parsing
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
                'question': q_text_html,
                'questionImage': q_img,
                'choices': choices,
                'answer': ans_key,
                'explanation': exp_html,
                'answerImage': ans_img,
                'note': note_html,
                'examType': exam_type,
                'examYear': exam_year
            }
            questions.append(q_obj)

        if questions:
            offline_questions[s_name] = questions
            offline_categories.append({
                'name': s_name,
                'count': len(questions),
                'track': track_guess
            })
            total_q_count += len(questions)
            print(f"     [OK] {len(questions)} questions extracted (Track: {track_guess})")

    # Output JS file
    print(f"\n  💾 Writing to {OUTPUT_JS}...")
    with open(OUTPUT_JS, 'w', encoding='utf-8') as f:
        f.write("/**\n")
        f.write(" * 📝 PLE-CC Quiz Practice -- Auto-compiled Offline Database (Rich Text & Column O)\n")
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

    print(f"\n  🎉 Compilation Complete! Extracted {total_q_count} questions successfully.\n")

def time_str():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    main()
