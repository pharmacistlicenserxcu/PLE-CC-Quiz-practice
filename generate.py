import json
import re

with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\endo_part4.json', encoding='utf-8') as f:
    data = json.load(f)

drug_rationales = {
    'Glipizide': 'Glipizide เป็นยากลุ่ม Sulfonylurea ที่ออกฤทธิ์ปิด K-ATP channel บนเบต้าเซลล์ ทำให้กระตุ้นการหลั่งอินซูลิน ใช้สำหรับเบาหวานชนิดที่ 2 เท่านั้น',
    'Empagliflozin': 'Empagliflozin เป็นยากลุ่ม SGLT2 inhibitor ออกฤทธิ์ยับยั้งการดูดกลับน้ำตาลที่ท่อไตส่วนต้น ขับน้ำตาลออกทางปัสสาวะ',
    'Sitagliptin': 'Sitagliptin เป็นยากลุ่ม DPP-4 inhibitor ช่วยยับยั้งเอนไซม์ที่ทำลาย GLP-1 ทำให้ฮอร์โมน Incretin ทำงานได้นานขึ้น',
    'Liraglutide': 'Liraglutide เป็น GLP-1 receptor agonist ออกฤทธิ์กระตุ้นการหลั่งอินซูลินตามระดับน้ำตาล ยับยั้งการหลั่ง Glucagon และชะลอการบีบตัวของกระเพาะอาหาร',
    'Propylthiouracil': 'Propylthiouracil (PTU) ยับยั้งเอนไซม์ Thyroid peroxidase และยับยั้งการเปลี่ยน T4 เป็น T3 ที่เนื้อเยื่อรอบนอก ใช้รักษาภาวะ Hyperthyroidism',
    'Methimazole': 'Methimazole ออกฤทธิ์ยับยั้งเอนไซม์ Thyroid peroxidase ยับยั้งการสังเคราะห์ฮอร์โมนไทรอยด์ ใช้รักษา Hyperthyroidism',
    'Pioglitazone': 'Pioglitazone เป็นยากลุ่ม Thiazolidinedione ออกฤทธิ์ผ่าน PPAR-gamma receptor ช่วยเพิ่ม Insulin sensitivity ที่เซลล์กล้ามเนื้อและไขมัน',
    'Insulin glargine': 'Insulin glargine เป็น Basal insulin ออกฤทธิ์ยาว ไม่มีพีค ใช้เพื่อควบคุมระดับน้ำตาลพื้นฐาน (Fasting blood glucose)',
    'Insulin lispro': 'Insulin lispro เป็น Rapid-acting insulin ออกฤทธิ์เร็ว ใช้ฉีดก่อนอาหารเพื่อควบคุมระดับน้ำตาลหลังมื้ออาหาร (Postprandial glucose)',
    'Dapagliflozin': 'Dapagliflozin เป็นยากลุ่ม SGLT2 inhibitor ขับน้ำตาลออกทางปัสสาวะ มีผลข้างเคียงคือน้ำหนักลด ไม่ใช่น้ำหนักเพิ่ม',
    'Semaglutide': 'Semaglutide เป็น GLP-1 receptor agonist มีทั้งรูปแบบฉีดและกิน ช่วยลดน้ำหนักและคุมน้ำตาล ไม่ทำให้น้ำหนักเพิ่ม',
    'Metformin': 'Metformin ออกฤทธิ์ยับยั้ง Gluconeogenesis ที่ตับ ไม่ทำให้น้ำหนักเพิ่ม และเป็น First-line drug สำหรับเบาหวานชนิดที่ 2',
    'Levothyroxine': 'Levothyroxine เป็นฮอร์โมน T4 สังเคราะห์ ใช้ทดแทนในผู้ป่วย Hypothyroidism ข้อควรระวังคือการเกิด Thyrotoxicosis หากได้รับขนาดสูงเกินไป',
    'Acarbose': 'Acarbose เป็น Alpha-glucosidase inhibitor ชะลอการดูดซึมคาร์โบไฮเดรต ต้องระวังการใช้ในผู้ป่วยโรคไตหรือโรคลำไส้',
    'Glibenclamide': 'Glibenclamide เป็น Sulfonylurea ที่ออกฤทธิ์ยาวและมี active metabolite ขับออกทางไต จึงมีข้อห้ามใช้ในผู้ป่วยโรคไตเสื่อม (CKD)',
    'Repaglinide': 'Repaglinide เป็น Meglitinide กระตุ้นการหลั่งอินซูลินแบบรวดเร็วและสั้น ขับออกทางตับเป็นหลัก สามารถใช้ในผู้ป่วยโรคไตได้',
    'Timolol': 'Timolol เป็น Beta-blocker ชนิด non-selective ลดการสร้าง Aqueous humor เพื่อรักษาต้อหิน',
    'Pilocarpine': 'Pilocarpine เป็น Muscarinic agonist กระตุ้นการหดตัวของ Ciliary muscle เพิ่มการระบาย Aqueous humor',
    'Acetazolamide': 'Acetazolamide เป็น Carbonic anhydrase inhibitor ลดการสร้าง Aqueous humor',
    'Betaxolol': 'Betaxolol เป็น Beta-1 selective blocker ลดการสร้าง Aqueous humor',
    'Brimonidine': 'Brimonidine เป็น Alpha-2 adrenergic agonist ช่วยลดการสร้างและเพิ่มการระบาย Aqueous humor',
    'omeprazole': 'Omeprazole เป็น PPI ยับยั้ง H+/K+ ATPase ปั๊มที่กระเพาะอาหาร ไม่เกี่ยวข้องกับการเสริม Folate',
    'calcium carbonate': 'Calcium carbonate ใช้เสริมแคลเซียมและจับฟอสเฟตในเลือด ไม่ป้องกันพิษจาก Methotrexate',
    'folic acid': 'Folic acid ป้องกันและลดพิษต่อไขกระดูกและเยื่อบุจากการใช้ยา Methotrexate',
    'vitamin K': 'Vitamin K เป็น Co-factor สำหรับปัจจัยการแข็งตัวของเลือดต้านฤทธิ์ Warfarin ไม่ลดผลข้างเคียงของ DMARDs',
    'finasteride': 'Finasteride ยับยั้งเอนไซม์ 5-alpha reductase ใช้รักษา BPH และผมร่วงทางพันธุกรรม',
    'Radioactive iodine': 'Radioactive iodine (I-131) ใช้ทำลายเนื้อเยื่อไทรอยด์อย่างถาวร ห้ามใช้ในสตรีมีครรภ์และสตรีให้นมบุตรเนื่องจากผ่านน้ำนมและรกได้',
    'KI solution': 'KI solution หรือ Lugol solution ให้ก่อนผ่าตัดไทรอยด์เพื่อลด vascularity ของต่อมไทรอยด์',
    'Propranolol': 'Propranolol ช่วยบรรเทาอาการใจสั่นจากไทรอยด์เป็นพิษ และช่วยยับยั้งการเปลี่ยน T4 เป็น T3 ที่ peripheral tissue'
}

