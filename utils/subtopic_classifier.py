# -*- coding: utf-8 -*-
"""
utils/subtopic_classifier.py - Standard Subtopic Classification Engine for PLE-CC
"""
import re

# Standard Subtopic Mapping
sheet_subtopic_map = {
    '1. Musculoskeleton': [
        ('Gout', ['gout', 'uric', 'เกาต์', 'เก๊าท์', 'colchicine', 'allopurinol', 'febuxostat', 'probenecid', 'ข้อเท้า', 'หัวแม่เท้า']),
        ('Osteoarthritis', ['osteoarthritis', 'ข้อเข่าเสื่อม', 'ข้อเสื่อม', 'oa', 'glucosamine', 'paracetamol', 'celecoxib']),
        ('Osteoporosis', ['osteoporosis', 'กระดูกพรุน', 'กระดูกบาง', 't-score', 'alendronate', 'zoledronic', 'denosumab', 'calcium']),
        ('Rheumatoid arthritis', ['rheumatoid', 'รูมาตอยด์', 'ra', 'methotrexate', 'leflunomide', 'sulfasalazine', 'anti-ccp'])
    ],
    '2. Cardiovascular': [
        ('Hypertension', ['ความดัน', 'hypertension', 'htn', 'sbp', 'dbp', 'losartan', 'enalapril', 'amlodipine', 'hctz', 'acei', 'arb']),
        ('Dyslipidemias', ['ไขมัน', 'statin', 'cholesterol', 'ldl', 'hdl', 'triglyceride', 'atorvastatin', 'simvastatin', 'ezetimibe']),
        ('Coronary artery disease', ['กล้ามเนื้อหัวใจ', 'angina', 'cad', 'mi', 'stemi', 'nstemi', 'aspirin', 'clopidogrel', 'ticagrelor', 'nitroglycerin']),
        ('Stable Heart Failure', ['หัวใจล้มเหลว', 'heart failure', 'hf', 'ef', 'hfreff', 'hfpef', 'spironolactone', 'furosemide', 'bisoprolol', 'entresto', 'sacubitril']),
        ('Venous thromboembolism', ['warfarin', 'inr', 'dvt', 'pe', 'heparin', 'enoxaparin', 'rivaroxaban', 'apixaban', 'noac', 'doac', 'ลิ่มเลือด'])
    ],
    '3. Dermatologic': [
        ('Superficial fungal', ['เชื้อรา', 'tinea', 'กลาก', 'เกลื้อน', 'candidiasis', 'ketoconazole', 'itraconazole', 'clotrimazole', 'terbinafine']),
        ('Acne', ['สิว', 'acne', 'benzoyl peroxide', 'isotretinoin', 'retinoid', 'clindamycin lotion']),
        ('Eczema & Dermatitis', ['ผื่น', 'eczema', 'atopic', 'dermatitis', 'topical steroid', 'hydrocortisone', 'triamcinolone', 'clobetasol']),
        ('Psoriasis', ['สะเก็ดเงิน', 'psoriasis', 'methotrexate', 'calcipotriol']),
        ('Herpes & Zoster', ['เริม', 'งูสวัด', 'herpes', 'zoster', 'acyclovir', 'valacyclovir']),
        ('Urticaria & Angioedema', ['ลมพิษ', 'urticaria', 'angioedema', 'antihistamine', 'ผื่นคัน']),
        ('Wound', ['แผล', 'burn', 'wound', 'silver sulfadiazine', 'dressing']),
        ('Seborrheic dermatitis', ['เซ็บเดิร์ม', 'seborrheic', 'รังแค', 'ketoconazole shampoo', 'tar shampoo'])
    ],
    '4. Endocrine': [
        ('Diabetes mellitus', ['เบาหวาน', 'diabetes', 'dm', 'hba1c', 'fpg', 'insulin', 'metformin', 'glipizide', 'sglt2', 'glp-1', 'dpp-4', 'hypoglycemia']),
        ('Hypo/Hyperthyroidism', ['ไทรอยด์', 'thyroid', 'hyperthyroid', 'hypothyroid', 'ptu', 'methimazole', 'levothyroxine', 'graves', 'tsh', 'ft4']),
        ('Obesity', ['ความอ้วน', 'obesity', 'น้ำหนักเกิน', 'orlistat', 'phentermine', 'liraglutide'])
    ],
    '5. Gastrointestinal': [
        ('GERD', ['gerd', 'กรดไหลย้อน', 'แสบร้อนกลางอก', 'heartburn', 'ppi', 'omeprazole']),
        ('Dyspepsia & PUD', ['peptic ulcer', 'pud', 'กระเพาะอาหาร', 'แผลในกระเพาะ', 'h. pylori', 'amoxicillin', 'clarithromycin']),
        ('Diarrhea & Constipation', ['ท้องเสีย', 'ท้องร่วง', 'อุจจาระร่วง', 'diarrhea', 'ors', 'loperamide', 'ท้องผูก', 'constipation', 'senna', 'bisacodyl', 'lactulose']),
        ('Nausea and vomiting', ['คลื่นไส้', 'อาเจียน', 'nausea', 'vomiting', 'domperidone', 'ondansetron', 'dimenhydrinate']),
        ('Hepatitis B virus', ['ตับอักเสบ', 'hepatitis', 'hbv', 'hcv', 'tenofovir', 'entecavir']),
        ('Inflammatory bowel', ['ibd', 'crohn', 'ulcerative colitis', 'sulfasalazine'])
    ],
    '6. Hematologic': [
        ('Anemia', ['anemia', 'โลหิตจาง', 'ซีด', 'ferrous', 'iron deficiency', 'ธาตุเหล็ก', 'mcv', 'folic', 'vitamin b12']),
        ('Hemolytic anemia', ['g6pd', 'hemolytic', 'ธาลัสซีเมีย', 'thalassemia'])
    ],
    '7. Immunologic': [
        ('Allergic rhinitis', ['ภูมิแพ้', 'หวัด', 'allergic rhinitis', 'คัดจมูก', 'น้ำมูก', 'cetirizine', 'loratadine', 'fexofenadine', 'cpm', 'nasal spray', 'budesonide spray', 'pseudoephedrine']),
        ('Hypersensitivity', ['แพ้ยา', 'drug allergy', 'sjs', 'ten', 'anaphylaxis', 'epinephrine', 'rash', 'dress']),
        ('Systemic lupus', ['sle', 'lupus', 'hydroxychloroquine', 'prednisolone']),
        ('EPI Vaccines', ['วัคซีน', 'vaccine', 'mmr', 'dpt', 'hpv', 'influenza', 'rabies', 'bcg'])
    ],
    '8. Infectious diseases': [
        ('Sexually Transmitted Infections (STIs)', ['urethritis', 'ท่อปัสสาวะ', 'หนองใน', 'gonorrhea', 'chlamydia', 'syphilis', 'ตกขาว', 'tricomon', 'trichomonas', 'std', 'sti', 'ceftriaxone 250']),
        ('Viral Hepatitis (HBV & HCV)', ['hepatitis b', 'hbv', 'ตับอักเสบบี', 'hbeag', 'hbsag', 'hcv', 'ตับอักเสบซี', 'ไวรัสตับอักเสบ']),
        ('Tuberculosis (TB)', ['tuberculosis', 'วัณโรค', 'tb', 'isoniazid', 'rifampin', 'rifampicin', 'pyrazinamide', 'ethambutol', '2hrze', 'afb']),
        ('HIV/AIDS & Opportunistic Infections', ['hiv', 'aids', 'cd4', 'viral load', 'tenofovir', 'efavirenz', 'dolutegravir', 'lamivudine', 'gpovir', 'zidovudine', 'ritonavir', 'arv', 'prep', 'pep', 'pcp', 'oi', 'opportunistic']),
        ('Fungal Infections (Superficial & Systemic)', ['tinea', 'น้ำกัดเท้า', 'เชื้อรา', 'fungal', 'candida', 'candidiasis', 'cryptococc', 'histoplasm', 'itraconazole', 'fluconazole', 'griseofulvin', 'ketoconazole', 'ฝ้าขาว', 'เชื้อราที่เล็บ']),
        ('Herpes Simplex & Varicella-Zoster', ['herpes', 'zoster', 'เริม', 'งูสวัด', 'acyclovir', 'valacyclovir', 'ตุ่มน้ำใส', 'ตุ่มน้ำพองใส', 'เสลดพังพอน']),
        ('Upper Respiratory Infections (URTI / Otitis / Pharyngitis)', ['aom', 'otitis', 'ปวดหู', 'หูส่วนกลาง', 'pharyng', 'คอหอยอักเสบ', 'mcisaac', 'sinus', 'โพรงจมูก', 'หวัด', 'ต่อมทอนซิล']),
        ('Parasitic & Tropical Diseases', ['มาลาเรีย', 'malaria', 'พยาธิ', 'parasite', 'albendazole', 'mebendazole', 'quinine', 'คันทวารหนัก', 'ivermectin', 'scabies', 'lice', 'หิด', 'เหา']),
        ('Lower Respiratory Infections (Pneumonia)', ['pneumonia', 'ปอดอักเสบ', 'ปอดบวม', 'cap', 'hap', 'curb-65', 's. pneumoniae']),
        ('Skin & Soft Tissue Infections (SSTI & Acne)', ['สิว', 'acne', 'pustule', 'benzoyl peroxide', 'cellulitis', 'impetigo', 'แผลตุ่ม', 'ผิวหนังพุพอง', 's. aureus', 'cloxacillin']),
        ('Urinary Tract Infections (UTI)', ['ปัสสาวะแสบขัด', 'uti', 'cystitis', 'pyelonephritis', 'ปัสสาวะอักเสบ', 'nitrofurantoin', 'fosfomycin', 'e. coli']),
        ('Gastrointestinal & Intra-abdominal Infections', ['h. pylori', 'h.pylori', 'ท้องเสีย', 'อุจจาระร่วง', 'diarrhea', 'peritonitis', 'ติดเชื้อในช่องท้อง']),
        ('CNS Infections, Sepsis & MDR Pathogens', ['meningitis', 'เยื่อหุ้มสมอง', 'sepsis', 'ติดเชื้อในกระแสเลือด', 'pseudomonas', 'p. aeruginosa', 'acinetobacter', 'a. baumannii', 'mrsa']),
        ('Antimicrobial Pharmacology (MOA & PK/PD)', ['dna gyrase', 'topoisomerase', 'bactericidal', 'bacteriostatic', 'concentration-dependent', 'time-dependent', '30s', '50s', 'ไรโบโซม', 'sulfonamide', 'vancomycin', 'aminoglycoside', 'quinolone', 'cephalosporin', 'penicillin', 'carbapenem', 'macrolide', 'tetracycline', 'doxycycline', 'chloramphenicol', 'polymyxin', 'colistin', 'gray baby'])
    ],
    '9. Neurologic': [
        ('Headache', ['ไมเกรน', 'migraine', 'ปวดศีรษะ', 'triptan', 'ergotamine', 'propranolol', 'topiramate', 'tension headache']),
        ('Epilepsy', ['ชัก', 'โรคลมชัก', 'epilepsy', 'seizure', 'phenytoin', 'valproic', 'carbamazepine', 'lamotrigine', 'levetiracetam']),
        ('Stroke', ['หลอดเลือดสมอง', 'stroke', 'ischemic stroke', 'rtpa', 'aspirin']),
        ('Parkinson disease', ['พาร์กินสัน', 'parkinson', 'levodopa', 'carbidopa', 'pramipexole', 'amantadine', 'สั่น']),
        ('Pain management', ['ปวด', 'neuropathic pain', 'gabapentin', 'pregabalin', 'tramadol', 'morphine', 'fentanyl', 'pain']),
        ('Peripheral neuropathy', ['ชาปลายมือปลายเท้า', 'neuropathy', 'vitamin b']),
        ("Dementia, Alzheimer's", ['สมองเสื่อม', 'alzheimer', 'donepezil', 'memantine'])
    ],
    '10. Psychiatric': [
        ('Anxiety/depression', ['ซึมเศร้า', 'depression', 'วิตกกังวล', 'anxiety', 'ssri', 'fluoxetine', 'sertraline', 'escitalopram', 'snri', 'venlafaxine', 'tca', 'amitriptyline']),
        ('Insomnia', ['นอนไม่หลับ', 'insomnia', 'lorazepam', 'diazepam', 'alprazolam', 'clonazepam', 'zolpidem', 'bzd']),
        ('Tobacco dependence', ['บุหรี่', 'สูบบุหรี่', 'เลิกบุหรี่', 'nicotine gum', 'nicotine patch', 'varenicline', 'bupropion']),
        ('Drug & alcohol abuse', ['ติดสุรา', 'alcohol', 'delirium', 'thiamine', 'withdrawal', 'สารเสพติด', 'ยาบ้า', 'methamphetamine'])
    ],
    '11. Pulmonary': [
        ('Asthma', ['หอบหืด', 'asthma', 'salbutamol', 'budesonide', 'ics', 'saba', 'laba', 'fluticasone', 'formoterol', 'montelukast']),
        ('COPD', ['copd', 'ถุงลมโป่งพอง', 'ปอดอุดกั้นเรื้อรัง', 'tiotropium', 'lama', 'ipratropium'])
    ],
    '12. Gynaecologic/Genitourinary': [
        ('Oral contraceptive', ['ยาคุม', 'ยาคุมกำเนิด', 'contraceptive', 'ethinyl estradiol', 'ee', 'levonorgestrel', 'drospirenone', 'ฉุกเฉิน', 'คุมกำเนิด']),
        ('Dysmenorrhea', ['ปวดประจำเดือน', 'dysmenorrhea', 'mefenamic', 'ponstan', 'nsaids']),
        ('Hormonal replacement', ['วัยทอง', 'menopause', 'hrt', 'hormone replacement', 'estrogen', 'progesterone']),
        ('Urinary incontinence', ['ปัสสาวะเล็ด', 'incontinence', 'bph', 'ต่อมลูกหมาก', 'tamsulosin', 'finasteride', 'oxybutynin'])
    ],
    '13. Eye disorder': [
        ('Glaucoma, Cataract', ['ต้อหิน', 'glaucoma', 'ความดันลูกตา', 'iop', 'timolol', 'latanoprost', 'brimonidine', 'acetazolamide', 'ต้อกระจก']),
        ('Conjunctivitis', ['เยื่อบุตาอักเสบ', 'ตาแดง', 'conjunctivitis', 'tobramycin', 'chloramphenicol eye', 'antazoline']),
        ('Contact Lens', ['คอนแทคเลนส์', 'contact lens', 'น้ำยาล้างคอนแทคเลนส์', 'ตาแห้ง', 'น้ำตาเทียม', 'artificial tears'])
    ],
    '14. Oncologic': [
        ('CINV & Supportive Care', ['มะเร็ง', 'chemotherapy', 'cisplatin', 'doxorubicin', 'cyclophosphamide', 'methotrexate', 'cinv', 'ondansetron', 'aprepitant', 'neutropenia', 'filgrastim'])
    ],
    '15. Renal': [
        ('Chronic kidney diseases', ['ckd', 'ไตวายเรื้อรัง', 'egfr', 'creatinine', 'bun', 'crcl', 'stage 3', 'stage 4', 'stage 5', 'hemodialysis', 'phosphate binder', 'epo']),
        ('Acute kidney injury', ['aki', 'ไตวายเฉียบพลัน', 'cin', 'contrast-induced', 'prerenal', 'postrenal']),
        ('Fluid & Electrolyte', ['โปแตสเซียม', 'hyperkalemia', 'hypokalemia', 'sodium', 'hyponatremia', 'kayexalate', 'calcium gluconate', 'electrolyte'])
    ],
    '18. Clinical Nutrition': [
        ('Clinical Nutrition', ['อาหารทางการแพทย์', 'nutrition', 'tpn', 'parenteral', 'enteral', 'แคลอรี่', 'osmolarity', 'amino acid iv'])
    ],
    '16. Others & Toxic': [
        ('Toxicology & Antidote', ['antidote', 'paracetamol toxicity', 'nac', 'acetylcysteine', 'organophosphate', 'atropine', 'pralidoxime', 'pam', 'พิษ', 'poisoning', 'overdose'])
    ]
}

