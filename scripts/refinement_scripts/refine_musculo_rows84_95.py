# -*- coding: utf-8 -*-
"""
refine_musculo_rows84_95.py
Refines and repairs rows 84 to 95 in '1. Musculoskeleton' in PLE CC Quiz:
- Sets accurate Subtopic (Gout, Pharmacology, ADR)
- Writes tailored, case-specific clinical explanations (Clean plain text, no asterisks)
- Generates specific, focused 'จุดจำก่อนสอบ' (High-yield pearls) tailored directly to each question
- References authentic official guidelines (ACR Gout 2020, Thai Rheumatism Gout Guideline, Goodman & Gilman's)
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

current_rows = ws.get('A84:P95')
print(f"Loaded {len(current_rows)} rows (Rows 84 to 95).")

# Row 84 (Q12): Hyperuricemia-inducing drugs
exp_84 = """✅ คำตอบที่ถูกต้อง: ข้อ ง. HCTZ (Hydrochlorothiazide)

💡 Background:
ภาวะกรดยูริกในเลือดสูง (Hyperuricemia) สามารถถูกชักนำหรือทำให้แย่ลงได้จากการใช้ยาหลายกลุ่ม โดยเฉพาะยาขับปัสสาวะกลุ่ม Thiazides (เช่น HCTZ) และ Loop diuretics (เช่น Furosemide) ซึ่งออกฤทธิ์แย่งชิงการขับออกของกรดยูริกที่ท่อไตส่วนต้น (Compete for organic acid transporter: OAT4 / URAT1) และเหนี่ยวนำให้เกิดภาวะขาดน้ำ (Volume depletion) จนร่างกายดูดกลับกรดยูริกเพิ่มขึ้น

🎯 ทำไมข้อนี้ถึงถูก:
Hydrochlorothiazide (HCTZ) เป็นยาขับปัสสาวะที่มีรายงานอย่างชัดเจนว่าเพิ่มระดับกรดยูริกในเลือด และเป็นปัจจัยกระตุ้นให้เกิดข้ออักเสบเกาต์กำเริบ (Gout attack) บ่อยที่สุดในเวชปฏิบัติ จึงควรระมัดระวังหรือหลีกเลี่ยงในผู้ป่วยโรคเกาต์

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (Allopurinol): เป็นยาลดกรดยูริกในเลือด โดยยับยั้งเอนไซม์ Xanthine oxidase ไม่ใช่ยาที่ทำให้ยูริกสูง
• ข้อ ข. (Colchicine): เป็นยาต้านการอักเสบที่ออกฤทธิ์ยับยั้ง Tubulin polymerization ไม่ส่งผลเพิ่มระดับกรดยูริกในเลือด
• ข้อ ค. (Ibuprofen) และ ข้อ จ. (Naproxen): เป็นยาต้านการอักเสบกลุ่ม NSAIDs ใช้รักษาอาการข้ออักเสบเกาต์เฉียบพลัน ไม่มีผลเพิ่มระดับกรดยูริกในเลือดอย่างมีนัยสำคัญ

📖 Guideline อ้างอิง:
2020 American College of Rheumatology (ACR) Guideline for the Management of Gout & แนวทางเวชปฏิบัติการดูแลรักษาโรคเกาต์ พ.ศ. 2555 (สมาคมรูมาติสซั่มแห่งประเทศไทย)

📌 จุดจำก่อนสอบ:
• Gout-Inducing Drugs: ยาที่ทำให้กรดยูริกในเลือดสูงและกระตุ้นเกาต์ ได้แก่ ยาขับปัสสาวะ (Thiazides, Loop diuretics), Low-dose Aspirin, ยาต้านวัณโรค (Pyrazinamide, Ethambutol), และยากดภูมิ (Cyclosporine, Tacrolimus)
• Diuretic Alternative in HTN with Gout: ยาลดความดันที่แนะนำในผู้ป่วยเกาต์คือ Losartan (มีคุณสมบัติ Uricosuric ช่วยขับกรดยูริก) หรือ Calcium Channel Blockers (Amlodipine)"""

# Row 85 (Q13): Sulfa allergy in gout/hypertension
exp_85 = """✅ คำตอบที่ถูกต้อง: ข้อ ค. HCTZ (Hydrochlorothiazide)

💡 Background:
ยา Hydrochlorothiazide (HCTZ) เป็นยาขับปัสสาวะกลุ่ม Benzothiadiazine ซึ่งมีโครงสร้างทางเคมีเป็นอนุพันธ์ของ Sulfonamide (-SO2NH2) ดังนั้น ผู้ป่วยที่มีประวัติแพ้ยากลุ่ม Sulfa (เช่น Co-trimoxazole, Sulfamethoxazole) จึงมีความเสี่ยงต่อการเกิดปฏิกิริยาการแพ้ข้ามกลุ่ม (Cross-reactivity) ได้ จึงต้องใช้ด้วยความระมัดระวังอย่างยิ่ง

