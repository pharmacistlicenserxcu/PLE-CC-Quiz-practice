# -*- coding: utf-8 -*-
"""
=============================================================================
  🚀 PLE-CC Quiz Practice -- Offline Database Compiler (v2.1 Pro Edition)
=============================================================================
Source Sheet: 1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w
Output: quiz-data-offline.js
Features:
- Pure clean text for Questions and Choices (NO HTML spans, highlights, or colors).
- Standardized math & comparison symbols (≥, ≤, →, ±).
- Strips student recollection tags and leak banners.
- Clean image resolution (strictly eliminates 'Medium', 'Easy', 'Hard', and placeholders).
- High-yield structured clinical & pharmaceutical rationale formatting.
- Selective / Incremental Compilation ("แยกเรื่อง") with Smart Merge.
- Remote Compile & Push via GitHub Actions or Local Batch runner.
- Auto-bump Service Worker cache in sw.js.
=============================================================================
"""

import os, sys, json, re, zipfile, io, time, argparse

sys.stdout.reconfigure(encoding='utf-8')

# Support running from within PLE CC Quiz or root repo
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.abspath(os.path.join(CURRENT_DIR, '..'))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)

# Import self-contained utils with fallback
try:
    from utils.master_cleaner import clean_text_advanced, clean_image_field, clean_explanation_field, classify_question_precise
    from utils.distractor_engine import DISTRACTOR_POOLS
    from utils.subtopic_classifier import determine_standard_subtopic
except ImportError:
    from scratch.master_cleaner import clean_text_advanced, clean_image_field, clean_explanation_field, classify_question_precise
    from scratch.quality_overhaul_engine import DISTRACTOR_POOLS
    from scratch.subtopic_classifier import determine_standard_subtopic

from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDS_FILE = 'C:/Users/thana/Desktop/PLE-CC/gemini-sheets-editor-497118-060a7f15daf9.json'
SPREADSHEET_ID = '1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w'
GAS_SCRIPT_ID = '1LB8brFu49jQwb5xR3WeeyW2Su_M8e1X2XX3mxD6sxlO7yVwWpDPwG-tS'
GAS_WEBAPP_URL = 'https://script.google.com/macros/s/AKfycby14F6sdMW67mOv2D6EzRW3NMP6rVnzUHKWjwr_8i10y3NWTOrQPvqmmy6p9LIITNrM/exec'

def get_google_credentials():
    """Load credentials from environment variable (GitHub Secrets) or local JSON file."""
    sa_json = os.environ.get('GCP_SA_KEY') or os.environ.get('COMPILE_AND_PUSH')
    scopes = [
        'https://www.googleapis.com/auth/spreadsheets.readonly',
        'https://www.googleapis.com/auth/drive.readonly'
    ]
    if sa_json:
        try:
            info = json.loads(sa_json)
            return service_account.Credentials.from_service_account_info(info, scopes=scopes)
        except Exception as e:
            print(f"  [WARN] Failed to load credentials from GCP_SA_KEY env: {e}")
            
    if os.path.exists(CREDS_FILE):
        return service_account.Credentials.from_service_account_file(CREDS_FILE, scopes=scopes)
        
    # Check parent dir
    parent_creds = os.path.join(PARENT_DIR, 'gemini-sheets-editor-497118-060a7f15daf9.json')
    if os.path.exists(parent_creds):
        return service_account.Credentials.from_service_account_file(parent_creds, scopes=scopes)
        
    raise FileNotFoundError(f"Could not find credentials in GCP_SA_KEY/COMPILE_AND_PUSH or at {CREDS_FILE}")

def load_existing_quiz_data(output_js_path):
    """Parse existing categories and questions from quiz-data-offline.js for smart merge."""
    if not os.path.exists(output_js_path):
        return [], {}
    try:
        with open(output_js_path, 'r', encoding='utf-8') as f:
            content = f.read()
        m_cat = re.search(r'window\.QUIZ_OFFLINE_CATEGORIES\s*=\s*(\[.*?\]);\s*\n', content, re.DOTALL)
        m_q = re.search(r'window\.QUIZ_OFFLINE_QUESTIONS\s*=\s*(\{.*?\});\s*$', content, re.DOTALL)
        if m_cat and m_q:
            cats = json.loads(m_cat.group(1))
            qs = json.loads(m_q.group(1))
            return cats, qs
    except Exception as e:
        print(f"  [WARN] Could not parse existing quiz-data-offline.js: {e}")
    return [], {}

