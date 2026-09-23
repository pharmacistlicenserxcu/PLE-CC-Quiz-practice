# -*- coding: utf-8 -*-
"""
parse_musculo.py
Extracts pure clinical questions for Musculoskeletal from Exam Extract Muscle ข้อสอบเก่า.md:
- Filters out non-clinic questions (Med Chem, Pharm Tech, QC, Calculations, Forensic Law, Pharmacoeconomics, CNS).
- Strictly classifies each question into one of 4 subtopics: 'OA', 'RA', 'Osteoporosis', 'Gout'.
- Sanitizes choices to prevent choice 5 leaks.
- Structures high-yield clinical explanations (Correct Answer, Clinical Rationale, Distractor Analysis, Guideline Pearls).
- Properly maps columns for Google Sheet (Col L: Subtopic, Col M: Clinic, Col N: Clinical Note, Col O: Exam Type).
"""

import os, sys, re

sys.stdout.reconfigure(encoding='utf-8')

FILE = r'C:\Users\thana\Desktop\PLE-CC\Contents\CC1 Clinic\1. Musculoskeletal\Exam Extract Muscle ข้อสอบเก่า.md'

with open(FILE, 'r', encoding='utf-8') as f:
    raw_content = f.read()

parts = raw_content.split('## 📌 เฉลยละเอียดข้อสอบเก่า')
q_section = parts[0]
a_section = parts[1] if len(parts) > 1 else ''