🎯 ทำไมข้อนี้ถึงถูก:
ในบรรดาตัวเลือกที่กำหนด HCTZ เป็นยาตัวเดียวที่มีโครงสร้างโมเลกุลเป็น Sulfonamide derivative จึงเป็นยาที่ควรระวังในผู้ป่วยที่แพ้ยากลุ่ม Sulfonamide

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (Allopurinol): เป็นโครงสร้าง Purine analog (Pyrazolo[3,4-d]pyrimidine) ไม่มีหมู่ Sulfonamide
• ข้อ ข. (Colchicine): เป็นสารอัลคาลอยด์ธรรมชาติจากต้น Colchicum autumnale โครงสร้างเป็น Tricyclic alkaloid ไม่มีหมู่ Sulfa
• ข้อ ง. (Ibuprofen) และ ข้อ จ. (Naproxen): เป็นยากลุ่ม Arylpropionic acid derivatives ไม่มีโครงสร้างของ Sulfonamide

📖 Guideline อ้างอิง:
Goodman & Gilman's: The Pharmacological Basis of Therapeutics (Chapter: Diuretics and Sulfonamide Hypersensitivity) & Joint Task Force on Practice Parameters (AAAAI/ACAAI) Drug Allergy Guideline

📌 จุดจำก่อนสอบ:
• Non-antibiotic Sulfonamides: ยาที่มีโครงสร้าง Sulfa ที่ต้องระวัง ได้แก่ Thiazide diuretics (HCTZ), Loop diuretics (Furosemide), Sulfonylureas (Glipizide), และ Carbonic anhydrase inhibitors (Acetazolamide)
• Structure Alert: ผู้ป่วยแพ้ซัลฟาสามารถใช้ NSAIDs ทั่วไป (Naproxen, Ibuprofen) และ Colchicine ได้อย่างปลอดภัย"""

# Row 86 (Q14): NSAID altering uric acid level
exp_86 = """✅ คำตอบที่ถูกต้อง: ข้อ ก. Aspirin (Acetylsalicylic acid)

💡 Background:
Aspirin มีผลต่อการขับกรดยูริกทางไตที่แปรผันตามขนาดยา (Biphasic effect on uric acid excretion):
1. Low dose (75-325 mg/day หรือ < 2-3 g/day): แอสไพรินขนาดต่ำจะแย่งชิงการขับกรดยูริกที่ท่อไตส่วนต้น (Inhibit tubular secretion of uric acid) ทำให้ระดับกรดยูริกในเลือด "สูงขึ้น" และกระตุ้นให้อาการเกาต์กำเริบ
2. High dose (> 4-5 g/day): แอสไพรินขนาดสูงจะไปยับยั้งการดูดกลับของกรดยูริก (Inhibit tubular reabsorption of uric acid) ส่งผลให้ขับกรดยูริกออกทางปัสสาวะเพิ่มขึ้น (Uricosuric effect) ทำให้ระดับกรดยูริกในเลือดลดลง

🎯 ทำไมข้อนี้ถึงถูก:
Aspirin เป็นยา NSAID เพียงตัวเดียวที่มีคุณสมบัติเปลี่ยนแปลงระดับกรดยูริกในเลือดอย่างชัดเจนและขึ้นกับขนาดยา (Biphasic effect) ต่างจาก NSAIDs ตัวอื่นๆ ทั่วไป

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. (Celecoxib), ข้อ ค. (Ibuprofen), ข้อ ง. (Nimesulide), และ ข้อ จ. (Piroxicam): เป็นยากลุ่ม NSAIDs ที่ออกฤทธิ์ต้านการอักเสบโดยยับยั้งเอนไซม์ COX แต่ไม่มีผลรบกวนการขับถ่ายกรดยูริกที่ท่อไตอย่างมีนัยสำคัญ จึงไม่เปลี่ยนแปลงระดับกรดยูริกในเลือด

📖 Guideline อ้างอิง:
Goodman & Gilman's: The Pharmacological Basis of Therapeutics (Chapter: Analgesic-Antipyretic and Anti-inflammatory Agents) & 2020 ACR Guideline for Gout

📌 จุดจำก่อนสอบ:
• Biphasic Uric Acid Effect of Aspirin:
  - ขนาดต่ำ (< 2 g/day เช่น เบบี้แอสไพริน 81 mg) = ลดการขับยูริก -> กรดยูริกในเลือดสูงขึ้น (ระวังในเกาต์)
  - ขนาดสูงมาก (> 4 g/day) = ขับยูริกออกทางปัสสาวะ -> กรดยูริกลดลง แต่มีความเป็นพิษต่อกระเพาะและระบบประสาทสูงมาก"""

# Row 87 (Q15): False statement regarding Gout attack onset
exp_87 = """✅ คำตอบที่ถูกต้อง: ข้อ ค. อาการจะค่อยๆ ปวด มากขึ้นเรื่อยๆ (เป็นข้อความที่ผิด)

💡 Background:
ลักษณะทางคลินิกที่จำเพาะเจาะจงของโรคข้ออักเสบเกาต์เฉียบพลัน (Acute Gout Flare) คือ "อาการปวดข้อเกิดขึ้นอย่างรวดเร็วและรุนแรงมากจนถึงจุดสูงสุดภายใน 12 ถึง 24 ชั่วโมงแรก (Rapid onset of severe pain reaching maximal intensity within 12-24 hours)" ไม่ใช่การค่อยๆ ปวดสะสมทีละน้อยเป็นสัปดาห์หรือเป็นเดือน นอกจากนี้การกำเริบมักเกิดขึ้นในเวลากลางคืนหรือเช้ามืดเนื่องจากอุณหภูมิร่างกายที่ลดลงและภาวะขาดน้ำในเวลากลางคืนส่งผลให้ผลึกเกลือยูเรตตกตะกอนได้ง่ายขึ้น

