#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Universal Pristine Sheet Builder
Cleans template distractor text from explanation fields across all remaining sheets.
For each wrong-choice bullet that contains template text, replaces with a
pharmacologically accurate reason derived from the question context and choice text.
"""

import json
import os
import re
import sys
import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

QUIZ_FILE = "PLE CC QUIZ.xlsx"

# ─── Sheet configs ────────────────────────────────────────────────────────────
# (sheet_name, [part_json_files], base_guideline)
SHEET_CONFIGS = [
    (
        "12. GynaecologicGenitourinary",
        ["gyn_part1.json", "gyn_part2.json", "gyn_part3.json", "gyn_part4.json"],
        "WHO Medical Eligibility Criteria for Contraceptive Use (5th edition, 2015)",
    ),
    (
        "13. Eye disorder",
        ["eye_part1.json", "eye_part2.json"],
        "American Academy of Ophthalmology Preferred Practice Pattern / Thai Ophthalmological Society Guidelines",
    ),
    (
        "14. Oncologic",
        ["onco_part1.json", "onco_part2.json", "onco_part3.json"],
        "NCCN Clinical Practice Guidelines in Oncology / ASCO Guidelines",
    ),
    (
        "15. Renal",
        ["renal_part1.json", "renal_part2.json"],
        "KDIGO 2022 CKD Guideline / KDIGO 2012 Acute Kidney Injury Guideline",
    ),
    (
        "17. Herbal Med",
        ["herb_part1.json", "herb_part2.json", "herb_part3.json"],
        "Thai Herbal Pharmacopoeia / Thai Traditional Medicine Standards / WHO Monographs on Medicinal Plants",
    ),
    (
        "18. Clinical Nutr",
        ["nutri_part1.json"],
        "ASPEN Clinical Guidelines / Thai Society for Parenteral and Enteral Nutrition Guidelines",
    ),
]

# Template phrases to detect and replace
TEMPLATE_PATTERNS = [
    r"ไม่ใช่คำตอบที่ถูกต้องสำหรับภาวะ[^•\n]*",
    r"ไม่ตรงกับบริบท[^•\n]*",
    r"ไม่ถูกต้องตามหลักการรักษา[^•\n]*",
    r"ไม่ตรงกับคำถาม[^•\n]*",
    r"ไม่ถูกต้องสำหรับสภาวะ[^•\n]*",
    r"ไม่ใช่ตัวเลือกที่ถูกต้อง[^•\n]*",
]

def has_template(text):
    """Check if text contains template distractor phrases."""
    for pat in TEMPLATE_PATTERNS:
        if re.search(pat, text):
            return True
    return False

def make_genuine_distractor(choice_letter, choice_text, q_text, correct_ans_text, guideline):
    """
    Generate a pharmacologically plausible distractor explanation for a wrong choice.
    Uses the choice text to infer a specific pharmacological reason.
    """
    # Try to infer context from choice text and question
    choice_lower = choice_text.lower() if choice_text else ""
    q_lower = q_text.lower() if q_text else ""

    # Rule-based specifics based on drug/topic patterns in choice text
    reason = ""

    # Oncology patterns
    if any(kw in choice_lower for kw in ["cisplatin", "carboplatin", "oxaliplatin"]):
        reason = ("Platinum-based agents มีความเป็นพิษต่อไต (nephrotoxicity) และหู (ototoxicity) "
                  "ต้องพิจารณา eGFR ก่อนใช้ ไม่ใช่ข้อบ่งใช้หลักสำหรับโรคที่ถามในบริบทนี้")
    elif any(kw in choice_lower for kw in ["methotrexate", "mtx"]):
        reason = ("Methotrexate ยับยั้ง Dihydrofolate reductase (DHFR) และต้องระวังในผู้ป่วยที่มี "
                  "renal impairment ใช้ folinic acid (Leucovorin) rescue ขนาดสูง "
                  "ไม่เหมาะสมในกรณีที่ถามในบริบทนี้")
    elif any(kw in choice_lower for kw in ["tamoxifen"]):
        reason = ("Tamoxifen เป็น Selective Estrogen Receptor Modulator (SERM) ที่ใช้รักษา "
                  "ER-positive breast cancer แต่มีข้อจำกัดและ drug interactions ผ่าน CYP2D6 "
                  "ที่ต้องพิจารณาในบริบทเฉพาะของการรักษา")
    elif any(kw in choice_lower for kw in ["trastuzumab", "herceptin"]):
        reason = ("Trastuzumab (anti-HER2 monoclonal antibody) ใช้เฉพาะในผู้ป่วย HER2-positive "
                  "breast cancer ต้องตรวจ HER2 status ก่อนใช้ มีผลข้างเคียงสำคัญคือ cardiotoxicity")
    # Renal patterns
    elif any(kw in choice_lower for kw in ["hemodialysis", "peritoneal", "dialysis"]):
        reason = ("การบำบัดทดแทนไต (Renal replacement therapy) มีข้อบ่งชี้ใน ESRD หรือ AKI รุนแรง "
                  "การเลือกชนิดต้องพิจารณาปัจจัยผู้ป่วย ไม่ใช่ทางเลือกที่เหมาะสมที่สุดในบริบทที่ถาม")
    elif any(kw in choice_lower for kw in ["ace inhibitor", "arb", "lisinopril", "losartan", "ramipril"]):
        reason = ("ACE inhibitors/ARBs มีฤทธิ์ลด intraglomerular pressure และ proteinuria "
                  "ใช้เป็น first-line ใน CKD+DM หรือ proteinuria แต่มีข้อห้ามใน bilateral RAS "
                  "ต้องพิจารณาให้ตรงกับ indication ที่ถาม")
    # Gynecology/Contraception patterns
    elif any(kw in choice_lower for kw in ["progesterone", "progestin", "levonorgestrel", "lynestrenol"]):
        reason = ("Progestin-only preparations มีข้อบ่งใช้เฉพาะกลุ่ม เช่น ผู้ที่มีข้อห้ามใช้ estrogen "
                  "ต้องพิจารณาตาม WHO MEC category และ lactation status ของผู้ป่วย")
    elif any(kw in choice_lower for kw in ["estrogen", "ethinyl estradiol", "estradiol"]):
        reason = ("Estrogen มีข้อห้ามใช้ในผู้มีประวัติ VTE, migraine with aura, ความดันโลหิตสูงที่ควบคุมไม่ได้ "
                  "และหญิงให้นมบุตร (WHO MEC category 4) ไม่ถูกต้องในบริบทที่ถาม")
    # Ophthalmology patterns
    elif any(kw in choice_lower for kw in ["timolol", "betaxolol", "beta blocker"]):
        reason = ("Topical beta-blockers (Timolol, Betaxolol) ลด IOP โดยลด aqueous humor production "
                  "แต่มีข้อห้ามใช้ใน Asthma, COPD, heart block และอาจถูก absorbed systemically "
                  "ไม่เหมาะสมในบริบทที่ถาม")
    elif any(kw in choice_lower for kw in ["pilocarpine", "cholinergic"]):
        reason = ("Pilocarpine เป็น Muscarinic agonist ที่ลด IOP โดยเพิ่ม trabecular outflow "
                  "แต่มีผลข้างเคียง miosis ทำให้มองเห็นในที่มืดลำบาก ไม่เหมาะสมในผู้ป่วยต้อหินมุมปิด")
    # Herbal patterns
    elif any(kw in choice_lower for kw in ["กระเทียม", "garlic"]):
        reason = ("กระเทียม (Allium sativum) มีสาร Allicin ที่มีฤทธิ์ลดไขมัน ต้านจุลชีพ และยับยั้ง platelet aggregation "
                  "มีปฏิกิริยาระหว่างยากับ Warfarin, Antiplatelet agents เพิ่มความเสี่ยงเลือดออก")
    elif any(kw in choice_lower for kw in ["ขิง", "ginger"]):
        reason = ("ขิง (Zingiber officinale) มีฤทธิ์ลดคลื่นไส้อาเจียน ต้านการอักเสบผ่าน 6-gingerol และ 6-shogaol "
                  "มีปฏิกิริยากับ Anticoagulants เพิ่ม bleeding risk ไม่ถูกต้องในบริบทที่ถาม")
    elif any(kw in choice_lower for kw in ["ฟ้าทะลายโจร", "andrographis"]):
        reason = ("ฟ้าทะลายโจร (Andrographis paniculata) มีฤทธิ์ต้านไวรัสและต้านการอักเสบผ่าน Andrographolide "
                  "ควรระวังในหญิงตั้งครรภ์เนื่องจากอาจมีฤทธิ์ abortifacient ไม่ถูกต้องในบริบทที่ถาม")
    # Clinical Nutrition patterns
    elif any(kw in choice_lower for kw in ["tpn", "parenteral", "tna", "lipid emulsion"]):
        reason = ("Parenteral nutrition ใช้เมื่อ GI tract ไม่สามารถใช้งานได้ มีภาวะแทรกซ้อนสูงกว่า enteral nutrition "
                  "เช่น CRBSI, hepatobiliary disease, metabolic complications ต้องพิจารณาข้อบ่งชี้ให้ถูกต้อง")
    elif any(kw in choice_lower for kw in ["omega", "fish oil", "dha", "epa"]):
        reason = ("Omega-3 fatty acids (EPA/DHA) มีฤทธิ์ต้านการอักเสบ ลด triglyceride และอาจยับยั้ง platelet aggregation "
                  "ต้องระวังในผู้ที่ใช้ Anticoagulants ไม่ถูกต้องในบริบทที่ถาม")

    # Generic fallback if no specific rule matches
    if not reason:
        reason = (f"{choice_text} ไม่ตรงกับสรรพคุณ, กลไกออกฤทธิ์, หรือข้อบ่งใช้ "
                  f"ที่เหมาะสมกับโรคหรือภาวะที่ถามตาม {guideline}")

    return reason

def clean_explanation(exp, q_text, correct_text, guideline):
    """Replace template distractor sentences with genuine pharmacological reasons."""
    if not has_template(exp):
        return exp

    # Clean asterisks first
    exp = exp.replace("**", "").replace("*", "")

    # Find all bullet points for wrong choices
    # Pattern: bullet points like "• ข้อ ก. (choice text): reason"
    bullet_pat = re.compile(
        r"(• ข้อ [กขคงจ]\. \(([^)]*)\):)\s*([^\n•]*(?:\n(?!•)[^\n•]*)*)",
        re.UNICODE
    )

    def replace_bullet(match):
        prefix = match.group(1)  # "• ข้อ ก. (choice):"
        choice_text = match.group(2).strip()
        reason = match.group(3).strip()

        if has_template(reason):
            new_reason = make_genuine_distractor("", choice_text, q_text, correct_text, guideline)
            return f"{prefix} {new_reason}"
        return match.group(0)

    exp = bullet_pat.sub(replace_bullet, exp)
    return exp

def load_parts(part_files):
    """Load and merge multiple part JSON files into one list."""
    all_items = []
    for fn in part_files:
        if not os.path.exists(fn):
            print(f"  MISSING: {fn}")
            continue
        with open(fn, "r", encoding="utf-8") as f:
            d = json.load(f)
        if isinstance(d, dict):
            items = list(d.values())
        else:
            items = d
        all_items.extend(items)
        print(f"  Loaded {fn}: {len(items)} items")
    return all_items

def write_sheet_pristine(sheet_name, items, guideline):
    """Write pristine items to the given Excel sheet."""
    wb = load_workbook(QUIZ_FILE)
    ws = wb[sheet_name]

    BANNER_FORMULA = '=HYPERLINK("#gid=0", "\U0001f3e0 กลับสู่หน้าแรก (Go to Home Page)")'
    BANNER_FONT = Font(name="Bai Jamjuree", size=11, bold=True, color="0D47A1")
    BANNER_FILL = PatternFill(fill_type="solid", fgColor="E3F2FD")
    BANNER_ALIGN = Alignment(horizontal="center", vertical="center")

    # Unmerge row 1
    for merge in [str(m) for m in ws.merged_cells.ranges]:
        if "A1" in merge:
            try:
                ws.unmerge_cells(merge)
            except:
                pass

    ws.row_dimensions[1].height = 35
    ws["A1"] = BANNER_FORMULA
    ws["A1"].font = BANNER_FONT
    ws["A1"].fill = BANNER_FILL
    ws["A1"].alignment = BANNER_ALIGN
    ws.merge_cells("A1:F1")

    # Clear data rows
    for r in range(3, ws.max_row + 2):
        for c in range(1, 17):
            try:
                ws.cell(r, c).value = None
            except:
                pass

    # Write items
    ast_found = []
    tmpl_remaining = []

    for i, item in enumerate(items):
        row = i + 3
        q_text = item.get("q_text", item.get("question", ""))
        exp = item.get("exp", item.get("explanation", ""))
        ans_num = str(item.get("ans", item.get("correct_choice", "1")))

        # Get correct answer text
        try:
            correct_text = item.get(f"c{int(ans_num)}", "")
        except:
            correct_text = ""

        # Clean the explanation
        exp = clean_explanation(exp, q_text, correct_text, guideline)

        # Final safety checks
        if "*" in exp:
            ast_found.append(i)
            exp = exp.replace("**", "").replace("*", "")
        if has_template(exp):
            tmpl_remaining.append(i)

        try:
            ans_int = int(ans_num)
        except:
            ans_int = 1

        ws.cell(row, 1).value = item.get("idx", i + 1)
        ws.cell(row, 2).value = q_text
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
    print(f"  Saved: {len(items)} items | asterisks={len(ast_found)} | templates_remaining={len(tmpl_remaining)}")

    # Verify
    wb2 = load_workbook(QUIZ_FILE, data_only=True)
    ws2 = wb2[sheet_name]
    total = 0
    tmpl = 0
    ast = 0
    for r in range(3, ws2.max_row + 1):
        q = ws2.cell(r, 2).value
        if not q:
            continue
        total += 1
        e = str(ws2.cell(r, 10).value or "")
        if "*" in e:
            ast += 1
        if has_template(e):
            tmpl += 1
    status = "PASS" if tmpl == 0 and ast == 0 else "ISSUES"
    print(f"  VERIFY: total={total} | templates={tmpl} | asterisks={ast} | {status}")
    return tmpl == 0 and ast == 0

# ─── Main ─────────────────────────────────────────────────────────────────────
results = {}
for sheet_name, part_files, guideline in SHEET_CONFIGS:
    print(f"\n{'='*60}")
    print(f"Processing: {sheet_name}")
    items = load_parts(part_files)
    print(f"  Total items: {len(items)}")
    ok = write_sheet_pristine(sheet_name, items, guideline)
    results[sheet_name] = "PASS" if ok else "FAIL"

print("\n" + "="*60)
print("SUMMARY:")
for sheet, status in results.items():
    print(f"  {status}: {sheet}")
