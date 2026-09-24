import openpyxl
import json
import sys
import io
import re

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

wb = openpyxl.load_workbook('PLE CC QUIZ.xlsx', read_only=True)
ws = wb['2. Cardiovascular']
rows = list(ws.iter_rows(values_only=True))

headers = rows[1]

valid_list = []
dummy_c1_list = [
    'Diltiazem 30 mg TID', 'Amlodipine 5 mg OD', 'Hydrochlorothiazide 25 mg OD',
    'Bisoprolol 5 mg OD', 'Aspirin 81 mg OD'
]

def clean_text(s):
    if not s:
        return s
    s = str(s)
    # Fix CP874 mojibake artifacts like % instead of ้, - instead of ่, etc.
    s = s.replace('_x001E_', '')
    s = s.replace('ข$อ', 'ข้อ')
    s = s.replace('ไม-ถูกต$อง', 'ไม่ถูกต้อง')
    s = s.replace('ไม-ได$', 'ไม่ได้')
    s = s.replace('ไม-ควรใช$ร-วมกับยา', 'ไม่ควรใช้ร่วมกับยา')
    s = s.replace('เคี้ยวให$ละเอียดก-อนรับประทาน', 'เคี้ยวให้ละเอียดก่อนรับประทาน')
    s = s.replace('พบน$อยที่สุด', 'พบน้อยที่สุด')
    s = s.replace('แต.ผู(ปcวยได(รับยา', 'แต่ผู้ป่วยได้รับยา')
    s = s.replace('เชื%อ', 'เชื้อ')
    s = s.replace('ขึ%น', 'ขึ้น')
    s = s.replace('นี%', 'นี้')
    s = s.replace('เพื_x001E_อ', 'เพื่อ')
    s = s.replace('ที_x001E_มิได้', 'ที่มิได้')
    s = s.replace('ที_x001E_ใช้', 'ที่ใช้')
    s = s.replace('ที_x001E_', 'ที่')
    # strip ** and *
    s = s.replace('**', '').replace('*', '')
    return s.strip()

for idx, r in enumerate(rows[2:], 3):
    if not any(x is not None for x in r):
        continue
    c1 = str(r[3]).strip() if r[3] else ''
    c2 = str(r[4]).strip() if r[4] else ''
    q_text = str(r[1]).strip() if r[1] else ''
    
    # Check corrupted rows
    if c1 in dummy_c1_list and c2 in [
        'Warfarin 3 mg OD (target INR 2-3)', 'Warfarin 3 mg OD (target INR 2.0-3.0)',
        'Losartan 50 mg OD', 'Atorvastatin 20 mg OD', 'Spironolactone 25 mg OD',
        'Sacubitril/Valsartan 49/51 mg BID'
    ]:
        continue
    if len(q_text) < 10 and not any(k in q_text.lower() for k in ['bp', 'hr', 'ecg', 'ckd', 'htn']):
        continue
        
    # Unpack row
    q_no = r[0]
    q_img = r[2]
    c3 = str(r[5]).strip() if r[5] else ''
    c4 = str(r[6]).strip() if r[6] else ''
    c5 = str(r[7]).strip() if r[7] else ''
    ans = r[8]
    exp = str(r[9]).strip() if r[9] else ''
    exp_img = r[10]
    subtopic = str(r[11]).strip() if r[11] else 'Cardiovascular'
    cat_pc = str(r[12]).strip() if len(r) > 12 and r[12] else 'Clinic'
    note = str(r[13]).strip() if len(r) > 13 and r[13] else ''
    q_type = str(r[14]).strip() if len(r) > 14 and r[14] else ''
    exam_year = str(r[15]).strip() if len(r) > 15 and r[15] else ''

    # Clean strings
    q_text = clean_text(q_text)
    c1 = clean_text(c1)
    c2 = clean_text(c2)
    c3 = clean_text(c3)
    c4 = clean_text(c4)
    c5 = clean_text(c5)
    exp = clean_text(exp)
    
    # Fix bundled choices in rows 63, 64, 65
    if '50 คน b) 80 คน c) 133 คน' in c1:
        c1 = '50 คน'
        c2 = '80 คน'
        c3 = '133 คน'
        c4 = '160 คน'
        c5 = '180 คน'
        ans = 2
    elif 'Masked hypertension b) ความดันโลหิตสูงระดับ 1' in c1:
        c1 = 'ความดันโลหิตปกติ (Normal blood pressure)'
        c2 = 'ความดันโลหิตสูงระดับ 1 (Stage 1 Hypertension)'
        c3 = 'ความดันโลหิตสูงระดับ 2 (Stage 2 Hypertension)'
        c4 = 'ความดันโลหิตสูงชนิด Isolated Systolic Hypertension'
        c5 = 'ความดันโลหิตสูงชนิด Masked Hypertension'
        ans = 2
    elif 'ลดน้ำหนัก b) ออกกำลังกาย c) งดบุหรี่' in c1:
        c1 = 'ลดน้ำหนักให้อยู่ในเกณฑ์เหมาะสม (BMI 18.5 - 22.9 kg/m²)'
        c2 = 'ออกกำลังกายแบบแอโรบิกสม่ำเสมออย่างน้อย 150 นาที/สัปดาห์'
        c3 = 'งดสูบบุหรี่และหลีกเลี่ยงควันบุหรี่มือสอง'
        c4 = 'จำกัดการดื่มเครื่องดื่มแอลกอฮอล์'
        c5 = 'งดรับประทานอาหารที่มีโพแทสเซียมสูง (งดผักและผลไม้ทุกชนิด)'
        ans = 5

    item = {
        'orig_row': idx,
        'q_no': q_no,
        'q_text': q_text,
        'q_img': q_img,
        'c1': c1,
        'c2': c2,
        'c3': c3,
        'c4': c4,
        'c5': c5,
        'ans': ans,
        'exp': exp,
        'exp_img': exp_img,
        'subtopic': subtopic,
        'cat_pc': cat_pc,
        'note': note,
        'q_type': q_type,
        'exam_year': exam_year
    }
    valid_list.append(item)

print(f"Total valid cleaned questions extracted: {len(valid_list)}")

with open('cardio_valid_extracted.json', 'w', encoding='utf-8') as f:
    json.dump(valid_list, f, ensure_ascii=False, indent=2)

print("Saved to cardio_valid_extracted.json")