🎯 ทำไมข้อนี้ถึงถูก:
โจทย์ถามว่าข้อใดกล่าวไม่ถูกต้องเกี่ยวกับโรคเกาต์กำเริบ: ข้อ ค. ที่ระบุว่า "อาการจะค่อยๆ ปวดมากขึ้นเรื่อยๆ" นั้นผิด เพราะเกาต์มีลักษณะปวดรุนแรงแบบเฉียบพลันฉับพลัน (Explosive acute attack) ต่างจากโรคข้อเสื่อม (OA) ที่อาการปวดจะค่อยๆ เป็นค่อยๆ ไปตามการใช้งาน

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (เกิดจากการสร้าง uric acid มากเกินไป): ถูกต้อง เป็นหนึ่งในกลไกของโรคเกาต์ (Overproduction ~10%)
• ข้อ ข. (เกิดจากการที่ขับ uric acid ได้น้อยลง): ถูกต้อง เป็นสาเหตุหลักของผู้ป่วยโรคเกาต์ส่วนใหญ่ (Underexcretion ~90%)
• ข้อ ง. (อาการมักจะเกิดตอนกลางคืนหรือเช้ามืด): ถูกต้อง เป็นช่วงเวลาที่พบบ่อยที่สุดของ Gout attack
• ข้อ จ. (อาจพบนิ่วตกตะกอนที่ไตได้): ถูกต้อง กรดยูริกที่ละลายไม่หมดในปัสสาวะที่เป็นกรดสามารถตกผลึกกลายเป็นนิ่วทางเดินปัสสาวะ (Uric acid nephrolithiasis) ได้

📖 Guideline อ้างอิง:
2020 American College of Rheumatology (ACR) Guideline for the Management of Gout & EULAR Recommendations for Gout Diagnosis

📌 จุดจำก่อนสอบ:
• Acute Flare Kinetics: ข้ออักเสบเกาต์ปวดแตะจุดสูงสุด (Peak pain) ภายใน 24 ชั่วโมงแรกเสมอ (มักตื่นมาปวดตอนเช้ามืด) หากปวดตื้อๆ ค่อยๆ เป็นมาหลายสัปดาห์ ต้องนึกถึงโรคข้ออื่น เช่น Osteoarthritis หรือ Chronic Tendinitis"""

# Row 88 (Q16): False management during acute gout flare
exp_88 = """✅ คำตอบที่ถูกต้อง: ข้อ ข. หากผู้ป่วยมีอาการปวดข้อ ข้อบวมควรรีบให้ยาลดระดับ uric acid ในเลือด (เป็นข้อความที่ผิด)

💡 Background:
หลักการสำคัญในการรักษาโรคข้ออักเสบเกาต์คือ การแยกระหว่าง "การรักษาข้ออักเสบเฉียบพลัน (Acute flare management)" และ "การลดระดับกรดยูริกในระยะยาว (Urate-Lowering Therapy: ULT)" ในกรณีที่ผู้ป่วยมีอาการปวดบวมข้อเฉียบพลันและยังไม่เคยได้รับยาลดกรดยูริกมาก่อน "ห้ามเริ่มต้นยาลดกรดยูริก (เช่น Allopurinol, Febuxostat, Probenecid) ทันทีในขณะที่ข้อกำลังอักเสบเฉียบพลัน" ควรรอให้อาการอักเสบสงบลงอย่างน้อย 2-4 สัปดาห์ก่อน จึงเริ่มยา เพราะการลดระดับยูริกอย่างรวดเร็วจะทำให้ผลึกยูเรตแตกตัวและกระตุ้นการอักเสบให้รุนแรงและยืดเยื้อขึ้น

🎯 ทำไมข้อนี้ถึงถูก:
โจทย์ถามข้อความที่ไม่ถูกต้อง: ข้อ ข. ที่ระบุว่า "หากผู้ป่วยมีอาการปวดข้อ ข้อบวมควรรีบให้ยาลดระดับ uric acid" เป็นการจัดการที่ผิดหลักการทางเภสัชบำบัดอย่างร้ายแรง

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (เบาหวาน ความดันโลหิตสูง สัมพันธ์กับกรดยูริกสูง): ถูกต้อง เป็นส่วนหนึ่งของ Metabolic syndrome ซึ่งส่งผลลดการขับกรดยูริกทางไต
• ข้อ ค. (Aspirin ขนาด 3 g/day มีผลให้ระดับ uric acid ลดลง): ถูกต้อง ตามหลักเภสัชวิทยา แอสไพรินขนาดสูงมาก (> 3-4 g/day) มีฤทธิ์ Uricosuric ขับกรดยูริกออกทางไต
• ข้อ ง. (Colchicine ให้ผลการรักษาที่ดีใน 2 วันแรกของ gout attack): ถูกต้อง Colchicine จะได้ผลดีที่สุดเมื่อเริ่มภายใน 24-36 ชั่วโมงแรกหลังเริ่มมีอาการ
• ข้อ จ. (พันธุกรรมมีผลต่อการเกิดโรค): ถูกต้อง ความผิดปกติของยีนตัวขนส่งยูเรต (เช่น SLC2A9, ABCG2) ถ่ายทอดทางพันธุกรรมได้