def extract_in_cell_images(drive_service, images_dir):
    """Extract embedded in-cell images from Google Sheets."""
    os.makedirs(images_dir, exist_ok=True)
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
                        ext = os.path.splitext(img_zip_path)[1].lower()
                        if not ext: ext = '.png'
                        if 'รวม' in sheet_name or 'ด่วน' in sheet_name or 'QI_' in sheet_name:
                            safe_sheet = 'quick_ingest'
                        elif 'Medicinal' in sheet_name:
                            safe_sheet = 'medchem'
                        else:
                            safe_sheet = re.sub(r'[^a-zA-Z0-9_]', '_', sheet_name).strip('_') or 'sheet'
                        out_fname = f"qimg_{safe_sheet}_r{row_idx}_c{col_idx}{ext}"
                        out_fpath = os.path.join(images_dir, out_fname)
                        with open(out_fpath, 'wb') as img_out:
                            img_out.write(img_data)
                        extracted_map[(sheet_name, row_idx, col_idx)] = f"images/{out_fname}"
        print(f"     [OK] Extracted {len(extracted_map)} embedded images.")
    except Exception as e:
        print(f"     [WARN] In-cell image extraction skipped: {e}")
    return extracted_map

def bump_service_worker_cache(sw_path):
    """Automatically increment Service Worker cache version in sw.js."""
    if not os.path.exists(sw_path):
        return
    try:
        with open(sw_path, 'r', encoding='utf-8') as f:
            content = f.read()
        m = re.search(r"const\s+CACHE_NAME\s*=\s*['\"]ple-cc-quiz-practice-v(\d+)['\"];", content)
        if m:
            curr_v = int(m.group(1))
            new_v = curr_v + 1
            new_content = content[:m.start(1)] + str(new_v) + content[m.end(1):]
            with open(sw_path, 'w', encoding='utf-8') as f:
                f.write(new_content)
            print(f"  ⚡ Service Worker cache bumped: v{curr_v} -> v{new_v}")
        else:
            print("  [INFO] Service Worker cache version pattern not matched.")
    except Exception as e:
        print(f"  [WARN] Failed to bump Service Worker cache: {e}")

def get_track_for_sheet(sheet_name):
    """Determine Track (Clinic, Product, SAP) from sheet name."""
    product_keywords = ['Titration', 'Chromatography', 'Spectroscopy', 'Preformulation', 'Calc', 'Solid', 'Liquid', 'Biopharm', 'Sterile', 'Biotech', 'Chemistry', 'Herbal', 'Food']
    sap_keywords = ['Laws', 'Administration', 'Research']
    if any(p in sheet_name for p in product_keywords):
        return 'Product'
    elif any(s in sheet_name for s in sap_keywords):
        return 'SAP'
    return 'Clinic'

def post_process_cases(offline_questions):
    """Post-process Case Clusters: Auto-Split duplicate Q1s, auto-assign order, and sort Type INT by Track Priority."""
    case_clusters = {}
    for cat_name, q_list in offline_questions.items():
        for q in q_list:
            gid = q.get('caseGroupId')
            if gid:
                scoped_key = f"{q.get('examYear') or 'all'}__{gid}"
                if scoped_key not in case_clusters:
                    case_clusters[scoped_key] = []
                case_clusters[scoped_key].append(q)

    track_priority = {'clinic': 1, 'product': 2, 'sap': 3}
    final_split_clusters = []

    for scoped_key, cluster_qs in case_clusters.items():
        q1_count = sum(1 for q in cluster_qs if q.get('caseOrder') == 1)
        if q1_count > 1:
            chunks = []
            curr_chunk = []
            for q in cluster_qs:
                if q.get('caseOrder') == 1 and curr_chunk:
                    chunks.append(curr_chunk)
                    curr_chunk = []
                curr_chunk.append(q)
            if curr_chunk:
                chunks.append(curr_chunk)

            for chunk_idx, chunk in enumerate(chunks, 1):
                split_suffix = f"__p{chunk_idx}"
                for q in chunk:
                    if not q['caseGroupId'].endswith(split_suffix):
                        q['caseGroupId'] = f"{q['caseGroupId']}{split_suffix}"
                final_split_clusters.append(chunk)
        else:
            final_split_clusters.append(cluster_qs)

    for cluster_qs in final_split_clusters:
        is_int = any(q.get('caseType') == 'INT' or '_INT_' in q.get('caseGroupId', '') for q in cluster_qs)
        if is_int:
            for q in cluster_qs:
                q['caseType'] = 'INT'
            cluster_qs.sort(key=lambda x: (track_priority.get(x.get('track', '').lower(), 99), x.get('caseOrder') or 0))
        else:
            cluster_qs.sort(key=lambda x: x.get('caseOrder') or 0)

        for idx, q in enumerate(cluster_qs):
            q['caseOrder'] = idx + 1
            q['caseTotal'] = len(cluster_qs)