# 1. Parse raw answer blocks
ans_map = {}
a_blocks = re.split(r'###\s*เฉลยข้อ(?:ที่|\s*=)\s*', a_section)
for ab in a_blocks[1:]:
    lines = ab.strip().split('\n')
    m_num = re.match(r'(\d+)', lines[0])
    if not m_num: continue
    q_num = int(m_num.group(1))
    
    m_ans = re.search(r'คำตอบ[*:\s]+([ก-จa-eA-E1-5])', ab)
    letter = m_ans.group(1) if m_ans else 'ก'
    mapping = {'ก': 1, 'ข': 2, 'ค': 3, 'ง': 4, 'จ': 5, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
    ans_key = mapping.get(letter.lower(), 1)
    ans_map[q_num] = {
        'key': ans_key,
        'letter': letter,
        'raw_text': ab.strip()
    }

# 2. Parse Case Scenarios
case_scenarios = {}
case_matches = re.finditer(r'(\*{0,2}กรณีศึกษาที่\s*([A-Za-zก-ฮ0-9]+)[^\n]*\((?:ข้อ\s*)?(\d+)\s*[-–—]\s*(\d+)\)\*{0,2}[\s\S]*?)(?=###\s*ข้อที่|\Z)', q_section)
for cm in case_matches:
    full_block = cm.group(1).strip()
    start_q = int(cm.group(3))
    end_q = int(cm.group(4))
    scenario_lines = full_block.split('\n')
    scenario_text = '\n'.join([l.strip() for l in scenario_lines if l.strip()])
    for q_idx in range(start_q, end_q + 1):
        case_scenarios[q_idx] = scenario_text

# Exact Subtopic mapping for the 70 Pure Clinical Questions
SUBTOPIC_MAP = {
    # Gout (26 questions)
    1: 'Gout', 2: 'Gout', 3: 'Gout', 5: 'Gout', 8: 'Gout', 9: 'Gout',
    11: 'Gout', 13: 'Gout', 20: 'Gout', 21: 'Gout', 22: 'Gout',
    24: 'Gout', 25: 'Gout', 26: 'Gout', 27: 'Gout',
    36: 'Gout', 37: 'Gout', 38: 'Gout', 39: 'Gout', 40: 'Gout', 41: 'Gout', 45: 'Gout',
    85: 'Gout', 86: 'Gout', 87: 'Gout', 88: 'Gout',
    
    # OA (25 questions)
    6: 'OA', 7: 'OA', 10: 'OA', 17: 'OA', 18: 'OA', 19: 'OA',
    29: 'OA', 34: 'OA', 46: 'OA', 47: 'OA', 48: 'OA', 51: 'OA',
    59: 'OA', 66: 'OA', 68: 'OA', 70: 'OA', 71: 'OA', 72: 'OA',
    75: 'OA', 77: 'OA', 78: 'OA', 79: 'OA', 81: 'OA', 82: 'OA', 91: 'OA',
    
    # RA (9 questions)
    12: 'RA', 14: 'RA', 15: 'RA', 16: 'RA', 28: 'RA', 30: 'RA', 31: 'RA', 35: 'RA', 74: 'RA',
    
    # Osteoporosis (10 questions)
    32: 'Osteoporosis', 33: 'Osteoporosis', 49: 'Osteoporosis', 50: 'Osteoporosis',
    52: 'Osteoporosis', 57: 'Osteoporosis', 58: 'Osteoporosis', 61: 'Osteoporosis',
    62: 'Osteoporosis', 67: 'Osteoporosis'
}

# High-Yield Guideline Pearls per subtopic
GUIDELINE_NOTES = {
    'Gout': 'ACR 2020 Gout: Flare first-line = Low-dose Colchicine / NSAID / Steroid; Target SUA < 6.0 mg/dL (< 5.0 if tophi); Screen HLA-B*58:01 before allopurinol.',
    'OA': 'ACR 2019 Knee OA: Strongly recommend Topical NSAIDs over oral NSAIDs; Exercise & weight management are core non-pharmacologic interventions.',
    'RA': 'ACR 2021 RA: First-line csDMARD = Methotrexate monotherapy; Treat-to-target aiming for remission or low disease activity; Supplement Folic acid.',
    'Osteoporosis': 'TOPF 2021 / NOF: T-score ≤ -2.5 SD defines osteoporosis; Oral Bisphosphonates (Alendronate/Risedronate) are first-line antiresorptive therapy.'
}

# Specific question clinical takeaway for Column N
SPECIFIC_NOTES = {
    1: 'Gout Acute Flare: First-line = NSAIDs / Colchicine. ห้ามเริ่มยาลดกรดยูริกขณะ acute flare',
    2: 'Gout Lifestyle: Low-fat dairy ช่วยลดกรดยูริก; หลีกเลี่ยง High-fructose, แอลกอฮอล์, เครื่องใน',
    3: 'Colchicine Toxicity: สัญญาณเตือนพิษเฉียบพลัน = Diarrhea, N/V. แนะนำ Low-dose regimen',
    5: 'Allopurinol SCARs: ผู้ป่วยไทยมีความชุกของ HLA-B*58:01 สูง เสี่ยง SJS/TEN ต้องคัดกรอง',
    6: 'OA Diagnosis: Morning stiffness < 30 นาที, Crepitus, ปวดเมื่อใช้งาน ดีขึ้นเมื่อพัก',
    7: 'OA Knee First-line: Topical NSAIDs (Diclofenac emulgel) มีประสิทธิภาพดีและปลอดภัยต่อ GI/CV/Renal',
    8: 'Allopurinol Pharmacogenomics: ตรวจยีน HLA-B*58:01 ก่อนเริ่มยาในคนไทยทุกราย',
    9: 'Gout Flare Prophylaxis: ให้ Colchicine / NSAID ร่วมกับ Allopurinol นานอย่างน้อย 3-6 เดือน',
    10: 'ACR 2019 OA: แนะนำ Topical NSAID เป็นอันดับแรกก่อน Oral NSAID ในข้อเข่าเสื่อม',
    11: 'Colchicine Counseling: หยุดยาหรือลดขนาดทันทีหากเกิดอาการถ่ายเหลวรุนแรง',
    12: 'RA Treat-to-target: หากคุมโรคไม่ได้ด้วย MTX ให้พิจารณา Add-on csDMARDs อื่น (เช่น HCQ, SSZ)',
    13: 'Gout Prophylaxis: ป้องกัน Gout flare จากการแกว่งของระดับกรดยูริกในช่วงเริ่ม ULT',
    14: 'DMARDs Monitoring: HCQ ต้องตรวจคัดกรอง Retinal toxicity ด้วย Eye exam ประจำปี (MTX ไม่ต้อง)',
    15: 'DMARDs Counseling: MTX ทานสัปดาห์ละ 1 ครั้งเท่านั้น ห้ามทานทุกวัน และห้ามปรับลดขนาดยาเอง',
    16: 'RA Sulfa Allergy: Sulfasalazine มีโครงสร้าง Sulfa ห้ามใช้ในคนไข้แพ้ Sulfa ให้เลี่ยงไปใช้ HCQ หรือ LEF',
    17: 'OA Clinical Features: ข้อฝืดขัดสั้น ๆ (<30 นาที), อาการปวดสัมพันธ์กับการลงน้ำหนัก/เคลื่อนไหว',
    18: 'OA CV Safety: Etoricoxib / COX-2 inhibitors เพิ่มความเสี่ยง Thrombotic CV events สูงสุด',
    19: 'OA Capsaicin: Capsaicin ทาเฉพาะที่ออกฤทธิ์ยับยั้ง Substance P บรรเทาปวดข้อเข่าได้อย่างปลอดภัย',
    20: 'Colchicine ADR: Diarrhea เป็น ADR พบบ่อยสุดจากการรบกวนเซลล์เยื่อบุลำไส้ที่แบ่งตัวเร็ว',
    21: 'Gout Prophylaxis: Colchicine ป้องกันข้ออักเสบกำเริบซ้ำจากการสลายผลึก Urate ในช่วงเริ่มยาลดกรดยูริก',
    22: 'Allopurinol Gene Screening: HLA-B*58:01 allele เป็น biomarker ทำนายการเกิด SCARs',
    24: 'Acute Gout: Naproxen / NSAIDs เป็นทางเลือกแรก ห้ามเริ่ม Allopurinol ทันที',
    25: 'Allopurinol Contraindication: ห้ามใช้เด็ดขาดในผู้ป่วยที่มีประวัติแพ้ยา Allopurinol รุนแรง (SJS/TEN)',
    26: 'Gout Advice: การหยุดยาลดกรดยูริกทันทีเมื่อปวดทำให้ยูริกแกว่งและอักเสบเรื้อรัง',
    27: 'Gout Drug-Induced: Losartan ช่วยขับกรดยูริกทางปัสสาวะ ขณะที่ Thiazide/Aspirin ลดการขับยูริก',
    28: 'RA Disease Activity: ประเมินด้วย CDAI, SDAI หรือ DAS28 เพื่อปรับขนาดยาตาม Treat-to-target',
    29: 'Herbal Medicine: สารสกัดเถาวัลย์เปรียง บรรเทาอาการปวดข้อเข่าเสื่อมได้เทียบเท่า NSAIDs',
    30: 'MTX Toxicity: ตรวจพบ Leukopenia / Myelosuppression จากฤทธิ์ Antifolate ของ MTX',
    31: 'Drug-Induced Cytopenia: MTX กดไขกระดูก ป้องกันได้ด้วยการให้ Folic acid เสริม',
    32: 'Osteoporosis Definition: T-score ≤ -2.5 SD ณ Lumbar spine หรือ Hip',
    33: 'Osteoporosis First-line: Alendronate / Risedronate (Oral Bisphosphonates) ลด Fracture ได้ดีที่สุด',
    34: 'NSAIDs Safety: ปัจจัยเสี่ยงแผลทางเดินอาหาร ได้แก่ ผู้สูงอายุ, ประวัติ GI bleed, ยาต้านเกล็ดเลือด',
    35: 'NSAIDs GI Protection: ใช้ Celecoxib ร่วมกับ PPIs ในผู้ป่วย High GI risk และ low CV risk',
    36: 'Allopurinol Metabolism: เปลี่ยนเป็นสารออกฤทธิ์ Oxypurinol ขับออกทางไตเป็นหลัก ต้องปรับตาม CrCl',
    37: 'Colchicine Flare Duration: ควรเริ่มยาภายใน 24-36 ชั่วโมงหลังมีอาการ และให้ต่อเนื่องจนอาการสงบ',
    38: 'Gout SUA Target: เป้าหมายกรดยูริกในเลือด < 6.0 mg/dL (< 5.0 mg/dL หากมี Tophi)',
    39: 'NSAIDs AKI: ยับยั้ง Renal PGE2/PGI2 ทำให้เกิด Afferent arteriole vasoconstriction',
    40: 'NSAIDs Nephrotoxicity: เสี่ยงต่อ Hemodynamic acute kidney injury โดยเฉพาะเมื่อใช้ร่วมกับ ACEI/Diuretics',
    41: 'Gout Drug Caution: HCTZ และ Thiazide diuretics แย่งขับกรดยูริกที่ท่อไต ทำให้กรดยูริกสูงขึ้น',
    45: 'Gout Add-on ULT: หากใช้ Allopurinol เต็มขนาดแล้วยังไม่ถึงเป้า แนะนำ Add-on Uricosuric (Benzbromarone)',
    46: 'OA Diagnosis: ปวดเข่า, ขยับมีเสียง Crepitus, ข้อติดตอนเช้า < 30 นาที, ไม่มีอาการอักเสบร้อนแดง',
    47: 'OA CKD Caution: ห้ามใช้ Oral NSAIDs ในผู้ป่วย ESRD หรือ Severe CKD (eGFR < 30 mL/min)',
    48: 'OA Management: ลดน้ำหนัก, กายภาพบำบัดเพิ่มความแข็งแรงของกล้ามเนื้อรอบข้อเข่า Quadriceps',
    49: 'Osteoporosis First-line: Alendronate เพิ่ม BMD และลดอุบัติการณ์กระดูกหักได้อย่างมีนัยสำคัญ',
    50: 'Bisphosphonates ADR: Osteonecrosis of the Jaw (ONJ) ต้องตรวจและทำหัตถการทันตกรรมก่อนเริ่มยา',
    51: 'Steroids Mechanism: จับกับ Glucocorticoid receptor ยับยั้ง NF-kB และลดการสร้าง Pro-inflammatory cytokines',
    52: 'BMD Criteria: WHO เกณฑ์ Osteoporosis คือ T-score ≤ -2.5 SD',
    57: 'Osteoporosis Fragility Fracture: ผู้สูงอายุหกล้มกระดูกข้อมือหัก ร่วมกับ T-score ≤ -2.5 วินิจฉัย Osteoporosis',
    58: 'Osteoporosis Risk Factors: วัยหมดประจำเดือน ขาดฮอร์โมน Estrogen ทำให้ Osteoclast สลายกระดูกเด่น',
    59: 'Derris scandens Caution: เถาวัลย์เปรียงยับยั้ง COX มีฤทธิ์ระคายเคืองกระเพาะอาหาร ระวังใน Peptic ulcer',
    61: 'Osteoporosis Secondary Prevention: Alendronate เป็นยาทางเลือกแรกในการป้องกันกระดูกหักซ้ำ',
    62: 'Bisphosphonates Rare ADR: ONJ และ Atypical femoral fracture (AFF) สัมพันธ์กับการใช้ยาระยะยาว',
    66: 'NSAIDs Renal Safety: ยับยั้ง Prostaglandins ลดเลือดไปเลี้ยงไต ส่งผลให้ Scr สูงขึ้นและเกิดไตวาย',
    67: 'Bisphosphonates Administration: ทานตอนเช้าก่อนอาหาร 30 นาที ดื่มน้ำเปล่าเต็มแก้ว และห้ามนอนราบ 30 นาที',
    68: 'NSAIDs Blood Pressure: NSAIDs ยับยั้ง Renal PG ทำให้เกิดการคั่งของโซเดียมและน้ำ ส่งผลให้ความดันโลหิตสูงขึ้น',
    70: 'OA Treatment Hierarchy: Paracetamol หรือ Topical NSAIDs เป็นตัวเลือกลำดับแรกในข้อเข่าเสื่อม',
    71: 'NSAIDs Mechanism: ยับยั้งเอนไซม์ Cyclooxygenase (COX) ลดการสร้าง Prostaglandins บรรเทาปวดอักเสบ',
    72: 'NSAIDs GI Prevention: ให้ PPI (เช่น Omeprazole) ร่วมกับ NSAID ช่วยป้องกันการเกิด Gastric & Duodenal ulcers',
    74: 'Hydroxychloroquine Ocular Toxicity: ตกตะกอนที่ Retinal pigment epithelium ต้องตรวจลานสายตาและจอประสาทตาทุกปี',
    75: 'Capsaicin Gel: สารสกัดจากพริก ยับยั้งการหลั่ง Substance P จากปลายประสาทรับความรู้สึกปวด',
    77: 'OA Diagnostic Criteria: Morning stiffness นานเกิน 1 ชั่วโมง เป็นลักษณะของ RA ไม่ใช่ OA (OA < 30 นาที)',
    78: 'OA First-line Analgesic: Paracetamol ขนาดไม่เกิน 3,000-4,000 mg/day เหมาะสำหรับ Mild-to-moderate OA pain',
    79: 'Curcumin in Knee OA: สารสกัดขมิ้นชัน มีฤทธิ์ลดปวดข้อเข่าเสื่อมได้ดีเทียบเท่า Ibuprofen และ GI safety สูงกว่า',
    81: 'PPI Co-prescription: Omeprazole เป็นยาทางเลือกมาตรฐานในการป้องกัน NSAID-induced ulcer',
    82: 'NSAIDs CV Risk: Parecoxib / Selective COX-2 inhibitors มีความเสี่ยงต่อ CV events สูงสุด',
    85: 'TEN Hypersensitivity: จัดเป็น Type IV (Delayed cell-mediated) hypersensitivity กระตุ้นโดย CD8+ T cells',
    86: 'Allopurinol-induced TEN: Allopurinol เป็นสาเหตุพบบ่อยอันดับต้น ๆ ของ SJS/TEN ในประเทศไทย',
    87: 'TEN Diagnosis: เกณฑ์การวินิจฉัยประเมินจาก Skin detachment > 30% BSA, Mucosal involvement, และ SCORTEN',
    88: 'TEN Severity Level: SJS/TEN เป็นอาการไม่พึงประสงค์ระดับ Life-threatening ที่มีอัตราการเสียชีวิตสูง'
}

# 3. Parse Questions
q_blocks = re.split(r'###\s*ข้อที่\s*', q_section)
clinical_questions = []

for qb in q_blocks[1:]:
    lines = [l.strip() for l in qb.strip().split('\n') if l.strip()]
    if not lines: continue
    m_header = re.match(r'(\d+)\s*(?:\[ปี\s*(\d+)\])?(?:\s*\[เรื่อง:\s*([^\]]+)\])?', lines[0])
    if not m_header: continue
    
    q_num = int(m_header.group(1))
    if q_num not in SUBTOPIC_MAP:
        continue
        
    year = m_header.group(2) or ''
    topic = m_header.group(3) or ''
    subtopic = SUBTOPIC_MAP[q_num]
    exam_type = f"ข้อสอบจริงปี {year}" if year else "ข้อสอบจริง"
    
    # Extract prompt and choices with clean cutoff
    body_lines = []
    choices = {}
    current_choice = None
    
    for line in lines[1:]:
        # Cut off choice accumulation immediately on markdown headers, case studies, dividers, or breaks
        if line.startswith('#') or line.startswith('กรณีศึกษา') or line.startswith('---') or line.startswith('<br>'):
            current_choice = None
            continue
            
        m_c = re.match(r'^([ก-จa-eA-E])\.\s*(.+)', line)
        if m_c:
            current_choice = m_c.group(1).lower()
            choices[current_choice] = m_c.group(2).strip()
        elif current_choice:
            choices[current_choice] += ' ' + line.strip()
        else:
            body_lines.append(line)
            
    q_prompt = ' '.join(body_lines).strip()
    
    # Prepend case scenario if applicable
    if q_num in case_scenarios:
        full_q_text = f"▶ [{case_scenarios[q_num]}]\n\n📌 ข้อที่ {q_num}: {q_prompt}"
    else:
        full_q_text = f"📌 ข้อที่ {q_num}: {q_prompt}"
        
    def sanitize(text):
        if not text: return ''
        text = re.sub(r'<\s*br\s*/?\s*>', ' ', text, flags=re.IGNORECASE)
        text = re.sub(r'---', '', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text

    c_list = [
        sanitize(choices.get('ก', choices.get('a', ''))),
        sanitize(choices.get('ข', choices.get('b', ''))),
        sanitize(choices.get('ค', choices.get('c', ''))),
        sanitize(choices.get('ง', choices.get('d', ''))),
        sanitize(choices.get('จ', choices.get('e', '')))
    ]
    
    ans_info = ans_map.get(q_num, {'key': 1, 'letter': 'ก', 'raw_text': ''})
    ans_key = ans_info['key']
    ans_letter = ['ก', 'ข', 'ค', 'ง', 'จ'][ans_key - 1]
    correct_choice_text = c_list[ans_key - 1] if 0 <= ans_key - 1 < len(c_list) else ''
    
    # Build clean structured explanation
    raw_exp = ans_info['raw_text']
    # Clean leading question number/header
    raw_exp = re.sub(r'^\s*\d+\s*(?:\[ปี\s*\d+\])?\s*', '', raw_exp).strip()
    # Strip local file URLs
    raw_exp = re.sub(r'\[([^\]]+)\]\(file:///[^\)]+\)', r'\1', raw_exp)
    
    # Extract clinical rationale and references
    m_exp = re.search(r'\*\s*\*\*💡\s*คำอธิบายทางคลินิก\*\*:?\s*([\s\S]*?)(?=\*\s*\*\*📖|\Z)', raw_exp)
    clinical_body = m_exp.group(1).strip() if m_exp else raw_exp
    
    m_ref = re.search(r'\*\s*\*\*📖\s*แหล่งอ้างอิง[^\*:]*\*\*:?\s*([\s\S]*?)\Z', raw_exp)
    clinical_ref = m_ref.group(1).strip() if m_ref else ''
    
    # Format high-yield explanation
    structured_exp = f"✅ **คำตอบที่ถูกต้อง:** ข้อ {ans_letter}. {correct_choice_text}\n\n"
    structured_exp += f"💡 **คำอธิบายทางคลินิก (Clinical Rationale):**\n{clinical_body}\n\n"
    if clinical_ref:
        structured_exp += f"📖 **แนวทางเวชปฏิบัติอ้างอิง:** {clinical_ref}\n\n"
    structured_exp += f"📌 **High-Yield Exam Pearl:** {SPECIFIC_NOTES.get(q_num, GUIDELINE_NOTES[subtopic])}"
    
    col_n_note = SPECIFIC_NOTES.get(q_num, GUIDELINE_NOTES[subtopic])
    
    clinical_questions.append({
        'orig_q_num': q_num,
        'year': year,
        'topic': topic,
        'subtopic': subtopic,
        'exam_type': exam_type,
        'question': full_q_text,
        'choices': c_list,
        'answer': ans_key,
        'explanation': structured_exp.strip(),
        'note': col_n_note
    })

parsed_questions = clinical_questions

print(f"✅ Successfully processed {len(clinical_questions)} pure clinical questions!")
sub_counts = {}
for q in clinical_questions:
    sub_counts[q['subtopic']] = sub_counts.get(q['subtopic'], 0) + 1
print(f"📊 Subtopics breakdown: {sub_counts}")