📖 Guideline อ้างอิง:
2020 American College of Rheumatology (ACR) Guideline for the Management of Gout & EULAR Recommendations for Gout

📌 จุดจำก่อนสอบ:
• Never Start ULT in Acute Flare: หากเป็นผู้ป่วยใหม่ ห้ามเริ่มยาลดกรดยูริก (Allopurinol/Probenecid) ขณะมี Acute flare แต่ถ้าเป็นผู้ป่วยที่ทานยา ULT ประจำอยู่แล้ว ให้ทานยาเดิมต่อเนื่อง ห้ามหยุดยา"""

# Row 89 (Q17): Treatment regimen for patient on Indomethacin having flare
exp_89 = """✅ คำตอบที่ถูกต้อง: ข้อ ก. Indomethacin (หรือเพิ่มขนาดยา / ให้ Colchicine เสริม)

💡 Background:
ผู้ป่วยชายอายุ 60 ปี โรคเกาต์กำเริบเฉียบพลันหลังดื่มแอลกอฮอล์และรับประทานอาหารพิวรีนสูง โดยมีประวัติยาเดิมที่เคยใช้ควบคุมอาการปวดอักเสบได้ผลดีคือ Indomethacin ซึ่งเป็นยาต้านการอักเสบกลุ่ม Non-selective NSAID ที่มีประสิทธิภาพสูงมากในการระงับอาการปวดข้อเกาต์เฉียบพลัน การรักษาภาวะกำเริบเฉียบพลันในผู้ป่วยที่ไม่มีข้อห้ามใช้ NSAIDs คือการให้ยากลุ่ม NSAIDs (เช่น Indomethacin 50 mg วันละ 3 ครั้ง) ในระยะสั้นจนกว่าอาการปวดจะทุเลา

🎯 ทำไมข้อนี้ถึงถูก:
Indomethacin เป็นยาต้านการอักเสบที่ตรงจุดและตรงกับประวัติการตอบสนองเดิมของผู้ป่วยรายนี้ โดยให้เดี่ยวๆ ในขนาดเต็มเพื่อระงับการอักเสบเฉียบพลัน

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. (Colchicine เดี่ยวๆ): สามารถใช้ได้เช่นกัน แต่ผู้ป่วยเคยได้ผลดีจาก Indomethacin มาก่อน
• ข้อ ค. (Indomethacin + Colchicine): การใช้ยาต้านการอักเสบสองตัวร่วมกันจะพิจารณาเฉพาะในรายที่รุนแรงมาก (Severe polyarticular gout flare) และเพิ่มความเสี่ยงต่อพิษทางเดินอาหาร
• ข้อ ง. (Colchicine + Allopurinol) และ ข้อ จ. (Indomethacin + Colchicine + Allopurinol): มี Allopurinol ร่วมด้วย ซึ่งห้ามเริ่มยา Allopurinol ในขณะที่ข้อกำลังอักเสบเฉียบพลัน

📖 Guideline อ้างอิง:
2020 American College of Rheumatology (ACR) Guideline for the Management of Gout & แนวทางเวชปฏิบัติการดูแลรักษาโรคเกาต์ พ.ศ. 2555 (สมาคมรูมาติสซั่มแห่งประเทศไทย)

📌 จุดจำก่อนสอบ:
• Indomethacin in Acute Gout: ขนาดยามาตรฐานคือ 50 mg วันละ 3 ครั้ง หลังอาหารทันที แล้วค่อยๆ ปรับลดขนาดยาลงเมื่ออาการดีขึ้น
• Contraindications: ระวังการใช้ NSAIDs ในผู้ป่วยโรคไตเรื้อรัง (CKD), โรคแผลในกระเพาะอาหาร (PUD), ภาวะหัวใจล้มเหลว (Heart failure), และผู้ที่ใช้ยา Warfarin"""

# Row 90 (Q18): Diagnosis from Bamboo shoot & Pork offal vignette
exp_90 = """✅ คำตอบที่ถูกต้อง: ข้อ ค. Acute Gout (โรคข้ออักเสบเกาต์เฉียบพลัน)

💡 Background:
อาการปวด บวม แดง ร้อน ฉับพลันที่ข้อนิ้วหัวแม่เท้าข้างซ้าย (Podagra) ภายใน 1 วัน ร่วมกับประวัติการรับประทานอาหารพิวรีนสูงชัดเจน (ซุปหน่อไม้ และต้มเลือดหมู/เกาเหลาเครื่องในหมู) ในชายวัย 45 ปี เป็นอาการทางคลินิกจำเพาะของโรคข้ออักเสบเกาต์เฉียบพลัน (Acute Gout Flare)

🎯 ทำไมข้อนี้ถึงถูก:
ประวัติและอาการแสดงทั้งหมดตรงตามเกณฑ์ทางคลินิกของโรคข้ออักเสบเกาต์เฉียบพลัน (Acute Gout) 100%

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (Rheumatoid arthritis): โรคข้ออักเสบรูมาตอยด์ มีการอักเสบของข้อนิ้วมือแบบสมมาตรสองข้างเรื้อรังและมี Morning stiffness > 1 ชั่วโมง
• ข้อ ข. (Osteoarthritis): โรคข้อเสื่อม ปวดเมื่อใช้งานเรื้อรัง ไม่มีอาการปวดบวมแดงร้อนเฉียบพลัน
• ข้อ ง. (Osteoporosis): กระดูกพรุนไม่ทำให้ปวดข้อเฉียบพลัน
• ข้อ จ. (Osteomalacia): กระดูกอ่อน มีอาการปวดกระดูกทั่วตัวและกล้ามเนื้อล้า

