import json
import re

def generate_rationale(choice_text):
    text = str(choice_text).lower()
    if 'amlodipine' in text:
        return 'Amlodipine เป็น DHP-CCBs ที่ออกฤทธิ์ขยายหลอดเลือดแดงส่วนปลาย (Peripheral vasodilation) ไม่ได้มีผลลด Heart rate หรือยับยั้ง RAAS โดยตรง และอาจเกิดผลข้างเคียงคือ peripheral edema'
    elif 'enalapril' in text or 'acei' in text or 'arb' in text:
        return 'ยากลุ่ม ACEIs/ARBs มีกลไกยับยั้งระบบ RAAS ทำให้เกิด Vasodilation แต่มีข้อควรระวังในผู้ป่วยที่มีภาวะ Bilateral renal artery stenosis และอาจทำให้เกิด Hyperkalemia ได้'
    elif 'beta' in text or 'propranolol' in text or 'metoprolol' in text:
        return 'Beta-blockers มีฤทธิ์ Negative inotrope และ chronotrope ซึ่งอาจบดบังอาการ Hypoglycemia ในผู้ป่วยเบาหวาน และห้ามใช้ในผู้ป่วยที่มีภาวะ Heart block ระดับรุนแรง'
    elif 'furosemide' in text or 'diuretic' in text:
        return 'Furosemide ออกฤทธิ์ยับยั้ง Na-K-2Cl symporter ที่ Thick ascending limb of Henle\'s loop ใช้เพื่อลด Volume overload ใน Heart failure แต่ไม่มีผลลด Mortality rate'
    elif 'simvastatin' in text or 'statin' in text:
        return 'Statins ออกฤทธิ์ยับยั้งเอนไซม์ HMG-CoA reductase ทำให้ลดการสร้าง Cholesterol ภายในเซลล์ตับ แต่มีผลข้างเคียงที่สำคัญคือ Myopathy และ Rhabdomyolysis'
    elif 'gemfibrozil' in text or 'fibrate' in text:
        return 'Fibrates เป็น PPAR-alpha agonists ที่มีประสิทธิภาพสูงในการลด Triglyceride แต่เพิ่มความเสี่ยง Rhabdomyolysis อย่างมากหากใช้ร่วมกับยาในกลุ่ม Statins'
    elif 'aspirin' in text or 'clopidogrel' in text:
        return 'Aspirin ยับยั้งเอนไซม์ COX-1 แบบ Irreversible ขณะที่ Clopidogrel เป็น P2Y12 inhibitor ทั้งคู่เป็น Antiplatelets ที่มีข้อควรระวังเรื่องความเสี่ยงในการเกิดเลือดออกในทางเดินอาหาร'
    elif 'digoxin' in text:
        return 'Digoxin มีฤทธิ์ Positive inotrope โดยยับยั้ง Na+/K+ ATPase แต่มี Therapeutic window ที่แคบ และความเป็นพิษจะเพิ่มขึ้นหากผู้ป่วยมีภาวะ Hypokalemia'
    elif 'verapamil' in text or 'diltiazem' in text or 'non-dhp' in text:
        return 'Non-DHP CCBs ออกฤทธิ์ยับยั้ง L-type calcium channel ที่เซลล์กล้ามเนื้อหัวใจ มีฤทธิ์ลด Heart rate จึงมีข้อห้ามใช้ในผู้ป่วย Heart failure with reduced ejection fraction (HFrEF)'
    elif 'dash' in text or 'sodium' in text or 'exercise' in text:
        return 'การปรับเปลี่ยนพฤติกรรมเป็นพื้นฐานสำคัญของการรักษา แต่การจำกัดเกลือ (Sodium restriction) หรือการออกกำลังกายมีประสิทธิภาพในการลดความดันโลหิตน้อยกว่าการรับประทานอาหารแบบ DASH'
    elif '120/80' in text or '130/80' in text or '140/90' in text:
        return 'เป้าหมายความดันโลหิตตาม Guideline แตกต่างกันไปตามโรคร่วม โดยผู้ป่วยที่มีความเสี่ยงสูงหรือมีโรคไตเรื้อรัง มักตั้งเป้าหมายไว้เข้มงวดกว่าผู้ป่วยทั่วไป เพื่อป้องกัน Target organ damage'
    elif 'docetaxel' in text or 'cisplatin' in text or 'cytarabine' in text:
        return 'ยากลุ่มนี้เป็นยาเคมีบำบัดที่ออกฤทธิ์รบกวนกระบวนการแบ่งเซลล์ (Cell cycle specific/non-specific) ซึ่งมีความเป็นพิษต่อเซลล์ไขกระดูกและระบบประสาท'
    elif 'mg/day' in text or 'ml' in text or 'g' in text:
        return 'การคำนวณขนาดยาผิดพลาดจากสูตรมาตรฐาน อาจส่งผลให้ผู้ป่วยได้รับยาในขนาด Subtherapeutic dose หรือ Overdose ซึ่งเพิ่มความเสี่ยงต่อ Toxicity ของยา'
    elif 'vasoconstrictor' in text or 'phenylephrine' in text:
        return 'ยากลุ่ม Sympathomimetic amines ออกฤทธิ์กระตุ้น Alpha-adrenergic receptors ที่หลอดเลือด ทำให้เกิด Vasoconstriction แต่หากใช้ต่อเนื่องอาจเกิด Rebound congestion ได้'
    elif 'thyroid' in text or 'hyperthyroidism' in text:
        return 'การรักษาภาวะ Hyperthyroidism ขึ้นกับสาเหตุและอายุผู้ป่วย โดย Antithyroid drugs เป็นทางเลือกแรก ขณะที่ Radioactive iodine พิจารณาในผู้ป่วยสูงอายุหรือกลับเป็นซ้ำ'
    elif 'amitriptyline' in text or 'tca' in text:
        return 'Amitriptyline เป็น Tricyclic antidepressant ที่ยับยั้งการเก็บกลับทั้ง Serotonin และ Norepinephrine แต่มีผลข้างเคียงจากฤทธิ์ Anticholinergic เช่น ปากแห้ง ปัสสาวะคั่ง และ Orthostatic hypotension'
    else:
        return 'กลไกนี้ไม่สอดคล้องกับ Pharmacokinetics หรือ Pharmacodynamics ของยาตาม Guideline ปัจจุบัน หรืออาจเป็นข้อบ่งใช้ที่ทำให้เกิด Adverse drug reaction หากนำมาใช้ผิดบริบท'

def process():
    try:
        with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\cardio_part4.json', encoding='utf-8') as f:
            data = json.load(f)
        
        out_dict = {}
        for d in data:
            c_idx = str(d['cardio_idx'])
            ans = str(d.get('ans', '')).strip()
            # Convert ans to digit if possible
            correct_num = None
            if ans.isdigit():
                correct_num = int(ans)
            
            distractors = {}
            letters = {1: 'ก', 2: 'ข', 3: 'ค', 4: 'ง', 5: 'จ'}
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
