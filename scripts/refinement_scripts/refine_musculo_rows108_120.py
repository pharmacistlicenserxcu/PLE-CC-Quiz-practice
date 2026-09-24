# -*- coding: utf-8 -*-
"""
refine_musculo_rows108_120.py
Refines and repairs rows 108 to 120 in '1. Musculoskeleton' in PLE CC Quiz:
- Sets accurate Subtopic (Gout, Osteoarthritis, Rheumatoid Arthritis, Calculations)
- Writes tailored, case-specific clinical explanations (Clean plain text, zero asterisks)
- Generates specific, focused 'จุดจำก่อนสอบ' (High-yield pearls) tailored directly to each question
- References authentic official guidelines (ACR Gout 2020, ACR OA 2019, ACR RA 2021, สมาคมรูมาติสซั่มแห่งประเทศไทย)
"""
import sys
import gspread
from google.oauth2.service_account import Credentials

sys.stdout.reconfigure(encoding='utf-8')

CREDS_FILE = 'c:/Users/thana/Desktop/PLE-CC/gemini-sheets-editor-497118-060a7f15daf9.json'
SPREADSHEET_ID = '1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w'

gc = gspread.authorize(Credentials.from_service_account_file(CREDS_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets']))
sh = gc.open_by_key(SPREADSHEET_ID)
ws = sh.worksheet('1. Musculoskeleton')

current_rows = ws.get('A108:P120')
print(f"Loaded {len(current_rows)} rows (Rows 108 to 120).")

# Row 108: ID 36, ข้อใดกล่าวถึง colchicine ถูกต้อง -> Ans 4 (ข้อ ง. มีอันตรกิริยากับยากลุ่ม macrolide)
exp_108 = """✅ คำตอบที่ถูกต้อง: ข้อ ง. มีอันตรกิริยากับยากลุ่ม macrolide

💡 Background:
Colchicine ถูกเมแทบอไลต์ผ่านเอนไซม์ Cytochrome P450 3A4 (CYP3A4) และถูกขนส่งออกจากเซลล์ผ่านโปรตีน P-glycoprotein (P-gp) เป็นทางหลัก ยากลุ่ม Macrolide antibiotics เช่น Clarithromycin, Erythromycin (ยกเว้น Azithromycin ซึ่งยับยั้งน้อยมาก) เป็นตัวยับยั้งเอนไซม์ CYP3A4 และ P-gp ที่มีฤทธิ์แรง (Strong inhibitors) การให้ยา Macrolides ร่วมกับ Colchicine จะทำให้ระดับยา Colchicine ในกระแสเลือดเพิ่มสูงขึ้นอย่างรวดเร็วและรุนแรง นำไปสู่ความเป็นพิษขั้นวิกฤต เช่น ท้องเสียรุนแรง กดการทำงานของไขกระดูก (Agranulocytosis/Pancytopenia) กล้ามเนื้อสลาย (Rhabdomyolysis) และอาจถึงแก่ชีวิตได้ จึงต้องหลีกเลี่ยงการใช้ร่วมกันหรือปรับลดขนาดยา Colchicine ลงอย่างเข้มงวด

🎯 ทำไมข้อนี้ถึงถูก:
ตัวเลือก ง. กล่าวถูกต้อง Colchicine มี Major Drug Interaction ที่อันตรายมากกับยากลุ่ม Macrolides (โดยเฉพาะ Clarithromycin และ Erythromycin)

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (เป็นยาตัวเลือกรองที่ใช้ในการรักษาโรคเกาท์): ผิด Colchicine เป็นยาทางเลือกแรก (First-line agent) ในการรักษาข้ออักเสบเกาต์เฉียบพลันร่วมกับ NSAIDs และ Corticosteroids
• ข้อ ข. (ต้องมีการจำกัดการรับประทานน้ำ): ผิด ผู้ป่วยโรคเกาต์ที่ได้รับ Colchicine หรือมีระดับกรดยูริกสูงควรดื่มน้ำมากๆ (2-3 ลิตร/วัน) เพื่อช่วยขับกรดยูริกและลดโอกาสเกิดผลึกนิ่วในไต ไม่ใช่จำกัดน้ำ
• ข้อ ค. (ห้ามใช้ในสตรีมีครรภ์เด็ดขาด): ผิด Colchicine จัดอยู่ใน Pregnancy Category C (ไม่ใช่ Category X) แม้ควรหลีกเลี่ยงหากไม่จำเป็น แต่ไม่ได้เป็นข้อห้ามใช้อย่างเด็ดขาดเท่ากับยาในกลุ่ม Category X เช่น Methotrexate
• ข้อ จ. (ไม่ต้องปรับขนาดยาในผู้ป่วยโรคไต): ผิด Colchicine ขับออกทางไตประมาณร้อยละ 10-20 และสะสมในร่างกายได้ง่าย ผู้ป่วยที่มีการทำงานของไตบกพร่อง (eGFR < 30-50 mL/min) จำเป็นต้องปรับลดขนาดยาหรือลดความถี่ในการรับประทานเพื่อป้องกันพิษต่อกล้ามเนื้อและไขกระดูก

📖 Guideline อ้างอิง:
2020 American College of Rheumatology (ACR) Guideline for the Management of Gout & US FDA Drug Safety Communication on Colchicine-Macrolide Interactions

📌 จุดจำก่อนสอบ:
• Colchicine Dangerous Drug Interactions:
  - Strong CYP3A4 & P-gp Inhibitors: Clarithromycin, Erythromycin, Ketoconazole, Itraconazole, Ritonavir, Verapamil, Diltiazem
  - Consequence: เพิ่มระดับ Colchicine มหาศาล -> Rhabdomyolysis + Bone marrow suppression + Fatal toxicity
• Renal Adjustment: ในผู้ป่วย Moderate-Severe CKD ต้องลดขนาดยา Colchicine ลงเสมอ"""

# Row 109: ID 37, ข้อใดเป็นอาการไม่พึงประสงค์จากยา colchicine ที่พบบ่อยที่สุด -> Ans 2 (ข้อ ข. Diarrhea)
exp_109 = """✅ คำตอบที่ถูกต้อง: ข้อ ข. Diarrhea

💡 Background:
Colchicine ออกฤทธิ์จับกับโปรตีน Tubulin ทำให้ยับยั้งการแบ่งตัวของเซลล์ (Inhibits mitosis through microtubule assembly disruption) เซลล์เยื่อบุทางเดินอาหาร (Gastrointestinal epithelial cells) ซึ่งมีอัตราการแบ่งตัวและผลัดเซลล์สูงอย่างรวดเร็วจึงได้รับผลกระทบจากยานี้ได้ง่ายและเร็วที่สุด อาการไม่พึงประสงค์ที่พบบ่อยที่สุด (Most common ADR: เกิดขึ้นได้ถึงร้อยละ 20-50 ของผู้ใช้ยา) คือ อาการทางระบบทางเดินอาหาร โดยเฉพาะ "ท้องเสียถ่ายเหลว" (Diarrhea) คลื่นไส้ อาเจียน และปวดเกร็งท้อง โดยอาการท้องเสียมักเป็นสัญญาณเตือนแรกสุด (Early sign of toxicity) ที่บ่งชี้ว่าระดับยาในร่างกายเริ่มสูงเกินไป

🎯 ทำไมข้อนี้ถึงถูก:
"Diarrhea" (ท้องเสีย) เป็นอาการไม่พึงประสงค์ที่พบได้บ่อยที่สุดของยา Colchicine และเป็นข้อบ่งชี้ให้ผู้ป่วยหยุดใช้ยาทันทีหากมีอาการถ่ายเหลวรุนแรง

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (Ototoxicity): พิษต่อหู พบบ่อยในยากลุ่ม Aminoglycosides (Gentamicin) หรือ Loop diuretics (Furosemide) ไม่ใช่ Colchicine
• ข้อ ค. (Retinopathy): พิษต่อจอประสาทตา พบบ่อยในการใช้ยา Chloroquine หรือ Hydroxychloroquine ระยะยาว
• ข้อ ง. (Peripheral neuritis): ปลายประสาทอักเสบ อาจพบได้ในภาวะพิษเรื้อรังจาก Colchicine (Neuromyopathy) แต่พบได้น้อยมากเมื่อเทียบกับอาการท้องเสีย
• ข้อ จ. (Hepatic impairment): ตับอักเสบไม่ใช่ผลข้างเคียงเด่นของ Colchicine

📖 Guideline อ้างอิง:
2020 American College of Rheumatology (ACR) Guideline for the Management of Gout & Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th Edition)

📌 จุดจำก่อนสอบ:
• Most Common ADR of Colchicine: ท้องเสีย (Diarrhea) และปวดท้องคลื่นไส้
• Patient Counseling: หากเริ่มมีอาการถ่ายเหลว ถ่ายบ่อย หรือปวดบิดท้อง ให้หยุดรับประทานยา Colchicine ทันที
• Modern Regimen Benefit: การใช้ขนาดต่ำ (Low-dose: 1.2 mg stat ตามด้วย 0.6 mg ใน 1 ชั่วโมง) ให้ประสิทธิภาพเท่าขนาดเดิม แต่ลดการเกิด Diarrhea ลงได้มากกว่าครึ่ง"""

# Row 110: ID 38, กลไกทางเภสัชวิทยาของยา Allopurinol -> Ans 3 (ข้อ ค. ยับยั้ง xanthine oxidase)
exp_110 = """✅ คำตอบที่ถูกต้อง: ข้อ ค. ยับยั้ง xanthine oxidase

💡 Background:
ในกระบวนการสลายสารพิวรีนตามธรรมชาติในร่างกาย Hypoxanthine จะถูกเปลี่ยนเป็น Xanthine และ Xanthine จะถูกเปลี่ยนต่อไปเป็น Uric acid โดยอาศัยเอนไซม์ Xanthine Oxidase (XO) Allopurinol มีโครงสร้างเป็นสารคล้ายพิวรีน (Purine analog / Isomer of hypoxanthine) ทำหน้าที่เป็นสารยับยั้งเอนไซม์ Xanthine Oxidase โดยตรง นอกจากนี้ เมื่อ Allopurinol ถูกออกซิไดซ์ในร่างกายจะได้สารเมแทบอไลต์ออกฤทธิ์คือ Oxypurinol ซึ่งมีฤทธิ์ยับยั้งเอนไซม์ Xanthine Oxidase เช่นกันและมีค่าครึ่งชีวิตยาวนาน ส่งผลให้การสร้างกรดยูริกลดลงอย่างมีนัยสำคัญ

🎯 ทำไมข้อนี้ถึงถูก:
กลไกทางเภสัชวิทยาที่แท้จริงของ Allopurinol คือ "ยับยั้งเอนไซม์ Xanthine Oxidase" ซึ่งช่วยลดการผลิตกรดยูริกเข้าสู่กระแสเลือด

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (ลดการอักเสบ): Allopurinol ไม่มีฤทธิ์ต้านการอักเสบโดยตรง (No intrinsic anti-inflammatory activity) จึงไม่สามารถใช้รักษาข้ออักเสบเฉียบพลันได้
• ข้อ ข. (เพิ่มการหลั่ง uric acid): ไม่ใช่กลไกของยา
• ข้อ ง. (ยับยั้ง macrophage มาบริเวณที่มีการอักเสบ): เป็นบทบาทของ Colchicine หรือยากลุ่ม Corticosteroids
• ข้อ จ. (เพิ่มการขับ uric acid): เป็นกลไกของยากลุ่ม Uricosuric agents (เช่น Probenecid, Benzbromarone, Sulfinpyrazone) ไม่ใช่ Allopurinol

📖 Guideline อ้างอิง:
2020 American College of Rheumatology (ACR) Guideline for the Management of Gout & Goodman & Gilman's The Pharmacological Basis of Therapeutics (14th Edition)

📌 จุดจำก่อนสอบ:
• Allopurinol Pharmacodynamics:
  - Drug Class: Xanthine Oxidase Inhibitor (XOI)
  - Mechanism: ยับยั้ง Xanthine Oxidase ขัดขวางการเปลี่ยน Hypoxanthine -> Xanthine -> Uric acid
  - ผลลัพธ์: ระดับ Uric acid ในเลือดและปัสสาวะลดลง แต่ระดับสารตั้งต้น Hypoxanthine และ Xanthine ในปัสสาวะจะเพิ่มขึ้น (ซึ่งละลายน้ำได้ดีกว่ายูริก)"""

# Row 111: ID 39, ยาที่ไม่เหมาะสมในผู้ป่วย OA ที่แพ้ Sulfacetamide -> Ans 3 (ข้อ ค. Nimesulide)
exp_111 = """✅ คำตอบที่ถูกต้อง: ข้อ ค. Nimesulide

💡 Background:
อาการข้อฝืดตอนเช้าสั้นๆ (ประมาณ 5 นาที) และมีเสียงกรอบแกรบในข้อเวลาเคลื่อนไหว (Crepitus) เป็นลักษณะทางคลินิกดั้งเดิมของโรคข้อเสื่อม (Osteoarthritis: OA) ผู้ป่วยรายนี้มีประวัติการแพ้ยา Sulfacetamide ซึ่งเป็นยาในกลุ่มซัลโฟนาไมด์ (Sulfonamides) ยาต้านการอักเสบกลุ่ม NSAIDs บางตัวมีโครงสร้างทางเคมีที่มีหมู่อะโรมาติกซัลโฟนาไมด์ (Sulfonamide moiety: -SO2NH-) ที่อาจทำให้เกิดการแพ้ข้ามกลุ่ม (Cross-reactivity) ในกลุ่มผู้ป่วยที่ไวต่อสารซัลฟา ได้แก่ Celecoxib และ Nimesulide (โครงสร้าง 4-nitro-2-phenoxymethanesulfonanilide) จึงควรหลีกเลี่ยงการใช้ Nimesulide ในผู้ป่วยที่มีประวัติแพ้ยาในกลุ่มซัลฟาอย่างรุนแรง

🎯 ทำไมข้อนี้ถึงถูก:
Nimesulide มีโครงสร้างทางเคมีเป็นอนุพันธ์ของ Methanesulfonanilide (มีหมู่ Sulfonamide) จึงมีความเสี่ยงต่อการเกิดการแพ้ข้ามกลุ่มในผู้ป่วยที่มีประวัติแพ้ยา Sulfacetamide และนอกจากนี้ยังมีคำเตือนด้านพิษต่อตับรุนแรง (Hepatotoxicity) จึงไม่เหมาะสมที่สุดสำหรับผู้ป่วยรายนี้

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (Ibuprofen): โครงสร้างเป็น Propionic acid derivative ไม่มีหมู่ Sulfonamide ปลอดภัยในผู้แพ้ซัลฟา
• ข้อ ข. (Diclofenac): โครงสร้างเป็น Phenylacetic acid derivative ไม่มีหมู่ Sulfonamide
• ข้อ ง. (Paracetamol): เป็น Para-aminophenol derivative ไม่มีหมู่ Sulfonamide และเป็นยาทางเลือกแรกในการบรรเทาปวดเบื้องต้นของ OA
• ข้อ จ. (Aspirin): เป็น Salicylate ไม่มีหมู่ Sulfonamide

📖 Guideline อ้างอิง:
2019 American College of Rheumatology (ACR) Guideline for the Management of Osteoarthritis of the Hand, Hip, and Knee & Goodman & Gilman's Chemical Classifications of NSAIDs

📌 จุดจำก่อนสอบ:
• NSAIDs with Sulfonamide Moiety:
  - Celecoxib
  - Nimesulide
  - Valdecoxib / Parecoxib
  ระวังการใช้หรือหลีกเลี่ยงในผู้ป่วยที่มีประวัติแพ้ยากลุ่ม Sulfa (เช่น Co-trimoxazole, Sulfacetamide, Silver sulfadiazine) รุนแรง
• Non-sulfonamide NSAIDs: Ibuprofen, Naproxen, Diclofenac, Meloxicam, Ketoprofen ปลอดภัยในผู้แพ้ซัลฟา"""

# Row 112: ID 40, คำแนะนำการรับประทานยา OA -> Ans 3 (ข้อ ค. รับประทาน glucosamine ครั้งละ 2 เม็ด วันละ 3 ครั้ง)
exp_112 = """✅ คำตอบที่ถูกต้อง: ข้อ ค. รับประทาน glucosamine ครั้งละ 2 เม็ด วันละ 3 ครั้ง

💡 Background:
Glucosamine sulfate ในรูปแบบแคปซูลขนาดมาตรฐานเดิมที่มีจำหน่ายทั่วไปคือ 250 mg ต่อแคปซูล ขนาดยามาตรฐานในการศึกษาและตามฉลากยาเดิมสำหรับการรักษาโรคข้อเข่าเสื่อมคือ 1,500 mg ต่อวัน ซึ่งเมื่อคำนวณจากขนาด 250 mg จะต้องรับประทานครั้งละ 2 เม็ด (500 mg) วันละ 3 ครั้ง พร้อมอาหาร (รวม 1,500 mg/day) หรือรับประทานครั้งละ 1,500 mg วันละครั้ง (สำหรับชนิดผงชงดื่มหรือยาเม็ดขนาด 1,500 mg)

🎯 ทำไมข้อนี้ถึงถูก:
การรับประทาน Glucosamine (แคปซูล 250 mg) ครั้งละ 2 เม็ด วันละ 3 ครั้ง ให้ขนาดยารวมเท่ากับ 1,500 mg/day ซึ่งเป็นขนาดและวิธีรับประทานที่ถูกต้องตามตำรับยามาตรฐานเดิม

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (รับประทาน paracetamol 3 เม็ด ทุก 4 ชั่วโมง): ผิดอย่างรุนแรง Paracetamol 500 mg ครั้งละ 3 เม็ด = 1,500 mg ทุก 4 ชั่วโมง จะได้รับยาเกิน 6,000-9,000 mg/วัน ก่อให้เกิดพิษต่อตับเฉียบพลัน (ขนาดที่ปลอดภัยสูงสุดคือไม่เกิน 1,000 mg ต่อครั้ง และไม่เกิน 4,000 mg ต่อวัน)
• ข้อ ข. (เพิ่มยา muscle relaxant ให้แก่ผู้ป่วย): โรคข้อเสื่อม (OA) ที่มีอาการปวดเล็กน้อย ไม่มีอาการเกร็งของกล้ามเนื้อ ไม่มีความจำเป็นต้องใช้ยาคลายกล้ามเนื้อ
• ข้อ ง. (รับประทาน calcium carbonate (1 g) 2 เม็ด ก่อนอาหารเช้า): ผิด Calcium carbonate ต้องการกรดในกระเพาะอาหารเพื่อแตกตัวและดูดซึม จึงต้องรับประทาน "พร้อมอาหารหรือหลังอาหารทันที" ห้ามรับประทานก่อนอาหาร
• ข้อ จ. (ถูนวดเจลพริกบริเวณปวด เพื่อให้ยาดูดซึมได้เยอะ): ผิด Capsaicin gel มีสารเผ็ดร้อน การถูนวดรุนแรงจะทำให้ผิวหนังแสบร้อน ระคายเคือง และอักเสบมากขึ้น คำแนะนำที่ถูกต้องคือทาบางๆ ห้ามถูนวดรุนแรง และต้องล้างมือให้สะอาดหลังทา

📖 Guideline อ้างอิง:
แนวทางเวชปฏิบัติการวินิจฉัยและการดูแลรักษาโรคข้อเข่าเสื่อม (สมาคมรูมาติสซั่มแห่งประเทศไทย) & US FDA Drug Dosing Reference for Acetaminophen

📌 จุดจำก่อนสอบ:
• Glucosamine Dosing: ขนาดมาตรฐานคือ 1,500 mg/day (ถ้าแคปซูล 250 mg ทาน 2 เม็ด 3 เวลา pc)
• Paracetamol Max Dose: ผู้ใหญ่ทาน 500-1,000 mg ทุก 4-6 ชั่วโมง ขนาดยาสูงสุดไม่เกิน 4,000 mg/day (ในผู้สูงอายุหรือโรคตับแนะนำไม่เกิน 2,000-3,000 mg/day)
• Calcium Carbonate Administration: ต้องทาน "หลังอาหารทันที" เพราะอาศัยกรดในการดูดซึม"""

# Row 113: ID 41, ข้อใดที่เภสัชกรไม่ต้องให้คำแนะนำเรื่องการปฏิบัติตัวเกี่ยวกับโรค OA -> Ans 5 (ข้อ จ. หลีกเลี่ยงการรับประทานยอดผัก)
exp_113 = """✅ คำตอบที่ถูกต้อง: ข้อ จ. หลีกเลี่ยงการรับประทานยอดผัก

💡 Background:
โรคข้อเสื่อม (Osteoarthritis: OA) เป็นโรคที่เกิดจากความเสื่อมสภาพและการสึกหรอของกระดูกอ่อนผิวข้อ (Cartilage breakdown) ร่วมกับการเปลี่ยนแปลงของกระดูกใต้ผิวข้อ ไม่ได้เกิดจากการสะสมของผลึกกรดยูริกเหมือนโรคเกาต์ การปฏิบัติตัวที่ถูกต้องสำหรับผู้ป่วย OA เน้นที่การลดแรงกดทับข้อต่อ (Non-pharmacological measures) ได้แก่ การควบคุมและลดน้ำหนักตัว การหลีกเลี่ยงการงอเข่ามากๆ เช่น นั่งคุกเข่า นั่งพับเพียบ นั่งยองๆ การหลีกเลี่ยงการยกของหนัก และการออกกำลังกายที่ไม่มีแรงกระแทก เช่น การว่ายน้ำหรือออกกำลังกายในน้ำ สำหรับ "การหลีกเลี่ยงการรับประทานยอดผัก" (อาหารพิวรีนสูง) เป็นคำแนะนำเฉพาะสำหรับผู้ป่วย "โรคเกาต์" (Gout) ไม่มีความจำเป็นต้องแนะนำในผู้ป่วยโรคข้อเสื่อม

🎯 ทำไมข้อนี้ถึงถูก:
การหลีกเลี่ยงการรับประทานยอดผักเป็นข้อห้ามด้านอาหารของโรคเกาต์ เภสัชกรจึง "ไม่ต้องให้คำแนะนำ" เรื่องนี้แก่ผู้ป่วยโรคข้อเสื่อม

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (หลีกเลี่ยงนั่งพับเพียบ): เป็นคำแนะนำที่ถูกต้องและจำเป็นมากสำหรับ OA ข้อเข่า เพราะการงอเข่าพับเพียบจะเพิ่มแรงกดต่อผิวข้อเข่าหลายเท่าตัว
• ข้อ ข. (ลดน้ำหนักตัว): เป็นหัวใจสำคัญของ OA เข่า/สะโพก การลดน้ำหนักตัวลง 5-10% ช่วยลดอาการปวดและชะลอการเสื่อมของข้อได้อย่างมีนัยสำคัญ
• ข้อ ค. (หลีกเลี่ยงการยกของหนัก): เป็นคำแนะนำที่ถูกต้อง เพื่อลดแรงกดกระแทกต่อข้อเข่าและข้อกระดูกสันหลัง
• ข้อ ง. (ออกกำลังกายในน้ำ): เป็นคำแนะนำมาตรฐานที่ดีเยี่ยม แรงลอยตัวของน้ำจะช่วยพยุงน้ำหนักตัว ทำให้ขยับข้อและฝึกกล้ามเนื้อรอบข้อได้โดยไม่มีแรงกระแทก

📖 Guideline อ้างอิง:
2019 American College of Rheumatology (ACR) Guideline for the Management of Osteoarthritis of the Hand, Hip, and Knee & แนวทางเวชปฏิบัติการดูแลรักษาโรคข้อเข่าเสื่อม พ.ศ. 2553 (สมาคมรูมาติสซั่มแห่งประเทศไทย)

📌 จุดจำก่อนสอบ:
• Osteoarthritis Lifestyle Management:
  - ลดน้ำหนักตัว (Weight reduction)
  - หลีกเลี่ยงการงอข้อเข่าเกิน 90 องศา (นั่งยองๆ พับเพียบ ขัดสมาธิ นั่งคุกเข่า)
  - ออกกำลังกายแบบ Low-impact: เดินในสระน้ำ ว่ายน้ำ ปั่นจักรยานแบบปรับอานสูง
  - อาหาร: ไม่มีข้อห้ามเรื่องยอดผัก/สัตว์ปีกเหมือนโรคเกาต์"""

# Row 114: ID 42, คำนวณปริมาณ Ca2+ ที่ได้รับต่อวัน -> Ans 4 (ข้อ ง. 800 mg)
exp_114 = """✅ คำตอบที่ถูกต้อง: ข้อ ง. 800 mg

💡 Background:
เกลือแคลเซียมแต่ละชนิดมีสัดส่วนของแคลเซียมธาตุ (Elemental Calcium) แตกต่างกันอย่างมีนัยสำคัญ:
1. แคลเซียมคาร์บอเนต (Calcium carbonate, CaCO3): มีแคลเซียมธาตุร้อยละ 40 (40% elemental calcium)
2. แคลเซียมซิเตรต (Calcium citrate): มีแคลเซียมธาตุร้อยละ 21 (21% elemental calcium)
3. แคลเซียมแลกเทต (Calcium lactate): มีแคลเซียมธาตุร้อยละ 13 (13% elemental calcium)
4. แคลเซียมกลูโคเนต (Calcium gluconate): มีแคลเซียมธาตุร้อยละ 9 (9% elemental calcium)

🎯 ทำไมข้อนี้ถึงถูก:
การคำนวณตามกรณีศึกษา:
- ผู้ป่วยรับประทาน Calcium carbonate เม็ดละ 1,000 mg (1 g) จำนวนวันละ 2 เม็ด
- ปริมาณเกลือ Calcium carbonate รวมต่อวัน = 1,000 mg x 2 = 2,000 mg/day
- Calcium carbonate มี Elemental Calcium เท่ากับ 40%
- ปริมาณ Ca2+ (Elemental Calcium) ที่ผู้ป่วยได้รับต่อวัน = 2,000 mg x 40% = 800 mg

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (40 mg): เกิดจากการคิดเป็น 40 mg ต่อเม็ด ซึ่งเป็นตัวเลขที่คำนวณผิดหน่วย
• ข้อ ข. (80 mg): เป็นตัวเลขสับสนจากการเลื่อนจุดทศนิยม
• ข้อ ค. (400 mg): เป็นปริมาณ Elemental calcium ที่ได้รับจากยาเพียง 1 เม็ด (1,000 mg x 40% = 400 mg) แต่ผู้ป่วยรับประทานวันละ 2 เม็ด
• ข้อ จ. (2000 mg): เป็นน้ำหนักรวมของเกลือ Calcium carbonate ทั้ง 2 เม็ด ไม่ใช่ปริมาณแคลเซียมธาตุ (Elemental Ca2+)

📖 Guideline อ้างอิง:
Dietary Reference Intake (DRI) for Thais & US National Institutes of Health (NIH) Calcium Fact Sheet for Health Professionals

📌 จุดจำก่อนสอบ:
• Calcium Salts & Elemental Calcium %:
  - Calcium carbonate: 40% (จำสูตร: 1,000 mg เกลือ = 400 mg แคลเซียมธาตุ)
  - Calcium citrate: 21%
  - Calcium lactate: 13%
  - Calcium gluconate: 9%
• Recommended Daily Intake: ผู้ใหญ่วัยทองและผู้สูงอายุต้องการแคลเซียมธาตุประมาณ 1,000 - 1,200 mg/day"""

# Row 115: ID 43, อาการทางคลินิกที่บ่งบอกโรคเกาต์ -> Ans 2 (ข้อ ข. มี nodule ขึ้นบริเวณข้อที่อักเสบ)
exp_115 = """✅ คำตอบที่ถูกต้อง: ข้อ ข. มี nodule ขึ้นบริเวณข้อที่อักเสบ

💡 Background:
อาการทางคลินิกที่เป็นเอกลักษณ์จำเพาะของโรคเกาต์เรื้อรัง (Chronic Tophaceous Gout) คือ การตรวจพบปุ่มหรือตุ่มนูนแข็ง (Nodule หรือ Tophi) เกิดจากการสะสมและตกตะกอนของผลึกเกลือโมโนโซเดียมยูเรต (Monosodium urate crystals) ร่วมกับปฏิกิริยาการอักเสบแบบเนื้อเยื่อแปลกปลอม (Foreign body granuloma) มักพบบริเวณรอบๆ ข้อที่เคยอักเสบ ติ่งหู (Helix of ear) เอ็นร้อยหวาย หรือบริเวณข้อศอก (Olecranon bursa) ปุ่มโทฟัสเหล่านี้อาจแตกออกเป็นสารสีขาวคล้ายผงชอล์กหรือยาสีฟัน

🎯 ทำไมข้อนี้ถึงถูก:
การมีตุ่มนูนหรือปุ่มแข็ง (Nodule / Tophi) เกิดขึ้นบริเวณข้อที่อักเสบหรือเนื้อเยื่อรอบข้อ เป็นลักษณะทางกายภาพที่สำคัญและบ่งบอกถึงโรคเกาต์เรื้อรังได้อย่างชัดเจน

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (ข้อฝืดยามเช้า (morning stiffness) อย่างน้อย 1 ชม.): เป็นลักษณะเด่นของ "โรคข้ออักเสบรูมาตอยด์" (Rheumatoid arthritis) จากการอักเสบของเยื่อหุ้มข้อ ไม่ใช่โรคเกาต์
• ข้อ ค. (มักเกิดกับข้อใหญ่ๆ ที่รับน้ำหนักมาก): เป็นลักษณะทางคลินิกของ "โรคข้อเสื่อม" (Osteoarthritis) เช่น ข้อเข่า ข้อสะโพก ส่วนเกาต์มักเกิดกับข้อส่วนปลาย (ข้อนิ้วหัวแม่เท้า ข้อเท้า)
• ข้อ ง. (อาจพบนิ่วตะกอนที่ไตได้ มีข้อเท้าบวม): ตัวเลือกในข้อสอบเดิมพิมพ์ผิดความหมายและไม่จำเพาะเจาะจงเท่ากับปุ่มโทฟัส
• ข้อ จ. (อาการปวดเกิดขึ้นที่ข้อเดียวกันทั้งสองข้างของร่างกาย): การอักเสบแบบสมมาตร (Symmetric involvement) เป็นอาการเฉพาะของ "Rheumatoid arthritis" ส่วนโรคเกาต์ในการกำเริบมักเป็นแบบข้อเดียว (Monoarthritis) หรือไม่สมมาตร (Asymmetric)

📖 Guideline อ้างอิง:
2020 American College of Rheumatology (ACR) Guideline for the Management of Gout & แนวทางเวชปฏิบัติการดูแลรักษาโรคเกาต์ พ.ศ. 2555 (สมาคมรูมาติสซั่มแห่งประเทศไทย)

📌 จุดจำก่อนสอบ:
• Gout vs RA vs OA Clinical Pearls:
  - Gout: ปวดข้อเดียวเฉียบพลัน บวมแดงร้อนจัด (Podagra) + มีปุ่ม Tophi (MSU crystal)
  - RA: ข้ออักเสบสมมาตร 2 ข้าง (Symmetric) + Morning stiffness > 1 ชั่วโมง
  - OA: ข้อรับน้ำหนัก (เข่า) + ปวดเมื่อใช้งาน + มีเสียง Crepitus + Morning stiffness < 30 นาที"""

# Row 116: ID 44, แบบแผนการรักษาที่เหมาะสมสำหรับเกาต์กำเริบ -> Ans 1 (ข้อ ก. Indomethacin หรือ NSAIDs)
exp_116 = """✅ คำตอบที่ถูกต้อง: ข้อ ก. Indomethacin

💡 Background:
ผู้ป่วยชายอายุ 55 ปี เป็นโรคเกาต์ที่กำลังมีอาการกำเริบเฉียบพลัน (Acute Gout Flare) หลังจากดื่มเหล้าและรับประทานอาหารพิวรีนสูง (เป็ดย่าง) โดยมีประวัติการใช้ยาเดิมในการระงับอาการอักเสบคือ Indomethacin ตามแนวทางเวชปฏิบัติการรักษาโรคข้ออักเสบเกาต์เฉียบพลัน แนะนำให้ใช้ยาต้านการอักเสบชนิดเดี่ยว (Monotherapy) เช่น NSAIDs (Indomethacin, Naproxen) หรือ Colchicine ขนาดต่ำ เป็นทางเลือกแรกในผู้ป่วยที่มีอาการปวดในระดับน้อยถึงปานกลาง หรือให้ยาเดิมที่ผู้ป่วยเคยตอบสนองได้ดีและไม่มีข้อห้ามใช้ ที่สำคัญที่สุดคือ "ห้ามเริ่มต้นหรือปรับเพิ่มยาลดกรดยูริก Allopurinol ในขณะที่ข้อกำลังอักเสบเฉียบพลัน" เพราะจะทำให้ระดับกรดยูริกในเลือดแกว่งและกระตุ้นให้ข้ออักเสบรุนแรงยิ่งขึ้น

🎯 ทำไมข้อนี้ถึงถูก:
Indomethacin เป็นยากลุ่ม NSAIDs ที่มีประสิทธิภาพสูงในการระงับการอักเสบของ Acute gout flare และเป็นยาเดิมที่ผู้ป่วยเคยใช้ได้ผล การให้ Indomethacin เพื่อระงับอาการอักเสบเฉียบพลันจึงเป็นแบบแผนการรักษาที่เหมาะสมที่สุด

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. (Colchicine): แม้จะเป็น First-line เช่นกัน แต่ผู้ป่วยรายนี้มีประวัติเคยใช้ Indomethacin และในตัวเลือกที่เป็นคำตอบเดี่ยว Indomethacin เป็นตัวเลือกตรงตามเฉลยชุดข้อสอบ
• ข้อ ค. (Indomethacin + colchicine): การให้ยาร่วมสองชนิด (Combination therapy) แนะนำเฉพาะในรายที่มีอาการปวดรุนแรงมาก (Severe pain: Pain score >= 7) หรือข้ออักเสบหลายข้อพร้อมกัน (Polyarticular) การให้ร่วมกันเพิ่มความเสี่ยงต่อพิษทางเดินอาหาร
• ข้อ ง. (Colchicine + allopurinol): ผิดอย่างยิ่ง ห้ามเริ่มยา Allopurinol ในช่วงที่ข้อกำลังอักเสบเฉียบพลัน
• ข้อ จ. (Indomethacin + colchicine + allopurinol): ผิดอย่างยิ่งเพราะมี Allopurinol ในช่วง Acute flare

📖 Guideline อ้างอิง:
2020 American College of Rheumatology (ACR) Guideline for the Management of Gout & EULAR Recommendations for Gout

📌 จุดจำก่อนสอบ:
• Acute Flare Management:
  - First-line: Monotherapy ด้วย NSAIDs (Indomethacin, Naproxen) หรือ Colchicine หรือ Systemic Corticosteroids
  - ห้ามเริ่มยา ULT (Allopurinol, Probenecid) ระหว่าง Acute flare กำเริบ (แต่ถ้าทานอยู่เดิมให้ทานต่อได้)
  - รอให้อาการข้ออักเสบสงบอย่างน้อย 2-4 สัปดาห์ จึงค่อยเริ่มยาลดกรดยูริก ULT"""

# Row 117: ID 45, ยาทดแทน Indomethacin ในผู้ป่วยที่เป็น Peptic Ulcer -> Ans 4 (ข้อ ง. Celecoxib)
exp_117 = """✅ คำตอบที่ถูกต้อง: ข้อ ง. Celecoxib

💡 Background:
Indomethacin เป็นยาต้านการอักเสบในกลุ่ม Non-selective NSAIDs ซึ่งยับยั้งเอนไซม์ทั้ง Cyclooxygenase-1 (COX-1) และ Cyclooxygenase-2 (COX-2) การยับยั้ง COX-1 จะขัดขวางการสร้าง Prostaglandin E2 และ Prostacyclin (PGI2) ที่ทำหน้าที่ปกป้องเยื่อบุทางเดินอาหาร (Cytoprotection) ทำให้ลดการหลั่งเมือก ลดการหลั่งไบคาร์บอเนต และลดการไหลเวียนเลือดที่เยื่อบุกระเพาะ จึงมีความเสี่ยงสูงมากต่อการเกิดแผลในทางเดินอาหาร (Peptic Ulcer Disease) และเลือดออกในทางเดินอาหาร (GI bleeding) ในผู้ป่วยที่ได้รับการวินิจฉัยว่าเป็นโรคแผลในกระเพาะอาหาร หากยังมีความจำเป็นต้องใช้ยาต้านการอักเสบ แนวทางเวชปฏิบัติแนะนำให้เปลี่ยนไปใช้ยากลุ่ม Selective COX-2 Inhibitor (เช่น Celecoxib) ร่วมกับยาลดกรดกลุ่ม Proton Pump Inhibitors (PPIs) เพื่อลดความเป็นพิษต่อกระเพาะอาหารลงให้เหลือน้อยที่สุด

🎯 ทำไมข้อนี้ถึงถูก:
Celecoxib เป็นยายับยั้งจำเพาะต่อเอนไซม์ COX-2 (Selective COX-2 inhibitor) จึงแทบไม่ส่งผลกระทบต่อ COX-1 ในกระเพาะอาหาร ทำให้มีความปลอดภัยต่อระบบทางเดินอาหารสูงที่สุดในตัวเลือกทั้งหมด เหมาะสำหรับใช้ทดแทน Indomethacin ในผู้ป่วยที่เป็นโรคกระเพาะอาหาร

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (Meloxicam): เป็น Preferential COX-2 inhibitor ในขนาดยังคงมีผลยับยั้ง COX-1 และระคายเคืองกระเพาะอาหารได้มากกว่า Celecoxib
• ข้อ ข. (Nabumetone): แม้จะเป็น Prodrug แต่เมแทบอไลต์ออกฤทธิ์ยังคงยับยั้ง COX-1 และมีความเสี่ยงต่อแผลในกระเพาะอาหาร
• ข้อ ค. (Loxoprofen): เป็น Non-selective NSAID ในกลุ่ม Propionic acid ระคายเคืองกระเพาะอาหารได้สูง
• ข้อ จ. (Sulindac): เป็น Non-selective NSAID ที่มีโครงสร้างใกล้เคียงกับ Indomethacin ไม่เหมาะกับผู้ป่วยโรคแผลในกระเพาะอาหาร

📖 Guideline อ้างอิง:
American College of Gastroenterology (ACG) Guidelines on Prevention of NSAID-Related Ulcer Complications & 2020 ACR Guideline for Gout

📌 จุดจำก่อนสอบ:
• NSAID GI Risk Strategy:
  - ผู้ป่วย High GI Risk (เช่น มีประวัติ Peptic Ulcer / Bleeding): แนะนำให้ใช้ "Celecoxib + PPI" (เช่น Omeprazole) ซึ่งเป็นสูตรที่มีความปลอดภัยต่อกระเพาะอาหารสูงที่สุด
  - Indomethacin, Piroxicam, Ketoprofen เป็นกลุ่มที่มีความเสี่ยงต่อ GI สูงที่สุด ต้องหลีกเลี่ยง"""

# Row 118: ID 46, การออกกำลังกายที่เหมาะสมสำหรับผู้ป่วยโรคข้อ -> Ans 1 (ข้อ ก. เทนนิส / หรือออกกำลังกายแบบแรงกระแทกต่ำ)
exp_118 = """✅ คำตอบที่ถูกต้อง: ข้อ ก. เทนนิส

💡 Background:
ตามหลักเวชศาสตร์ฟื้นฟูและแนวทางเวชปฏิบัติสำหรับผู้ป่วยโรคข้อ (ทั้งโรคข้อเสื่อมและโรคเกาต์ในระยะสงบ) การออกกำลังกายที่เหมาะสมที่สุดคือการออกกำลังกายที่ไม่มีแรงกระแทกต่อข้อต่อ (Low-impact exercises) เช่น การว่ายน้ำ เดินในน้ำ หรือปั่นจักรยานอยู่กับที่ เพื่อช่วยเสริมสร้างความแข็งแรงของกล้ามเนื้อรอบข้อโดยไม่ทำให้ข้อต่อได้รับแรงกดกระแทก อย่างไรก็ตาม ในบริบทข้อสอบปรนัยชุดนี้ ตัวเลือกที่ให้มาประกอบด้วย เทนนิส, รักบี้, จ็อกกิ้ง, บาสเกตบอล, ยิมนาสติก ซึ่งกีฬาอย่างรักบี้ บาสเกตบอล และยิมนาสติก มีการปะทะ การกระโดด และแรงบิดกระแทกต่อข้อต่อสูงมาก (Contact/High-impact sports) ข้อสอบเฉลยข้อ ก. เทนนิส ในฐานะกีฬาที่ไม่ใช่กีฬาปะทะร่างกาย (Non-contact sport) เมื่อเทียบกับตัวเลือกอื่น

🎯 ทำไมข้อนี้ถึงถูก:
ตามเฉลยข้อสอบชุดดั้งเดิม เฉลยข้อ ก. เทนนิส เนื่องจากเป็นกีฬาที่ไม่มีการปะทะร่างกาย (Non-contact) เมื่อเปรียบเทียบกับรักบี้หรือบาสเกตบอล (อย่างไรก็ตาม ในทางปฏิบัติทางคลินิกที่ถูกต้อง ควรแนะนำกีฬาแรงกระแทกต่ำ เช่น ว่ายน้ำ หรือเดินเร็ว)

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. (รักบี้): มีการปะทะทางร่างกายอย่างรุนแรง (Contact sport) เสี่ยงต่อการเกิดอุบัติเหตุและการบาดเจ็บต่อข้อต่ออย่างยิ่ง
• ข้อ ค. (จ็อกกิ้ง): มีแรงกระแทกซ้ำๆ ต่อข้อนิ้วเท้า ข้อเท้า และข้อเข่า (Repetitive high-impact)
• ข้อ ง. (บาสเกตบอล): มีการกระโดดลงสู่พื้นและการปะทะ ทำให้เกิดแรงกดมหาศาลต่อข้อเท้าและหัวแม่เท้า
• ข้อ จ. (ยิมนาสติก): มีการบิด หมุน และลงน้ำหนักที่ข้อต่อในมุมที่ผิดธรรมชาติ

📖 Guideline อ้างอิง:
American College of Rheumatology (ACR) Recommendations for Physical Activity in Arthritis & [NEED_REVIEW]

📌 จุดจำก่อนสอบ:
• Exercise Pearls in Joint Diseases:
  - Best Choice (Golden Standard): ว่ายน้ำ (Swimming), เดินในน้ำ (Water aerobics), ปั่นจักรยานแบบอยู่กับที่ (Stationary cycling)
  - หลีกเลี่ยง: กีฬาปะทะ (Contact sports เช่น รักบี้ มวย) และกีฬาที่มีแรงกระแทกซ้ำๆ หรือกระโดดสูง (บาสเกตบอล วิ่งมาราธอน)
  - ช่วงข้ออักเสบเฉียบพลัน: ให้ "พักการใช้ข้อ" (Rest) ห้ามออกกำลังกายจนกว่าข้อจะหายอักเสบสนิท"""

# Row 119: ID 47, อาหารประเภทใดที่เหมาะแก่ผู้ป่วยโรคเกาต์รายนี้ -> Ans 4 (ข้อ ง. แกงจืดเต้าหู้หมูสับ)
exp_119 = """✅ คำตอบที่ถูกต้อง: ข้อ ง. แกงจืดเต้าหู้หมูสับ

💡 Background:
การจัดการอาหารสำหรับผู้ป่วยโรคเกาต์มุ่งเน้นการหลีกเลี่ยงอาหารที่มีสารพิวรีนสูงมาก (Very high purine: > 150 mg/100 g) ได้แก่ เครื่องในสัตว์ทุกชนิด (ตับ ไต ไส้) สัตว์ปีก (ไก่ เป็ด) อาหารหมักดองยอดผักเข้มข้น และเครื่องดื่มแอลกอฮอล์ สำหรับอาหารที่ทำจากถั่วเหลือง เช่น "เต้าหู้" แม้ว่าถั่วเหลืองดิบจะมีพิวรีนปานกลาง แต่หลักฐานทางการแพทย์และงานวิจัยระบาดวิทยาในปัจจุบันพบว่า โปรตีนจากพืชและผลิตภัณฑ์จากถั่วเหลือง (เช่น เต้าหู้ นมถั่วเหลือง) ไม่ได้เพิ่มระดับกรดยูริกในเลือดและไม่เพิ่มความเสี่ยงต่อการกำเริบของโรคเกาต์ อีกทั้งเต้าหู้ยังเป็นแหล่งโปรตีนชั้นดีที่แนะนำให้รับประทานทดแทนเนื้อสัตว์ปีกและเครื่องในสัตว์

🎯 ทำไมข้อนี้ถึงถูก:
"แกงจืดเต้าหู้หมูสับ" เป็นอาหารประเภทต้มที่มีเนื้อหมูปริมาณพอเหมาะและมีเต้าหู้ขาวเป็นส่วนประกอบหลัก จัดเป็นอาหารที่มีพิวรีนต่ำถึงปานกลางและไม่มีแอลกอฮอล์หรือเครื่องใน จึงปลอดภัยและเหมาะสมที่สุดสำหรับผู้ป่วยโรคเกาต์

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (ปีกไก่เหล้าแดง): ปีกไก่เป็นสัตว์ปีกที่มีพิวรีนสูงมาก และมีส่วนผสมของเหล้า (แอลกอฮอล์) ซึ่งกระตุ้นการสร้างยูริกและขัดขวางการขับยูริกทางไต เป็นสิ่งกระตุ้นรุนแรงที่สุด
• ข้อ ข. (ยอดมะพร้าวผัดกุ้ง): กุ้งเป็นอาหารทะเลที่มีพิวรีนสูง
• ข้อ ค. (ซุปหน่อไม้): หน่อไม้เป็นพืชที่มีปริมาณพิวรีนสูง ควรจำกัดหรือหลีกเลี่ยงในผู้ป่วยโรคเกาต์
• ข้อ จ. (เกาเหลาเครื่องในหมู): เครื่องในสัตว์ (ตับ ม้าม ไส้) มีสารพิวรีนเข้มข้นสูงที่สุด ห้ามรับประทานเด็ดขาด

📖 Guideline อ้างอิง:
2020 American College of Rheumatology (ACR) Guideline for the Management of Gout & แนวทางเวชปฏิบัติการดูแลรักษาโรคเกาต์ พ.ศ. 2555 (สมาคมรูมาติสซั่มแห่งประเทศไทย)

📌 จุดจำก่อนสอบ:
• Diet Facts for Gout:
  - อาหารที่ปลอดภัย/แนะนำ: เต้าหู้ ผลิตภัณฑ์นมไขมันต่ำ (Low-fat milk/yogurt) ไข่ ผักใบเขียว กาแฟ น้ำสะอาดปริมาณมาก
  - อาหารที่ต้องงดเว้น: เครื่องในสัตว์ทุกชนิด สัตว์ปีก เครื่องดื่มแอลกอฮอล์ (เบียร์ เหล้า) น้ำหวานที่มี High-fructose corn syrup"""

# Row 120: ID 48, วินิจฉัย หญิง 24 ปี ปวดข้อนิ้วมือ 2 ข้าง ข้อตึงตอนเช้า 20 นาที -> Ans 2 (ข้อ ข. Rheumatoid arthritis)
exp_120 = """✅ คำตอบที่ถูกต้อง: ข้อ ข. Rheumatoid arthritis

💡 Background:
โรคข้ออักเสบรูมาตอยด์ (Rheumatoid Arthritis: RA) เป็นโรคแพ้ภูมิตัวเองเรื้อรัง (Autoimmune systemic inflammatory disease) ที่มีลักษณะพยาธิสภาพเด่นคือ การอักเสบเรื้อรังของเยื่อหุ้มข้อ (Synovitis) ส่งผลให้เกิดการทำลายกระดูกอ่อนและกระดูกรอบข้อ อาการแสดงทางคลินิกที่สำคัญ ได้แก่:
1. พบบ่อยในเพศหญิงวัยเจริญพันธุ์หรือวัยทำงาน (อายุ 20-50 ปี)
2. อาการปวดบวมข้อแบบสมมาตรทั้งสองข้างของร่างกาย (Symmetric polyarthritis)
3. พบบ่อยที่สุดที่ข้อนิ้วมือและข้อมือ (Proximal Interphalangeal: PIP joints, Metacarpophalangeal: MCP joints, และ Wrist joints)
4. อาการข้อตึงฝืดหลังตื่นนอนตอนเช้า (Morning stiffness) ซึ่งสะท้อนถึงการอักเสบของเยื่อหุ้มข้อ

🎯 ทำไมข้อนี้ถึงถูก:
ผู้ป่วยเป็นหญิงอายุน้อย (24 ปี) มีอาการปวดข้อนิ้วมือทั้งสองข้างแบบสมมาตร และมีอาการข้อตึงฝืดในตอนเช้าหลังตื่นนอน ลักษณะทางคลินิกสอดคล้องกับ "โรคข้ออักเสบรูมาตอยด์" (Rheumatoid arthritis) มากที่สุด

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (Gouty arthritis): โรคเกาต์มักพบในเพศชายวัยกลางคน มักเกิดที่ข้อเดียวเฉียบพลัน บวมแดงร้อนจัดที่ข้อนิ้วหัวแม่เท้า (Podagra) ไม่ได้เกิดที่ข้อนิ้วมือสองข้างพร้อมกันแบบสมมาตร
• ข้อ ค. (Osteoarthritis): โรคข้อเสื่อมมักพบในผู้สูงอายุ (> 50-65 ปี) มักเกิดกับข้อรับน้ำหนัก (ข้อเข่า ข้อสะโพก) หรือข้อปลายนิ้ว (DIP joints) และมี Morning stiffness สั้นๆ ไม่เกิน 15-30 นาที และมักไม่มีการอักเสบสมมาตรในหญิงสาว
• ข้อ ง. (Osteoporosis) และ ข้อ จ. (Osteopenia): ภาวะกระดูกพรุนและกระดูกบาง ไม่มีอาการปวดข้อนิ้วมือสองข้างหรือข้อตึงตอนเช้า ผู้ป่วยมักไม่มีอาการจนกว่าจะมีกระดูกหัก

📖 Guideline อ้างอิง:
2021 American College of Rheumatology (ACR) Guideline for the Treatment of Rheumatoid Arthritis & แนวทางเวชปฏิบัติการดูแลรักษาโรคข้ออักเสบรูมาตอยด์ พ.ศ. 2562 (สมาคมรูมาติสซั่มแห่งประเทศไทย)

📌 จุดจำก่อนสอบ:
• RA Diagnostic Clues: หญิงวัยสาว/วัยเจริญพันธุ์ + ปวดบวมข้อนิ้วมือ/ข้อมือ 2 ข้างสมมาตร (Symmetric) + มี Morning stiffness ตอนเช้า = Rheumatoid Arthritis
• Treatment of Choice: เริ่มต้นด้วย Conventional Synthetic DMARDs (csDMARDs) ทันที โดยมี Methotrexate (MTX) เป็น First-line Anchor Drug"""

updates = [
    # Row 108: Q36
    {
        "row": 108, "subtopic": "Gout", "type": "Clinic", "ans": "4",
        "exp": exp_108
    },
    # Row 109: Q37
    {
        "row": 109, "subtopic": "Gout", "type": "Clinic", "ans": "2",
        "exp": exp_109
    },
    # Row 110: Q38
    {
        "row": 110, "subtopic": "Gout", "type": "Clinic", "ans": "3",
        "exp": exp_110
    },
    # Row 111: Q39
    {
        "row": 111, "subtopic": "Osteoarthritis", "type": "Clinic", "ans": "3",
        "exp": exp_111
    },
    # Row 112: Q40
    {
        "row": 112, "subtopic": "Osteoarthritis", "type": "Clinic", "ans": "3",
        "exp": exp_112
    },
    # Row 113: Q41
    {
        "row": 113, "subtopic": "Osteoarthritis", "type": "Clinic", "ans": "5",
        "exp": exp_113
    },
    # Row 114: Q42
    {
        "row": 114, "subtopic": "Pharmaceutical Calculations", "type": "Clinic", "ans": "4",
        "exp": exp_114
    },
    # Row 115: Q43
    {
        "row": 115, "subtopic": "Gout", "type": "Clinic", "ans": "2",
        "exp": exp_115
    },
    # Row 116: Q44
    {
        "row": 116, "subtopic": "Gout", "type": "Clinic", "ans": "1",
        "exp": exp_116
    },
    # Row 117: Q45
    {
        "row": 117, "subtopic": "Gout", "type": "Clinic", "ans": "4",
        "exp": exp_117
    },
    # Row 118: Q46
    {
        "row": 118, "subtopic": "Gout", "type": "Clinic", "ans": "1",
        "exp": exp_118
    },
    # Row 119: Q47
    {
        "row": 119, "subtopic": "Gout", "type": "Clinic", "ans": "4",
        "exp": exp_119
    },
    # Row 120: Q48
    {
        "row": 120, "subtopic": "Rheumatoid Arthritis", "type": "Clinic", "ans": "2",
        "exp": exp_120
    },
]

# Update in sheet
for item in updates:
    r_idx = item["row"] - 108
    row_data = current_rows[r_idx]
    while len(row_data) < 16:
        row_data.append('')
    row_data[8] = item["ans"]
    row_data[9] = item["exp"]
    row_data[11] = item["subtopic"]
    row_data[12] = item["type"]
    current_rows[r_idx] = row_data

ws.update(range_name='A108:P120', values=current_rows)
print("✅ Successfully updated '1. Musculoskeleton'!A108:P120 with refined custom explanations & specific pearls!")
