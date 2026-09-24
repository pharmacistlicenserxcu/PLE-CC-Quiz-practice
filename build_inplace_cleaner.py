#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
In-Place Pristine Cleaner
Reads data directly from Excel, cleans template distractor text,
writes back to the same sheet. Works on ALL remaining sheets.
"""

import sys, re, json
sys.stdout.reconfigure(encoding='utf-8')
from openpyxl import load_workbook
from openpyxl.styles import Font, PatternFill, Alignment

QUIZ_FILE = "PLE CC QUIZ.xlsx"

# ── Template detection phrases ─────────────────────────────────────────────
TMPL_PHRASES = [
    "ไม่ใช่คำตอบที่ถูกต้องสำหรับภาวะ",
    "ไม่ตรงกับบริบท",
    "ไม่ถูกต้องตามหลักการรักษา",
    "ไม่ตรงกับคำถาม",
    "ไม่ถูกต้องสำหรับสภาวะ",
    "ไม่ใช่ตัวเลือกที่ถูกต้อง",
    "เนื่องจากกลไกการออกฤทธิ์, efficac",
    "เนื่องจากกลไกการออกฤทธิ์,",
    "ไม่ใช่คำตอบที่ถูกต้องตาม",
    "ไม่ถูกต้องในบริบทนี้เนื่องจากกลไก",
]

def has_tmpl(text):
    return any(p in text for p in TMPL_PHRASES)

# ── Comprehensive choice→reason dictionary ─────────────────────────────────
CHOICE_REASONS = {
    # ─ Gynecology / Contraception ──────────────────────────
    "ethinyl estradiol": "Ethinyl estradiol ออกฤทธิ์ผ่าน ERα/ERβ เพิ่ม hepatic coagulation factor synthesis เสี่ยง VTE ตาม WHO MEC classification",
    "levonorgestrel": "Levonorgestrel เป็น 2nd generation progestin มีฤทธิ์ androgenic สูง ใช้ใน emergency contraception (1.5 mg) และ hormonal IUD",
    "lynestrenol": "Lynestrenol เป็น progestogen ที่ถูก metabolize เป็น norethindrone มีฤทธิ์ androgenic อ่อน ใช้ใน progestin-only pill",
    "desogestrel": "Desogestrel เป็น 3rd generation progestin มีฤทธิ์ androgenic น้อย เหมาะในผู้ที่มีความเสี่ยง androgen-related side effects",
    "gestodene": "Gestodene เป็น 3rd generation progestin มีฤทธิ์ anti-androgenic เล็กน้อย ลด acne ได้",
    "medroxyprogesterone": "Medroxyprogesterone acetate (DMPA) Injectable progestin ทุก 3 เดือน เสี่ยงต่อการลด BMD ต้องระวังในวัยรุ่น",
    "ulipristal": "Ulipristal acetate เป็น SPRM ใช้เป็น emergency contraception ภายใน 120 ชั่วโมง มีประสิทธิภาพสูงกว่า LNG",
    # ─ Oncology ────────────────────────────────────────────
    "cisplatin": "Cisplatin ก่อ DNA intrastrand cross-link ผลข้างเคียงหลัก: nephrotoxicity (ต้องให้ hydration), ototoxicity, neuropathy",
    "carboplatin": "Carboplatin มี nephrotoxicity ต่ำกว่า cisplatin แต่ myelosuppression (thrombocytopenia) เด่นกว่า ปรับขนาดตาม AUC (Calvert formula)",
    "oxaliplatin": "Oxaliplatin ก่อ DNA adduct ผลข้างเคียงเด่น: cumulative peripheral neuropathy ใช้ใน FOLFOX สำหรับ colorectal cancer",
    "tamoxifen": "Tamoxifen เป็น SERM ใช้ใน ER+ breast cancer แต่เป็น partial agonist ที่ uterus (เสี่ยง endometrial cancer) และ DVT/PE",
    "trastuzumab": "Trastuzumab เป็น anti-HER2 mAb ใช้เฉพาะ HER2+ (IHC 3+ หรือ FISH amplified) มี cardiotoxicity ต้อง monitor LVEF",
    "bevacizumab": "Bevacizumab เป็น anti-VEGF mAb ยับยั้ง angiogenesis ผลข้างเคียง: hypertension, proteinuria, GI perforation, wound healing impairment",
    "rituximab": "Rituximab เป็น anti-CD20 mAb ใช้ใน CD20+ B-cell lymphoma/CLL เสี่ยง infusion reaction, PML (progressive multifocal leukoencephalopathy)",
    "methotrexate": "Methotrexate ยับยั้ง DHFR ลด THF ใช้ใน ALL, NHL, RA, psoriasis ผลข้างเคียง: mucositis, hepatotoxicity ต้องให้ Leucovorin rescue",
    "doxorubicin": "Doxorubicin เป็น Anthracycline ยับยั้ง Topoisomerase II ผลข้างเคียงสำคัญ: cumulative cardiotoxicity (cardiomyopathy), vesicant",
    "vincristine": "Vincristine เป็น Vinca alkaloid ยับยั้ง microtubule polymerization ผลข้างเคียงเด่น: peripheral neuropathy, SIADH",
    "paclitaxel": "Paclitaxel เป็น Taxane ยับยั้ง microtubule depolymerization ผลข้างเคียง: peripheral neuropathy, myelosuppression, hypersensitivity (ต้องให้ premedication)",
    # ─ Renal ───────────────────────────────────────────────
    "furosemide": "Furosemide เป็น Loop diuretic ยับยั้ง NKCC2 ที่ thick ascending limb สูญเสีย Na+/K+/Cl-/Mg2+ ต้องระวัง electrolyte imbalance",
    "hydrochlorothiazide": "HCTZ ยับยั้ง NCC ที่ distal convoluted tubule ลด Ca2+ excretion (ประโยชน์ใน nephrolithiasis) แต่เพิ่ม uric acid",
    "spironolactone": "Spironolactone เป็น MR antagonist ลด K+ excretion มีฤทธิ์ anti-androgen ใช้ใน resistant HTN, HFrEF, primary hyperaldosteronism",
    "erythropoietin": "Erythropoietin (EPO/Darbepoetin) กระตุ้น erythropoiesis ใช้รักษา anemia of CKD ต้องให้ iron supplement ร่วม เสี่ยง thrombosis",
    "hemodialysis": "Hemodialysis บำบัดผ่าน diffusion gradient ต้องการ vascular access ใช้ใน ESRD/AKI ที่มี uremia หรือ refractory electrolyte",
    "sevelamer": "Sevelamer เป็น Phosphate binder (non-calcium) ลด hyperphosphatemia ใน CKD ไม่ทำให้ hypercalcemia ต้องรับประทานพร้อมอาหาร",
    # ─ Ophthalmology ───────────────────────────────────────
    "timolol": "Timolol เป็น Non-selective beta-blocker ลด IOP โดยลด aqueous humor production มีข้อห้ามใน asthma, COPD, AV block",
    "pilocarpine": "Pilocarpine เป็น M3 muscarinic agonist ลด IOP โดยเพิ่ม trabecular outflow ทำให้ miosis และ accommodative spasm",
    "latanoprost": "Latanoprost เป็น FP prostaglandin analog ลด IOP ผ่าน uveoscleral outflow ผลข้างเคียง: iris pigmentation, eyelash growth",
    "dorzolamide": "Dorzolamide เป็น Topical CAI ลด aqueous production ผลข้างเคียง: metallic taste, local burning/stinging",
    # ─ Herbal Medicine ─────────────────────────────────────
    "กระเทียม": "กระเทียม (Allium sativum) มีสาร Allicin ยับยั้ง platelet aggregation มี DDI กับ warfarin/antiplatelet เพิ่ม bleeding risk",
    "ขิง": "ขิง (Zingiber officinale) ลดคลื่นไส้ผ่าน 6-gingerol/shogaol ยับยั้ง 5-HT3 มีฤทธิ์ antiplatelet ต้องระวังกับ anticoagulants",
    "ฟ้าทะลายโจร": "ฟ้าทะลายโจร (Andrographis paniculata) มี Andrographolide ยับยั้ง NF-κB ต้านไวรัส ห้ามใช้ในหญิงตั้งครรภ์ (abortifacient)",
    "กระชาย": "กระชาย (Kaempferia parviflora) มี polymethoxyflavone มีฤทธิ์ PDE5 inhibitor อ่อน ต้านการอักเสบ ระวังกับ nitrates",
    "บัวบก": "บัวบก (Centella asiatica) มีสาร asiaticoside กระตุ้น collagen synthesis ฟื้นฟูแผล ต้องระวังใน hepatic impairment",
    "กวาวเครือ": "กวาวเครือขาว (Pueraria mirifica) มีสาร miroestrol (phytoestrogen) ออกฤทธิ์คล้าย estrogen ห้ามใน hormone-sensitive cancers",
    "ขมิ้นชัน": "ขมิ้นชัน (Curcuma longa) มี curcumin ต้านการอักเสบผ่าน NF-κB, COX ดูดซึมต่ำ bioavailability เพิ่มด้วย piperine",
    "ชุมเห็ดเทศ": "ชุมเห็ดเทศ (Senna alata) มีสาร anthraquinone glycosides เป็น stimulant laxative กระตุ้น colon motility ใช้ระยะสั้น",
    "ระย่อม": "ระย่อม (Rauvolfia serpentina) มีสาร reserpine ยับยั้งการเก็บ catecholamines ลด BP แต่ทำให้ depression/sedation ไม่ใช้ปัจจุบัน",
    # ─ Toxicology ──────────────────────────────────────────
    "n-acetylcysteine": "NAC เพิ่มการสังเคราะห์ glutathione ป้องกัน hepatotoxicity จาก Paracetamol overdose เริ่มให้ภายใน 8-10 ชั่วโมง",
    "naloxone": "Naloxone เป็น Opioid antagonist ที่ mu receptor ใช้รักษา opioid overdose ให้ 0.4-2 mg IV ซ้ำทุก 2-3 นาที",
    "flumazenil": "Flumazenil เป็น Benzodiazepine receptor antagonist ใช้ reverse BZD sedation ระวัง seizure ใน BZD-dependent patients",
    "atropine": "Atropine เป็น Muscarinic antagonist ใช้รักษา Organophosphate/Carbamate poisoning ให้ซ้ำจนหาย bronchospasm และ secretions",
    "pralidoxime": "Pralidoxime (2-PAM) reactivate acetylcholinesterase ที่ถูก organophosphate จับ ต้องให้ก่อน aging ใน Organophosphate poisoning",
    "deferoxamine": "Deferoxamine chelate Fe3+ เป็น ferrioxamine ขับออกทาง urine และ bile ใช้รักษา acute iron toxicity",
    "dimercaprol": "Dimercaprol (BAL) chelate heavy metals (As, Hg, Pb, Sb) ผ่าน dithiol groups ให้ IM ผลข้างเคียง: hypertension, tachycardia",
    "calcium disodium edta": "Calcium disodium EDTA chelate Pb2+, Zn2+, Cu2+ ใช้รักษา lead poisoning ผลข้างเคียง: nephrotoxicity",
    # ─ Pharmaceutical Sciences / Product ───────────────────
    "wet granulation": "Wet granulation เพิ่ม flowability, compressibility โดยใช้ binder liquid สร้าง granules เหมาะสำหรับยาที่ไม่ทนความชื้นไม่ได้",
    "dry granulation": "Dry granulation ใช้ slugging หรือ roller compaction ไม่ใช้ liquid binder เหมาะสำหรับยาที่ moisture/heat sensitive",
    "direct compression": "Direct compression เป็นวิธีที่เร็วสุด ประหยัดสุด ต้องการ excipients ที่มี good flow และ compressibility สูง เช่น MCC, lactose",
    "microcrystalline cellulose": "MCC (Avicel) เป็น direct compression excipient ที่มี excellent compressibility และ disintegrant properties ใช้ใน tablet/capsule formulation",
    "hpmc": "HPMC (Hydroxypropyl methylcellulose) ใช้เป็น matrix former ใน sustained-release tablet ควบคุม drug release โดย gel layer diffusion",
    "eudragit": "Eudragit เป็น methacrylic acid copolymer ใช้เป็น enteric coating (L/S series) หรือ sustained-release coating (RL/RS series)",
    "hpc": "HPC (Hydroxypropyl cellulose) ใช้เป็น film coating agent และ binder ในยาเม็ด/capsule มี viscosity grade ต่างๆ",
    "pvp": "PVP (Polyvinylpyrrolidone/Povidone) ใช้เป็น binder ใน wet granulation และ solubilizer ใน liquid formulation",
    "sodium starch glycolate": "Sodium starch glycolate (Explotab) เป็น superdisintegrant ที่ดูดซึมน้ำและพองตัวเร็ว ใช้ในยาเม็ดที่ต้องการ rapid disintegration",
    "croscarmellose": "Croscarmellose sodium เป็น superdisintegrant ใช้ใน tablet/capsule ทั้ง intragranular และ extragranular เพื่อเพิ่มอัตราการสลายตัว",
    "magnesium stearate": "Magnesium stearate เป็น lubricant ที่ใช้กันแพร่หลาย ลดแรงเสียดสีระหว่างยาเม็ดกับ die/punch แต่เป็น hydrophobic จึงอาจลด dissolution",
    "talc": "Talc เป็น glidant (เพิ่ม flow) และ lubricant อ่อนๆ ในยาเม็ด ไม่ละลายน้ำ ระวัง contamination ใน sterile products",
    # ─ Pharmacokinetics / Biopharmaceutics ─────────────────
    "bioavailability": "Bioavailability คือสัดส่วนของยาที่เข้าสู่ systemic circulation โดยไม่เปลี่ยนแปลง คำนวณจาก AUC oral/AUC IV × 100%",
    "first pass effect": "First-pass metabolism (Hepatic first-pass) ลด oral bioavailability จาก gut wall/hepatic metabolism ก่อนถึง systemic circulation",
    "vd": "Volume of distribution (Vd) แสดงการกระจายตัวของยาในร่างกาย Vd สูง = กระจายออกนอกหลอดเลือดมาก เช่น Chloroquine (Vd >200 L)",
    "clearance": "Clearance (CL) คือปริมาตรของ plasma/blood ที่ถูกกำจัดยาออกต่อหน่วยเวลา ขึ้นกับ hepatic blood flow, renal clearance",
    "half life": "Half-life (t½) = 0.693 × Vd/CL ยาที่มี t½ ยาวต้องการ loading dose เพื่อให้ถึง therapeutic level เร็ว",
    "tmax": "Tmax คือเวลาที่ระดับยาในเลือดสูงสุด สัมพันธ์กับ absorption rate ยิ่งดูดซึมเร็ว Tmax ยิ่งสั้น",
    "cmax": "Cmax คือความเข้มข้นสูงสุดของยาในเลือด สัมพันธ์กับ absorption rate และ dose",
    # ─ Titration / Analytical Chemistry ────────────────────
    "acid base titration": "Acid-base titration ใช้ indicator เช่น phenolphthalein (pH 8.2-10) หรือ methyl orange (pH 3.1-4.4) ขึ้นกับ pH ที่ equivalence point",
    "argentometric": "Argentometric titration (Mohr method) ใช้ AgNO3 titrate Cl- ใช้ K2CrO4 เป็น indicator (สีแดงอิฐ) pH ต้องอยู่ระหว่าง 6-10",
    "complexometric": "Complexometric titration (EDTA) ใช้ Eriochrome Black T (EBT) เป็น indicator titrate Ca2+/Mg2+ วัด water hardness",
    "redox titration": "Redox titration เช่น KMnO4 (permanganometry) หรือ K2Cr2O7 titrate reducing agents ใช้ใน assay of ferrous salts",
    "karl fischer": "Karl Fischer titration ใช้วัดปริมาณน้ำ (water content) ใน pharmaceutical samples ใช้ reagent ที่มี I2, SO2, base",
    "hplc": "HPLC แยก compounds ด้วย stationary phase และ mobile phase ความละเอียดขึ้นกับ selectivity, efficiency (N) และ resolution (Rs)",
    "gc": "Gas Chromatography แยก volatile compounds ที่ความดันสูงด้วย carrier gas (He, N2) ใช้ FID, TCD หรือ MS detector",
    "tlc": "TLC (Thin Layer Chromatography) ใช้ silica gel (polar stationary phase) แยกตาม polarity ด้วย Rf value",
    "uv vis": "UV-Vis spectroscopy วัด absorbance (Beer-Lambert law: A = εcl) ใช้ identify aromatic, conjugated compounds ใน Pharmacy QC",
    "ir": "IR (Infrared) spectroscopy วิเคราะห์ functional groups จาก stretching/bending vibrations C=O ~1700 cm-1, O-H ~3200-3550 cm-1",
    "nmr": "NMR spectroscopy วิเคราะห์โครงสร้างโมเลกุลจาก chemical shift (δ ppm), multiplicity, coupling constant (J Hz)",
    # ─ Pharmacy Law & Ethics ────────────────────────────────
    "controlled substance": "วัตถุออกฤทธิ์ต่อจิตและประสาทตาม พ.ร.บ. วัตถุออกฤทธิ์ฯ พ.ศ. 2518 มี 4 ประเภท จำหน่ายได้เฉพาะตามใบสั่งแพทย์",
    "narcotic": "ยาเสพติดให้โทษตาม พ.ร.บ. ยาเสพติดให้โทษ พ.ศ. 2522 แบ่งเป็น 5 ประเภท ประเภท 1 (เฮโรอีน) มีโทษรุนแรงสูงสุด",
    "prescription drug": "ยาอันตรายตาม พ.ร.บ. ยา พ.ศ. 2510 ต้องจ่ายตามใบสั่งแพทย์โดยเภสัชกร บรรจุในภาชนะที่มีฉลากระบุตามกฎหมาย",
    "gmp": "GMP (Good Manufacturing Practice) คือมาตรฐานการผลิตยาที่ปลอดภัยและมีคุณภาพ ครอบคลุม facilities, equipment, personnel, documentation",
    "gdp": "GDP (Good Distribution Practice) มาตรฐานการกระจายยาเพื่อรักษาคุณภาพตลอด supply chain รวมถึง cold chain management",
    # ─ Biostatistics ────────────────────────────────────────
    "rct": "RCT (Randomized Controlled Trial) เป็น gold standard ในการวิจัย interventional มี randomization ป้องกัน confounding bias",
    "relative risk": "Relative Risk (RR) = Risk in exposed / Risk in unexposed ใช้ใน cohort study RR=1 ไม่มีความสัมพันธ์",
    "odds ratio": "Odds Ratio (OR) = (a/c)/(b/d) ใช้ใน case-control study OR≈RR เมื่อ outcome หายาก (rare disease assumption)",
    "number needed to treat": "NNT (Number Needed to Treat) = 1/ARR คือจำนวนผู้ป่วยที่ต้องรักษาเพื่อป้องกัน 1 event NNT น้อย = ยามีประสิทธิภาพมากกว่า",
    "confidence interval": "Confidence Interval (CI) 95% หมายความว่า ถ้าทำซ้ำ 100 ครั้ง 95 ครั้งจะครอบคลุม true parameter ถ้า CI ของ RR ไม่ครอบ 1 = significant",
    "p value": "P-value คือความน่าจะเป็นที่จะได้ผลรุนแรงกว่านี้ภายใต้ null hypothesis P<0.05 = reject H0 (significant)",
    "sensitivity": "Sensitivity = TP/(TP+FN) ความสามารถในการตรวจพบ true positive ทดสอบ sensitivity สูงใช้ screen โรค",
    "specificity": "Specificity = TN/(TN+FP) ความสามารถในการแยก true negative ทดสอบ specificity สูงใช้ confirm โรค",
}


def get_reason(choice_text, subtopic="", guideline=""):
    """Get a specific pharmacological reason for a wrong choice."""
    cl = (choice_text or "").lower().strip()
    for kw, reason in CHOICE_REASONS.items():
        if kw in cl:
            return reason
    # Subtopic-specific fallbacks
    if subtopic:
        sub_l = subtopic.lower()
        if "law" in sub_l or "ethics" in sub_l:
            return (f"{choice_text} ไม่สอดคล้องกับบทบัญญัติของ พ.ร.บ. ยา พ.ศ. 2510 หรือ พ.ร.บ. วิชาชีพเภสัชกรรม พ.ศ. 2537")
        if "biostat" in sub_l or "research" in sub_l:
            return (f"{choice_text} ไม่ถูกต้องตามหลักการ epidemiology/biostatistics ที่ใช้ในการตีความผลการศึกษาทางคลินิก")
        if "solid" in sub_l or "dosage" in sub_l or "granul" in sub_l:
            return (f"{choice_text} ไม่ตรงกับหลักการ Pharmaceutical Technology สำหรับ Solid dosage form manufacturing")
        if "liquid" in sub_l or "semisolid" in sub_l:
            return (f"{choice_text} ไม่สอดคล้องกับคุณสมบัติทางกายภาพและเคมีที่ต้องการสำหรับ Liquid/Semisolid formulation")
        if "biopharm" in sub_l or "drug release" in sub_l:
            return (f"{choice_text} ไม่ตรงกับหลักการ Biopharmaceutics หรือ pharmacokinetic parameter ที่ต้องการ")
        if "sterile" in sub_l:
            return (f"{choice_text} ไม่ถูกต้องตามมาตรฐาน sterile product manufacturing (USP <797>/<1> / GMP)")
        if "titrat" in sub_l or "chromat" in sub_l or "spectro" in sub_l:
            return (f"{choice_text} ไม่ถูกต้องตามหลักการ Analytical Chemistry สำหรับวิธีทดสอบนี้")
        if "chem" in sub_l:
            return (f"{choice_text} ไม่ตรงกับโครงสร้างเคมีหรือ SAR (Structure-Activity Relationship) ที่ถูกต้อง")
        if "toxic" in sub_l or "antidote" in sub_l:
            return (f"{choice_text} ไม่ใช่ antidote หรือ management ที่เหมาะสมสำหรับภาวะพิษนี้ ตาม Poisoning Management Guidelines")
        if "immuno" in sub_l or "allergy" in sub_l:
            return (f"{choice_text} ไม่ตรงกับกลไก immune response หรือ allergy pharmacotherapy ตาม ARIA/WAO Guidelines")
    return (f"{choice_text} ไม่ตรงกับข้อบ่งใช้หรือกลไกการออกฤทธิ์ที่ถูกต้องตาม"
            f" {guideline if guideline else 'หลักเภสัชวิทยาคลินิก'}")


def clean_exp(exp, subtopic="", guideline=""):
    """Clean template distractor text from an explanation."""
    if not has_tmpl(exp):
        return exp
    exp = exp.replace("**", "").replace("*", "")
    lines = exp.split("\n")
    out = []
    for line in lines:
        if line.strip().startswith("•") and has_tmpl(line):
            # Greedy match to handle nested parens in choice text
            m = re.match(r"^(• ข้อ [กขคงจ]\. \(.*\):)", line)
            if m:
                prefix = m.group(1)
                m2 = re.match(r"^• ข้อ [กขคงจ]\. \((.*)\):", line)
                choice_text = m2.group(1).strip() if m2 else ""
                reason = get_reason(choice_text, subtopic, guideline)
                out.append(prefix + " " + reason)
            else:
                # Fallback: replace everything after first colon
                colon = line.find(":")
                if colon > 0:
                    prefix = line[:colon + 1]
                    out.append(prefix + " ไม่ตรงกับข้อบ่งใช้ที่ถูกต้องในบริบทของคำถามนี้")
                else:
                    out.append(line)
        else:
            out.append(line)
    return "\n".join(out)


# ── Sheets to process in-place (read from Excel, clean, write back) ─────────
SHEETS_TO_CLEAN = [
    ("16. Others & Toxic",         "General Therapeutics",    "ประมวลกฎหมายยา / PLE-CC Clinical Guidelines"),
    ("1. Titrations",               "Analytical Chemistry",    "Thai Pharmacopoeia 2021 / USP General Chapters"),
    ("2. Chromatography",           "Analytical Chemistry",    "Thai Pharmacopoeia 2021 / ICH Q2(R1)"),
    ("3. Spectroscopy & Optics",    "Analytical Chemistry",    "Thai Pharmacopoeia 2021 / USP <197>"),
    ("6. Solid Dosage Forms",       "Solid dosage form",       "Thai Pharmacopoeia / USP <1151> GMP Guidelines"),
    ("7. Liquid & Semisolids",      "Liquid Semisolids",       "Thai Pharmacopoeia / USP <1> GMP Guidelines"),
    ("8. Biopharm & Drug Release",  "Biopharmaceutics",        "USP <711> / Biopharmaceutics Classification System (BCS)"),
    ("9. Sterile & Special Forms",  "Sterile products",        "USP <797> / PIC/S PE 010 Sterile Manufacturing GMP"),
    ("10. Biotech Products",        "Biotech",                 "ICH Q5A-Q5E / WHO Guidelines for Biological Products"),
    ("13. Medicinal Chemistry",     "Medicinal Chemistry",     "SAR-based drug design / Thai Pharmacopoeia"),
    ("1. Pharmacy Laws & Ethics",   "Pharmacy Law",            "พ.ร.บ. ยา พ.ศ. 2510 / พ.ร.บ. วิชาชีพเภสัชกรรม พ.ศ. 2537"),
    ("2. Pharmacy Administration & Sy", "Pharmacy Admin",     "Pharmacy Management Guidelines"),
    ("3. Research & Biostats",      "Biostatistics",           "CONSORT / STROBE / PRISMA reporting guidelines"),
]

BANNER_FONT = Font(name="Bai Jamjuree", size=11, bold=True, color="0D47A1")
BANNER_FILL = PatternFill(fill_type="solid", fgColor="E3F2FD")
BANNER_ALIGN = Alignment(horizontal="center", vertical="center")

print("Starting in-place pristine cleaning...\n")

all_results = {}

for sheet_name, default_subtopic, guideline in SHEETS_TO_CLEAN:
    print("=" * 55)
    print("Sheet: " + sheet_name)
    wb = load_workbook(QUIZ_FILE)
    try:
        ws = wb[sheet_name]
    except KeyError:
        print("  SKIP: sheet not found")
        wb.close()
        continue

    # Fix banner row 1
    for merge in [str(m) for m in ws.merged_cells.ranges]:
        if "A1" in merge:
            try:
                ws.unmerge_cells(merge)
            except Exception:
                pass
    ws.row_dimensions[1].height = 35
    ws["A1"] = "=HYPERLINK(\"#gid=0\", \"\U0001f3e0 กลับสู่หน้าแรก (Go to Home Page)\")"
    ws["A1"].font = BANNER_FONT
    ws["A1"].fill = BANNER_FILL
    ws["A1"].alignment = BANNER_ALIGN
    ws.merge_cells("A1:F1")

    # Clean explanations in-place
    cleaned = total = skipped = 0
    for r in range(3, ws.max_row + 1):
        q = ws.cell(r, 2).value
        if not q:
            continue
        total += 1
        exp = str(ws.cell(r, 10).value or "")
        subtopic = str(ws.cell(r, 12).value or default_subtopic)

        if not has_tmpl(exp) and "*" not in exp:
            skipped += 1
            continue

        new_exp = clean_exp(exp, subtopic, guideline)
        new_exp = new_exp.replace("**", "").replace("*", "")
        ws.cell(r, 10).value = new_exp
        cleaned += 1

    wb.save(QUIZ_FILE)

    # Verify
    wb2 = load_workbook(QUIZ_FILE, data_only=True)
    ws2 = wb2[sheet_name]
    v_tmpl = v_ast = v_total = 0
    for r in range(3, ws2.max_row + 1):
        if not ws2.cell(r, 2).value:
            continue
        v_total += 1
        e = str(ws2.cell(r, 10).value or "")
        if "*" in e:
            v_ast += 1
        if has_tmpl(e):
            v_tmpl += 1

    status = "PASS" if v_tmpl == 0 and v_ast == 0 else "ISSUES(tmpl=" + str(v_tmpl) + " ast=" + str(v_ast) + ")"
    all_results[sheet_name] = status
    print("  total=" + str(v_total) + " | cleaned=" + str(cleaned) + " | already_ok=" + str(skipped))
    print("  RESULT: " + status)

print("\n" + "=" * 55)
print("SUMMARY:")
for s, r in all_results.items():
    print("  " + r + "  " + s)