def get_rationale(choice_text):
    for key, rationale in drug_rationales.items():
        if key.lower() in str(choice_text).lower():
            return rationale
    return 'ตัวเลือกนี้ไม่ได้มีกลไกทางเภสัชวิทยาหรือข้อบ่งใช้ที่ตรงกับพยาธิสภาพทางคลินิกที่ระบุในโจทย์ข้อนี้'

out = {}
options_map = {'1': 'ก', '2': 'ข', '3': 'ค', '4': 'ง', '5': 'จ'}

for item in data:
    idx = str(item['endo_idx'])
    ans = str(item['ans'])
    distractors = {}
    
    for k, v in options_map.items():
        if k != ans:
            choice_key = f'c{k}'
            choice_text = str(item.get(choice_key, ''))
            
            # Special manual overrides based on idx and choice
            if idx == '133': 
                if k == '2': distractors[v] = 'Methimazole มีความเสี่ยงในการเกิด Aplasia cutis และ Choanal atresia ในทารก จึงควรหลีกเลี่ยงในไตรมาสแรกของการตั้งครรภ์'
                elif k == '3': distractors[v] = 'Levothyroxine เป็นยารักษา Hypothyroidism ไม่ใช่สำหรับการรักษา Hyperthyroidism ในหญิงตั้งครรภ์'
                elif k == '4': distractors[v] = 'ตัวเลือกนี้ผิดเนื่องจาก Methimazole ควรหลีกเลี่ยงในไตรมาสแรกของการตั้งครรภ์'
                elif k == '5': distractors[v] = 'ผิดทั้งหมดเนื่องจากมีตัวเลือกที่ไม่เหมาะสมคือ Methimazole และ Levothyroxine'
            elif idx == '134': 
                if k == '2': distractors[v] = 'ทนร้อนไม่ได้ (Heat intolerance) เป็นอาการของภาวะ Hyperthyroidism (Thyrotoxicosis) ที่เกิดจากการได้รับยาเกินขนาด'
                elif k == '3': distractors[v] = 'หัวใจเต้นเร็ว (Tachycardia) เป็นผลจากฤทธิ์กระตุ้นระบบประสาทซิมพาเทติกเมื่อมีไทรอยด์ฮอร์โมนสูงเกิน'
                elif k == '4': distractors[v] = 'กระดูกบาง (Osteoporosis) เป็นผลข้างเคียงระยะยาวจากการได้รับ Levothyroxine ขนาดสูงจนกด TSH นานๆ'
                elif k == '5': distractors[v] = 'ชัก (Seizure) สามารถถูกกระตุ้นได้จากภาวะ Severe thyrotoxicosis หรือ Thyroid storm'
                if ans == '1':
                    distractors.pop(options_map.get(ans, ''), None)
            elif idx == '135': 
                if k == '2': distractors[v] = 'ทนต่อความเย็นไม่ได้ (Cold intolerance) เป็นอาการที่พบใน Hypothyroidism เนื่องจากอัตราการเผาผลาญพื้นฐานต่ำลง'
                elif k == '3': distractors[v] = 'ซึมเศร้า อ่อนเพลีย เป็นอาการทางประสาทที่พบได้จากภาวะฮอร์โมนไทรอยด์ต่ำ'
                elif k == '4': distractors[v] = 'ผิวหนังแห้ง เป็นอาการแสดงคลาสสิกของ Hypothyroidism จากการลดลงของการไหลเวียนเลือดที่ผิวหนัง'
                elif k == '5': distractors[v] = 'น้ำหนักลด เป็นอาการของ Hyperthyroidism (Thyrotoxicosis) ผู้ป่วย Hypothyroidism มักจะมีน้ำหนักตัวเพิ่มขึ้น'
            elif idx == '136': 
                if k == '2': distractors[v] = 'Sucralfate ออกฤทธิ์ขัดขวางการดูดซึม (absorption) ของ Levothyroxine ที่ทางเดินอาหาร ไม่ได้เร่งการทำลายยา'
                elif k == '3': distractors[v] = 'Phenytoin เป็น CYP450 inducer ซึ่งจะไปเร่งกระบวนการ Metabolism (การทำลาย) ของฮอร์โมน T4 ทำให้ระดับฮอร์โมนลดลง'
                elif k == '4': distractors[v] = 'Cholestyramine เป็น Bile acid sequestrant ขัดขวางการดูดซึมของฮอร์โมน T4 ในลำไส้'
                elif k == '5': distractors[v] = 'Sodium polystyrene sulfonate ขัดขวางการดูดซึม T4 จากทางเดินอาหาร'
            elif idx == '137':
                if k == '1': distractors[v] = 'Propylthiouracil ยับยั้งการสร้างไทรอยด์ฮอร์โมน แต่ไม่มีผลลดปริมาณเลือดที่มาเลี้ยงต่อมไทรอยด์ (Vascularity)'
                elif k == '2': distractors[v] = 'Methimazole ยับยั้งการสังเคราะห์ฮอร์โมน แต่ไม่ได้ช่วยลดขนาดและเลือดที่มาเลี้ยงต่อมไทรอยด์ก่อนการผ่าตัด'
                elif k == '4': distractors[v] = 'Propranolol ใช้เพื่อควบคุมอาการใจสั่น (Sympathetic overactivity) ไม่มีผลลด Vascularity ของต่อมไทรอยด์'
                elif k == '5': distractors[v] = 'Radioactive iodine ใช้ทำลายเนื้อเยื่อไทรอยด์ ไม่ใช่ยาสำหรับเตรียมผ่าตัด (Preoperative preparation)'
            elif idx == '138': 
                if k == '2': distractors[v] = 'Propylthiouracil (PTU) ขับออกทางน้ำนมในปริมาณน้อย สามารถใช้ได้ แต่ตาม Guidelines ปัจจุบันมักใช้เป็นทางเลือกรองเนื่องจากเสี่ยงต่อภาวะตับวายรุนแรง'
                elif k == '3': distractors[v] = 'Radioactive iodine (I-131) มีข้อห้ามใช้เด็ดขาดในสตรีให้นมบุตร เนื่องจากจะถูกขับออกทางน้ำนมและทำลายต่อมไทรอยด์ของทารก'
                elif k == '4': distractors[v] = 'ตาม Guidelines ปัจจุบัน Methimazole ถือเป็นยาทางเลือกแรกในสตรีให้นมบุตร (ที่ขนาดน้อยกว่า 20 mg/day) เพื่อลดความเสี่ยง Hepatotoxicity จาก PTU'
                elif k == '5': distractors[v] = 'I-131 ห้ามใช้ในหญิงให้นมบุตรอย่างเด็ดขาด จึงไม่สามารถใช้ได้ทุกข้อ'
            elif idx == '173': 
                if k == '2': distractors[v] = 'Acarbose ไม่แนะนำให้ใช้ในผู้ป่วยโรคไตเรื้อรังรุนแรง (CrCl น้อยกว่า 25 mL/min)'
                elif k == '3': distractors[v] = 'Sitagliptin เป็นยาที่ขับออกทางไตเป็นหลัก จึงต้องปรับขนาดยาตามระดับการทำงานของไต (eGFR)'
                elif k == '4': distractors[v] = 'Empagliflozin ห้ามเริ่มใช้เมื่อ eGFR ต่ำกว่า 30 mL/min เนื่องจากประสิทธิภาพในการลดน้ำตาลจะลดลงตามการทำงานของไต'
                elif k == '5': distractors[v] = 'Glibenclamide มี Active metabolites ที่ขับออกทางไต จึงมีข้อห้ามใช้ในผู้ป่วยโรคไตเสื่อมเนื่องจากเพิ่มความเสี่ยงภาวะน้ำตาลในเลือดต่ำอย่างรุนแรง'
            else:
                rationale = get_rationale(choice_text)
                distractors[v] = rationale
                
    out[idx] = {'distractors': distractors}

