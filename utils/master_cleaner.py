# -*- coding: utf-8 -*-
"""
utils/master_cleaner.py - Production-Grade Text Sanitizer, Image Filter & Topic Classifier for PLE-CC
"""
import sys, re

def normalize_thai_sara_am(text):
    if not text:
        return ''
    # Fix broken Thai syllables from OCR: 'ท า' -> 'ทำ', 'ค า' -> 'คำ', 'ท ำ' -> 'ทำ'
    t = re.sub(r'([ก-ฮ])([่้๊๋]?)\s+[ำา]', r'\1\2ำ', text)
    # Fix broken 'จำ' / 'นำ' / 'ลำ'
    t = t.replace('ค าถาม', 'คำถาม').replace('ข(อ', 'ข้อ').replace('ถูกต(อง', 'ถูกต้อง')
    return t

def clean_text_advanced(text, is_choice=False):
    if not text:
        return ''
    t = str(text).strip()
    
    # 0. Thai OCR syllable normalization
    t = normalize_thai_sara_am(t)
    
    # 1. Unescape HTML entities
    t = t.replace('&nbsp;', ' ').replace('&quot;', '"').replace('&amp;', '&')
    
    # 2. Math & comparison symbols
    t = t.replace('&gt;=', '≥').replace('>=', '≥').replace('&ge;', '≥')
    t = t.replace('&lt;=', '≤').replace('<=', '≤').replace('&le;', '≤')
    t = t.replace('&plusmn;', '±').replace('+/-', '±')
    t = t.replace('-&gt;', '→').replace('->', '→').replace('&rarr;', '→')
    t = t.replace('&gt;', '>').replace('&lt;', '<')
    
    # 3. Strip HTML tags like <br>, <span ...>, <mark>, <b>, </b>, <div>, etc.
    t = re.sub(r'<\s*br\s*/?\s*>', '\n' if not is_choice else ' ', t, flags=re.IGNORECASE)
    t = re.sub(r'&lt;\s*br\s*/?\s*&gt;', '\n' if not is_choice else ' ', t, flags=re.IGNORECASE)
    t = re.sub(r'<[^>]+>', '', t)
    t = re.sub(r'&lt;[^&gt;]+&gt;', '', t)
    
    # 4. Remove Markdown headers and asterisks
    t = re.sub(r'#{1,6}\s*(?:ข้อที่\s*\d+\s*[:\.]?)?', '', t)
    t = re.sub(r'\*{1,3}', '', t)
    t = re.sub(r'[\uf0d8\u25ba\u25cf\u2022\u25aa]', '', t)
    t = re.sub(r'^-{3,}', '', t, flags=re.MULTILINE)
    
    # 5. Remove leaked line headers, case banners, and 'ใช้ตอบคำถามข้อ ...'
    t = re.sub(r'^[^\n]*?\(?ใช้ตอบคำถามข้อ\s*\d+[-–]\d+\)?\s*\n?', '', t, flags=re.MULTILINE)
    t = re.sub(r'^[▶\s]*\[กรณีศึกษา[^\]]*\]?\s*\n?', '', t, flags=re.MULTILINE)
    t = re.sub(r'^[▶\s]*\[สถานการณ์[^\]]*\]?\s*\n?', '', t, flags=re.MULTILINE)
    t = re.sub(r'^(?:📌\s*)?ข้อที่\s*\d+\s*[:\.]\s*', '', t, flags=re.MULTILINE)
    t = re.sub(r'^\s*▶\s*', '', t, flags=re.MULTILINE)

    # 6. Remove student recollection / author tags
    t = re.sub(r'\(\s*[ก-๙a-zA-Z\s\./]*\d{2,3}[ก-๙a-zA-Z\s\./]*\s*\)', '', t)
    t = re.sub(r'\(\s*(?:จำ|คนจำ|ข้อจำ|เพื่อนจำ|พี่ชม|พี่|น้อง|ไอซ์|ปอย|ตอง|มีมี่|หมีพูห์|จุ๊บ|ปุ๋ย|กวาง|ปาม|จิ๊บ|ฮุ|นี่ตอบ|ซ้ำกับ|credit)[^\)]*\)', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\(จำโจทย์ไม่ได้[^\)]*\)', '', t)
    t = re.sub(r'\(จำคำตอบไม่ได้[^\)]*\)', '', t)
    t = re.sub(r'\(จำตัวเลือกไม่ได้[^\)]*\)', '', t)
    t = re.sub(r'\(ข้อ\s*\d+\s*[-–]\s*\d+\)', '', t)
    t = re.sub(r'\[NEED_REVIEW\]\s*', '', t)
    t = re.sub(r'\[ปี\s*\d{4}\]', '', t)
    t = re.sub(r'\[กลุ่มวิชา:\s*[^\]]+\]', '', t)
    t = re.sub(r'\[หมวดหมู่:\s*[^\]]+\]', '', t)

    # Headers from mock rxcu83
    header_patterns = [
        r'Mock\s+PLE-CC\s+ครั้งที่\s*\d+',
        r'จัดทำโดย\s*ฝ่าย\s*CC1\s*rxcu\d+',
        r'หมายเหตุ\s*:\s*/\s*หมายถึง.*',
        r'\*เป็นการจำข้อสอบออกมาภายในรุ่น.*',
        r'งดส่งต่อให้บุคคลภายนอก.*',
        r'ถัดไป\s*\(น้องๆจะได้ทดสอบตนเองนะ\)\*',
        r'ข้อสอบ\s*CC1\s*ชุดที่\s*\d+\s*วันที่.*'
    ]
    for pat in header_patterns:
        t = re.sub(pat, '', t, flags=re.IGNORECASE)

    # 6.5 Remove Pharma Plus / เล่มม่วง / Book watermark leakage (Strictly prohibited on Web)
    if 'PHARMA PLUS' in t.upper() or 'PHARMAPLUS' in t.upper():
        t = re.split(r'PHARMA\s*PLUS(?:\s*INSTITUTE)?', t, flags=re.IGNORECASE)[0].strip()
    t = re.sub(r'เล่มม่วง\s*(?:\(Pharma\s*Plus\))?', '', t, flags=re.IGNORECASE)
    t = re.sub(r'Pharma\s*Plus(?:\s*Fight\s*for\s*Pharmacy\s*License)?', '', t, flags=re.IGNORECASE)
    t = re.sub(r'Fight\s*for\s*Pharmacy\s*License', '', t, flags=re.IGNORECASE)
    t = re.sub(r'[\s,;:·\.\-\|]+(?:aas|contest|mounter|consumer|ÉÉ?|v\s*X)+\b.*$', '', t, flags=re.IGNORECASE)
    t = re.sub(r'\s+[vXx]\b.*$', '', t)

    # 7. Normalize whitespace
    if is_choice:
        t = re.sub(r'\s+', ' ', t).strip()
    else:
        lines = [re.sub(r'[ \t]+', ' ', l).strip() for l in t.split('\n')]
        clean_lines = []
        for l in lines:
            if l or (clean_lines and clean_lines[-1]):
                clean_lines.append(l)
        t = '\n'.join(clean_lines).strip()
        
    return t