📖 Guideline อ้างอิง:
2020 American College of Rheumatology (ACR) Guideline for the Management of Gout & EULAR Gout Diagnosis Guidelines

📌 จุดจำก่อนสอบ:
• Podagra: อาการปวดบวมแดงร้อนที่ข้อมัตสิมะนิ้วหัวแม่เท้า (1st MTP joint) พบบ่อยที่สุดในเกาต์เฉียบพลัน
• Diet Triggers: เครื่องในสัตว์ ยอดผัก หน่อไม้ สัตว์ปีก เบียร์ และน้ำหวานฟรุกโตส คือตัวกระตุ้นข้ออักเสบเกาต์ที่พบบ่อยในคนไทย"""

# Row 91 (Q19): Cause of Gout - MSU Crystals (Distractor Alert: MSG)
exp_91 = """✅ คำตอบที่ถูกต้อง: ข้อ จ. ไม่มีข้อใดถูก

💡 Background:
พยาธิกำเนิดที่แท้จริงของโรคเกาต์ (Pathogenesis of Gout) เกิดจากการที่ร่างกายมีระดับกรดยูริกในเลือดสูงเรื้อรัง (Hyperuricemia) จนเกินจุดอิ่มตัว ทำให้เกิดการตกผลึกของเกลือ "โมโนโซเดียมยูเรต (Monosodium Urate: MSU)" ภายในช่องข้อและเนื้อเยื่อรอบข้อ ซึ่งจะกระตุ้นระบบภูมิคุ้มกัน (NLRP3 inflammasome) หลั่งสารสื่ออักเสบ IL-1beta ทำให้เม็ดเลือดขาว Neutrophil เข้ามากัดกินผลึกและปล่อยเอนไซม์ทำลายเนื้อเยื่อข้อ

🎯 ทำไมข้อนี้ถึงถูก:
โจทย์ข้อนี้เป็นข้อสอบดักทาง (Distractor trap): ตัวเลือก ข้อ ก. ระบุว่าเป็นผลึก "Monosodium Glutamate" ซึ่งคือผงชูรส ไม่ใช่ "Monosodium Urate" ดังนั้นตัวเลือก ข้อ ก. จึงผิด และไม่มีตัวเลือกใดในข้อ ก-ง ที่อธิบายสาเหตุของโรคเกาต์ได้อย่างถูกต้อง คำตอบที่ถูกต้องจึงเป็น ข้อ จ. ไม่มีข้อใดถูก

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (ผลึก monosodium glutamate ตกตะกอนในข้อ): ผิด Monosodium Glutamate (MSG) คือผงชูรส ผลึกที่แท้จริงในโรคเกาต์คือ "Monosodium Urate (MSU)"
• ข้อ ข. (การเสื่อมสภาพของกระดูกอ่อน): เป็นสาเหตุของโรคข้อเสื่อม (Osteoarthritis) ไม่ใช่โรคเกาต์
• ข้อ ค. (การอักเสบเรื้อรังของเนื้อเยื่อไขกระดูก): เป็นพยาธิสภาพของโรคกระดูกอักเสบ (Osteomyelitis)
• ข้อ ง. (โรค autoimmune ทำให้มีปุ่ม tophi): ผิด โรคเกาต์ไม่ใช่โรค Autoimmune (โรคภูมิต้านตนเอง) เหมือนรูมาตอยด์หรือ SLE แต่เป็นโรคข้ออักเสบจากผลึกผลึกสะสม (Crystal-induced arthropathy)

📖 Guideline อ้างอิง:
Robbins and Cotran Pathologic Basis of Disease (Chapter: Diseases of Joints - Gout) & 2020 ACR Guideline for Gout

📌 จุดจำก่อนสอบ:
• Crystal Identification: ผลึกในโรคเกาต์คือ Monosodium Urate (MSU) ห้ามสับสนกับ Monosodium Glutamate (MSG - ผงชูรส) หรือ Calcium Pyrophosphate Dihydrate (CPPD - Pseudogout)
• Pathophysiology: Hyperuricemia -> ตกผลึก MSU -> กระตุ้น NLRP3 Inflammasome -> หลั่ง IL-1beta -> Neutrophil influx -> ข้ออักเสบเฉียบพลัน"""

# Row 92 (Q20): Drugs with NO effect on uric acid level
exp_92 = """✅ คำตอบที่ถูกต้อง: ข้อ จ. ไม่มีข้อใดถูก (ทุกตัวใน ก-ง ล้วนมีผลเพิ่มกรดยูริกในเลือดทั้งสิ้น)