def set_d(i, k, text):
    if i in out and k in out[i]['distractors']:
        out[i]['distractors'][k] = text

set_d('132', 'ข', 'Insulin lispro เป็น short-acting ออกฤทธิ์คุมน้ำตาลหลังอาหาร ทำให้น้ำหนักเพิ่มได้ แต่มักจะน้อยกว่ายาที่มีฤทธิ์ basal')
set_d('132', 'ค', 'Dapagliflozin เป็นยา SGLT2 inhibitor มีผลทำให้สูญเสียกลูโคสผ่านทางปัสสาวะ จึงส่งผลให้น้ำหนักตัวลดลง ไม่ใช่น้ำหนักเพิ่ม')
set_d('132', 'ง', 'Semaglutide เป็น GLP-1 receptor agonist ทำให้กระเพาะอาหารบีบตัวช้าลงและเพิ่มความอิ่ม ส่งผลให้น้ำหนักตัวลดลงอย่างมีนัยสำคัญ')
set_d('132', 'จ', 'Metformin เป็นยาลดระดับน้ำตาลที่มีผลเป็น Weight neutral หรืออาจทำให้น้ำหนักลดลงเล็กน้อย ไม่ทำให้น้ำหนักตัวเพิ่มขึ้น')

set_d('147', 'ข', 'Pilocarpine เป็นยากลุ่ม Cholinergic agonist ออกฤทธิ์หดตัว Ciliary muscle ทำให้เปิด Trabecular meshwork เพิ่มการไหลเวียน Aqueous humor')
set_d('147', 'ค', 'Acetazolamide เป็นยาลดการสร้าง Aqueous humor ผ่านการยับยั้งเอนไซม์ Carbonic anhydrase ที่ Ciliary epithelium')
set_d('147', 'ง', 'Betaxolol เป็น Beta-1 selective blocker ซึ่งออกฤทธิ์ลดการสร้าง Aqueous humor ผ่านการยับยั้ง Beta receptor ที่ Ciliary body')
set_d('147', 'จ', 'Brimonidine เป็น Alpha-2 agonist ที่ออกฤทธิ์ทั้งลดการสร้าง Aqueous humor และเพิ่ม Uveoscleral outflow')

for i in out:
    ans_key = options_map.get(str(data[[item['endo_idx'] for item in data].index(int(i))]['ans']), '')
    if ans_key in out[i]['distractors']:
        del out[i]['distractors'][ans_key]

with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\distractors_endo_part4.json', 'w', encoding='utf-8') as f:
    json.dump(out, f, ensure_ascii=False, indent=2)

print("Done generating distractors.")