def clean_image_field(val):
    if not val:
        return ''
    v = str(val).strip()
    if v in ['Medium', 'Easy', 'Hard', 'None', '-', 'null', 'undefined']:
        return ''
    if any(k in v for k in ['[รูปภาพ', 'รูปเฉลย', 'จำไม่ได้', 'ไม่มีรูป', 'ข้อสอบจริง']):
        return ''
    if v.startswith(('http://', 'https://', 'images/', 'drive.google')):
        return v
    if any(v.lower().endswith(ext) for ext in ['.jpg', '.jpeg', '.png', '.gif', '.webp', '.svg']):
        return v
    return ''

def clean_explanation_field(exp, ans_letter, ans_text, subtopic, track, choices=None, ans_num=None, q_text=""):
    if exp and str(exp).strip():
        c_exp = clean_text_advanced(str(exp).strip(), is_choice=False)
        return c_exp.replace('\n', '<br>')
    return f"✅ คำตอบที่ถูกต้อง: ข้อ {ans_letter}. {ans_text}"

def match_kw(text, keywords):
    for kw in keywords:
        if len(kw) <= 3 and kw.isalpha():
            if re.search(r'\b' + re.escape(kw) + r'\b', text, re.IGNORECASE):
                return True
        else:
            if kw.lower() in text.lower():
                return True
    return False