# Product Sheets default subtopics
product_subs = {
    '1. Titrations': 'Acid-base titration',
    '2. Chromatography': 'HPLC (Liquid Chromatography)',
    '3. Spectroscopy & Optics': 'UV-Vis Spectroscopy',
    '4. Preformulation & GMP': 'Good Manufacturing Practice',
    '5. Pharmaceutical Calc': 'Compounding adjustments',
    '6. Solid Dosage Forms': 'Tablet Manufacturing',
    '7. Liquid & Semisolids': 'Solutions, Syrups & Elixirs',
    '8. Biopharm & Drug Release': 'Dissolution testing',
    '9. Sterile & Special Forms': 'Sterility & Pyrogen testing',
    '10. Biotech Products': 'Recombinant DNA',
    '11. Herbal Products': 'Herbal Extraction methods',
    '12. Food Products & QA': 'Food classification & Law',
    '13. Medicinal Chemistry': 'SAR & Drug Design',
    '17. Herbal Medicine': 'Herbal Extraction methods'
}

# SAP Sheets default subtopics
sap_subs = {
    '1. Pharmacy Laws & Ethics': 'พ.ร.บ. ยา พ.ศ. 2510',
    '2. Pharmacy Administration & System': 'ระบบประกันสุขภาพ',
    '3. Research & Biostats': 'รูปแบบการวิจัยทางคลินิก'
}

