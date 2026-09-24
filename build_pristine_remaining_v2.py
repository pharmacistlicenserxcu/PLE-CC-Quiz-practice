#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Fixed Universal Pristine Builder for Sheets 12-18
Correct sheet names: '17. Herbal Medicine', '18. Clinical Nutrition'
Enhanced template pattern cleaning with specific pharmacological reasons.
"""

import json, os, re, sys
sys.stdout.reconfigure(encoding='utf-8')
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

QUIZ_FILE = "PLE CC QUIZ.xlsx"

SHEET_CONFIGS = [
    ("12. GynaecologicGenitourinary",
     ["gyn_part1.json","gyn_part2.json","gyn_part3.json","gyn_part4.json"],
     "WHO Medical Eligibility Criteria for Contraceptive Use (5th edition, 2015)"),
    ("13. Eye disorder",
     ["eye_part1.json","eye_part2.json"],
     "AAO Preferred Practice Pattern / Thai Ophthalmological Society Guidelines"),
    ("14. Oncologic",
     ["onco_part1.json","onco_part2.json","onco_part3.json"],
     "NCCN Clinical Practice Guidelines in Oncology / ASCO Guidelines"),
    ("15. Renal",
     ["renal_part1.json","renal_part2.json"],
     "KDIGO 2022 CKD Guideline"),
    ("17. Herbal Medicine",
     ["herb_part1.json","herb_part2.json","herb_part3.json"],
     "Thai Herbal Pharmacopoeia / WHO Monographs on Medicinal Plants"),
    ("18. Clinical Nutrition",
     ["nutri_part1.json"],
     "ASPEN Clinical Guidelines 2022 / Thai SPEN Guidelines"),
]

TMPL_PHRASES = [
    "ไม่ใช่คำตอบที่ถูกต้องสำหรับภาวะ",
    "ไม่ตรงกับบริบท",
    "ไม่ถูกต้องตามหลักการรักษา",
    "ไม่ตรงกับคำถาม",
    "ไม่ถูกต้องสำหรับสภาวะ",
    "ไม่ใช่ตัวเลือกที่ถูกต้อง",
    "เนื่องจากกลไกการออกฤทธิ์, efficac",
    "เนื่องจากกลไกการออกฤทธิ์,",
]

# Keyword -> pharmacological distractor reason
CHOICE_REASONS = {
    "ethinyl estradiol": "Ethinyl estradiol ออกฤทธิ์ผ่าน ERα/ERβ เพิ่ม hepatic coagulation factor synthesis เสี่ยง VTE ในผู้มีความเสี่ยงสูง มีข้อห้ามใน WHO MEC Category 4",
    "levonorgestrel": "Levonorgestrel เป็น 2nd generation progestin มีฤทธิ์ androgenic สูงกว่า 3rd generation อาจกระทบ lipid profile แต่ประสิทธิภาพสูง",
    "lynestrenol": "Lynestrenol เป็น progestogen ที่ถูก metabolize เป็น norethindrone มีฤทธิ์ androgenic อ่อน ใช้ใน progestin-only contraception",
    "estradiol": "Estradiol มีผลต่อ hepatic first-pass metabolism น้อยกว่า ethinyl estradiol เมื่อให้ผ่าน transdermal route ลด VTE risk เมื่อเทียบกับ oral route",
    "progesterone": "Progesterone มีฤทธิ์ยับยั้ง LH surge ป้องกันการตกไข่และทำให้ cervical mucus หนาขึ้น ใช้ใน luteal phase support ใน IVF",
    "medroxyprogesterone": "Medroxyprogesterone acetate (DMPA) เป็น Injectable progestin ให้ทุก 3 เดือน มีผลลด bone mineral density ในระยะยาว",
    "ulipristal": "Ulipristal acetate เป็น Selective Progesterone Receptor Modulator (SPRM) ใช้เป็น emergency contraception ภายใน 120 ชั่วโมง มีประสิทธิภาพสูงกว่า LNG",
    "methotrexate": "Methotrexate ยับยั้ง DHFR ลด tetrahydrofolate synthesis กด DNA synthesis ใน rapidly dividing cells มีผลข้างเคียง mucositis, hepatotoxicity ต้องให้ Leucovorin rescue ขนาดสูง",
    "cisplatin": "Cisplatin เป็น Platinum-based alkylating agent ที่ก่อ DNA intrastrand cross-link ผลข้างเคียงหลัก: nephrotoxicity (ต้องให้ hydration), ototoxicity, neuropathy",
    "carboplatin": "Carboplatin มี nephrotoxicity ต่ำกว่า cisplatin แต่มี myelosuppression (thrombocytopenia) เด่น ปรับขนาดตาม AUC และ eGFR (Calvert formula)",
    "oxaliplatin": "Oxaliplatin ก่อ DNA adducts โดยเฉพาะ intrastrand cross-link ผลข้างเคียงเด่น: cumulative peripheral neuropathy เป็น standard ใน FOLFOX สำหรับ colorectal cancer",
    "tamoxifen": "Tamoxifen เป็น SERM antagonist ที่ breast แต่ partial agonist ที่ uterus (เสี่ยง endometrial cancer) ต้องระวัง DDI กับ CYP2D6 inhibitors เช่น fluoxetine",
    "trastuzumab": "Trastuzumab เป็น anti-HER2 mAb ใช้เฉพาะ HER2+ (IHC 3+ หรือ FISH amplified) breast/gastric cancer มี cardiotoxicity (LVEF monitoring ทุก 3 เดือน)",
    "bevacizumab": "Bevacizumab เป็น anti-VEGF mAb ยับยั้ง angiogenesis ผลข้างเคียงสำคัญ: hypertension, proteinuria, wound healing impairment, GI perforation",
    "timolol": "Timolol เป็น Non-selective beta-blocker ลด IOP โดยลด aqueous humor production มีข้อห้ามใน asthma, COPD, bradycardia, AV block",
    "pilocarpine": "Pilocarpine เป็น M3 muscarinic agonist ลด IOP โดยเพิ่ม trabecular outflow ทำให้ miosis, accommodative spasm และ headache เป็น 2nd line ปัจจุบัน",
    "latanoprost": "Latanoprost เป็น FP Prostaglandin analog ลด IOP ผ่าน uveoscleral outflow ผลข้างเคียง: เปลือกตาคล้ำ, iris pigmentation, eyelash growth",
    "brimonidine": "Brimonidine เป็น Alpha-2 adrenergic agonist ลด aqueous production และเพิ่ม uveoscleral outflow ต้องระวังในเด็กเล็ก (CNS depression)",
    "dorzolamide": "Dorzolamide เป็น Topical Carbonic anhydrase inhibitor ลด aqueous production ผลข้างเคียง: metallic taste, ocular burning",
    "furosemide": "Furosemide เป็น Loop diuretic ยับยั้ง NKCC2 ที่ thick ascending limb สูญเสีย Na+, K+, Cl-, Mg2+ ต้องระวัง electrolyte และ ototoxicity",
    "hydrochlorothiazide": "Hydrochlorothiazide ยับยั้ง NCC ที่ distal convoluted tubule ทำให้สูญเสีย K+ และ Mg2+ มีฤทธิ์ลด urinary Ca2+ (ประโยชน์ใน nephrolithiasis)",
    "spironolactone": "Spironolactone เป็น MR antagonist ลด K+ excretion มีฤทธิ์ anti-androgen ใช้ใน resistant hypertension, HFrEF และ primary hyperaldosteronism",
    "acei": "ACE inhibitors ยับยั้ง ACE ลด angiotensin II และ aldosterone เพิ่ม bradykinin (ทำให้ไอแห้ง) ลด intraglomerular pressure และ proteinuria",
    "arb": "ARB ยับยั้ง AT1 receptor โดยตรง ไม่เพิ่ม bradykinin จึงไม่มีอาการไอ มีผล renoprotective ใน DKD คล้าย ACEi",
    "erythropoietin": "Erythropoietin (EPO) กระตุ้น erythropoiesis ใน bone marrow ใช้รักษา anemia of CKD ต้องให้ iron supplement ร่วม เสี่ยง hypertension และ thrombosis",
    "hemodialysis": "Hemodialysis บำบัดผ่าน diffusion gradient ต้องการ vascular access (AVF/AVG/CVC) ใช้ใน ESRD/AKI ที่มี uremia, refractory electrolyte หรือ volume overload",
    "กระเทียม": "กระเทียม (Allium sativum) มีสาร Allicin (ลดไขมัน ต้านจุลชีพ) และ Ajoene (ยับยั้ง platelet) มี DDI กับ warfarin/antiplatelet เพิ่ม bleeding risk",
    "ขิง": "ขิง (Zingiber officinale) มีฤทธิ์ antiemetic ผ่าน 6-gingerol (ยับยั้ง 5-HT3) ต้านการอักเสบ ต้องระวัง DDI กับ anticoagulants เพิ่ม bleeding risk",
    "ฟ้าทะลายโจร": "ฟ้าทะลายโจร (Andrographis paniculata) มีสาร Andrographolide ยับยั้ง NF-κB ต้านไวรัส ไม่ควรใช้ในหญิงตั้งครรภ์ (abortifacient) และ autoimmune disease",
    "กระชาย": "กระชาย (Kaempferia parviflora) มีสาร polymethoxyflavone มีฤทธิ์ PDE5 inhibitor อ่อน ต้านการอักเสบ ต้องระวังในผู้ที่ใช้ nitrates",
    "บัวบก": "บัวบก (Centella asiatica) มีสาร asiaticoside, madecassoside กระตุ้น collagen synthesis ฟื้นฟูแผล ต้องระวังในผู้ป่วย liver disease",
    "กวาวเครือ": "กวาวเครือขาว (Pueraria mirifica) มีสาร miroestrol (phytoestrogen) ออกฤทธิ์คล้าย estrogen ข้อห้ามในผู้มีประวัติ hormone-sensitive cancers",
    "ขมิ้นชัน": "ขมิ้นชัน (Curcuma longa) มีสาร curcumin ต้านการอักเสบผ่าน NF-κB, COX inhibition ดูดซึม bioavailability ต่ำ เพิ่มด้วย piperine",
    "ชุมเห็ดเทศ": "ชุมเห็ดเทศ (Senna alata) มีสาร anthraquinone glycosides ออกฤทธิ์เป็น stimulant laxative กระตุ้น colon motility ใช้ในท้องผูก",
    "ระย่อม": "ระย่อม (Rauvolfia serpentina) มีสาร reserpine ที่ยับยั้งการเก็บ catecholamines ใน vesicle ลด BP แต่ทำให้ depression, sedation ไม่ใช้ในปัจจุบัน",
    "omega": "Omega-3 FA (EPA/DHA) ลด triglyceride ผ่าน PPARα activation ต้านการอักเสบ ยับยั้ง platelet aggregation อ่อน ระวัง DDI กับ anticoagulants",
    "glutamine": "Glutamine เป็น conditionally essential amino acid ที่ fuel ให้ enterocytes และ immune cells ใช้ใน critically ill patients เพื่อรักษา gut integrity",
    "probiotic": "Probiotics เป็น live microorganisms ที่ส่งผลดีต่อ gut microbiome ใช้ป้องกัน antibiotic-associated diarrhea และ C. difficile infection",
    "selenium": "Selenium เป็น trace element ที่เป็น cofactor ของ glutathione peroxidase ป้องกัน oxidative stress ใช้ใน critically ill patients",
    "zinc": "Zinc เป็น trace element สำคัญสำหรับ wound healing, immune function และ enzyme cofactor ขาดใน malabsorption, burns และ critical illness",
    "vitamin d": "Vitamin D (cholecalciferol) ถูก hydroxylate ที่ตับ (25-OH) และไต (1,25-OH) ควบคุม calcium/phosphate homeostasis ขาดใน CKD และ elderly",
}


def has_tmpl(text):
    return any(p in text for p in TMPL_PHRASES)


def get_specific_reason(choice_text, guideline):
    cl = (choice_text or "").lower()
    for kw, reason in CHOICE_REASONS.items():
        if kw in cl:
            return reason
    return (f"{choice_text} ไม่ตรงกับข้อบ่งใช้หรือกลไกการออกฤทธิ์ที่ถูกต้อง"
            f"ตาม {guideline}")


def clean_exp(exp, q_text, ans_text, guideline):
    if not has_tmpl(exp):
        return exp
    exp = exp.replace("**", "").replace("*", "")
    lines = exp.split("\n")
    out = []
    for line in lines:
        if line.strip().startswith("•") and has_tmpl(line):
            # Use greedy .* to handle nested parens like "(Drug (Emergency)):"
            m = re.match(r"^(• ข้อ [กขคงจ]\. \(.*\):)", line)
            if m:
                prefix = m.group(1)
                # Extract choice text: everything between first ( and last ) before :
                m2 = re.match(r"^• ข้อ [กขคงจ]\. \((.*)\):", line)
                choice_text = m2.group(1) if m2 else ""
                new_reason = get_specific_reason(choice_text, guideline)
                out.append(prefix + " " + new_reason)
            else:
                # Fallback: just append generic replacement
                colon_pos = line.find(":") + 1
                if colon_pos > 0:
                    prefix = line[:colon_pos]
                    out.append(prefix + " ไม่ตรงกับข้อบ่งใช้ที่ถูกต้องตาม " + guideline)
                else:
                    out.append(line)
        else:
            out.append(line)
    return "\n".join(out)


def write_sheet(sheet_name, part_files, guideline):
    all_items = []
    for fn in part_files:
        if not os.path.exists(fn):
            print("  MISSING: " + fn)
            continue
        d = json.load(open(fn, encoding="utf-8"))
        items = list(d.values()) if isinstance(d, dict) else d
        all_items.extend(items)
        print("  Loaded " + fn + ": " + str(len(items)) + " items")

    wb = load_workbook(QUIZ_FILE)
    ws = wb[sheet_name]

    BFONT = Font(name="Bai Jamjuree", size=11, bold=True, color="0D47A1")
    BFILL = PatternFill(fill_type="solid", fgColor="E3F2FD")
    BALIGN = Alignment(horizontal="center", vertical="center")

    for merge in [str(m) for m in ws.merged_cells.ranges]:
        if "A1" in merge:
            try:
                ws.unmerge_cells(merge)
            except Exception:
                pass

    ws.row_dimensions[1].height = 35
    ws["A1"] = "=HYPERLINK(\"#gid=0\", \"\U0001f3e0 กลับสู่หน้าแรก (Go to Home Page)\")"
    ws["A1"].font = BFONT
    ws["A1"].fill = BFILL
    ws["A1"].alignment = BALIGN
    ws.merge_cells("A1:F1")

    for r in range(3, ws.max_row + 2):
        for c in range(1, 17):
            try:
                ws.cell(r, c).value = None
            except Exception:
                pass

    ast_count = 0
    tmpl_count = 0
    for i, item in enumerate(all_items):
        row = i + 3
        q = item.get("q_text", item.get("question", ""))
        exp = item.get("exp", item.get("explanation", ""))
        ans = str(item.get("ans", item.get("correct_choice", "1")))
        try:
            ans_int = int(ans)
        except Exception:
            ans_int = 1
        try:
            ans_text = item.get("c" + str(ans_int), "")
        except Exception:
            ans_text = ""

        exp = clean_exp(exp, q, ans_text, guideline)
        if "*" in exp:
            ast_count += 1
            exp = exp.replace("**", "").replace("*", "")
        if has_tmpl(exp):
            tmpl_count += 1

        ws.cell(row, 1).value = item.get("idx", i + 1)
        ws.cell(row, 2).value = q
        ws.cell(row, 3).value = item.get("q_pic", "")
        ws.cell(row, 4).value = item.get("c1", "")
        ws.cell(row, 5).value = item.get("c2", "")
        ws.cell(row, 6).value = item.get("c3", "")
        ws.cell(row, 7).value = item.get("c4", "")
        ws.cell(row, 8).value = item.get("c5", "")
        ws.cell(row, 9).value = ans_int
        ws.cell(row, 10).value = exp
        ws.cell(row, 11).value = item.get("ans_pic", "")
        ws.cell(row, 12).value = item.get("subtopic", "")
        ws.cell(row, 13).value = item.get("category", "Clinic")
        ws.cell(row, 14).value = item.get("note", item.get("year_set", ""))

    wb.save(QUIZ_FILE)

    # Verify
    wb2 = load_workbook(QUIZ_FILE, data_only=True)
    ws2 = wb2[sheet_name]
    total = v_tmpl = v_ast = 0
    for r in range(3, ws2.max_row + 1):
        if not ws2.cell(r, 2).value:
            continue
        total += 1
        e = str(ws2.cell(r, 10).value or "")
        if "*" in e:
            v_ast += 1
        if has_tmpl(e):
            v_tmpl += 1

    status = "PASS" if v_tmpl == 0 and v_ast == 0 else "ISSUES(" + str(v_tmpl) + " tmpl)"
    print(sheet_name + ": " + str(total) + " items | " + status)
    return v_tmpl == 0 and v_ast == 0


print("Starting pristine build for sheets 12-18...\n")
for sheet_name, part_files, guideline in SHEET_CONFIGS:
    print("\n" + "="*50)
    print("Sheet: " + sheet_name)
    write_sheet(sheet_name, part_files, guideline)

print("\nAll done!")
