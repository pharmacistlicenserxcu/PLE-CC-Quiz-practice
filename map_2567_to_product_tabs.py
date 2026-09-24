import sys
import io
import re
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

src = r'C:\Users\thana\Downloads\_CC1 Product Contents (1).md'
with open(src, 'r', encoding='utf-8') as f:
    text = f.read()

# Define the 13 Product tabs in PLE CC QUIZ.xlsx
product_groups = [
    '1. Titrations',
    '2. Chromatography',
    '3. Spectroscopy & Optics',
    '4. Preformulation & GMP',
    '5. Pharmaceutical Calc',
    '6. Solid Dosage Forms',
    '7. Liquid & Semisolids',
    '8. Biopharm & Drug Release',
    '9. Sterile & Special Forms',
    '10. Biotech Products',
    '11. Herbal Products',
    '12. Food Products & QA',
    '13. Medicinal Chemistry'
]

print("=== Scanning 2567 Questions & Mapping to 13 Product Tabs ===")
q_2567 = text[46:8404]
questions_2567 = re.findall(r'### \*\*ข้อ (\d+)\*\*(.*?)(?=### \*\*ข้อ \d+\*\*|$)', q_2567, re.DOTALL)

for q_num, content in questions_2567:
    lines = [l.strip() for l in content.strip().splitlines() if l.strip()]
    q_title = lines[0] if lines else ''
    
    # rule-based mapping demo
    tab = "Unknown"
    q_lower = content.lower()
    if 'titration' in q_lower or 'karl fischer' in q_lower or 'ไตเตรท' in q_lower or 'h2o' in q_lower:
        tab = '1. Titrations'
    elif 'chromatography' in q_lower or 'hplc' in q_lower or 'retention time' in q_lower or 'run time' in q_lower or 'tlc' in q_lower or 'gc' in q_lower:
        tab = '2. Chromatography'
    elif 'rotation' in q_lower or 'polarimetry' in q_lower or 'uv' in q_lower or 'nmr' in q_lower or 'ir ' in q_lower or 'refractometry' in q_lower:
        tab = '3. Spectroscopy & Optics'
    elif 'sterilization' in q_lower or 'clean room' in q_lower or 'aseptic' in q_lower or 'หยอดตา' in q_lower or 'ophthalmic' in q_lower:
        tab = '9. Sterile & Special Forms'
    elif 'สมุนไพร' in q_lower or 'กัญชา' in q_lower or 'ขี้เหล็ก' in q_lower:
        tab = '11. Herbal Products'
    elif 'suppository' in q_lower or 'gel' in q_lower or 'suspension' in q_lower or 'emulsion' in q_lower or 'cream' in q_lower:
        tab = '7. Liquid & Semisolids'
    elif 'capsule' in q_lower or 'tablet' in q_lower or 'magnesium stearate' in q_lower or 'microcrystalline' in q_lower or 'disintegration' in q_lower or 'friability' in q_lower:
        tab = '6. Solid Dosage Forms'
    elif 'โครงสร้าง' in q_lower or 'structure' in q_lower or 'azole' in q_lower:
        tab = '13. Medicinal Chemistry'
    elif 'biologic' in q_lower or 'antibody' in q_lower or 'vaccine' in q_lower or 'protein' in q_lower:
        tab = '10. Biotech Products'
    elif 'dissolution' in q_lower or 'fick' in q_lower or 'bcs' in q_lower or 'bioavailability' in q_lower:
        tab = '8. Biopharm & Drug Release'
    elif 'อาหาร' in q_lower or 'gmp' in q_lower or 'stability' in q_lower:
        tab = '4. Preformulation & GMP'
    elif 'คำนวณ' in q_lower or 'equivalent' in q_lower or 'meq' in q_lower or 'mosmol' in q_lower:
        tab = '5. Pharmaceutical Calc'
        
    print(f"ข้อ {q_num:>2}: {tab:<26} | {q_title[:65]}")
