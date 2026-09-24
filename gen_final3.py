import json

def generate_rationale(choice_text):
    text = str(choice_text).lower()
    if 'amlodipine' in text:
        return 'Amlodipine เป็นยากลุ่ม Dihydropyridine CCB ที่เน้นขยายหลอดเลือดส่วนปลาย ไม่มีผลลดอัตราตายในผู้ป่วย Heart failure และอาจทำให้เกิดผลข้างเคียงคือบวมน้ำ'
    elif 'enalapril' in text or 'acei' in text:
        return 'Enalapril ออกฤทธิ์ยับยั้งเอนไซม์ ACE ช่วยลด Afterload แต่มีข้อห้ามใช้ในสตรีมีครรภ์และอาจทำให้เกิด Hyperkalemia โดยไม่เกี่ยวกับการต้านการเกาะกลุ่มของเกล็ดเลือด'
    elif 'arb' in text:
        return 'Angiotensin II receptor blockers ปิดกั้นการทำงานของ Angiotensin II ที่ AT1 receptor ไม่มีผลยับยั้งเอนไซม์ ACE จึงไม่ทำให้เกิดอาการไอแห้ง'
    elif 'propranolol' in text:
        return 'Propranolol เป็น Non-selective beta-blocker ที่สามารถจับกับ Beta-2 receptor ในหลอดลมได้ ทำให้หลอดลมตีบ จึงห้ามใช้ในผู้ป่วยโรคหอบหืด'
    elif 'metoprolol' in text or 'bisoprolol' in text or 'beta-blocker' in text or 'beta-adrenergic' in text:
        return 'Beta-blockers มีฤทธิ์ลดการทำงานของหัวใจ (Negative inotrope/chronotrope) หากนำมาใช้ขณะที่ผู้ป่วยมีภาวะ Acute decompensated heart failure จะทำให้อาการแย่ลง'
    elif 'furosemide' in text:
        return 'Furosemide ยับยั้ง Na+/K+/2Cl- cotransporter ที่ Ascending loop of Henle ช่วยขับปัสสาวะเพื่อลดอาการบวม แต่ไม่มีผลยืดอายุขัยผู้ป่วย Heart failure'
    elif 'hctz' in text or 'diuretic' in text:
        return 'Thiazide diuretics ออกฤทธิ์ยับยั้ง Na+/Cl- cotransporter ที่ Distal convoluted tubule อาจเพิ่มความเสี่ยงของภาวะ Uric acid, Glucose และ Calcium ในเลือดสูง'
    elif 'simvastatin' in text or 'statin' in text:
        return 'Simvastatin มีค่าครึ่งชีวิตสั้นและการสร้างคอเลสเตอรอลในร่างกายเกิดสูงสุดในช่วงกลางคืน การบริหารยาในเวลาอื่นจะทำให้ประสิทธิภาพการลด LDL-C ลดลง'
    elif 'gemfibrozil' in text or 'fibrate' in text:
        return 'Gemfibrozil มีฤทธิ์ลดระดับ Triglyceride ได้ดี แต่หากใช้ร่วมกับ Statins จะยับยั้งการกำจัด Statins เพิ่มความเสี่ยงของภาวะกล้ามเนื้อสลาย (Rhabdomyolysis)'
    elif 'aspirin' in text:
        return 'Aspirin ยับยั้ง COX-1 แบบ Irreversible ทำให้เกล็ดเลือดไม่สามารถสร้าง Thromboxane A2 ได้ตลอดอายุขัยของเกล็ดเลือดนั้น'
    elif 'clopidogrel' in text:
        return 'Clopidogrel เป็น Prodrug ที่ต้องถูกเปลี่ยนโดย CYP2C19 ให้เป็น Active form เพื่อไปยับยั้ง P2Y12 receptor บนเกล็ดเลือด ป้องกันเกล็ดเลือดเกาะกลุ่ม'
    elif 'digoxin' in text:
        return 'Digoxin ยับยั้ง Na+/K+ ATPase pump ทำให้เพิ่ม Intracellular calcium แต่ผู้ป่วยที่มีภาวะ Hypokalemia จะเสี่ยงต่อ Digoxin toxicity ได้ง่ายขึ้น'
    elif 'verapamil' in text or 'diltiazem' in text or 'non-dhp' in text:
        return 'Non-DHP CCBs ออกฤทธิ์ยับยั้งแคลเซียมแชนแนลที่เซลล์กล้ามเนื้อหัวใจ มีฤทธิ์ Negative inotrope จึงมีข้อห้ามใช้ในผู้ป่วย Heart failure with reduced EF'
    elif 'dash' in text:
        return 'การรับประทานอาหารแบบ DASH เน้นลดปริมาณโซเดียมและเพิ่มโพแทสเซียม แม้จะมีประสิทธิภาพสูงแต่ก็ไม่ได้แก้ไขพยาธิสภาพของหลอดเลือดได้ทั้งหมด'
    elif 'sodium' in text or 'โซเดียม' in text:
        return 'การจำกัดปริมาณโซเดียมในอาหารช่วยลดความดันโลหิตได้จริง แต่ให้ผลลด SBP ได้เพียง 2-8 mmHg ซึ่งน้อยกว่าการรับประทานอาหารแบบ DASH'
    elif 'ออกกำลังกาย' in text or 'exercise' in text:
        return 'การออกกำลังกายแบบแอโรบิกมีประโยชน์ต่อระบบหัวใจและหลอดเลือด แต่สามารถลด SBP ได้เฉลี่ย 4-9 mmHg ซึ่งอาจไม่เพียงพอหากผู้ป่วยไม่ได้ปรับการกินอาหาร'
    elif 'บุหรี่' in text:
        return 'การเลิกบุหรี่ช่วยลดความเสี่ยงการเกิดโรคหลอดเลือดหัวใจโดยรวม แต่ไม่มีผลโดยตรงต่อการลดระดับความดันโลหิตในระยะสั้นอย่างมีนัยสำคัญ'
    elif 'แอลกอฮอล์' in text or 'alcohol' in text:
        return 'การจำกัดเครื่องดื่มแอลกอฮอล์สามารถช่วยลด SBP ได้เพียง 2-4 mmHg ซึ่งน้อยกว่าประโยชน์ที่ได้จากการคุมอาหารและการใช้ยา'
    elif 'docetaxel' in text:
        return 'Docetaxel เป็นยากลุ่ม Taxanes ออกฤทธิ์ส่งเสริมการรวมตัวของ Tubulin แต่ยับยั้งการสลายตัวของ Microtubule ทำให้เซลล์หยุดการแบ่งตัวในระยะ M phase'
    elif 'cytarabine' in text:
        return 'Cytarabine เป็นยาต้านมะเร็งกลุ่ม Antimetabolites ทำหน้าที่รบกวนการทำงานของเอนไซม์ DNA polymerase เฉพาะในระยะ S phase ของวงจรเซลล์'
    elif 'cisplatin' in text:
        return 'Cisplatin จับกับสาย DNA เกิดเป็น Cross-links รบกวนกระบวนการ Replication ทำให้เซลล์มะเร็งตายโดยไม่จำเพาะต่อระยะของวัฏจักรเซลล์ (Cell cycle non-specific)'
    elif 'navelbine' in text or 'vinorelbine' in text:
        return 'Vinorelbine เป็นยากลุ่ม Vinca alkaloids ออกฤทธิ์จับกับ Tubulin และยับยั้งการสร้าง Microtubule ป้องกันการแบ่งโครโมโซมในระยะ M phase'
    elif 'phenylephrine' in text:
        return 'Phenylephrine เป็น Alpha-1 agonist ที่ทำให้หลอดเลือดหดตัว หากใช้หยอดตาลดอาการตาแดงติดต่อกันนานเกินไปอาจเกิด Rebound congestion ได้'
    elif 'oxymetazoline' in text or 'naphazoline' in text or 'tetrahydrozoline' in text:
        return 'ยาสเตียรอยด์หรือยาในกลุ่ม Imidazoline มีฤทธิ์ Alpha-agonist ช่วยลดอาการคั่งของหลอดเลือด แต่ไม่เกี่ยวข้องกับการต้านจุลชีพหรือต้านการอักเสบ'
    elif 'anti-inflammatory' in text or 'อักเสบ' in text:
        return 'ฤทธิ์ลดการอักเสบเป็นส่วนหนึ่งของ Pleiotropic effects ของยา Statins ที่ลดการหลั่ง Cytokines แต่ไม่ใช่กลไกหลักในการยับยั้งการสร้างคอเลสเตอรอล'
    elif 'เกล็ดเลือด' in text or 'platelet' in text:
        return 'Statins มีฤทธิ์ลดการเกาะกลุ่มของเกล็ดเลือดได้ทางอ้อม (Pleiotropic effects) แต่ไม่สามารถนำมาใช้แทนยา Antiplatelets อย่าง Aspirin หรือ Clopidogrel ได้'
    elif 'oxidized ldl' in text:
        return 'Statins ยับยั้งกระบวนการเกิด Oxidation ของ LDL ลดการสร้าง Foam cells แต่ในผู้ป่วยที่มีไขมันสูงมากอาจยังต้องการยาเสริมอื่นๆ ร่วมด้วย'
    elif 'glucose' in text or 'กลูโคส' in text:
        return 'การรบกวนระดับกลูโคสหรือความไวต่ออินซูลินเป็นผลข้างเคียงของยา Statins บางชนิด ไม่ใช่ฤทธิ์ทางคลินิกที่นำมาใช้ประโยชน์ในการรักษา'
    elif 'grave' in text:
        return 'Grave\'s disease ทำให้ร่างกายสร้าง Antibody มากระตุ้นต่อมไทรอยด์ให้ทำงานหนัก แต่ผู้ป่วยบางรายอาจต้องรักษาด้วย Radioactive iodine มากกว่าการผ่าตัด'
    elif 'hashimoto' in text:
        return 'Hashimoto\'s thyroiditis เกิดจาก Antibody ทำลายต่อมไทรอยด์ ทำให้การทำงานลดลง (Hypothyroidism) จึงไม่ใช่สาเหตุหลักของการเกิดอาการ Hyperthyroidism ตามโจทย์'
    elif 'เด็ก' in text or 'ผู้สูงอายุ' in text:
        return 'การผ่าตัดหรือการให้แร่รังสีในเด็กหรือผู้สูงอายุมีข้อจำกัดและผลข้างเคียงสูง มักเริ่มต้นการรักษาด้วยยาต้านไทรอยด์กลุ่ม Thionamides ก่อน'
    elif 'amitriptyline' in text:
        return 'Amitriptyline ยับยั้งการเก็บกลับของ Serotonin และ Norepinephrine แต่มีฤทธิ์ Anticholinergic ค่อนข้างสูง ทำให้มีอาการข้างเคียง เช่น ปากแห้ง หรือปัสสาวะคั่ง'
    elif 'da transporter' in text or 'dopamine' in text:
        return 'การยับยั้ง Dopamine transporter เป็นกลไกของยากลุ่ม NDRI อย่าง Bupropion หรือยากระตุ้นประสาท ไม่ใช่กลไกของยาแก้ซึมเศร้ากลุ่ม TCAs'
    elif 'ne transporter' in text:
        return 'แม้ TCAs จะยับยั้ง NE transporter แต่ก็ยับยั้ง Serotonin transporter ด้วย การยับยั้งเพียง NE อย่างเดียวเป็นลักษณะของยากลุ่ม NRIs อย่าง Reboxetine'
    elif 'moa enzyme' in text or 'mao' in text:
        return 'ยาที่ยับยั้ง MAO enzyme คือกลุ่ม MAOIs เช่น Phenelzine ไม่ใช่ยา TCAs และมีข้อควรระวังเรื่องปฏิกิริยากับอาหารที่มี Tyramine'
    elif '5-ht receptor' in text:
        return 'การกระตุ้น 5-HT receptors เป็นกลไกของยากลุ่ม Triptans ใช้รักษาไมเกรน ไม่ใช่กลไกการออกฤทธิ์ของ Amitriptyline หรือยาต้านซึมเศร้ากลุ่ม TCAs'
    elif 'alpha2' in text or 'α2' in text:
        return 'การกระตุ้น Alpha-2 receptor เป็นกลไกของยา Clonidine หรือ Methyldopa เพื่อลดการหลั่ง Norepinephrine ไม่ใช่กลไกของ Amitriptyline'
    elif 'dry mouth' in text or 'sedation' in text or 'urinary retention' in text or 'hypotension' in text:
        return 'อาการเหล่านี้เกิดจากการที่ยาไปจับและปิดกั้น Muscarinic, Histamine H1 หรือ Alpha-1 receptors ตามลำดับ ถือเป็นผลข้างเคียงที่อธิบายได้จากตัวยา'
    elif 'hyperuricemia' in text or 'uric' in text:
        return 'Hyperuricemia มักเกิดจากยาขับปัสสาวะกลุ่ม Thiazide หรือ Loop diuretics เนื่องจากรบกวนการหลั่งกรดยูริกที่ท่อไต ไม่พบว่าเป็นผลข้างเคียงหลักของ TCAs'
    elif '120/80' in text:
        return '120/80 mmHg ถือเป็นความดันโลหิตระดับปกติ การกำหนดเป้าหมายในผู้ป่วยที่ได้รับยามักไม่ต้องการกดให้ต่ำถึงระดับนี้หากไม่มีข้อบ่งชี้จำเพาะ'
    elif '130/80' in text or '130/90' in text:
        return 'เป้าหมายความดันโลหิตนี้มักพิจารณาในผู้ป่วยที่มีโรคร่วมเสี่ยงสูง เช่น เบาหวาน หรือโรคไตเรื้อรังที่มีโปรตีนรั่วทางปัสสาวะ'
    elif '140/80' in text or '140/90' in text:
        return 'เป้าหมายระดับ 140/90 mmHg เป็นเกณฑ์มาตรฐานที่ยอมรับได้สำหรับผู้ป่วยทั่วไปตามหลาย Guideline หากไม่ได้มีความเสี่ยงทางหัวใจและหลอดเลือดสูง'
    elif 'mg/dl' in text:
        return 'ค่าระดับไขมันในเลือดนี้คลาดเคลื่อนจากการคำนวณผ่านสมการ Friedewald equation (LDL-C = TC - HDL-C - TG/5) เมื่อนำค่าจากโจทย์มาแทนในสูตร'
    elif 'ตอนเช้า' in text or 'ตอนกลางวัน' in text:
        return 'Simvastatin มีค่าครึ่งชีวิตเพียง 1-2 ชั่วโมง การบริหารยาในช่วงเวลานี้จะไม่ครอบคลุมการยับยั้งเอนไซม์ HMG-CoA reductase ในช่วงกลางคืน'
    elif 'เปลี่ยนไป' in text:
        return 'การเปลี่ยนแปลงเวลาหรือความถี่ของการให้ยาอย่างไม่เหมาะสมอาจส่งผลให้ระดับยาในเลือดไม่เข้าสู่ Therapeutic range และไม่ถึงเป้าหมายการรักษา'
    elif 'praziquantel' in text:
        return 'Praziquantel ออกฤทธิ์เพิ่มความซึมผ่านของแคลเซียมที่ผนังเซลล์ของพยาธิ ทำให้พยาธิเกิดอาการหดเกร็งและตาย ไม่ใช่กลไกยับยั้ง Microtubule'
    elif 'niclosamide' in text:
        return 'Niclosamide ยับยั้งกระบวนการ Oxidative phosphorylation ของพยาธิ ทำให้ขาดพลังงาน ATP นำไปใช้รักษาพยาธิตัวตืดได้ดี'
    elif 'mebendazole' in text:
        return 'Mebendazole ยับยั้งกระบวนการสร้าง Microtubule อย่างจำเพาะเจาะจงในพยาธิ และทำให้การดูดซึมกลูโคสของพยาธิลดลงจนขาดสารอาหารตาย'
    elif 'pyrantel pamoate' in text:
        return 'Pyrantel pamoate มีฤทธิ์เป็น Depolarizing neuromuscular blocker กระตุ้น Nicotinic receptors ของพยาธิ ทำให้พยาธิเป็นอัมพาตและถูกขับออกมา'
    elif 'ivermectin' in text:
        return 'Ivermectin ออกฤทธิ์กระตุ้น Glutamate-gated chloride channels ที่ระบบประสาทของพยาธิ ทำให้เซลล์เกิด Hyperpolarization และเป็นอัมพาต'
    elif 'insulin' in text or 'lispro' in text or 'nph' in text or 'aspart' in text:
        return 'คุณสมบัติทางเภสัชจลนศาสตร์ของ Insulin แต่ละชนิดแตกต่างกัน เช่น Rapid-acting ออกฤทธิ์เร็ว ส่วน NPH มีฤทธิ์ปานกลางและไม่เหมาะใช้แก้ภาวะ DKA'
    elif 'β-cell' in text or 'sulfonylurea' in text or 'glibenclamide' in text:
        return 'ยากลุ่ม Sulfonylureas เช่น Glibenclamide กระตุ้นการหลั่งอินซูลินจากเบต้าเซลล์ของตับอ่อน เพิ่มความเสี่ยงของภาวะน้ำตาลในเลือดต่ำ'
    elif 'ดูดซึม' in text or 'acarbose' in text:
        return 'Acarbose ยับยั้งเอนไซม์ Alpha-glucosidase ที่ลำไส้ ทำให้ชะลอการย่อยและดูดซึมคาร์โบไฮเดรต ช่วยลดระดับน้ำตาลหลังอาหาร (Postprandial glucose)'
    elif 'metformin' in text or 'ตับ' in text or 'egfr' in text:
        return 'Metformin มีกลไกหลักคือยับยั้ง Hepatic glucose production ห้ามใช้ในผู้ป่วยที่มี eGFR < 30 mL/min/1.73m2 เนื่องจากเสี่ยงต่อภาวะ Lactic acidosis'
    elif 'repaglinide' in text:
        return 'Repaglinide เป็นยากลุ่ม Meglitinides ออกฤทธิ์กระตุ้นการหลั่งอินซูลินในช่วงสั้นๆ (Short-acting secretagogue) สามารถนำมาใช้ในผู้ป่วยโรคไตเรื้อรังได้'
    elif 'cushing' in text or 'prader' in text or 'hyperthyroidism' in text:
        return 'Cushing\'s syndrome และ Prader-Willi syndrome สามารถทำให้เกิดความอ้วนได้ ขณะที่ Hyperthyroidism มักทำให้มีอัตราการเผาผลาญสูงและน้ำหนักลดลง'
    elif 'reye' in text or 'airway hypersensitivity' in text or 'bleeding' in text:
        return 'การให้ยา Aspirin ในเด็กที่มีการติดเชื้อไวรัส เช่น ไข้หวัดใหญ่ หรืออีสุกอีใส จะเพิ่มความเสี่ยงสูงมากต่อการเกิด Reye\'s syndrome ซึ่งทำให้สมองและตับบวม'
    elif 'ช่องแช่เย็น' in text or 'ตะแคง' in text or 'ละลาย' in text:
        return 'วิธีการเหน็บยาที่ถูกต้องควรรักษาความเย็นเพื่อไม่ให้ยาละลายก่อนสอด แต่ต้องให้ผู้ป่วยนอนตะแคงค้างไว้อย่างน้อย 15-30 นาทีเพื่อให้ยาออกฤทธิ์เต็มที่ ไม่ใช่แค่ 5 นาที'
    elif 'hydro' in text or 'demethylation' in text or 'reduction' in text:
        return 'ยากลุ่ม Nitroimidazole จำเป็นต้องอาศัยกระบวนการ Nitro-reduction ในเชื้อแบคทีเรียไร้ออกซิเจนหรือโปรโตซัว เพื่อเปลี่ยนให้กลายเป็นสารที่มีพิษทำลาย DNA ของเชื้อ'
    elif 'tinnitus' in text:
        return 'Tinnitus (หูอื้อ) มักพบเมื่อได้รับยา Aspirin ในขนาดสูง (Salicylism) แต่ไม่ใช่สาเหตุหลักที่ห้ามใช้ยา Aspirin ในเด็กที่ติดเชื้อไวรัส'
    else:
        return 'กลไกหรือคำแนะนำดังกล่าวไม่สอดคล้องกับพยาธิสภาพของโรคและเภสัชวิทยาของยาที่ระบุในกรณีศึกษา จึงอาจทำให้เกิดความล้มเหลวในการรักษา'

def process():
    try:
        with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\cardio_part4.json', encoding='utf-8') as f:
            data = json.load(f)
        
        out_dict = {}
        letters = {1: 'ก', 2: 'ข', 3: 'ค', 4: 'ง', 5: 'จ'}
        for d in data:
            c_idx = str(d['cardio_idx'])
            ans_str = str(d.get('ans', '')).strip()
            
            correct_num = None
            if ans_str.isdigit():
                correct_num = int(ans_str)
            
            distractors = {}
            for i in range(1, 6):
                if i != correct_num:
                    choice_text = d.get(f'c{i}', '')
                    if choice_text:
                        distractors[letters[i]] = generate_rationale(choice_text)
            
            out_dict[c_idx] = {"distractors": distractors}
            
        with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\distractors_cardio_part4.json', 'w', encoding='utf-8') as f:
            json.dump(out_dict, f, ensure_ascii=False, indent=4)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    process()
