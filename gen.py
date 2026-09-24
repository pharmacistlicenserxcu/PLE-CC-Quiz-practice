import json
import re

data = json.load(open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\cardio_part2.json', encoding='utf-8'))

def generate_rationale(text):
    text_lower = str(text).lower()
    
    if "nph 30" in text_lower:
        return "ส่วนประกอบของ Mixtard คือ NPH 70% และ Regular insulin 30% ทำให้มีการออกฤทธิ์แบบ biphasic ซึ่งไม่ตรงกับสัดส่วนในข้อนี้"
    if "diabetic ketoacidosis" in text_lower:
        return "Insulin Mixtard ไม่เหมาะสมในการรักษา DKA เนื่องจากมี NPH ซึ่งดูดซึมช้า การรักษาหลักคือ Regular insulin ทางหลอดเลือดดำ"
    if "lispro" in text_lower:
        return "Lispro เป็น rapid-acting insulin ที่มีความเสี่ยงในการเกิด late postprandial hypoglycemia ต่ำกว่า Mixtard"
    if "iv" in text_lower or "หลอดเลือดดำ" in text_lower:
        return "Mixtard มีส่วนผสมของ NPH ซึ่งเป็น suspension จึงห้ามบริหารยาทางหลอดเลือดดำ (IV) โดยเด็ดขาด"
    
    if "moduretic" in text_lower:
        return "Moduretic (Amiloride/HCTZ) มี Amiloride ซึ่งเป็น potassium-sparing diuretic ทำให้เพิ่มความเสี่ยงในการเกิด hyperkalemia"
    if "glipizide" in text_lower:
        return "Glipizide เป็นยาในกลุ่ม Sulfonylurea ออกฤทธิ์กระตุ้นการหลั่งอินซูลิน ไม่มีผลโดยตรงต่อการเพิ่มระดับโพแทสเซียมในเลือด"
    if "amlodipine" in text_lower:
        return "Amlodipine เป็น DHP-CCB มีผลขยายหลอดเลือดแดงส่วนปลาย อาการข้างเคียงหลักคือ peripheral edema แต่ไม่ทำให้เกิด hyperkalemia"
    if "omeprazole" in text_lower:
        return "Omeprazole เป็น PPI มีผลข้างเคียงที่อาจทำให้เกิด hypomagnesemia หากใช้ระยะยาว แต่ไม่เกี่ยวข้องกับ hyperkalemia"
        
    if "salbutamol" in text_lower:
        return "Salbutamol (beta-2 agonist) ออกฤทธิ์กระตุ้น Na-K ATPase ทำให้โพแทสเซียมเคลื่อนเข้าสู่เซลล์ ใช้ลดระดับ K ในเลือดได้"
    if "calcium gluconate" in text_lower:
        return "Calcium gluconate มีฤทธิ์เพียงแค่ stabilize myocardium membrane ป้องกัน arrhythmia แต่ไม่ช่วยลดระดับโพแทสเซียมในเลือด"
    if "furosemide" in text_lower or "lasix" in text_lower or "仿͡" in text_lower:
        return "Furosemide เป็น loop diuretic เพิ่มการขับโพแทสเซียมออกทางปัสสาวะ ใช้รักษา hyperkalemia ได้หากไตยังทำงาน"
    if "dialysis" in text_lower or "ฟอกเลือด" in text_lower or "ͧѡ" in text_lower:
        return "Hemodialysis เป็นวิธีที่มีประสิทธิภาพสูงสุดในการกำจัดโพแทสเซียมออกจากร่างกาย ใช้ในกรณี hyperkalemia รุนแรงหรือดื้อต่อยา"
        
    if "stage b" in text_lower:
        return "Stage B หมายถึงผู้ป่วยที่มีความผิดปกติของโครงสร้างหัวใจแล้ว แต่ยังไม่เคยมีอาการของภาวะหัวใจล้มเหลว"
    if "stage c" in text_lower:
        return "Stage C คือผู้ป่วยที่มีความผิดปกติของโครงสร้างหัวใจและเคยหรือกำลังมีอาการของภาวะหัวใจล้มเหลว (Heart Failure symptoms)"
    if "stage d" in text_lower:
        return "Stage D คือผู้ป่วยภาวะหัวใจล้มเหลวระยะสุดท้ายที่ดื้อต่อการรักษา (Refractory) และต้องการการรักษาขั้นสูง (เช่น Heart transplant)"
    if "stage e" in text_lower:
        return "ACC/AHA Guideline แบ่งระยะของ Heart Failure เพียง 4 ระยะ (Stage A ถึง D) ไม่มี Stage E ในระบบการประเมินนี้"
        
    if "activated thromboplastin time" in text_lower or "aptt" in text_lower:
        return "aPTT ใช้สำหรับการติดตามประสิทธิภาพของ Unfractionated Heparin (UFH) ไม่ใช่สำหรับการติดตามระดับยา Warfarin"
    if "international normalized ratio" in text_lower or "inr" in text_lower:
        return "INR เป็นค่าที่ได้จากการปรับมาตรฐานของ PT ใช้เพื่อติดตามประสิทธิภาพของ Warfarin โดยตรง"
    if "anti-factor xa" in text_lower:
        return "Anti-factor Xa level ใช้สำหรับการติดตามประสิทธิภาพของยา Low Molecular Weight Heparin (LMWH) เช่น Enoxaparin"
    if "international sensitivity index" in text_lower or "isi" in text_lower:
        return "ISI เป็นค่าความไวของน้ำยา thromboplastin ที่ใช้ในห้องปฏิบัติการเพื่อคำนวณค่า INR ไม่ใช่ตัวแปรที่เจาะวัดในเลือดผู้ป่วย"
        
    if "chiral carbon 2 atom" in text_lower:
        return "Warfarin มี chiral center เพียง 1 ตำแหน่งที่คาร์บอนตำแหน่งที่ 4 ทำให้มีเพียง 2 enantiomers คือ R- และ S-warfarin"
    if "s-form" in text_lower:
        return "S-warfarin มีความแรง (potency) มากกว่า R-warfarin ประมาณ 2.7 ถึง 3.8 เท่า และถูกทำลายหลักผ่าน CYP2C9"
    if "polarimeter" in text_lower:
        return "Polarimeter เป็นเครื่องมือสำหรับวัด optical rotation แต่ในทางคลินิกไม่มีความจำเป็นต้องแยกวัด S หรือ R-form"
    if "optical isomer" in text_lower:
        return "Warfarin ในรูปแบบยารับประทานที่จำหน่ายเป็น racemic mixture ซึ่งประกอบด้วย R- และ S-enantiomers ในสัดส่วนเท่ากัน"
        
    if "category b" in text_lower:
        return "Pregnancy Category B หมายถึงยาที่ศึกษาในสัตว์แล้วไม่พบความเสี่ยง แต่ไม่มีการศึกษาที่เพียงพอในมนุษย์ ซึ่งไม่ตรงกับ Warfarin"
    if "category e" in text_lower:
        return "FDA Pregnancy Categories มีเพียง A, B, C, D และ X ไม่มี Category E ในระบบการจำแนกความปลอดภัยในสตรีมีครรภ์"
    if "category f" in text_lower:
        return "FDA Pregnancy Categories มีเพียง A, B, C, D และ X ไม่มี Category F ระบบนี้ถูกยกเลิกและเปลี่ยนเป็น PLLR แล้ว"
    if "category i" in text_lower:
        return "ไม่มี Pregnancy Category I ในระบบของ US FDA ยา Warfarin จัดอยู่ใน Category X สำหรับหญิงตั้งครรภ์"
        
    if "metformin" in text_lower:
        return "Metformin เป็น insulin sensitizer ยับยั้ง gluconeogenesis ที่ตับ ไม่กระตุ้นการหลั่งอินซูลิน ความเสี่ยง hypoglycemia จึงต่ำมาก"
    if "insulin glargine" in text_lower:
        return "Insulin glargine เป็น basal insulin ออกฤทธิ์ยาว (peakless) มีความเสี่ยงการเกิด hypoglycemia ต่ำกว่า NPH หรือ regular insulin"
    if "acarbose" in text_lower:
        return "Acarbose เป็น alpha-glucosidase inhibitor ยับยั้งการดูดซึมกลูโคสที่ลำไส้ หากใช้เดี่ยวๆ จะไม่ทำให้เกิด hypoglycemia"
    if "pioglitazone" in text_lower:
        return "Pioglitazone เป็น Thiazolidinedione (TZD) เพิ่ม insulin sensitivity ที่เนื้อเยื่อไขมันและกล้ามเนื้อ ไม่ทำให้เกิด hypoglycemia หากใช้เดี่ยว"
        
    if "riboflavin" in text_lower:
        return "Riboflavin (Vitamin B2) ไม่ใช่เกลือแร่หรือวิตามินที่ได้รับผลกระทบจากการใช้ยา Metformin ในระยะยาว"
    if "niacin" in text_lower:
        return "Niacin (Vitamin B3) ไม่ได้ถูกยับยั้งการดูดซึมโดยยา Metformin และไม่เกี่ยวข้องกับอาการชาปลายประสาทจากยา"
    if "pyridoxine" in text_lower:
        return "Pyridoxine (Vitamin B6) เป็นวิตามินที่มีผลต่อระบบประสาท แต่ไม่ใช่ตัวที่ Metformin รบกวนการดูดซึมโดยตรง"
    if "cobalamin" in text_lower:
        return "Cobalamin (Vitamin B12) อาจถูกรบกวนการดูดซึมในลำไส้จากการใช้ Metformin ระยะยาว ทำให้เกิดภาวะโลหิตจางหรือปลายประสาทอักเสบได้"
        
    if "doxorubicin" in text_lower:
        return "Doxorubicin เป็น anthracycline ออกฤทธิ์ยับยั้ง topoisomerase II และเกิด DNA intercalation ไม่ได้ออกฤทธิ์ต่อ microtubule"
    if "cisplatin" in text_lower:
        return "Cisplatin เป็น alkylating-like agent ออกฤทธิ์โดยการสร้าง cross-links กับ DNA strand ยับยั้งการสังเคราะห์ DNA"
    if "cyclophosphamide" in text_lower:
        return "Cyclophosphamide เป็น nitrogen mustard alkylating agent ที่ต้องถูกเปลี่ยนรูปที่ตับก่อนออกฤทธิ์จับกับ DNA"
    if "methotrexate" in text_lower:
        return "Methotrexate เป็น antimetabolite (folate antagonist) ออกฤทธิ์ยับยั้งเอนไซม์ dihydrofolate reductase (DHFR)"
        
    if "proteinurea" in text_lower or "proteinuria" in text_lower:
        return "Phentermine เป็นยาลดน้ำหนักกลุ่ม sympathomimetic amine ไม่มีกลไกทำให้เกิดโปรตีนรั่วในปัสสาวะ"
    if "hyperphosphatemia" in text_lower:
        return "Hyperphosphatemia มักเกิดจากภาวะไตวายเรื้อรัง ไม่ใช่อาการไม่พึงประสงค์ที่เกี่ยวข้องกับการใช้ยา Phentermine"
    if "hyperuricemia" in text_lower:
        return "Hyperuricemia มักเกิดจากยาขับปัสสาวะกลุ่ม Thiazide หรือยาต้านวัณโรคบางชนิด ไม่ใช่ผลข้างเคียงของ Phentermine"
        
    if "140/90" in text_lower:
        return "ตาม JNC8 เป้าหมาย 140/90 mmHg เป็นเป้าหมายสำหรับผู้ป่วยอายุน้อยกว่า 60 ปี หรือผู้ป่วยที่มีเบาหวานและโรคไตเรื้อรัง"
    if "120/80" in text_lower:
        return "เป้าหมาย 120/80 mmHg ไม่ใช่คำแนะนำตาม JNC8 ซึ่งมักพิจารณาตัวเลขนี้เป็นความดันปกติ ไม่ใช่เป้าหมายในการรักษาผู้ป่วยทั่วไป"
    if "130/90" in text_lower:
        return "เป้าหมาย 130/90 mmHg ไม่ใช่ตัวเลขที่ปรากฏใน guideline สำคัญใดๆ มักใช้ 130/80 หรือ 140/90 เป็นจุดตัดหลัก"
    if "130/85" in text_lower:
        return "ไม่มี guideline ใดที่แนะนำเป้าหมาย 130/85 mmHg อย่างชัดเจน เป้าหมายส่วนใหญ่อิงที่ systolic 130 หรือ 140 และ diastolic 80 หรือ 90"
    if "150/90" in text_lower:
        return "ตาม JNC8 เป้าหมาย 150/90 mmHg แนะนำเฉพาะในผู้ป่วยสูงอายุ (≥ 60 ปี) ที่ไม่มีโรคเบาหวานหรือโรคไตเรื้อรังร่วมด้วย"
        
    if "complete blood count" in text_lower or "cbc" in text_lower:
        return "Enalapril เป็นยาในกลุ่ม ACE inhibitor ไม่ได้มีผลข้างเคียงหลักในการกดไขกระดูก จึงไม่ต้องติดตาม CBC เป็นประจำ"
    if "liver function test" in text_lower or "lft" in text_lower:
        return "Enalapril ไม่ได้มีผลต่อการทำงานของตับอย่างมีนัยสำคัญ การติดตาม LFT จึงไม่ใช่ข้อบังคับตาม guideline"
    if "fasting blood glucose" in text_lower:
        return "Enalapril มีคุณสมบัติ metabolic neutral หรืออาจเพิ่ม insulin sensitivity เล็กน้อย ไม่ทำให้ระดับน้ำตาลผิดปกติ"
    if "electrocardiogram" in text_lower or "ecg" in text_lower:
        return "ECG ไม่ใช่พารามิเตอร์ที่ต้องติดตามเป็นกิจวัตรหลังการให้ Enalapril ยกเว้นผู้ป่วยมีภาวะ hyperkalemia รุนแรง"
        
    if "diclofenac" in text_lower:
        return "Diclofenac เป็น NSAID ที่มีฤทธิ์ยับยั้ง COX-2 สูงเมื่อเทียบกับ COX-1 จึงเพิ่มความเสี่ยงต่อเหตุการณ์ทางหัวใจและหลอดเลือด (CV risk) ค่อนข้างมาก"
    if "naproxen" in text_lower:
        return "Naproxen เป็น non-selective NSAID ที่มีข้อมูลชี้ว่ามีความปลอดภัยต่อระบบหัวใจและหลอดเลือดมากที่สุดในกลุ่ม แต่ยังมีผลต่อทางเดินอาหาร"
    if "celecoxib" in text_lower:
        return "Celecoxib เป็น selective COX-2 inhibitor ซึ่งเพิ่ม CV risk ได้มากกว่า non-selective NSAIDs บางชนิด หากใช้ในขนาดสูง"
    if "piroxicam" in text_lower:
        return "Piroxicam มีฤทธิ์รบกวนการสร้าง prostaglandin และมีค่าครึ่งชีวิตที่ยาวนาน ทำให้มีความเสี่ยงทั้งต่อ GI และ CV สูง"
    if "ibuprofen" in text_lower:
        return "Ibuprofen อาจไปรบกวนฤทธิ์ต้านเกล็ดเลือดของ Aspirin ได้ หากให้ยาในเวลาใกล้เคียงกัน จึงต้องระมัดระวังในผู้ป่วยที่กิน Aspirin"
        
    if "hyperuricemia" in text_lower:
        return "Enalapril เป็น ACEI ไม่มีผลลดการขับกรดยูริกเหมือนกลุ่ม Thiazide diuretic จึงไม่ทำให้เกิดภาวะ hyperuricemia"
    if "hypernatremia" in text_lower:
        return "กลไกของ Enalapril คือลดระดับ Aldosterone ซึ่งอาจทำให้เกิด hyponatremia เล็กน้อยจากการขับโซเดียม ไม่ใช่ hypernatremia"
    if "hyperphosphatemia" in text_lower:
        return "ACEI ไม่มีผลโดยตรงต่อการควบคุมระดับฟอสเฟต ภาวะ hyperphosphatemia มักเกิดจากโรคไตวายเรื้อรัง (CKD)"
    if "hypercalcemia" in text_lower:
        return "Thiazide diuretics เป็นยาที่เพิ่มการดูดกลับของแคลเซียมและทำให้เกิด hypercalcemia แต่ Enalapril ไม่มีผลต่อระดับแคลเซียม"
        
    if "amlodipine" in text_lower:
        return "Amlodipine เป็น CCB ที่สามารถใช้ร่วมกับ ACEI ได้ดี และมีแนวทางแนะนำให้ใช้เป็นยาทางเลือกในการควบคุมความดันโลหิตร่วม"
    if "enalapril" in text_lower and "เพิ่ม" in text_lower:
        return "การเพิ่มขนาดยา Enalapril อาจทำได้หากยังไม่ถึง maximum dose แต่ในบางกรณีการเพิ่มยาอีกกลไกหนึ่ง (add-on) อาจมีประสิทธิภาพเหนือกว่า"
    if "indapamide" in text_lower:
        return "Indapamide เป็น thiazide-like diuretic มีผลลด morbidity/mortality ทาง CV ได้ดี แต่ต้องระวังผลข้างเคียงเรื่องเกลือแร่ผิดปกติ"
    if "hctz" in text_lower:
        return "HCTZ สามารถใช้เพิ่มประสิทธิภาพในการลดความดันเมื่อใช้ร่วมกับ ACEI แต่ระวังภาวะแทรกซ้อนด้าน metabolic (น้ำตาล/ยูริก) หากขนาดยาสูง"
    if "atenolol" in text_lower:
        return "Atenolol เป็น Beta-blocker ซึ่งตาม guideline ปัจจุบันไม่แนะนำให้ใช้เป็นยาลดความดันทางเลือกแรก ยกเว้นผู้ป่วยมีข้อบ่งชี้ทางหัวใจขาดเลือดร่วมด้วย"
        
    if "cyp 1a2" in text_lower:
        return "CYP 1A2 ไม่ใช่เอนไซม์หลักที่ใช้ในการทำลาย Simvastatin ยาที่มีผลเช่น Tizanidine, Theophylline จะเกี่ยวข้องกับเอนไซม์นี้มากกว่า"
    if "cyp 2c9" in text_lower:
        return "CYP 2C9 เป็นเอนไซม์หลักในการทำลายยา Warfarin และ Phenytoin ไม่ใช่เส้นทางหลักของ Simvastatin"
    if "sulfation" in text_lower:
        return "Sulfation เป็นกระบวนการ Phase II metabolism ซึ่งไม่ได้เป็นกลไกหลักในการเกิดปฏิกิริยาระหว่าง Simvastatin และ Gemfibrozil"
    if "oatp 1b1" in text_lower:
        return "Gemfibrozil ยับยั้ง OATP1B1 transporter ทำให้ Simvastatin เข้าสู่ตับลดลงและเกิดการสะสมในเลือด เพิ่มความเสี่ยงเกิด myopathy"
    if "cyp 3a4" in text_lower:
        return "Simvastatin ถูกทำลายผ่านเอนไซม์ CYP3A4 เป็นหลัก การยับยั้งเอนไซม์นี้โดยยาอื่นจะทำให้ระดับ Simvastatin สูงขึ้น"
        
    if "epimerization" in text_lower:
        return "Epimerization เป็นการเปลี่ยนสเตอริโอเคมีของโมเลกุล (เช่น tetracycline) ซึ่งไม่ใช่กลไกหลักในการเสื่อมสภาพของ Enalapril"
    if "dimerization" in text_lower:
        return "Dimerization คือการรวมตัวของโมเลกุลสองโมเลกุล ไม่ใช่ลักษณะการเสื่อมสลายของยาในกลุ่ม ACE inhibitors"
    if "tautomerization" in text_lower:
        return "Tautomerization คือการย้ายตำแหน่งโปรตอนภายในโมเลกุล ซึ่งไม่ได้ทำให้ยา Enalapril สูญเสียประสิทธิภาพทางคลินิกอย่างมีนัยสำคัญ"
    if "intramolecular cyclication" in text_lower or "cyclization" in text_lower:
        return "Enalapril เสื่อมสภาพผ่านกระบวนการ Intramolecular cyclization กลายเป็น diketopiperazine derivative"
    if "hydrolysis" in text_lower:
        return "Hydrolysis เป็นกลไกการเปลี่ยน Enalapril เป็น Enalaprilat (active form) ในร่างกาย แต่เมื่ออยู่ในรูปแบบยาเม็ด ความชื้นสามารถทำให้เสื่อมสภาพได้ผ่าน hydrolysis เช่นกัน"
        
    if "losartan" in text_lower or "ramipril" in text_lower or "enalapril" in text_lower:
        return "ยาในกลุ่ม ARB และ ACEI ห้ามใช้ในภาวะหลอดเลือดแดงที่ไตตีบทั้งสองข้าง (bilateral renal artery stenosis) เนื่องจากทำให้เกิดไตวายเฉียบพลันได้"
    if "metoprolol" in text_lower or "carvedilol" in text_lower:
        return "Beta-blocker ไม่มีข้อห้ามสัมพัทธ์ใน bilateral renal artery stenosis แต่ไม่ใช่ยาลำดับแรกที่แนะนำในการลดความดันโลหิตแบบ uncomplicated"
        
    if "al(oh)3" in text_lower:
        return "Aluminum hydroxide ใช้เป็น phosphate binder ในผู้ป่วยไตวายเรื้อรัง ไม่มีผลในการจับหรือขับโพแทสเซียมในลำไส้"
    if "caco3" in text_lower:
        return "Calcium carbonate เป็น phosphate binder และเสริมแคลเซียม ไม่ใช่ยาสำหรับรักษาภาวะ hyperkalemia"
    if "sodium bicarbonate" in text_lower:
        return "Sodium bicarbonate ใช้รักษาภาวะเลือดเป็นกรด (Metabolic acidosis) และช่วยดึงโพแทสเซียมเข้าเซลล์ชั่วคราว แต่ไม่ใช่ยาหลักในการกำจัดโพแทสเซียม"
    if "sodium polystyrene sulfonate" in text_lower:
        return "Sodium polystyrene sulfonate (Kalimate) เป็น cation-exchange resin ที่ลำไส้ ใช้จับโพแทสเซียมเพื่อขับออกทางอุจจาระ"
    if "sevelamer" in text_lower:
        return "Sevelamer เป็น non-calcium phosphate binder ใช้ควบคุมระดับฟอสเฟตในเลือด ไม่ได้มีข้อบ่งชี้ในการลดระดับโพแทสเซียม"
        
    if "sulindac" in text_lower:
        return "Sulindac เป็น NSAID ที่มีผลต่อการทำงานของไตน้อย แต่ไม่มีข้อมูลชัดเจนว่าปลอดภัยต่อโรคหลอดเลือดหัวใจมากที่สุดเทียบกับ Naproxen"
    if "parecoxib" in text_lower:
        return "Parecoxib เป็นยาฉีดในกลุ่ม COX-2 inhibitor ซึ่งข้อห้ามใช้รวมถึงผู้ป่วยที่เพิ่งผ่าตัดทำ CABG หรือมี CV risk สูง"
        
    if "imipenem" in text_lower:
        return "Imipenem เป็นยา broad-spectrum carbapenem ที่เก็บไว้ใช้สำหรับการติดเชื้อแบคทีเรียดื้อยา หรือ ESBL-producing organisms ไม่ใช่ empirical therapy แรกของ SBP"
    if "ceftazidime" in text_lower:
        return "Ceftazidime ครอบคลุมเชื้อ Pseudomonas แต่มีประสิทธิภาพครอบคลุมแบคทีเรียแกรมบวก สู้ Cefotaxime ไม่ได้ จึงไม่เป็น First-line สำหรับ SBP"
    if "norfloxacin" in text_lower:
        return "Norfloxacin ชนิดรับประทานมักใช้เป็นยาป้องกัน (Prophylaxis) SBP ไม่ใช่ยาหลักที่ใช้รักษาในภาวะ acute infection ที่ต้องใช้ยาฉีดเข้าหลอดเลือดดำ"
    if "amoxicillin" in text_lower and "clavulanic" in text_lower:
        return "Amoxicillin/clavulanic acid มีประสิทธิภาพครอบคลุมเชื้อได้ แต่ Guideline แนะนำ 3rd generation cephalosporin เช่น Cefotaxime หรือ Ceftriaxone เป็น first-line"
    if "cefotaxime" in text_lower:
        return "Cefotaxime เป็น third-generation cephalosporin ที่ได้รับการแนะนำเป็น empirical therapy ลำดับแรกในการรักษา Spontaneous Bacterial Peritonitis (SBP)"
        
    if "s. pyogenes" in text_lower:
        return "Streptococcus pyogenes (Group A Strep) มักก่อโรคที่ผิวหนัง ทางเดินหายใจ ไม่ใช่เชื้อฉวยโอกาสที่เป็นสาเหตุหลักของ SBP ในผู้ป่วยตับแข็ง"
    if "p. aeroginosa" in text_lower or "p. aeruginosa" in text_lower:
        return "Pseudomonas aeruginosa เป็นเชื้อก่อโรคฉวยโอกาสในโรงพยาบาล พบได้น้อยมากในภาวะ SBP เว้นแต่ผู้ป่วยมีประวัตินอนโรงพยาบาลนาน"
    if "proteus mirabilis" in text_lower:
        return "Proteus mirabilis เป็นแบคทีเรียแกรมลบที่มักพบในการติดเชื้อทางเดินปัสสาวะ (UTI) ไม่ใช่เชื้อที่พบเป็นอันดับแรกใน SBP"
    if "s. aureus" in text_lower:
        return "Staphylococcus aureus เป็นแบคทีเรียแกรมบวกที่ก่อโรคผิวหนังหรือเยื่อบุหัวใจอักเสบ พบได้ประปรายใน SBP แต่ไม่ใช่สาเหตุหลัก"
    if "k. pneumoniea" in text_lower or "e. coli" in text_lower:
        return "แบคทีเรียแกรมลบในลำไส้ เช่น E. coli หรือ K. pneumoniae เป็นสาเหตุหลักของการเกิด Spontaneous Bacterial Peritonitis"
        
    if "mucositis" in text_lower:
        return "Mucositis เป็นอาการข้างเคียงหลักจากยากลุ่ม Antimetabolite เช่น Methotrexate หรือ 5-FU ไม่ใช่ลักษณะเฉพาะที่เด่นที่สุดของ Cyclophosphamide"
    if "neuropathy" in text_lower:
        return "Peripheral neuropathy มักสัมพันธ์กับยากลุ่ม Vinca alkaloids (เช่น Vincristine) หรือ Platinum-based (เช่น Oxaliplatin) ไม่ใช่ Cyclophosphamide"
    if "hand foot syndrome" in text_lower:
        return "Hand-foot syndrome เป็นอาการข้างเคียงที่เด่นชัดของยา Capecitabine และ 5-FU ไม่ใช่เกิดจาก Cyclophosphamide"
    if "anemia" in text_lower:
        return "แม้ Cyclophosphamide จะมีฤทธิ์กดไขกระดูก (Myelosuppression) ทำให้เกิด anemia ได้ แต่อาการแทรกซ้อนเฉพาะตัวที่ต้องระวังเป็นพิเศษคือ Hemorrhagic cystitis"
    if "hemorrhagic cystitis" in text_lower:
        return "Hemorrhagic cystitis เป็นอาการข้างเคียงเฉพาะของ Cyclophosphamide และ Ifosfamide เกิดจากสาร Acrolein ทำลายเยื่อบุท่อปัสสาวะ"
        
    if "depolymerization" in text_lower:
        return "ยาที่ Inhibit depolymerization of mitotic spindle คือกลุ่ม Taxanes (เช่น Paclitaxel) เพื่อหยุดวงจรเซลล์ในระยะ M phase"
    if "intercalation" in text_lower:
        return "กระบวนการ Intercalation คือการแทรกตัวเข้าไปใน DNA ซึ่งเป็นกลไกหลักของยากลุ่ม Anthracyclines (เช่น Doxorubicin)"
    if "polymerization" in text_lower:
        return "ยาที่ Inhibit polymerization of microtubule คือกลุ่ม Vinca alkaloids (เช่น Vincristine) ไม่ใช่กลไกของ Cyclophosphamide"
    if "topoisomerase" in text_lower:
        return "Topoisomerase inhibitors เช่น Etoposide หรือ Irinotecan ยับยั้งการคลายเกลียว DNA ไม่ใช่กลไกแบบ alkylation"
    if "alkylated dna" in text_lower:
        return "Cyclophosphamide ออกฤทธิ์เป็น Alkylating agent ทำให้เกิดการ cross-link บนสาย DNA ทำให้เซลล์แบ่งตัวไม่ได้"
        
    if "n/v" in text_lower or "headache" in text_lower:
        return "คลื่นไส้อาเจียนและปวดศีรษะ (Rebound headache) เป็นอาการข้างเคียงที่พบได้บ่อยจากการใช้ Ergotamine เกินขนาด"
    if "leg weakness" in text_lower or "neuropathy" in text_lower:
        return "อาการกล้ามเนื้อขาอ่อนแรง หรือชาปลายมือปลายเท้า (Ergotism) เกิดจากฤทธิ์ vasoconstriction ที่รุนแรงของยา Ergotamine"
    if "hypotension" in text_lower:
        return "Ergotamine มีฤทธิ์เป็น non-selective 5-HT receptor agonist และ alpha-agonist ทำให้หลอดเลือดหดตัว อาการข้างเคียงจึงเป็นความดันโลหิตสูง (Hypertension) ไม่ใช่ Hypotension"
        
    # Catch all based on drug names
    if "amlodipine" in text_lower: return "Amlodipine เป็นยากลุ่ม DHP-CCB มีกลไกขยายหลอดเลือดแดงส่วนปลาย อาการข้างเคียงที่สำคัญคือข้อเท้าบวม (peripheral edema)"
    if "omeprazole" in text_lower: return "Omeprazole เป็น PPI มีข้อบ่งใช้ยับยั้งการหลั่งกรดในกระเพาะอาหาร ไม่มีฤทธิ์ในทางระบบหลอดเลือดและหัวใจ"
    if "aspirin" in text_lower: return "Aspirin ยับยั้งเอนไซม์ COX-1 แบบ irreversible ทำให้ลดการสร้าง Thromboxane A2 ลดการเกาะกลุ่มของเกล็ดเลือด"
    
    return "ยาในข้อนี้ไม่มีข้อบ่งใช้ ประสิทธิภาพ หรือกลไกการออกฤทธิ์ที่สอดคล้องกับแนวทางการรักษามาตรฐานสำหรับผู้ป่วยในกรณีนี้"

# Process all items
result = {}
choices_keys = ['c2', 'c3', 'c4', 'c5']
thai_letters = ['ข', 'ค', 'ง', 'จ']

for item in data:
    idx = str(item['cardio_idx'])
    result[idx] = {"distractors": {}}
    
    # ans = "1", c1 is correct. c2-c5 are distractors.
    for c_key, t_letter in zip(choices_keys, thai_letters):
        choice_text = str(item.get(c_key, ''))
        if choice_text and choice_text != "None":
            rationale = generate_rationale(choice_text)
            result[idx]["distractors"][t_letter] = rationale

with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\distractors_cardio_part2.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=2)

print("SUCCESS")
