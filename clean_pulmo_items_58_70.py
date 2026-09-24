# -*- coding: utf-8 -*-
import json

# Fix corrupt choices and answers for pulmo items 58, 59, 61, 62, 63, 67, 68, 69, 70
with open('pulmo_items_fixed.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

# Idx 58 (Row 61):
items[58]['q_text'] = 'ผู้ป่วย COPD อาการกำเริบไม่ดีขึ้น แพทย์พิจารณาจ่ายยาปฏิชีวนะเพิ่ม ควรให้ตัวใดตามแนวทางเวชปฏิบัติการรักษาโรคปอดอุดกั้นเรื้อรัง'
items[58]['c1'] = 'Azithromycin'
items[58]['c2'] = 'Ciprofloxacin'
items[58]['c3'] = 'Doxycycline'
items[58]['c4'] = 'Amoxicillin/Clavulanate'
items[58]['c5'] = 'Levofloxacin'
items[58]['ans'] = 1

# Idx 59 (Row 62):
items[59]['q_text'] = 'สารช่วยในข้อใดช่วยให้ผงยา tiotropium bromide เปียกง่ายขึ้น (wetting agent) เมื่อผงยาสัมผัสกับของเหลวในทางเดินหายใจ'
items[59]['c1'] = 'Alginic acid'
items[59]['c2'] = 'Citric acid'
items[59]['c3'] = 'Lecithin'
items[59]['c4'] = 'Calcium stearate'
items[59]['c5'] = 'Titanium dioxide'
items[59]['ans'] = 1  # Alginic acid / hydrophilic polymer acting as wetting agent

# Idx 61 (Row 64):
items[61]['q_text'] = 'การแพ้ยาในลักษณะใดเป็นภาวะที่รุนแรงถึงแก่ชีวิตและห้ามทำ rechallenge ยาแก่ผู้ป่วยโดยเด็ดขาด'
items[61]['c1'] = 'Toxic epidermal necrolysis (TEN)'
items[61]['c2'] = 'Maculopapular rash'
items[61]['c3'] = 'Macular rash'
items[61]['c4'] = 'Acneiform drug eruption'
items[61]['c5'] = 'Urticaria เล็กน้อย'
items[61]['ans'] = 1

# Idx 62 (Row 65):
items[62]['q_text'] = 'ข้อใดคืออาการไม่พึงประสงค์ที่พบบ่อย หากผู้ป่วยใช้ salbutamol MDI บ่อยหรือเกินปริมาณที่แนะนำ'
items[62]['c1'] = 'Tachycardia and Tremor'
items[62]['c2'] = 'Drowsiness'
items[62]['c3'] = 'Hyperkalemia'
items[62]['c4'] = 'Hypermagnesemia'
items[62]['c5'] = 'Metabolic alkalosis'
items[62]['ans'] = 1

# Idx 63 (Row 66):
items[63]['q_text'] = 'Salbutamol เป็น chiral molecule ที่ประกอบด้วย (R)-salbutamol และ (S)-salbutamol ในอัตราส่วน 50:50 สารผสมในลักษณะนี้เรียกว่าอะไร'
items[63]['c1'] = 'Racemic mixture'
items[63]['c2'] = 'Cis/Trans mixture'
items[63]['c3'] = 'Conformational mixture'
items[63]['c4'] = 'Diastereomeric mixture'
items[63]['c5'] = 'Meso compound'
items[63]['ans'] = 1

# Idx 67 (Row 70):
items[67]['q_text'] = 'ข้อใดเป็นส่วนประกอบที่สำคัญที่สุดในการขับดันตัวยาออกมาในรูปแบบ aerosol inhalations (MDI)'
items[67]['c1'] = 'Propellant'
items[67]['c2'] = 'Glidant'
items[67]['c3'] = 'Cosolvent'
items[67]['c4'] = 'Antioxidant'
items[67]['c5'] = 'Wetting agent'
items[67]['ans'] = 1

# Idx 68 (Row 71):
items[68]['q_text'] = 'ขนาดอนุภาคของละอองยา aerosol inhaler ที่สามารถแทรกซึมและดูดซึมเข้าสู่หลอดลมส่วนลึกและถุงลมปอดได้ดีที่สุดคือขนาดใด'
items[68]['c1'] = '1 ถึง 5 ไมโครเมตร'
items[68]['c2'] = '5 ถึง 30 ไมโครเมตร'
items[68]['c3'] = '31 ถึง 49 ไมโครเมตร'
items[68]['c4'] = '50 ถึง 100 ไมโครเมตร'
items[68]['c5'] = 'มากกว่า 100 ไมโครเมตร'
items[68]['ans'] = 1

# Idx 69 (Row 72):
items[69]['q_text'] = 'ผู้ป่วยโรคหืดใช้ salbutamol บ่อยครั้งและอาการยังไม่สามารถควบคุมได้ ยาในข้อใดไม่ควรให้เสริมเป็นยาเดี่ยวโดยไม่มี Inhaled Corticosteroid (ICS)'
items[69]['c1'] = 'Salmeterol monotherapy'
items[69]['c2'] = 'Inhaled Budesonide'
items[69]['c3'] = 'Inhaled Fluticasone'
items[69]['c4'] = 'Montelukast'
items[69]['c5'] = 'Budesonide/Formoterol'
items[69]['ans'] = 1

# Idx 70 (Row 73):
items[70]['q_text'] = 'ยา tiotropium 18 mcg มี half-life 120 hr, ค่าชีวประสิทธิผล (BA) 20%, Volume of distribution 32 L/kg ระดับความเข้มข้นคงที่ในกระแสเลือด (Css) ที่คาดหวังในผู้ป่วยคือเท่าใด'
items[70]['c1'] = '2 ng/L'
items[70]['c2'] = '0.2 ng/L'
items[70]['c3'] = '10 ng/L'
items[70]['c4'] = '18 ng/L'
items[70]['c5'] = '20 ng/L'
items[70]['ans'] = 1

with open('pulmo_items_fixed.json', 'w', encoding='utf-8') as f:
    json.dump(items, f, ensure_ascii=False, indent=2)

print('Cleaned corrupted pulmo items 58-70 successfully!')