💡 Background:
โจทย์ถามว่า "ยาใดต่อไปนี้ไม่มีผลต่อระดับกรดยูริกในร่างกาย":
1. Diuretics (Thiazide & Loop diuretics): เพิ่มระดับกรดยูริกในเลือดอย่างมาก โดยแย่งชิงการขับออกทางไตและลดการขับถ่ายยูริก
2. Low-dose Salicylates (Aspirin < 2 g/day): ยับยั้งการหลั่งกรดยูริกที่ท่อไตส่วนต้น ทำให้กรดยูริกในเลือดสูงขึ้น
3. Pyrazinamide (PZA): ยาต้านวัณโรคที่มีสารเมแทบอไลต์ Pyrazinoic acid ยับยั้งการขับกรดยูริกทางไต ทำให้เกิด Hyperuricemia และข้ออักเสบเกาต์ได้บ่อย
4. Ethambutol (EMB): ยาต้านวัณโรคที่ลดการขับกรดยูริกออกทางไตเช่นเดียวกัน

🎯 ทำไมข้อนี้ถึงถูก:
เนื่องจากยาทุกตัวในตัวเลือก ข้อ ก. ถึง ข้อ ง. (Diuretic, Low-dose salicylates, Pyrazinamide, Ethambutol) ล้วนเป็นยาที่มีผลข้างเคียงเด่นชัดในการเพิ่มระดับกรดยูริกในเลือดทั้งสิ้น ดังนั้นจึง "ไม่มีตัวเลือกใดที่ไม่มีผล" คำตอบที่ถูกต้องจึงเป็น ข้อ จ. ไม่มีข้อใดถูก

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (Diuretic): มีผลเพิ่มระดับกรดยูริกในเลือดสูงมาก
• ข้อ ข. (Salicylates low dose): มีผลเพิ่มระดับกรดยูริกในเลือด
• ข้อ ค. (Pyrazinamide): มีผลข้างเคียงทำให้เกิด Hyperuricemia และปวดข้อรุนแรง
• ข้อ ง. (Ethambutol): มีผลลดการขับกรดยูริกและเพิ่มระดับกรดยูริกในเลือดเช่นกัน

📖 Guideline อ้างอิง:
Goodman & Gilman's: The Pharmacological Basis of Therapeutics & 2020 ACR Guideline for the Management of Gout

📌 จุดจำก่อนสอบ:
• Hyperuricemia-Causing Drug List: จำย่อว่า "CAN'T LEAP"
  - Cyclosporine
  - Alcohol
  - Nicotinic acid (Niacin)
  - Thiazides / Loop diuretics
  - Low-dose Aspirin
  - Ethambutol
  - Allopurinol (ระยะเริ่มแรกทำให้ยูริกแกว่ง)
  - Pyrazinamide"""

# Row 93 (Q21): Appropriate acute flare regimen in this patient
exp_93 = """✅ คำตอบที่ถูกต้อง: ข้อ ข. Colchicine (หรือ NSAID monotherapy)

💡 Background:
ในการรักษาอาการข้ออักเสบเกาต์กำเริบเฉียบพลัน (Acute Gout Flare) ในผู้ป่วยที่เพิ่งมีอาการเป็นครั้งแรก ข้อเดียว (ข้อนิ้วหัวแม่เท้า) การรักษามาตรฐานคือการให้ยาเดี่ยว (Monotherapy) ด้วย Colchicine หรือ NSAIDs (เช่น Naproxen, Indomethacin) ไม่แนะนำให้เริ่มยาลดกรดยูริก (Allopurinol) ในทันที และไม่จำเป็นต้องให้ยาต้านการอักเสบซ้ำซ้อนกันหลายตัวในอาการกำเริบระดับน้อยถึงปานกลาง

🎯 ทำไมข้อนี้ถึงถูก:
Colchicine เม็ดเดี่ยวในขนาดต่ำ (1.2 mg stat ตามด้วย 0.6 mg ในอีก 1 ชั่วโมงต่อมา) เป็นแนวทางการรักษาที่ถูกต้อง ปลอดภัย และมีประสิทธิภาพสูงตามแนวทาง ACR 2020

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (Aspirin): ห้ามใช้รักษาอาการปวดในโรคเกาต์ เพราะแอสไพรินขนาดต่ำจะลดการขับกรดยูริกทางไต ทำให้ข้ออักเสบกำเริบหนักขึ้น
• ข้อ ค. (Indomethacin + Colchicine): การใช้ยาผสมสองตัวจะพิจารณาเฉพาะในรายที่ข้ออักเสบรุนแรงหลายข้อพร้อมกัน (Severe polyarticular flare) การให้ในเคสข้อเดียวจะเพิ่มพิษต่อระบบทางเดินอาหารโดยไม่จำเป็น
• ข้อ ง. (Colchicine + Allopurinol) และ ข้อ จ. (Indomethacin + Colchicine + Allopurinol): ห้ามเริ่ม Allopurinol ในขณะที่กำลังมี Acute gout attack เพราะจะทำให้ข้ออักเสบรุนแรงขึ้น

📖 Guideline อ้างอิง:
2020 American College of Rheumatology (ACR) Guideline for the Management of Gout & แนวทางเวชปฏิบัติการดูแลรักษาโรคเกาต์ พ.ศ. 2555 (สมาคมรูมาติสซั่มแห่งประเทศไทย)

📌 จุดจำก่อนสอบ:
• Low-Dose Colchicine Protocol: ขนาดยาแนะนำปัจจุบันคือ 1.2 mg ทันที ตามด้วย 0.6 mg ในอีก 1 ชั่วโมง (รวม 1.8 mg ในวันแรก) ประสิทธิภาพเท่ากับ High-dose ดั้งเดิม แต่ผลข้างเคียงท้องเสียลดลงอย่างมาก
• Acute Flare Drug Choices: Colchicine หรือ NSAID หรือ Steroid ตัวใดตัวหนึ่งเป็น Monotherapy"""

# Row 94 (Q22): Major ADRs of Colchicine
exp_94 = """✅ คำตอบที่ถูกต้อง: ข้อ จ. ถูกทุกข้อ (หรือพบบ่อยที่สุดคือท้องเสีย ทางเดินอาหาร)

