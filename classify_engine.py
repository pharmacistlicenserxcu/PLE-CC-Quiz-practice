import sys
import io
import re
import json

sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

# The 13 Product tabs + Law
PRODUCT_TABS = [
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
    '13. Medicinal Chemistry',
    '1. Pharmacy Laws & Ethics'
]

def classify_product_question(q_text, choices_text, exp_text=""):
    full_text = f"{q_text} {' '.join(choices_text)} {exp_text}".lower()
    
    # 1. Pharmacy Laws & Ethics
    if any(k in full_text for k in ['ขย.11', 'ข.ย.', 'พระราชบัญญัติยา', 'พ.ร.บ.ยา', 'ยาอันตราย', 'ยาควบคุมพิเศษ', 'ยาสามัญประจำบ้าน', 'ใบอนุญาตขายยา', 'ร้านขายส่ง']):
        if not any(k in full_text for k in ['คัดย้าย', 'คำนวณ mEq', 'ไตเตรท', 'hplc']):
            return '1. Pharmacy Laws & Ethics', 'Pharmacy Laws & Ethics'

    # 11. Herbal Products
    if any(k in full_text for k in [
        'สมุนไพร', 'บัญชียาสมุนไพร', 'กัญชา', 'ขมิ้นชัน', 'ฟ้าทะลายโจร', 'รางจืด', 'เถาวัลย์เปรียง',
        'พญายอ', 'บัวบก', 'มะระขี้นก', 'andrographolide', 'curcumin', 'thc', 'cbd', 'สารสกัด',
        'thai herbal pharmacopoeia', 'thp', 'maceration', 'percolation', 'soxhlet', 'decoction'
    ]):
        return '11. Herbal Products', 'Herbal Products & Standardization'

    # 12. Food Products & QA
    if any(k in full_text for k in [
        'อาหารเสริม', 'ผลิตภัณฑ์เสริมอาหาร', 'สารปนเปื้อน', 'วัตถุกันเสีย', 'benzoic', 'sorbic',
        'aflatoxin', 'ฟอร์มาลิน', 'บอแรกซ์', 'สารกันบูด', 'สารฟอกขาว', 'sodium hydrosulfite',
        'ฉลากอาหาร', 'ghp', 'haccp', 'codex', 'มาตรฐานอาหาร', 'วิตามินรวม'
    ]):
        return '12. Food Products & QA', 'Food Products & Quality Assurance'

    # 1. Titrations
    if any(k in full_text for k in [
        'titration', 'titrant', 'karl fischer', 'acid-base titration', 'redox titration',
        'precipitation titration', 'complexometric', 'edta', 'fajans', 'volhard', 'mohr',
        'ceric', 'iodometry', 'iodimetry', 'perchloric', 'non-aqueous titration', 'ไตเตรท'
    ]):
        return '1. Titrations', 'Titrimetric Analysis'

    # 2. Chromatography
    if any(k in full_text for k in [
        'chromatography', 'hplc', 'retention time', 'capacity factor', 'selectivity factor',
        'theoretical plate', 'tailing factor', 'resolution', 'gas chromatography', 'gc-ms',
        'thin layer chromatography', 'tlc', 'rf value', 'stationary phase', 'mobile phase',
        'c18', 'reverse phase', 'normal phase', 'run time'
    ]):
        return '2. Chromatography', 'Chromatographic Analysis'

    # 3. Spectroscopy & Optics
    if any(k in full_text for k in [
        'polarimeter', 'polarimetry', 'specific rotation', 'optical rotation', 'refractive index',
        'refractometer', 'refractometry', 'uv-vis', 'uv ', 'spectrophotometry', 'beer-lambert',
        'absorbance', 'molar absorptivity', 'ir ', 'infrared', 'ftir', 'nmr', 'chemical shift',
        'mass spec', 'mass spectrometry', 'chromophore', 'auxochrome', 'bathochromic'
    ]):
        return '3. Spectroscopy & Optics', 'Spectroscopy & Optical Analysis'

    # 9. Sterile & Special Forms
    if any(k in full_text for k in [
        'sterilization', 'autoclave', 'dry heat', 'moist heat', 'ethylene oxide', 'radiation sterilization',
        'filtration sterilization', '0.22 micron', 'depyrogenation', 'pyrogen', 'bacterial endotoxin',
        'lal test', 'clean room', 'grade a', 'grade b', 'grade c', 'grade d', 'laminar air flow',
        'aseptic', 'eye drop', 'ophthalmic', 'ยาหยอดตา', 'ยาฉีด', 'iv infusion', 'large volume parenterals'
    ]):
        return '9. Sterile & Special Forms', 'Sterile Preparations & Sterilization'

    # 10. Biotech Products
    if any(k in full_text for k in [
        'biotech', 'biologic', 'monoclonal antibody', 'mab', 'biosimilar', 'recombinant',
        'protein aggregation', 'denaturation', 'glycosylation', 'immunogenicity', 'cold chain',
        'vaccine', 'dna', 'rna', 'mrna', 'elisa', 'western blot', 'sds-page', 'filgrastim',
        'erythropoietin', 'infliximab', 'adalimumab', 'trastuzumab'
    ]):
        return '10. Biotech Products', 'Biotechnology & Biological Products'

    # 8. Biopharm & Drug Release
    if any(k in full_text for k in [
        'dissolution', 'noyes-whitney', 'fick', 'diffusion layer', 'bcs class', 'biopharmaceutics',
        'bioavailability', 'bioequivalence', 'cmax', 'tmax', 'auc', 'apparatus 1', 'apparatus 2',
        'basket', 'paddle', 'flow-through cell', 'sink condition', 'f1', 'f2', 'similarity factor',
        'extended-release', 'delayed-release', 'sustained-release'
    ]):
        return '8. Biopharm & Drug Release', 'Biopharmaceutics & Dissolution'

    # 5. Pharmaceutical Calc
    if any(k in full_text for k in [
        'คำนวณ', 'meq', 'mosmol', 'osmolarity', 'tonicity', 'sodium chloride equivalent', 'e-value',
        'displacement factor', 'aliquot', 'dilution factor', 'alligation', 'hlb calculation'
    ]):
        return '5. Pharmaceutical Calc', 'Pharmaceutical Calculations'

    # 7. Liquid & Semisolids
    if any(k in full_text for k in [
        'suspension', 'ยาสารแขวนตะกอน', 'ยาน้ำเชื่อม', 'syrup', 'elixir', 'emulsion', 'ยาอิมัลชัน',
        'cream', 'ยาครีม', 'ointment', 'ยาขี้ผึ้ง', 'gel', 'เจล', 'suppository', 'ยาเหน็บ',
        'carbopol', 'methylcellulose', 'stearic acid', 'triethanolamine', 'viscosity', 'thixotropy',
        'pseudoplastic', 'sedimentation volume', 'flocculated', 'deflocculated', 'hydrophilic-lipophilic'
    ]):
        return '7. Liquid & Semisolids', 'Liquid & Semisolid Dosage Forms'

    # 6. Solid Dosage Forms
    if any(k in full_text for k in [
        'tablet', 'ยาเม็ด', 'capsule', 'แคปซูล', 'granule', 'pellet', 'binder', 'disintegrant',
        'glidant', 'lubricant', 'diluent', 'filler', 'microcrystalline cellulose', 'lactose',
        'magnesium stearate', 'capping', 'lamination', 'sticking', 'picking', 'friability',
        'hardness', 'disintegration time', 'content uniformity', 'weight variation', 'enteric coat'
    ]):
        return '6. Solid Dosage Forms', 'Solid Dosage Forms & Manufacturing'

    # 13. Medicinal Chemistry
    if any(k in full_text for k in [
        'โครงสร้าง', 'structure', 'sar', 'structure-activity', 'prodrug', 'metabolism', 'metabolite',
        'pharmacophore', 'stereochemistry', 'isomer', 'chiral', 'bioisostere', 'pka', 'log p',
        'functional group', 'receptor binding'
    ]):
        return '13. Medicinal Chemistry', 'Medicinal Chemistry & SAR'

    # 4. Preformulation & GMP
    if any(k in full_text for k in [
        'gmp', 'pic/s', 'stability', 'accelerated stability', 'shelf life', 'q10', 'arrhenius',
        'packaging', 'blister', 'strip', 'container', 'closure', 'leachable', 'extractable',
        'cross-contamination', 'hvac', 'qualification', 'validation', 'sop', 'iq', 'oq', 'pq'
    ]):
        return '4. Preformulation & GMP', 'Preformulation & Good Manufacturing Practice'

    # Default fallback
    return '4. Preformulation & GMP', 'Pharmaceutical Technology General'

print("Classification engine defined successfully.")