def main():
    parser = argparse.ArgumentParser(description='PLE-CC Quiz Offline Database Compiler (v2.1 Pro)')
    parser.add_argument('--mode', choices=['all', 'category', 'track'], default='all',
                        help='Compilation mode: all (rebuild all), category (selective category), track (Clinic/Product/SAP)')
    parser.add_argument('--query', type=str, default='',
                        help='Search query for selective category or track name')
    parser.add_argument('--web-dir', type=str, default=CURRENT_DIR,
                        help='Path to PLE CC Quiz web directory')
    parser.add_argument('--skip-images', action='store_true',
                        help='Skip in-cell image extraction export')
    parser.add_argument('--no-sw-bump', action='store_true',
                        help='Do not bump Service Worker cache version')
    args = parser.parse_args()

    mode = args.mode
    query = (args.query or '').strip()
    web_dir = os.path.abspath(args.web_dir)
    output_js = os.path.join(web_dir, 'quiz-data-offline.js')
    sw_js = os.path.join(web_dir, 'sw.js')
    images_dir = os.path.join(web_dir, 'images')

    print("=" * 65)
    print("  📝 PLE-CC Quiz Practice -- Offline Database Compiler (v2.1 Pro)")
    print(f"  Target Sheet : {SPREADSHEET_ID}")
    print(f"  Mode         : {mode}")
    if query:
        print(f"  Query        : {query}")
    print(f"  Output JS    : {output_js}")
    print("=" * 65)

    start_time = time.time()
    creds = get_google_credentials()
    service = build('sheets', 'v4', credentials=creds)
    drive_service = build('drive', 'v3', credentials=creds)

    # 1. Fetch metadata & all sheet names
    print("\n  📊 Fetching spreadsheet metadata...")
    meta = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
    sheet_names = [s['properties']['title'] for s in meta['sheets']]

    SYSTEM_SHEETS = {'สารบัญ', 'User_Profiles', 'Community_Chat', 'Report_Quiz_Issues', 'Log_Quiz_Results', 'Template', '🔍 รวมข้อสอบ & กรองข้อมูล', '📑 ทะเบียนรหัสเคส', '📖 System Guideline (คู่มือระบบ)'}
    
    def is_sys_sheet(name):
        return (name in SYSTEM_SHEETS or 
                name.startswith(('Log_', 'Report_', 'Eval_', 'User_', 'Community_', '🔍', '📑', '📖')) or 
                'ทะเบียน' in name or 
                'Guideline' in name or 
                'คู่มือ' in name)

    content_sheets = [s for s in sheet_names if not (is_sys_sheet(s) or s.startswith(('📥', 'QI_')) or 'ด่วน' in s)]
    ingestion_sheets = [s for s in sheet_names if s.startswith(('📥', 'QI_')) or 'ด่วน' in s]

    # 2. Determine target sheets to compile based on mode
    target_content_sheets = []
    is_selective = (mode in ['category', 'track'])

    if mode == 'all':
        target_content_sheets = content_sheets
        print(f"  🌐 Mode 'all': Compiling all {len(content_sheets)} categories.")
    elif mode == 'category':
        if not query:
            print("  [ERROR] Mode 'category' requires --query (e.g. 'Musculo' or 'Cardio')")
            sys.exit(1)
        q_low = query.lower()
        target_content_sheets = [s for s in content_sheets if q_low in s.lower()]
        if not target_content_sheets:
            print(f"  [ERROR] No category matched query: '{query}'")
            print("  Available categories:")
            for s in content_sheets:
                print(f"    - {s}")
            sys.exit(1)
        print(f"  🎯 Mode 'category': Matched {len(target_content_sheets)} category/categories:")
        for s in target_content_sheets:
            print(f"     -> {s}")
    elif mode == 'track':
        if not query:
            print("  [ERROR] Mode 'track' requires --query ('Clinic', 'Product', or 'SAP')")
            sys.exit(1)
        q_track = query.strip().capitalize()
        target_content_sheets = [s for s in content_sheets if get_track_for_sheet(s).lower() == q_track.lower()]
        if not target_content_sheets:
            print(f"  [ERROR] No sheets found for track: '{query}'. Choose Clinic, Product, or SAP.")
            sys.exit(1)
        print(f"  🏷️ Mode 'track': Matched {len(target_content_sheets)} sheets for Track '{q_track}'.")

    # 3. Smart Merge: Load existing database if selective mode
    offline_questions = {}
    if is_selective:
        existing_cats, existing_qs = load_existing_quiz_data(output_js)
        if existing_qs:
            print(f"  📦 Smart Merge: Loaded existing offline DB with {len(existing_qs)} categories.")
            offline_questions = existing_qs
            # Clear questions for target sheets so we replace them fresh
            for s in target_content_sheets:
                offline_questions[s] = []
        else:
            print("  [INFO] No existing offline DB found. Building fresh target categories.")
            for s in target_content_sheets:
                offline_questions[s] = []
    else:
        # Full mode: Initialize all content sheet buckets
        for s in content_sheets:
            offline_questions[s] = []

    # 4. In-cell images extraction (Skip in selective unless explicitly asked)
    images_map = {}
    should_extract_images = not args.skip_images if mode == 'all' else (not args.skip_images and False)
    if should_extract_images:
        images_map = extract_in_cell_images(drive_service, images_dir)
    else:
        print("  ⚡ In-cell image extraction skipped for maximum compile speed.")

    # 5. Process sheets
    # If selective, we only fetch target content sheets (and ingestion sheet if category belongs to it)
    sheets_to_process = target_content_sheets + ingestion_sheets

    for s_name in sheets_to_process:
        is_ingestion_sheet = s_name.startswith(('📥', 'QI_')) or 'ด่วน' in s_name
        print(f"  -> Reading sheet: '{s_name}'...")
        read_range = f"'{s_name}'!A2:Z"
        try:
            val_res = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range=read_range).execute()
            rows = val_res.get('values', [])
        except Exception as e:
            print(f"     [WARN] values.get failed for '{s_name}': {e}")
            continue

        if not rows:
            continue

        # Inspect Row 2 header
        header_row = [str(x or '').strip().lower() for x in rows[0]]
        case_col_idx = -1
        category_tag_col_idx = -1
        for h_idx, h_text in enumerate(header_row):
            if 'case' in h_text or 'เคส' in h_text:
                case_col_idx = h_idx
            elif 'ปลายทาง' in h_text or 'หมวดวิชา/ชีต' in h_text:
                category_tag_col_idx = h_idx

        if case_col_idx == -1:
            case_col_idx = 17 if is_ingestion_sheet else 16
        if category_tag_col_idx == -1 and is_ingestion_sheet:
            category_tag_col_idx = 16

        data_rows = rows[1:]

        for idx, r in enumerate(data_rows):
            row_num = idx + 3
            needed_cols = max(18, case_col_idx + 1)
            while len(r) < needed_cols:
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
            
            category_tag = ''
            if is_ingestion_sheet:
                if category_tag_col_idx != -1 and category_tag_col_idx < len(r):
                    category_tag = str(r[category_tag_col_idx] or '').strip()
                elif len(r) > 16:
                    category_tag = str(r[16] or '').strip()

            target_sheet = category_tag if (is_ingestion_sheet and category_tag) else s_name

            # In selective mode, skip questions not belonging to target sheets
            if is_selective and target_sheet not in target_content_sheets:
                continue

            case_id_raw = ''
            if case_col_idx != -1 and case_col_idx < len(r):
                case_id_raw = str(r[case_col_idx] or '').strip()

            if not case_id_raw:
                for cell in r:
                    val_str = str(cell or '').strip()
                    if re.match(r'^CASE_', val_str, re.I):
                        case_id_raw = val_str
                        break

            if not case_id_raw and note_raw:
                m_case = re.search(r'\[CASE:\s*([^\]]+)\]', note_raw, re.I)
                if m_case:
                    case_id_raw = m_case.group(1).strip()

            case_group_id = ''
            case_order = 0
            case_type = ''
            if case_id_raw:
                clean_case = re.sub(r'\s+', '', case_id_raw.upper())
                m_q = re.search(r'^(.*?)(?:[_\-]Q(\d+))?$', clean_case)
                if m_q:
                    case_group_id = m_q.group(1)
                    case_order = int(m_q.group(2)) if m_q.group(2) else 0
                else:
                    case_group_id = clean_case
                    case_order = 0

                if '_INT_' in case_group_id or case_group_id.startswith('CASE_INT'):
                    case_type = 'INT'
                elif '_CLN_' in case_group_id or case_group_id.startswith('CASE_CLN'):
                    case_type = 'CLN'
                elif '_PRD_' in case_group_id or case_group_id.startswith('CASE_PRD'):
                    case_type = 'PRD'
                elif '_SAP_' in case_group_id or case_group_id.startswith('CASE_SAP'):
                    case_type = 'SAP'
                else:
                    case_type = 'STD'

            if is_ingestion_sheet and not category_tag:
                continue

            if not q_text_raw and not c1_raw:
                continue
            if q_text_raw == 'คำถาม' or 'กลับหน้าแรก' in q_text_raw or 'กลับสู่หน้าแรก' in q_text_raw:
                continue

            # 1. Clean Question Text
            q_clean = clean_text_advanced(q_text_raw, is_choice=False)
            if not q_clean:
                q_clean = f"แบบทดสอบความรู้ทางเภสัชกรรม ข้อที่ {idx+1}"

            # 2. Subtopic & Track
            target_sub = subtopic_raw or determine_standard_subtopic(target_sheet, q_clean, subtopic_raw)
            target_track = track_raw or get_track_for_sheet(target_sheet)

            # Musculoskeleton subtopic normalization
            if 'musculo' in target_sheet.lower():
                parts = [p.strip() for p in re.split(r'[/,;]', target_sub) if p.strip()]
                if not parts:
                    target_sub = 'OA'
                else:
                    norm_parts = []
                    for p in parts:
                        st_low = p.lower()
                        if 'gout' in st_low or 'เกาต์' in st_low:
                            norm_parts.append('Gout')
                        elif 'osteoarthritis' in st_low or 'ข้อเสื่อม' in st_low or 'ข้อเข่า' in st_low or st_low == 'oa':
                            norm_parts.append('OA')
                        elif 'osteoporosis' in st_low or 'กระดูกพรุน' in st_low or 'กระดูกบาง' in st_low:
                            norm_parts.append('Osteoporosis')
                        elif 'rheumatoid' in st_low or 'รูมาตอยด์' in st_low or st_low == 'ra':
                            norm_parts.append('RA')
                        elif p and p != target_sheet:
                            norm_parts.append(p)
                    if not norm_parts:
                        norm_parts = ['OA']
                    seen = set()
                    target_sub = ' / '.join([x for x in norm_parts if not (x in seen or seen.add(x))])

            # 3. Clean Images
            q_img = clean_image_field(q_img_raw)
            ans_img = clean_image_field(ans_img_raw)
            if not q_img and images_map:
                for c in [2, 1, 0, 3]:
                    if (s_name, row_num, c) in images_map:
                        q_img = images_map[(s_name, row_num, c)]
                        break
            if not ans_img and images_map:
                for c in [10, 9, 8, 11]:
                    if (s_name, row_num, c) in images_map:
                        ans_img = images_map[(s_name, row_num, c)]
                        break

            # 4. Standardize Answer (1-5)
            ans_map = {'ก': 1, 'ข': 2, 'ค': 3, 'ง': 4, 'จ': 5, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
            ans_num = ans_map.get(ans_raw.lower())
            if not ans_num:
                m = re.search(r'[1-5]', ans_raw)
                ans_num = int(m.group(0)) if m else 1

            # 5. Clean Choices
            raw_choices = [c1_raw, c2_raw, c3_raw, c4_raw, c5_raw]
            choices = [clean_text_advanced(c, is_choice=True) for c in raw_choices]
            
            # Distractor guarantee
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

            # 6. Format Explanation
            choice_letters = ['ก', 'ข', 'ค', 'ง', 'จ']
            ans_letter = choice_letters[ans_num - 1]
            ans_text = choices[ans_num - 1]
            
            if exp_raw and exp_raw.strip():
                clean_exp = clean_text_advanced(exp_raw.strip(), is_choice=False)
                exp_html = clean_exp.replace('\n', '<br>')
            else:
                exp_html = f"✅ คำตอบที่ถูกต้อง: ข้อ {ans_letter}. {ans_text}"

            q_html = q_clean.replace('\n', '<br>')
            item_no = int(q_num_raw) if q_num_raw.isdigit() else len(offline_questions.get(target_sheet, [])) + 1

            # Exam type auto mapping
            clean_exam_type = exam_type
            if clean_exam_type.lower() == 'mock' or clean_exam_type == 'Mock Exam' or clean_exam_type == 'ข้อสอบ Mock':
                clean_exam_type = 'ข้อสอบจำลอง'

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
                'examType': clean_exam_type,
                'examYear': exam_year,
                'caseGroupId': case_group_id,
                'caseOrder': case_order,
                'caseType': case_type
            }

            if target_sheet not in offline_questions:
                offline_questions[target_sheet] = []
            offline_questions[target_sheet].append(q_obj)

    # 6. Post-process Cases
    post_process_cases(offline_questions)

    # 7. Build categories metadata
    offline_categories = []
    track_order = {'Clinic': 1, 'Product': 2, 'SAP': 3}
    total_q_count = 0

    for cat_name, q_list in offline_questions.items():
        if not q_list: continue
        cat_track = q_list[0]['track'] if q_list else get_track_for_sheet(cat_name)
        total_q_count += len(q_list)
        offline_categories.append({
            'name': cat_name,
            'count': len(q_list),
            'track': cat_track
        })

    offline_categories.sort(key=lambda x: (track_order.get(x['track'], 4), x['name']))

    # 8. Write quiz-data-offline.js
    print(f"\n  💾 Writing to {output_js}...")
    with open(output_js, 'w', encoding='utf-8') as f:
        f.write("/**\n")
        f.write(" * 📝 PLE-CC Quiz Practice -- Auto-compiled Offline Database (v2.1 Pro Edition)\n")
        f.write(f" * Total Questions: {total_q_count} across {len(offline_categories)} Categories\n")
        f.write(f" * Build Timestamp: {time_str()}\n")
        f.write(f" * Build Mode: {mode} (query: '{query}')\n")
        f.write(" */\n\n")
        f.write(f'window.QUIZ_GOOGLE_SHEET_ID = "{SPREADSHEET_ID}";\n')
        f.write(f"window.QUIZ_GAS_SCRIPT_ID = '{GAS_SCRIPT_ID}';\n")
        f.write(f"window.QUIZ_GAS_WEBAPP_URL = '{GAS_WEBAPP_URL}';\n\n")
        f.write("window.QUIZ_OFFLINE_CATEGORIES = ")
        f.write(json.dumps(offline_categories, ensure_ascii=False, indent=2))
        f.write(";\n\n")
        f.write("window.QUIZ_OFFLINE_QUESTIONS = ")
        f.write(json.dumps(offline_questions, ensure_ascii=False, indent=2))
        f.write(";\n")

    # 9. Bump Service Worker cache
    if not args.no_sw_bump:
        bump_service_worker_cache(sw_js)

    elapsed = time.time() - start_time
    print(f"\n  🎉 Compilation Complete! Extracted {total_q_count} clean questions across {len(offline_categories)} categories.")
    print(f"  ⏱️ Time taken: {elapsed:.2f} seconds.\n")

def time_str():
    import datetime
    return datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if __name__ == '__main__':
    main()