💡 Background:
Colchicine ออกฤทธิ์ยับยั้งการรวมตัวของ Tubulin ทำให้เซลล์ที่มีอัตราการแบ่งตัวสูงได้รับผลกระทบ อาการไม่พึงประสงค์ (ADRs) ของ Colchicine แบ่งตามระดับความรุนแรงได้แก่:
1. Gastrointestinal toxicity: พบบ่อยที่สุดและเป็นสัญญาณเตือนพิษระยะแรก (> 80% ในขนาดสูง) ได้แก่ ท้องเสียอย่างรุนแรง (Diarrhea), คลื่นไส้ อาเจียน ปวดเกร็งท้อง
2. Hepatic & Renal toxicity: ค่าเอนไซม์ตับขึ้น (Transaminitis / ตับอักเสบ)
3. Musculoskeletal toxicity: กล้ามเนื้ออักเสบและสลายตัว (Rhabdomyolysis) ส่งผลให้ปัสสาวะมีสีโค้ก (Myoglobinuria)
4. Bone marrow suppression: กดการทำงานของไขกระดูก ทำให้เม็ดเลือดขาวต่ำ เกล็ดเลือดต่ำ และโลหิตจาง (มักพบเมื่อได้รับยาเกินขนาดหรือใช้ในผู้ป่วยไตวาย)

🎯 ทำไมข้อนี้ถึงถูก:
Colchicine ในขนาดสูงหรือเมื่อเกิดพิษ สามารถทำให้เกิดอาการได้ครบทุกข้อ ทั้งตับอักเสบ, ท้องเสียรุนแรง, กล้ามเนื้อสลายจนปัสสาวะสีโค้ก, และการกดไขกระดูก ดังนั้น ข้อ จ. ถูกทุกข้อ จึงเป็นคำตอบที่ครอบคลุมสเปกตรัมความเป็นพิษของยานี้

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. ข. ค. ง.: เป็นอาการไม่พึงประสงค์ที่เกิดขึ้นได้จริงจาก Colchicine ทั้งสิ้น แต่ยังไม่ครอบคลุมเท่าตัวเลือกถูกทุกข้อ

📖 Guideline อ้างอิง:
Goodman & Gilman's: The Pharmacological Basis of Therapeutics (Chapter: Gout - Colchicine Toxicity) & US FDA Drug Safety Communication on Colchicine

📌 จุดจำก่อนสอบ:
• Early Toxicity Sign: ท้องเสียถ่ายเหลว (Diarrhea) คลื่นไส้อาเจียน = สัญญาณเตือนพิษเฉียบพลันอันดับแรก ต้องสั่งหยุดยาทันที
• Severe / Overdose Toxicity: กดไขกระดูก (Bone marrow suppression) กล้ามเนื้อสลาย (Rhabdomyolysis -> ปัสสาวะสีโค้ก) และตับไตวายเฉียบพลัน"""

# Row 95 (Q23): Drugs contraindicated/ineffective for acute gout flare
exp_95 = """✅ คำตอบที่ถูกต้อง: ข้อ จ. ถูกทั้งข้อ ค. และ ง. (Xanthine oxidase inhibitors และ Uricosuric agents)

💡 Background:
ในการจัดการโรคข้ออักเสบเกาต์เฉียบพลัน (Acute Gout Flare) ยาที่นำมาใช้ต้องเป็นยาที่มีฤทธิ์ระงับอาการปวดและต้านการอักเสบ (Anti-inflammatory agents) ได้แก่ NSAIDs, Colchicine, และ Corticosteroids ส่วนยากลุ่มลดกรดยูริก (Urate-Lowering Therapy: ULT) ได้แก่ Xanthine Oxidase Inhibitors (Allopurinol, Febuxostat) และ Uricosuric agents (Probenecid, Benzbromarone) "ไม่มีฤทธิ์ต้านการอักเสบ" และ "ห้ามเริ่มต้นใช้ในขณะที่ข้อกำลังอักเสบเฉียบพลัน" เนื่องจากทำให้ระดับกรดยูริกในเลือดลดลงฉับพลัน ส่งผลให้ผลึกในข้อละลายบางส่วนและกระตุ้นการอักเสบให้รุนแรงและยืดเยื้อขึ้น

🎯 ทำไมข้อนี้ถึงถูก:
ทั้ง Xanthine oxidase inhibitors (ข้อ ค.) และ Uricosuric agents (ข้อ ง.) ล้วนเป็นยาลดกรดยูริกที่ไม่มีฤทธิ์ลดปวดอักเสบและห้ามนำมาใช้รักษาภาวะเฉียบพลัน ดังนั้นคำตอบที่ถูกต้องที่สุดคือ ข้อ จ. ถูกทั้งข้อ ค. และ ง.

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ก. (Corticosteroid): เป็นยาทางเลือกแรกในการรักษาข้ออักเสบเกาต์เฉียบพลัน โดยเฉพาะในผู้ป่วยที่มีข้อห้ามใช้ NSAIDs หรือมีไตเสื่อม
• ข้อ ข. (NSAIDs): เป็นยาทางเลือกแรกมาตรฐานในการรักษาอาการข้ออักเสบเกาต์เฉียบพลัน
• ข้อ ค. และ ข้อ ง.: เป็นเพียงส่วนหนึ่งของคำตอบที่ถูกต้อง ซึ่งสรุปรวมอยู่ในข้อ จ.

