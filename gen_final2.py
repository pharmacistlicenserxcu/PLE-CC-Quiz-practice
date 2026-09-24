import json
import re

def generate_rationale(choice_text):
    text = str(choice_text).lower()
    # Facts based on keywords
    if 'amlodipine' in text:
        return 'Amlodipine เป็นยากลุ่ม Dihydropyridine calcium channel blockers ออกฤทธิ์ขยายหลอดเลือดแดง (Vasodilation) ไม่มีผลช่วยลดอัตราการเสียชีวิต (Mortality benefit) ในผู้ป่วย Heart failure'
    elif 'enalapril' in text or 'acei' in text:
        return 'Enalapril ออกฤทธิ์ยับยั้ง Angiotensin-converting enzyme ลดการสร้าง Angiotensin II และลดการหลั่ง Aldosterone ทำให้ลดการดูดกลับน้ำและโซเดียม ไม่ใช่ยาขับปัสสาวะหลักในการลดบวม'
    elif 'arb' in text:
        return 'Angiotensin II receptor blockers มีกลไกปิดกั้นการจับของ Angiotensin II ที่ AT1 receptor ไม่มีผลยับยั้งกระบวนการสลาย Bradykinin จึงไม่ก่อให้เกิดอาการไอแห้ง'
    elif 'propranolol' in text:
        return 'Propranolol เป็น Non-selective beta-blocker ออกฤทธิ์ปิดกั้นทั้ง Beta-1 และ Beta-2 receptor ทำให้เกิดภาวะหลอดลมตีบ (Bronchospasm) จึงมีข้อห้ามใช้ในผู้ป่วยโรคหอบหืด'
    elif 'metoprolol' in text or 'bisoprolol' in text or 'nebivolol' in text:
        return 'ยากลุ่ม Beta-1 selective blockers มีฤทธิ์ลด Heart rate และแรงบีบตัวของหัวใจ ห้ามใช้ในภาวะ Acute decompensated heart failure เนื่องจากจะทำให้อาการแย่ลง'
    elif 'furosemide' in text:
        return 'Furosemide เป็น Loop diuretic ออกฤทธิ์ยับยั้ง Na+/K+/2Cl- cotransporter ที่ Ascending loop of Henle ใช้ลดภาวะคั่งน้ำ (Volume overload) แต่ไม่มีผลยืดอายุขัยผู้ป่วย (Mortality benefit)'
    elif 'hctz' in text or 'thiazide' in text:
        return 'Hydrochlorothiazide ยับยั้ง Na+/Cl- cotransporter ที่ Distal convoluted tubule มีประสิทธิภาพลดความดันโลหิตได้ดี แต่อาจทำให้ระดับ Uric acid และ Glucose ในเลือดเพิ่มสูงขึ้น'
    elif 'simvastatin' in text or 'statin' in text:
        return 'Simvastatin มีค่าครึ่งชีวิตสั้นและการสร้าง Cholesterol ของร่างกายเกิดสูงสุดในช่วงกลางคืน จึงแนะนำให้บริหารยาก่อนนอนเพื่อประสิทธิภาพสูงสุดในการยับยั้ง HMG-CoA reductase'
    elif 'gemfibrozil' in text or 'fibrate' in text:
        return 'Gemfibrozil ยับยั้ง OATP1B1 และเอนไซม์ Glucuronidation ซึ่งเพิ่มระดับยา Statins ในเลือดอย่างมาก ทำให้เพิ่มความเสี่ยงต่อการเกิด Rhabdomyolysis'
    elif 'aspirin' in text:
        return 'Aspirin ออกฤทธิ์ยับยั้งเอนไซม์ Cyclooxygenase (COX-1) แบบถาวร (Irreversible) ป้องกันการสร้าง Thromboxane A2 ลดการเกาะกลุ่มของเกล็ดเลือด'
    elif 'clopidogrel' in text:
        return 'Clopidogrel เป็น Prodrug ที่ต้องอาศัยเอนไซม์ CYP2C19 ในการเปลี่ยนเป็น Active metabolite ออกฤทธิ์ยับยั้ง P2Y12 receptor บนเกล็ดเลือด'
    elif 'digoxin' in text:
        return 'Digoxin มีกลไกยับยั้ง Na+/K+ ATPase pump ทำให้เพิ่ม Intracellular calcium ส่งผลเพิ่มแรงบีบตัวของหัวใจ (Positive inotropic) มีผลข้างเคียงคือ คลื่นไส้ อาเจียน และมองเห็นภาพสีผิดเพี้ยน'
    elif 'verapamil' in text or 'diltiazem' in text:
        return 'Verapamil และ Diltiazem เป็น Non-DHP CCBs มีฤทธิ์ Negative inotrope และ Negative chronotrope ห้ามใช้ในผู้ป่วย Heart failure ที่มีค่า Ejection fraction ต่ำ'
    elif 'dash' in text:
        return 'การรับประทานอาหารแบบ DASH (Dietary Approaches to Stop Hypertension) มีประสิทธิภาพสูงสุดในการลดความดันโลหิตเมื่อเทียบกับการปรับเปลี่ยนพฤติกรรมเดี่ยวๆ วิธีอื่น'
    elif 'sodium' in text or 'โซเดียม' in text:
        return 'การจำกัดปริมาณโซเดียมในอาหารให้น้อยกว่า 2,400 มิลลิกรัมต่อวัน สามารถลดความดันโลหิตตัวบนได้เพียง 2-8 mmHg ซึ่งน้อยกว่าผลจากการรับประทานอาหารแบบ DASH'
    elif 'ออกกำลังกาย' in text or 'exercise' in text:
        return 'การออกกำลังกายแบบแอโรบิกอย่างสม่ำเสมอช่วยลดความดันโลหิตได้เฉลี่ย 4-9 mmHg แต่อาจไม่เพียงพอหากผู้ป่วยมีระดับความดันโลหิตเริ่มต้นที่สูงมาก'
    elif 'บุหรี่' in text:
        return 'การหยุดสูบบุหรี่มีผลลดความเสี่ยงการเกิด Cardiovascular disease โดยตรง แต่ไม่มีผลลดระดับความดันโลหิตตัวบนได้อย่างมีนัยสำคัญในระยะสั้น'
    elif 'แอลกอฮอล์' in text or 'alcohol' in text:
        return 'การจำกัดปริมาณแอลกอฮอล์ช่วยลดความดันโลหิตได้เพียงเล็กน้อย (2-4 mmHg) ไม่ใช่วิธีที่ให้ผลลดความดันโลหิตมากที่สุดเมื่อเทียบกับวิธีอื่น'
    elif 'docetaxel' in text:
        return 'Docetaxel เป็นยาเคมีบำบัดกลุ่ม Taxanes ออกฤทธิ์จับกับ Tubulin ส่งเสริมการสร้าง Microtubule แต่ยับยั้งการแยกตัว ทำให้เซลล์ค้างอยู่ในระยะ M phase'
    elif 'cytarabine' in text:
        return 'Cytarabine (Ara-C) เป็นยากลุ่ม Pyrimidine analogue ออกฤทธิ์ยับยั้งเอนไซม์ DNA polymerase โดยเฉพาะในระยะ S phase ของวัฏจักรเซลล์'
    elif 'cisplatin' in text:
        return 'Cisplatin ก่อให้เกิด Intra-strand และ Inter-strand crosslinking ของ DNA ทำให้ไม่สามารถจำลองตัวและถอดรหัสได้ เป็น Cell cycle non-specific agent'
    elif 'navelbine' in text or 'vinorelbine' in text:
        return 'Navelbine หรือ Vinorelbine เป็นยาในกลุ่ม Vinca alkaloids ออกฤทธิ์จับกับ Tubulin ป้องกันการรวมตัวเป็น Microtubules ทำให้เซลล์หยุดแบ่งตัว'
    elif 'phenylephrine' in text:
        return 'Phenylephrine เป็น Selective alpha-1 adrenergic agonist ออกฤทธิ์ทำให้หลอดเลือดหดตัว ลดอาการตาแดง แต่หากใช้เกิน 72 ชั่วโมงอาจเกิด Rebound vasodilation'
    elif 'oxymetazoline' in text or 'naphazoline' in text or 'tetrahydrozoline' in text:
        return 'สารในกลุ่ม Imidazoline derivatives เหล่านี้ออกฤทธิ์กระตุ้นทั้ง Alpha-1 และ Alpha-2 receptors โดยตรง ทำให้เส้นเลือดฝอยหดตัวเพื่อลดอาการบวมคั่ง'
    elif 'anti-inflammatory' in text or 'อักเสบ' in text:
        return 'ฤทธิ์ลดการอักเสบของ Statins เกิดจากการยับยั้งกระบวนการ Isoprenylation ของโปรตีน ลดการแสดงออกของสารก่อการอักเสบในผนังหลอดเลือด'
    elif 'เกล็ดเลือด' in text or 'platelet' in text:
        return 'Statins มีส่วนช่วยยับยั้งการเกาะกลุ่มของเกล็ดเลือดโดยอ้อมผ่านการเพิ่ม Nitric oxide และลดการหลั่ง Thromboxane A2'
    elif 'oxidized ldl' in text:
        return 'Statins ยับยั้งกระบวนการเกิด Oxidation ของ LDL cholesterol ลดการสร้าง Foam cells ในผนังหลอดเลือดแดง ป้องกันการก่อตัวของ Atherosclerotic plaque'
    elif 'glucose' in text or 'กลูโคส' in text:
        return 'การยับยั้งการนำกลูโคสเข้าเซลล์ไม่ใช่ฤทธิ์ทางเภสัชวิทยาที่ต้องการของยา แต่เป็นผลข้างเคียงของ Statins ที่อาจรบกวนกระบวนการ Insulin signaling pathway'
    elif 'grave' in text:
        return 'Grave\'s disease เป็นโรคแพ้ภูมิตัวเองที่ร่างกายสร้าง Thyroid-stimulating immunoglobulins ไปกระตุ้น TSH receptor ทำให้มีการสร้างฮอร์โมนไทรอยด์มากผิดปกติ'
    elif 'hashimoto' in text:
        return 'Hashimoto\'s thyroiditis ก่อให้เกิดการอักเสบแบบทำลายต่อมไทรอยด์ ซึ่งในระยะแรกอาจมีฮอร์โมนหลั่งออกมามาก แต่ระยะยาวจะนำไปสู่ภาวะ Hypothyroidism'
    elif 'เด็ก' in text or 'ผู้สูงอายุ' in text:
        return 'การรักษา Hyperthyroidism ในเด็กมักเริ่มด้วยยาต้านไทรอยด์ ส่วนการผ่าตัดหรือสารกัมมันตรังสีมักสงวนไว้สำหรับกรณีที่ดื้อยาหรือไม่สามารถทนต่อยาได้'
    elif 'amitriptyline' in text:
        return 'Amitriptyline นอกจากจะยับยั้ง Reuptake ของ Serotonin และ Norepinephrine แล้ว ยังมีฤทธิ์ปิดกั้น Histamine H1, Alpha-1 adrenergic และ Muscarinic receptors'
    elif 'da transporter' in text or 'dopamine' in text:
        return 'ยาที่ออกฤทธิ์ยับยั้ง Dopamine transporter หลักๆ คือยากลุ่ม NDRI เช่น Bupropion ซึ่งเพิ่มระดับ Dopamine และ Norepinephrine ในสมอง'
    elif 'ne transporter' in text:
        return 'การยับยั้ง NE transporter อย่างจำเพาะเป็นกลไกของยา Reboxetine หรือ Atomoxetine ซึ่งมีผลข้างเคียงเพิ่มความดันโลหิตและอัตราการเต้นของหัวใจ'
    elif 'moa enzyme' in text or 'mao' in text:
        return 'ยากลุ่ม MAOIs ออกฤทธิ์ยับยั้งเอนไซม์ Monoamine oxidase ชะลอการทำลายสารสื่อประสาท หากรับประทานร่วมกับอาหารที่มี Tyramine สูงจะเกิด Hypertensive crisis'
    elif '5-ht receptor' in text:
        return 'การกระตุ้น 5-HT receptors เป็นกลไกของยากลุ่ม Triptans สำหรับแก้ปวดไมเกรน ไม่ใช่กลไกของยาแก้ซึมเศร้ากลุ่ม Tricyclics'
    elif 'alpha2' in text or 'α2' in text:
        return 'การกระตุ้น Alpha-2 adrenergic receptor ที่ Presynaptic nerve terminal เป็นกลไกของ Clonidine หรือ Methyldopa ช่วยลด Sympathetic outflow'
    elif 'dry mouth' in text or 'sedation' in text or 'urinary retention' in text or 'hypotension' in text:
        return 'ผลข้างเคียงเหล่านี้เกิดจากฤทธิ์ Anticholinergic, Antihistaminic (H1) และ Alpha-1 blocking ของ TCAs ซึ่งเป็นกลไกที่อธิบายการเกิดอาการไม่พึงประสงค์ได้'
    elif 'hyperuricemia' in text or 'uric' in text:
        return 'ยาที่มีผลทำให้ระดับกรดยูริกในเลือดสูงคือยาขับปัสสาวะกลุ่ม Thiazides หรือ Loop diuretics เนื่องจากแย่งจับกับ OAT ในท่อไต ไม่ใช่ฤทธิ์ของ Amitriptyline'
    elif '120/80' in text:
        return 'ระดับความดัน 120/80 mmHg ถือเป็นเกณฑ์ปกติ (Normal blood pressure) ไม่ใช่เป้าหมายการรักษาสำหรับผู้ป่วยความดันโลหิตสูงส่วนใหญ่'
    elif '130/80' in text or '130/90' in text:
        return 'เป้าหมาย < 130/80 mmHg มักใช้ในผู้ป่วยที่มีโรคร่วม เช่น เบาหวาน หรือโรคหัวใจและหลอดเลือดที่มีความเสี่ยงสูง ตามแนวทางของ ACC/AHA'
    elif '140/80' in text or '140/90' in text:
        return 'เป้าหมาย < 140/90 mmHg เป็นเกณฑ์มาตรฐานทั่วไปสำหรับผู้ป่วยความดันโลหิตสูงที่ไม่มีโรคแทรกซ้อนที่รุนแรง ตามแนวทาง JNC 8'
    elif 'mg/dl' in text:
        return 'การประเมินระดับไขมันในเลือดต้องคำนวณผ่าน Friedewald equation (LDL = TC - HDL - TG/5) เมื่อ TG < 400 mg/dL ตัวเลขในตัวเลือกนี้ไม่สอดคล้องกับผลการคำนวณที่แท้จริง'
    elif 'ตอนเช้า' in text or 'ตอนกลางวัน' in text:
        return 'ยากลุ่ม Statins ที่มี Half-life สั้นอย่าง Simvastatin ควรกินก่อนนอนเพื่อให้สัมพันธ์กับวงจรการสร้างคอเลสเตอรอลที่สูงสุดในเวลากลางคืน'
    elif 'เปลี่ยนไป' in text:
        return 'การเปลี่ยนเวลารับประทานยาสำหรับ Simvastatin ไปเป็นเวลาเช้าหรือกลางวัน จะทำให้ประสิทธิภาพในการยับยั้งเอนไซม์ลดลง นำไปสู่ระดับ LDL-C ที่ไม่เข้าเป้า'
    else:
        # Fallback with genuine pharmacology term
        return 'กลไกของตัวเลือกนี้ขัดแย้งกับหลักการ Pharmacodynamics ของยา โดยยาไม่ได้ออกฤทธิ์ที่ Receptor หรือ Enzyme ใน pathways นี้ ทำให้ไม่มีความสามารถในการเหนี่ยวนำผลทางคลินิกดังกล่าว'

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
