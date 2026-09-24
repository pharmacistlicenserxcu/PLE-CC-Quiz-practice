# -*- coding: utf-8 -*-
"""
apply_user_tag_and_scenario_fixes.py
1. Fix Q95: Prepend Gout acute scenario (from situation 5) and set multi-tag:
   Topic = "Gout / Pharmacy Laws & Ethics"
2. Fix Q112: Prepend Knee OA case scenario with medication list (from situation 10) and set multi-tag:
   Topic = "Osteoarthritis / Pharmaceutical Calculations"
3. Update Herbal questions to dual-tag (e.g. "Gout / Herbal Medicine", "Osteoarthritis / Herbal Medicine")
4. Update master_musculo_217_pristine.json and PLE CC QUIZ.xlsx
"""
import sys, io, json, openpyxl

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# Load items
with open('master_musculo_217_pristine.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# 1. Update Q95 (Index 94)
q95_scenario = (
    "สถานการณ์ต่อเนื่อง (โรคเกาต์เฉียบพลัน):\n"
    "ผู้ป่วยชายไทย อายุ 45 ปี มารับการรักษาที่โรงพยาบาลด้วยอาการปวด บวม แดง ที่ข้อนิ้วหัวแม่เท้าข้างซ้ายเฉียบพลันหลังรับประทานซุปหน่อไม้และเครื่องในหมู แพทย์วินิจฉัยเป็น Acute Gout และสั่งจ่ายยาบรรเทาอาการอักเสบ\n"
    "หลังจากนั้นอีก 2 สัปดาห์ยาที่ได้รับจากโรงพยาบาลใกล้หมด ผู้ป่วยไม่อยากไปโรงพยาบาลจึงนำตัวอย่างยาเดิมที่ได้รับไปซื้อยาที่ร้านขายยาแผนปัจจุบัน และเล่าอาการให้เภสัชกรฟัง\n"
    "คำถาม: เภสัชกรที่ร้านขายยาไม่สามารถจ่ายยาใดต่อไปนี้ให้ผู้ป่วยรายนี้ได้"
)
items[94]['question'] = q95_scenario
items[94]['topic'] = "Gout / Pharmacy Laws & Ethics"

# 2. Update Q112 (Index 111)
q112_scenario = (
    "สถานการณ์ต่อเนื่อง (โรคข้อเข่าเสื่อม):\n"
    "ผู้ป่วยหญิงได้รับการวินิจฉัยว่าเป็นโรคข้อเข่าเสื่อม (Osteoarthritis) มีอาการปวดเล็กน้อย ไม่มีบวม โดยแพทย์สั่งใช้ยาบำรุงกระดูกและข้อร่วมด้วย ดังนี้:\n"
    "- Paracetamol 500 mg\n"
    "- Glucosamine 250 mg\n"
    "- Calcium carbonate (1 g) รับประทานวันละ 2 เม็ด\n"
    "- เจลพริกทาเฉพาะที่\n"
    "คำถาม: จงคำนวณปริมาณ Ca2+ (Elemental Calcium) ที่ผู้ป่วยได้รับต่อวัน"
)
items[111]['question'] = q112_scenario
items[111]['topic'] = "Osteoarthritis / Pharmaceutical Calculations"

# 3. Update Herbal questions to dual tag
for idx, it in enumerate(items):
    t = it.get('topic', '')
    q_txt = (it['question'] + ' ' + ' '.join(it['choices'])).lower()
    
    # Check if herbal question needs dual tag
    if any(h in q_txt for h in ['สมุนไพร', 'เถาวัลย์เปรียง', 'ขมิ้นชัน', 'เจลพริก', 'capsaicin', 'capsicum']):
        if t == "Herbal Medicine":
            # Determine clinical disease
            if 'gout' in q_txt or 'เกาต์' in q_txt or 'uric' in q_txt:
                it['topic'] = "Gout / Herbal Medicine"
            elif 'oa' in q_txt or 'เข่า' in q_txt or 'ข้อเสื่อม' in q_txt or 'diclofenac' in q_txt:
                it['topic'] = "Osteoarthritis / Herbal Medicine"
        elif "Herbal" not in t:
            it['topic'] = f"{t} / Herbal Medicine"

# Save updated JSON
with open('master_musculo_217_pristine.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print("Updated master_musculo_217_pristine.json")

# 4. Write to Excel
wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx')
ws = wb['1. Musculoskeleton']

for idx, it in enumerate(items):
    row_num = idx + 3
    ws.cell(row=row_num, column=2, value=it['question'])
    ws.cell(row=row_num, column=12, value=it['topic'])

wb.save('PLE CC QUIZ.xlsx')
print("Successfully updated PLE CC QUIZ.xlsx!")