def classify_question_precise(q_text):
    q = q_text
    
    # 1. Pulmonary
    if match_kw(q, ['asthma', 'หอบหืด', 'copd', 'ปอดอุดกั้น', 'inhaler', 'salbutamol', 'budesonide', 'formoterol', 'tiotropium', 'ipratropium', 'fluticasone', 'salmeterol', 'seretide', 'symbicort', 'theophylline', 'montelukast', 'fev1', 'หลอดลม', 'สูบบุหรี่', 'บุหรี่', 'smoking', 'nicotine', 'หมากฝรั่งนิโคติน', 'hsi', 'fagerstrom']):
        return '11. Pulmonary', 'Pulmonary Diseases', 'Clinic'

    # 2. Infectious Diseases
    if match_kw(q, ['hiv', 'tb', 'วัณโรค', 'arv', 'cd4', 'viral load', 'pneumonia', 'cap', 'hap', 'uti', 'sepsis', 'cellulitis', 'meningitis', 'antibiotic', 'antifungal', 'antiviral', 'amoxicillin', 'ceftriaxone', 'meropenem', 'vancomycin', 'ciprofloxacin', 'azithromycin', 'doxycycline', 'bactrim', 'ติดเชื้อ', 'เชื้อรา', 'ไข้หวัดใหญ่', 'covid', 'tenofovir', 'emtricitabine', 'dolutegravir', 'efavirenz', 'zidovudine', 'acyclovir', 'oseltamivir', 'fluconazole', 'amphotericin', 'colistin', 'piperacillin', 'tazobactam', 'cloxacillin', 'penicillin', 'gentamicin', 'amikacin', 'clarithromycin', 'erythromycin', 'metronidazole', 'ไซนัสอักเสบ', 'antiretroviral', 'lipodystrophy', 'haart', 'insti', 'nnrti', 'nrti', 'protease inhibitor']):
        return '8. Infectious diseases', 'Infectious Diseases', 'Clinic'
        
    # 3. Eye disorders
    if match_kw(q, ['ต้อหิน', 'glaucoma', 'ต้อกระจก', 'cataract', 'ตาแดง', 'conjunctivitis', 'timolol', 'latanoprost', 'travoprost', 'brimonidine', 'dorzolamide', 'brinzolamide', 'ยาหยอดตา', 'หยอดตา', 'eye drop', 'ophthalmic', 'ดวงตา', 'น้ำตาเทียม', 'hydroxypropyl-guar', 'กระจกตา']):
        return '13. Eye disorder', 'Eye Disorders', 'Clinic'
        
    # 4. Cardiovascular
    if match_kw(q, ['hypertension', 'ความดันโลหิต', 'ความดันสูง', 'ลดความดัน', 'heart failure', 'หัวใจล้มเหลว', 'angina', 'acs', 'mi', 'stemi', 'nstemi', 'af', 'atrial fibrillation', 'arrhythmia', 'lipid', 'statin', 'cholesterol', 'triglyceride', 'amlodipine', 'enalapril', 'losartan', 'bisoprolol', 'warfarin', 'noac', 'doac', 'aspirin', 'clopidogrel', 'diltiazem', 'verapamil', 'hydrochlorothiazide', 'spironolactone', 'furosemide', 'digoxin', 'nitroglycerin', 'isordil', 'edoxaban', 'rivaroxaban', 'apixaban', 'dabigatran', 'atorvastatin', 'simvastatin', 'rosuvastatin', 'gemfibrozil', 'fenofibrate', 'angiotensin', 'raas', 'acei', 'arb', 'aliskiren', 'aldosterone', 'carvedilol', 'metoprolol', 'sacubitril']):
        return '2. Cardiovascular', 'Cardiovascular Diseases', 'Clinic'
        
    # 5. Endocrine & Diabetes
    if match_kw(q, ['diabetes', 'เบาหวาน', 'dm', 'hba1c', 'glucose', 'น้ำตาลในเลือด', 'metformin', 'insulin', 'sulfonylurea', 'glipizide', 'sglt2', 'dapagliflozin', 'empagliflozin', 'glp-1', 'semaglutide', 'liraglutide', 'dpp-4', 'sitagliptin', 'pioglitazone', 'thyroid', 'ไทรอยด์', 'hypothyroid', 'hyperthyroid', 'methimazole', 'ptu', 'propylthiouracil', 'levothyroxine']):
        return '4. Endocrine', 'Diabetes & Endocrine', 'Clinic'
        
    # 6. Musculoskeletal & Joint
    if match_kw(q, ['gout', 'เกาต์', 'uric', 'colchicine', 'allopurinol', 'febuxostat', 'osteoarthritis', 'ข้อเสื่อม', 'ข้อเข่า', 'osteoporosis', 'กระดูกพรุน', 'กระดูกหัก', 'ra', 'rheumatoid', 'รูมาตอยด์', 'nsaid', 'celecoxib', 'etoricoxib', 'naproxen', 'ibuprofen', 'indomethacin', 'methotrexate', 'alendronate', 'zoledronic', 'denosumab', 'glucosamine', 'chondroitin', 'xanthine oxidase', 'pain score', 'ปวดข้อ']):
        return '1. Musculoskeleton', 'Musculoskeletal & Joint', 'Clinic'
        
    # 7. Laws & SAP
    if match_kw(q, ['พ.ร.บ.', 'พรบ', 'กฎหมาย', 'ยาอันตราย', 'ยาควบคุมพิเศษ', 'วัตถุออกฤทธิ์', 'ยาเสพติด', 'ฉลากยา', 'จรรยาบรรณ', 'ร้านยา', 'ร้านขายส่ง', 'gpp', 'ใบอนุญาต', 'ผู้มีหน้าที่ปฏิบัติการ', 'ขย.11', 'ขย.', 'ยาสามัญประจำบ้าน', 'pseudoephedrine', 'โทษ', 'จำคุก', 'ปรับ', 'อย.', 'fda']):
        return '1. Pharmacy Laws & Ethics', 'Pharmacy Laws & Ethics', 'SAP'
    if match_kw(q, ['หลักประกันสุขภาพ', 'สิทธิบัตรทอง', 'ประกันสังคม', 'csmbs', 'rdu', 'rational drug use', 'รพ.สต.', 'นโยบายแห่งชาติด้านยา', 'nlem', 'บัญชียาหลัก']):
        return '2. Pharmacy Administration & System', 'Administration & System', 'SAP'
    if match_kw(q, ['rct', 'cohort', 'case-control', 'relative risk', 'odds ratio', 'icer', 'qaly', 'cost-effectiveness', 'p-value', 'chi-square', 't-test', 'ระบาดวิทยา', 'ชีวสถิติ', 'sample size', 'ต้นทุน', 'ต้นทุนใด', 'cost']):
        return '3. Research & Biostats', 'Biostats & Research', 'SAP'
        
    # 8. Neurologic
    if match_kw(q, ['epilepsy', 'ชัก', 'ยากันชัก', 'phenytoin', 'valproate', 'valproic', 'carbamazepine', 'lamotrigine', 'levetiracetam', 'gabapentin', 'pregabalin', 'parkinson', 'พาร์กินสัน', 'levodopa', 'benserazide', 'carbidopa', 'migraine', 'ไมเกรน', 'ปวดศีรษะ', 'headache', 'triptan', 'sumatriptan', 'ergotamine', 'stroke', 'หลอดเลือดสมอง', 'rtpa', 'alteplase', 'alzheimer', 'สมองเสื่อม', 'donepezil', 'galantamine', 'rivastigmine', 'nihss', 'หน้าเบี้ยว', 'ปากเบี้ยว']):
        return '9. Neurologic', 'Neurologic Disorders', 'Clinic'
        
    # 9. Renal
    if match_kw(q, ['ckd', 'aki', 'ไตวาย', 'ไตเรื้อรัง', 'โรคไต', 'egfr', 'gfr', 'kdigo', 'bun', 'creatinine', 'crcl', 'hemodialysis', 'hyperkalemia', 'calcium carbonate', 'sevelamer', 'epo', 'erythropoietin', 'calcitriol']):
        return '15. Renal', 'Renal Diseases', 'Clinic'
        
    # 10. GI
    if match_kw(q, ['peptic ulcer', 'gerd', 'กรดไหลย้อน', 'กระเพาะอาหาร', 'แผลในกระเพาะ', 'ท้องเสีย', 'diarrhea', 'ท้องผูก', 'constipation', 'คลื่นไส้', 'อาเจียน', 'nausea', 'vomiting', 'h. pylori', 'ppi', 'omeprazole', 'esomeprazole', 'lansoprazole', 'pantoprazole', 'antacid', 'ยาลดกรด', 'ยาระบาย', 'domperidone', 'metoclopramide', 'dimenhydrinate', 'loperamide', 'bisacodyl', 'senna', 'lactulose']):
        return '5. Gastrointestinal', 'GI Disorders', 'Clinic'

    # 11. Dermatologic
    if match_kw(q, ['ผื่น', 'สิว', 'acne', 'psoriasis', 'สะเก็ดเงิน', 'atopic', 'eczema', 'เชื้อราที่ผิวหนัง', 'tinea', 'scabies', 'แผลไฟไหม้', 'burn', 'clotrimazole', 'ketoconazole', 'terbinafine', 'hydrocortisone', 'triamcinolone', 'clobetasol', 'benzoyl peroxide', 'adapalene', 'isotretinoin']):
        return '3. Dermatologic', 'Dermatologic Disorders', 'Clinic'
        
    # 12. Immunologic
    if match_kw(q, ['ภูมิแพ้', 'allergic', 'allergy', 'anaphylaxis', 'epinephrine', 'adr', 'sjs', 'ten', 'แพ้ยา', 'antihistamine', 'cetirizine', 'loratadine', 'fexofenadine', 'chlorpheniramine', 'cpm', 'dexamethasone', 'prednisolone']):
        return '7. Immunologic', 'Allergy & Immunology', 'Clinic'
        
    # 13. Gynaecologic & GU
    if match_kw(q, ['คุมกำเนิด', 'contraceptive', 'ยาคุม', 'ตั้งครรภ์', 'pregnancy', 'ให้นมบุตร', 'lactation', 'menopause', 'วัยทอง', 'dysmenorrhea', 'ปวดประจำเดือน', 'bph', 'ต่อมลูกหมาก', 'tamsulosin', 'alfuzosin', 'finasteride', 'dutasteride', 'oxybutynin', 'tolterodine', 'sildenafil', 'tadalafil']):
        return '12. Gynaecologic/Genitourinary', 'Gynaecologic & GU', 'Clinic'

    # 14. Oncologic
    if match_kw(q, ['มะเร็ง', 'cancer', 'chemotherapy', 'เคมีบำบัด', 'cisplatin', 'carboplatin', 'doxorubicin', 'cyclophosphamide', 'paclitaxel', 'docetaxel', 'tamoxifen', 'letrozole', 'anastrozole', 'trastuzumab', 'rituximab', 'antiemetic', 'ondansetron', 'granisetron', 'aprepitant', 'palonosetron', 'g-csf', 'filgrastim', 'febrile neutropenia', 'extravasation']):
        return '14. Oncologic', 'Oncology & Chemotherapy', 'Clinic'

    # 15. Product Categories
    if match_kw(q, ['tablet', 'ยาเม็ด', 'capsule', 'แคปซูล', 'granule', 'capping', 'lamination', 'binder', 'disintegrant', 'lubricant', 'glidant', 'diluent', 'coating', 'wet granulation', 'dry granulation', 'ตอกเม็ด', 'talcum', 'corn starch', 'stearic acid', 'magnesium stearate', 'aerosil', 'lactose', 'avicel', 'sorbitol', 'excipient']):
        return '6. Solid Dosage Forms', 'Solid Dosage Forms', 'Product'
    if match_kw(q, ['suspension', 'ยาน้ำแขวนตะกอน', 'emulsion', 'อิมัลชัน', 'ointment', 'ขี้ผึ้ง', 'cream', 'ครีม', 'gel', 'เจล', 'suppository', 'ยาเหน็บ', 'hlb', 'surfactant', 'flocculat', 'deflocculat', 'syrup', 'ยาน้ำ', 'elixir', 'oleaginous', 'lanolin', 'petrolatum']):
        return '7. Liquid & Semisolids', 'Liquid & Semisolids', 'Product'
    if match_kw(q, ['stability', 'shelf life', 'q10', 'arrhenius', 'degradation', 'accelerated', 'hydrolysis', 'oxidation', 'preformulation', 'ความคงตัว', 'อายุยา', 'สภาวะเร่ง', 'usp']):
        return '4. Preformulation & GMP', 'Preformulation & Stability', 'Product'
    if match_kw(q, ['ไทเทรต', 'titrat', 'karl fischer', 'acid-base titrat', 'redox titrat', 'potentiometr']):
        return '1. Titrations', 'Titrations', 'Product'
    if match_kw(q, ['chromatograph', 'hplc', 'gc-ms', 'gc', 'tlc', 'retention time', 'column c18', 'โครมาโทกราฟี']):
        return '2. Chromatography', 'Chromatography', 'Product'
    if match_kw(q, ['uv-vis', 'nmr', 'spectro', 'ftir', 'absorbance', 'beer-lambert', 'wavelength', 'สเปกโทร', 'ความยาวคลื่น', 'polarimeter', 'refractometer']):
        return '3. Spectroscopy & Optics', 'Spectroscopy & Optics', 'Product'
    if match_kw(q, ['alligation', 'meq', 'mmol', 'mval', 'e-value', 'isotonic', 'displacement value', 'คำนวณ']):
        return '5. Pharmaceutical Calc', 'Pharmaceutical Calculations', 'Product'
    if match_kw(q, ['sterile', 'ปราศจากเชื้อ', 'autoclave', 'pyrogen', 'endotoxin', 'lal test', 'cleanroom', 'grade a', 'laminar air']):
        return '9. Sterile & Special Forms', 'Sterile Products', 'Product'
    if match_kw(q, ['biotech', 'monoclonal antibody', 'mab', 'recombinant', 'protein', 'peptide', 'elisa', 'biologic', 'วัคซีน', 'ชีววัตถุ', 'biosimilar']):
        return '10. Biotech Products', 'Biotech Products', 'Product'
    if match_kw(q, ['structure-activity', 'sar', 'prodrug', 'log p', 'pka', 'lipophilicity', 'bioisostere', 'metabolism cyp', 'medicinal chem']):
        return '13. Medicinal Chemistry', 'Medicinal Chemistry', 'Product'
    if match_kw(q, ['สมุนไพร', 'herbal', 'ขมิ้นชัน', 'ฟ้าทะลายโจร', 'curcumin', 'andrographolide', 'สารสกัด', 'maceration', 'soxhlet', 'บัวบก', 'สารสำคัญ', 'ยาแผนโบราณ']):
        return '17. Herbal Medicine', 'Herbal Medicine', 'Product'
    if match_kw(q, ['tpn', 'parenteral nutrition', 'enteral', 'สารอาหารทางหลอดเลือดดำ', 'โภชนบำบัด']):
        return '18. Clinical Nutrition', 'Clinical Nutrition', 'Product'

    # 16. Antidotes & Toxicology
    if match_kw(q, ['antidote', 'ยาแก้พิษ', 'สารพิษ', 'toxic', 'poisoning', 'overdose', 'paracetamol toxicity', 'nac', 'organophosphate', 'atropine', 'pralidoxime', '2-pam', 'naloxone', 'flumazenil', 'methanol', 'ethanol', 'snake', 'เซรุ่ม', 'ตะขาบ', 'แมงป่อง', 'สารหนู', 'ปรอท', 'ตะกั่ว']):
        return '16. Others & Toxic', 'Toxicology & Antidote', 'Clinic'
        
    return '16. Others & Toxic', 'General Therapeutics', 'Clinic'