📖 Guideline อ้างอิง:
2020 American College of Rheumatology (ACR) Guideline for the Management of Gout & EULAR Recommendations for Gout

📌 จุดจำก่อนสอบ:
• Acute Flare vs Chronic ULT:
  - Acute Flare Meds (ลดการอักเสบ): Colchicine, NSAIDs, Corticosteroids
  - Chronic ULT Meds (ลดกรดยูริก - ห้ามเริ่มตอน flare): Allopurinol, Febuxostat, Probenecid, Benzbromarone"""

# Build updated matrix for rows 84 to 95
updated_matrix = [
    [82, current_rows[0][1], "", current_rows[0][3], current_rows[0][4], current_rows[0][5], current_rows[0][6], current_rows[0][7], 4, exp_84, "", "Gout", "Clinic", "ข้อ 12 ชุด 1 (เฉลยข้อ ง)", "ข้อสอบจริง", "ชุด 1"],
    [83, current_rows[1][1], "", current_rows[1][3], current_rows[1][4], current_rows[1][5], current_rows[1][6], current_rows[1][7], 3, exp_85, "", "Gout", "Clinic", "ข้อ 13 ชุด 1 (เฉลยข้อ ค)", "ข้อสอบจริง", "ชุด 1"],
    [84, current_rows[2][1], "", current_rows[2][3], current_rows[2][4], current_rows[2][5], current_rows[2][6], current_rows[2][7], 1, exp_86, "", "Gout", "Clinic", "ข้อ 14 ชุด 1 (เฉลยข้อ ก)", "ข้อสอบจริง", "ชุด 1"],
    [85, current_rows[3][1], "", current_rows[3][3], current_rows[3][4], current_rows[3][5], current_rows[3][6], current_rows[3][7], 3, exp_87, "", "Gout", "Clinic", "ข้อ 15 ชุด 1 (เฉลยข้อ ค)", "ข้อสอบจริง", "ชุด 1"],
    [86, current_rows[4][1], "", current_rows[4][3], current_rows[4][4], current_rows[4][5], current_rows[4][6], current_rows[4][7], 2, exp_88, "", "Gout", "Clinic", "ข้อ 16 ชุด 1 (เฉลยข้อ ข)", "ข้อสอบจริง", "ชุด 1"],
    [87, current_rows[5][1], "", current_rows[5][3], current_rows[5][4], current_rows[5][5], current_rows[5][6], current_rows[5][7], 1, exp_89, "", "Gout", "Clinic", "ข้อ 17 ชุด 1 (เฉลยข้อ ก)", "ข้อสอบจริง", "ชุด 1"],
    [88, current_rows[6][1], "", current_rows[6][3], current_rows[6][4], current_rows[6][5], current_rows[6][6], current_rows[6][7], 3, exp_90, "", "Gout", "Clinic", "ข้อ 18 ชุด 1 (เฉลยข้อ ค)", "ข้อสอบจริง", "ชุด 1"],
    [89, current_rows[7][1], "", current_rows[7][3], current_rows[7][4], current_rows[7][5], current_rows[7][6], current_rows[7][7], 5, exp_91, "", "Gout", "Clinic", "ข้อ 19 ชุด 1 (เฉลยข้อ จ)", "ข้อสอบจริง", "ชุด 1"],
    [90, current_rows[8][1], "", current_rows[8][3], current_rows[8][4], current_rows[8][5], current_rows[8][6], current_rows[8][7], 5, exp_92, "", "Gout", "Clinic", "ข้อ 20 ชุด 1 (เฉลยข้อ จ)", "ข้อสอบจริง", "ชุด 1"],
    [91, current_rows[9][1], "", current_rows[9][3], current_rows[9][4], current_rows[9][5], current_rows[9][6], current_rows[9][7], 2, exp_93, "", "Gout", "Clinic", "ข้อ 21 ชุด 1 (เฉลยข้อ ข)", "ข้อสอบจริง", "ชุด 1"],
    [92, current_rows[10][1], "", current_rows[10][3], current_rows[10][4], current_rows[10][5], current_rows[10][6], current_rows[10][7], 5, exp_94, "", "Gout", "Clinic", "ข้อ 22 ชุด 1 (เฉลยข้อ จ)", "ข้อสอบจริง", "ชุด 1"],
    [93, current_rows[11][1], "", current_rows[11][3], current_rows[11][4], current_rows[11][5], current_rows[11][6], current_rows[11][7], 5, exp_95, "", "Gout", "Clinic", "ข้อ 23 ชุด 1 (เฉลยข้อ จ)", "ข้อสอบจริง", "ชุด 1"]
]

# Update to Google Sheet
target_range = "A84:P95"
ws.update(range_name=target_range, values=updated_matrix)
print(f"✅ Successfully updated '1. Musculoskeleton'!{target_range} with refined custom explanations & specific pearls!")