def determine_standard_subtopic(sheet_name, q_text, curr_subtopic):
    text = (q_text + ' ' + (curr_subtopic or '')).lower()
    
    if sheet_name in sheet_subtopic_map:
        for std_sub, kw_list in sheet_subtopic_map[sheet_name]:
            if any(k in text for k in kw_list):
                return std_sub
        return sheet_subtopic_map[sheet_name][0][0]
        
    if sheet_name in product_subs:
        if sheet_name == '1. Titrations':
            if any(k in text for k in ['redox', 'iodine', 'permanganate', 'ceric']): return 'Redox titration'
            if any(k in text for k in ['complex', 'edta', 'zn', 'mg']): return 'Complexometric titration'
            if any(k in text for k in ['precipitat', 'fajans', 'volhard', 'mohr', 'ag']): return 'Precipitation titration'
            return 'Acid-base titration'
        elif sheet_name == '2. Chromatography':
            if any(k in text for k in ['tlc', 'rf', 'thin layer']): return 'TLC (Thin Layer)'
            if any(k in text for k in ['gc', 'gas chrom', 'flame ionization', 'fid']): return 'GC (Gas Chromatography)'
            if any(k in text for k in ['system suitability', 'tailing', 'resolution', 'theoretical plate', 'capacity factor', 'n = 16']): return 'System Suitability Testing'
            return 'HPLC (Liquid Chromatography)'
        elif sheet_name == '3. Spectroscopy & Optics':
            if any(k in text for k in ['ir', 'ftir', 'infrared', 'wavenumber', 'carbonyl', 'cm-1']): return 'Infrared (IR) Spectroscopy'
            if any(k in text for k in ['nmr', 'mass', 'ms', 'm/z']): return 'NMR & Mass Spectrometry'
            if any(k in text for k in ['polarim', 'specific rotation', 'chiral', 'optical']): return 'Polarimetry'
            return 'UV-Vis Spectroscopy'
        elif sheet_name == '6. Solid Dosage Forms':
            if any(k in text for k in ['defect', 'capping', 'lamination', 'sticking', 'picking', 'chipping']): return 'Tablet Defects'
            if any(k in text for k in ['coat', 'film coat', 'enteric', 'sugar coat']): return 'Tablet Coating'
            if any(k in text for k in ['capsule', 'capsules', 'แคปซูล']): return 'Hard & Soft Gelatin Capsules'
            if any(k in text for k in ['granul', 'powder', 'angle of repose', 'carr']): return 'Powders & Granules'
            return 'Tablet Manufacturing'
        elif sheet_name == '7. Liquid & Semisolids':
            if any(k in text for k in ['suspension', 'flocculat', 'deflocculat', 'sedimentation']): return 'Suspensions'
            if any(k in text for k in ['emulsion', 'creaming', 'coalescence', 'hlb', 'surfactant', 'span', 'tween']): return 'Emulsions'
            if any(k in text for k in ['gel', 'carbopol', 'triethanolamine']): return 'Gels'
            if any(k in text for k in ['suppository', 'suppositories', 'cacao butter', 'fattibase', 'ยาเหน็บ']): return 'Suppositories'
            if any(k in text for k in ['cream', 'ointment', 'ครีม', 'ขี้ผึ้ง', 'petrolatum']): return 'Creams & Ointments'
            return 'Solutions, Syrups & Elixirs'
        elif sheet_name == '8. Biopharm & Drug Release':
            if any(k in text for k in ['bcs', 'solubility', 'permeability']): return 'BCS Classification'
            if any(k in text for k in ['transdermal', 'patch', 'tds']): return 'Transdermal Delivery (TDS)'
            if any(k in text for k in ['diffusion', 'fick']): return "Diffusion & Fick's laws"
            return 'Dissolution testing'
        elif sheet_name == '9. Sterile & Special Forms':
            if any(k in text for k in ['autoclave', 'dry heat', 'sterilization', 'd-value', 'z-value', 'f0']): return 'Autoclave & Sterilization'
            if any(k in text for k in ['pyrogen', 'endotoxin', 'lal', 'rabbit']): return 'Sterility & Pyrogen testing'
            if any(k in text for k in ['cleanroom', 'grade a', 'grade b', 'hepa', 'laminar']): return 'Sterile Cleanroom specs'
            if any(k in text for k in ['inhaler', 'mdi', 'dpi', 'aerosol']): return 'Inhalation devices'
            return 'Parenterals & Ophthalmic'
        return product_subs.get(sheet_name, curr_subtopic or sheet_name)
        
    if sheet_name in sap_subs:
        if sheet_name == '1. Pharmacy Laws & Ethics':
            if any(k in text for k in ['เสพติด', 'วัตถุออกฤทธิ์', 'ประเภท 2', 'ประเภท 4', 'bzd', 'morphine', 'codeine']): return 'พ.ร.บ. ยาเสพติดให้โทษ & วัตถุออกฤทธิ์'
            if any(k in text for k in ['สมุนไพร', 'เครื่องสำอาง']): return 'พ.ร.บ. ผลิตภัณฑ์สมุนไพร & เครื่องสำอาง'
            if any(k in text for k in ['จรรยาบรรณ', 'จริยธรรม', 'สภาเภสัชกรรม', 'ใบอนุญาตประกอบวิชาชีพ']): return 'พ.ร.บ. วิชาชีพเภสัชกรรม 2537'
            return 'พ.ร.บ. ยา พ.ศ. 2510'
        elif sheet_name == '2. Pharmacy Administration & System':
            if any(k in text for k in ['rdu', 'asu', 'การใช้ยาอย่างสมเหตุผล']): return 'นโยบายการใช้ยาอย่างสมเหตุผล'
            return 'ระบบประกันสุขภาพ'
        elif sheet_name == '3. Research & Biostats':
            if any(k in text for k in ['icer', 'qaly', 'cma', 'cea', 'cua', 'cba', 'ความคุ้มค่า', 'ต้นทุน']): return 'วิธีประเมินต้นทุนและประสิทธิผล'
            if any(k in text for k in ['p-value', 'relative risk', 'odds ratio', '95% ci', 'mean', 'sd', 'anova', 'chi-square']): return 'สถิติวิเคราะห์'
            return 'รูปแบบการวิจัยทางคลินิก'
        return sap_subs.get(sheet_name, curr_subtopic or sheet_name)
        
    return curr_subtopic or sheet_name
