import json
import re

exact_dict = {
    "170": {
        "ก": "728 mg/day เป็นปริมาณที่ต่ำกว่าการคำนวณตามสูตร BSA จริง ซึ่งอาจทำให้ได้ขนาดยาแบบ subtherapeutic dose",
        "ข": "748 mg/day เป็นการคำนวณที่ผิดพลาดจากสูตร DuBois หรือ Mosteller ซึ่งไม่ตรงกับค่าน้ำหนักและส่วนสูงของผู้ป่วย",
        "ค": "768 mg/day เป็นค่าที่ได้จากการปัดเศษที่ไม่ถูกต้อง หรือการใช้ค่าน้ำหนักอุดมคติ (IBW) แทนน้ำหนักจริง",
        "ง": "788 mg/day ใกล้เคียงกับคำตอบที่ถูกต้องแต่ยังคงคลาดเคลื่อนจากการถอดรากที่สองของผลคูณน้ำหนักและส่วนสูง"
    },
    "171": {
        "ก": "Docetaxel เป็นยาในกลุ่ม Taxanes ออกฤทธิ์จับกับ Tubulin ส่งเสริมการสร้าง Microtubule แต่ยับยั้งการแยกตัว",
        "ข": "Cytarabine เป็นยาในกลุ่ม Antimetabolites ทำหน้าที่รบกวนเอนไซม์ DNA polymerase เฉพาะในระยะ S phase",
        "ค": "Cisplatin จับกับสาย DNA เกิดเป็น Cross-links รบกวนการถอดรหัส โดยเป็น Cell cycle non-specific agent",
        "จ": "Navelbine หรือ Vinorelbine เป็นยาในกลุ่ม Vinca alkaloids ออกฤทธิ์ยับยั้งการสร้าง Microtubules ป้องกันการแบ่งโครโมโซม"
    },
    "172": {
        "ก": "400 ml. เป็นปริมาตรที่ไม่สอดคล้องกับขนาดยารวม 1400 mg หากผสมจะทำให้ได้ความเข้มข้นที่สูงเกินไป",
        "ค": "440 ml. ทำให้ความเข้มข้นของยาลดลงต่ำกว่าเป้าหมาย 50 mg/tbs ส่งผลให้ผู้ป่วยได้รับยาไม่ครบโดส",
        "ง": "460 ml. เป็นปริมาตรที่เจือจางเกินไป ทำให้ต้องบริหารยาในปริมาตรที่มากขึ้นต่อครั้ง",
        "จ": "480 ml. คำนวณผิดพลาดจากการใช้จำนวนเม็ดยา 56 เม็ดมาคูณกับปัจจัยอื่น แทนที่จะนำปริมาณรวม 1400 mg มาหาร"
    },
    "173": {
        "ก": "Brown mixture มีส่วนผสมของ Opium tincture จัดเป็นยาอันตราย ไม่ใช่วัตถุออกฤทธิ์ต่อจิตและประสาท",
        "ข": "Brown mixture จัดเป็นยาอันตราย สามารถจ่ายโดยเภสัชกรในร้านขายยาแผนปัจจุบันได้โดยไม่ต้องใช้ใบสั่งแพทย์",
        "ค": "ยาในกลุ่มนี้เมื่อพิจารณาในรูปแบบตำรับสามารถขายโดยผู้รับอนุญาตในกรณีที่เป็นยาสามัญประจำบ้านได้",
        "จ": "Brown mixture เป็นยาที่มีส่วนผสมของ Opium tincture ซึ่งมีฤทธิ์กดศูนย์ไอ แต่ไม่ใช่ยาบรรจุเสร็จที่อยู่นอกเหนือกฎหมายยาอันตราย"
    },
    "174": {
        "ก": "Phenylephrine เป็นยากลุ่ม alpha-1 agonist มีฤทธิ์ทำให้หลอดเลือดหดตัว ใช้ลดอาการตาแดง",
        "ข": "Oxymetazoline เป็น alpha-adrenergic agonist ที่ออกฤทธิ์กระตุ้นตัวรับ alpha ทำให้หลอดเลือดที่เยื่อบุตาหดตัว",
        "ค": "Naphazoline เป็นยาในกลุ่ม imidazoline derivative มีฤทธิ์กระตุ้น alpha-adrenergic receptors โดยตรง ลดการคั่งของเลือดในตา",
        "ง": "Tetrahydrozoline เป็น sympathomimetic agent ที่มีฤทธิ์ alpha-agonist ใช้เป็นยาหยอดตาเพื่อลดอาการบวมและตาแดง"
    },
    "175": {
        "ก": "0.015 g คือปริมาณความเทียบเท่า NaCl ของยา Gentamicin 15 mg เท่านั้น ยังไม่ได้คำนวณหักล้างเพื่อให้เป็น Isotonic",
        "ข": "0.45 g คือปริมาณ NaCl ทั้งหมดที่ต้องใช้เพื่อให้สารละลาย 50 mL เป็น Isotonic (0.9% w/v) แต่ยังไม่ได้หักลบ Gentamicin",
        "ง": "0.465 g เป็นผลลัพธ์จากการนำปริมาณ NaCl ทั้งหมด 0.45 g ไปบวกเพิ่มกับค่า E ของ Gentamicin แทนที่จะนำไปหักลบออก",
        "จ": "0.9 g เป็นปริมาณ NaCl สำหรับการเตรียมสารละลาย Isotonic ปริมาตร 100 mL ไม่ใช่ 50 mL ตามที่โจทย์กำหนด"
    },
    "176": {
        "ก": "ฤทธิ์ Anti-inflammatory เป็นหนึ่งใน Pleiotropic effects ของ Statins โดยลดการหลั่ง pro-inflammatory cytokines เช่น CRP",
        "ข": "การยับยั้งการเกาะกลุ่มของเกล็ดเลือดเกิดจากฤทธิ์ลด Thromboxane A2 ของ Statins ซึ่งเป็นส่วนหนึ่งของ Pleiotropic effects",
        "ง": "การรบกวน Insulin signaling pathway จนทำให้ระดับกลูโคสในเลือดเพิ่มขึ้นเป็นอาการข้างเคียงของ Statins ไม่ใช่ฤทธิ์ที่เป็นประโยชน์ในการรักษา",
        "จ": "Statins มีฤทธิ์ Plaque stabilization ช่วยเพิ่มความแข็งแรงของผนังหลอดเลือด ป้องกันการแตกของ atheroma ได้"
    },
    "177": {
        "ก": "Grave's disease เป็นโรคที่ร่างกายสร้าง Thyroid-stimulating immunoglobulins มากระตุ้น TSH receptor ทำให้มีการสร้างฮอร์โมนมากผิดปกติ",
        "ค": "การรักษาในเด็กมักเริ่มต้นด้วยยาต้านไทรอยด์กลุ่ม Thionamides การผ่าตัดจะสงวนไว้สำหรับกรณีที่ดื้อยาหรือทนต่อยาไม่ได้",
        "ง": "ในผู้สูงอายุที่มีภาวะ Hyperthyroidism มักพิจารณาการรักษาด้วย Radioactive iodine มากกว่าการผ่าตัดที่มีความเสี่ยงสูงกว่า",
        "จ": "Euthyroid หมายถึงสภาวะที่ระดับฮอร์โมนไทรอยด์อยู่ในระดับสมดุลและปกติ ไม่ใช่ระดับฮอร์โมนที่สูงเกินกว่าค่าพื้นฐาน"
    },
    "178": {
        "ข": "การยับยั้งเฉพาะ Norepinephrine transporter เป็นกลไกของยากลุ่ม NRIs เช่น Reboxetine ไม่ใช่ยา TCAs อย่าง Amitriptyline",
        "ค": "การยับยั้งการทำงานของ MAO enzyme เป็นกลไกของยากลุ่ม MAOIs เช่น Phenelzine ไม่ใช่ยาในกลุ่ม Tricyclic antidepressants",
        "ง": "การกระตุ้น 5-HT receptor เป็นกลไกของยากลุ่ม Triptans สำหรับแก้อาการปวดไมเกรน ไม่ใช่กลไกของยาแก้ซึมเศร้า",
        "จ": "การกระตุ้น Alpha-2 adrenergic receptor เป็นกลไกของยาลดความดันโลหิตกลุ่ม Centrally acting อย่าง Clonidine"
    },
    "179": {
        "ข": "Dry mouth เป็นอาการข้างเคียงที่พบบ่อยจากฤทธิ์ปิดกั้น Muscarinic receptors (Anticholinergic effect) ของ Amitriptyline",
        "ค": "Orthostatic hypotension เกิดจากฤทธิ์ปิดกั้น Alpha-1 adrenergic receptor ของ Amitriptyline ทำให้หลอดเลือดไม่หดตัวตอบสนอง",
        "ง": "Urinary retention เป็นผลจากฤทธิ์ Anticholinergic ของ Amitriptyline ทำให้กล้ามเนื้อกระเพาะปัสสาวะคลายตัวและหูรูดหดเกร็ง",
        "จ": "Hyperuricemia มักเกิดจากยาขับปัสสาวะกลุ่ม Thiazide หรือ Loop diuretics เนื่องจากรบกวนการขับกรดยูริกที่ท่อไต ไม่พบในกลุ่ม TCAs"
    },
    "180": {
        "ข": "ความครอบคลุมทุกรูปแบบการดูแลคือ การบูรณาการบริการปฐมภูมิ แต่ยังไม่สะท้อนถึงการแก้ปัญหาเชิงลึกแบบเบ็ดเสร็จ (Comprehensive) ตามหลักการแพทย์",
        "ค": "ความรู้ การปฏิบัติ และเจตคติ คือองค์ประกอบของการประเมินการเรียนรู้ (Domains of learning) ไม่ใช่นิยามของเวชปฏิบัติปฐมภูมิ",
        "ง": "ทุกระดับของการทำเวชปฏิบัติเป็นการขยายสเกลการดูแลจากปัจเจกสู่ชุมชน (Community-oriented) ไม่ใช่นิยามของ Comprehensive care โดยตรง",
        "จ": "Atorvastatin 20 mg OD จัดเป็น Moderate intensity statin ใช้สำหรับลดไขมันในเลือด ไม่มีความเกี่ยวข้องกับนิยามของการป้องกันตติยภูมิ"
    },
    "181": {
        "ข": "Emollient คือสารเคลือบผิวที่ช่วยลดการระเหยของน้ำและให้ความชุ่มชื้น เช่น Mineral oil ไม่ใช่บทบาทหลักของวิตามินอี",
        "ค": "Suspending agent เป็นสารเพิ่มความหนืดที่ช่วยชะลอการตกตะกอนในตำรับยาแขวนตะกอน เช่น CMC ซึ่งไม่ใช่วิตามินอี",
        "ง": "Thickening agent เป็นสารเพิ่มความข้นหนืดของตำรับ เช่น Carbomer หรือ Cetyl alcohol ขณะที่วิตามินอีไม่มีคุณสมบัตินี้",
        "จ": "สารต้านอนุมูลอิสระ (Anti-oxidant) คือกลไกที่ถูกต้องของวิตามินอีในการป้องกันการเกิด Lipid peroxidation ในตำรับ"
    },
    "182": {
        "ข": "ยาประจำบางชนิดเช่น NSAIDs อาจทำให้ความดันโลหิตสูงขึ้นได้โดยการคั่งของโซเดียมและน้ำ แต่มักไม่ใช่ปัจจัยเสี่ยงหลักในผู้ป่วยส่วนใหญ่",
        "ค": "การสูบบุหรี่เป็นปัจจัยเสี่ยงหลักของโรคหลอดเลือดหัวใจ (Cardiovascular risk factor) แต่อาจไม่ใช่สาเหตุเดียวของการเกิดโรค",
        "ง": "อายุที่เพิ่มขึ้นทำให้ผนังหลอดเลือดแดงมีความยืดหยุ่นลดลง (Arterial stiffness) เป็นปัจจัยเสี่ยงที่ไม่สามารถปรับเปลี่ยนได้",
        "จ": "การระบุว่าทุกข้อเป็นปัจจัยเสี่ยงอาจดูครอบคลุม แต่หลักฐานทางคลินิกมักมุ่งเน้นไปที่โรคร่วมและพฤติกรรมที่มีนัยสำคัญสูงสุด"
    },
    "183": {
        "ข": "130/80 mmHg เป็นเป้าหมายสำหรับผู้ป่วยความดันโลหิตสูงที่มีโรคร่วมเสี่ยงสูง เช่น เบาหวาน หรือโรคไตเรื้อรัง (CKD)",
        "ค": "130/90 mmHg ไม่ใช่ค่าเป้าหมายที่ถูกแนะนำใน Clinical Practice Guidelines มาตรฐานใดๆ สำหรับการควบคุมความดันโลหิต",
        "ง": "140/80 mmHg ไม่ใช่เกณฑ์เป้าหมายมาตรฐานเนื่องจากค่าความดันตัวล่าง (Diastolic) มักตั้งเป้าไว้ที่ต่ำกว่า 90 mmHg",
        "จ": "140/90 mmHg เป็นเป้าหมายมาตรฐานตาม JNC 8 สำหรับผู้ป่วยทั่วไปที่มีอายุน้อยกว่า 60 ปีและไม่มีโรคแทรกซ้อน"
    },
    "184": {
        "ข": "ACEIs มีโครงสร้างที่สามารถจับกับ Zinc ion บริเวณ active site ของเอนไซม์ ACE เช่น Sulfhydryl หรือ Dicarboxylate group",
        "ค": "Alpha-adrenergic antagonists มักมีโครงสร้างหลักเป็น Quinazoline ring ดังเช่นที่พบใน Prazosin หรือ Doxazosin",
        "ง": "Beta-adrenergic antagonists มีโครงสร้างจำเพาะคือ Aryloxypropanolamine ซึ่งมีสายโซ่ข้างเชื่อมด้วย oxymethylene bridge",
        "จ": "Direct vasodilators เช่น Hydralazine มักมีโครงสร้างเป็น Phthalazine derivative ซึ่งออกฤทธิ์ขยายหลอดเลือดโดยตรง"
    }
}

def generate_rationale(choice_text):
    text = str(choice_text).lower()
    if 'amlodipine' in text:
        return 'Amlodipine เป็นยากลุ่ม Dihydropyridine CCB ที่ขยายหลอดเลือดส่วนปลาย ไม่มีผลลดอัตราตายในผู้ป่วย Heart failure'
    elif 'enalapril' in text or 'acei' in text:
        return 'Enalapril ออกฤทธิ์ยับยั้งเอนไซม์ ACE มีข้อห้ามใช้ในสตรีมีครรภ์และอาจทำให้เกิด Hyperkalemia โดยไม่เกี่ยวกับการต้านการเกาะกลุ่มของเกล็ดเลือด'
    elif 'arb' in text:
        return 'Angiotensin II receptor blockers ปิดกั้นการทำงานของ Angiotensin II ที่ AT1 receptor ไม่มีผลยับยั้งเอนไซม์ ACE จึงไม่ทำให้เกิดอาการไอแห้ง'
    elif 'propranolol' in text:
        return 'Propranolol เป็น Non-selective beta-blocker ที่สามารถจับกับ Beta-2 receptor ในหลอดลมได้ ทำให้หลอดลมตีบ จึงห้ามใช้ในผู้ป่วยโรคหอบหืด'
    elif 'metoprolol' in text or 'bisoprolol' in text or 'beta-blocker' in text or 'beta-adrenergic' in text:
        return 'Beta-blockers มีฤทธิ์ลดการทำงานของหัวใจ (Negative inotrope/chronotrope) หากนำมาใช้ขณะผู้ป่วยมีภาวะ Acute decompensated heart failure จะทำให้อาการแย่ลง'
    elif 'furosemide' in text:
        return 'Furosemide ยับยั้ง Na+/K+/2Cl- cotransporter ที่ Ascending loop of Henle ช่วยขับปัสสาวะเพื่อลดอาการบวม แต่ไม่มีผลยืดอายุขัยผู้ป่วย Heart failure'
    elif 'hctz' in text or 'diuretic' in text:
        return 'Thiazide diuretics ออกฤทธิ์ยับยั้ง Na+/Cl- cotransporter ที่ Distal convoluted tubule อาจเพิ่มความเสี่ยงของภาวะ Uric acid และ Glucose สูง'
    elif 'simvastatin' in text or 'statin' in text:
        return 'Simvastatin มีค่าครึ่งชีวิตสั้นและการสร้างคอเลสเตอรอลในร่างกายเกิดสูงสุดในช่วงกลางคืน การบริหารยาในเวลาอื่นจะทำให้ประสิทธิภาพลดลง'
    elif 'gemfibrozil' in text or 'fibrate' in text:
        return 'Gemfibrozil มีฤทธิ์ลดระดับ Triglyceride ได้ดี แต่หากใช้ร่วมกับ Statins จะยับยั้งการกำจัด Statins เพิ่มความเสี่ยงของภาวะ Rhabdomyolysis'
    elif 'aspirin' in text:
        return 'Aspirin ยับยั้ง COX-1 แบบ Irreversible ทำให้เกล็ดเลือดไม่สามารถสร้าง Thromboxane A2 ได้ตลอดอายุขัยของเกล็ดเลือดนั้น'
    elif 'clopidogrel' in text:
        return 'Clopidogrel เป็น Prodrug ที่ต้องถูกเปลี่ยนโดย CYP2C19 เพื่อไปยับยั้ง P2Y12 receptor บนเกล็ดเลือด ป้องกันเกล็ดเลือดเกาะกลุ่ม'
    elif 'digoxin' in text:
        return 'Digoxin ยับยั้ง Na+/K+ ATPase ทำให้เพิ่ม Intracellular calcium แต่ผู้ป่วยที่มีภาวะ Hypokalemia จะเสี่ยงต่อ Digoxin toxicity ได้ง่ายขึ้น'
    elif 'verapamil' in text or 'diltiazem' in text or 'non-dhp' in text:
        return 'Non-DHP CCBs ออกฤทธิ์ยับยั้งแคลเซียมแชนแนลที่เซลล์กล้ามเนื้อหัวใจ มีฤทธิ์ Negative inotrope จึงมีข้อห้ามใช้ในผู้ป่วย HFrEF'
    elif 'dash' in text:
        return 'การรับประทานอาหารแบบ DASH เน้นลดปริมาณโซเดียมและเพิ่มโพแทสเซียม แม้จะมีประสิทธิภาพสูงแต่ก็ไม่ได้แก้ไขพยาธิสภาพของหลอดเลือดทั้งหมด'
    elif 'sodium' in text or 'โซเดียม' in text:
        return 'การจำกัดปริมาณโซเดียมในอาหารช่วยลดความดันโลหิตได้จริง แต่ให้ผลลด SBP ได้เพียง 2-8 mmHg ซึ่งน้อยกว่าการรับประทานอาหารแบบ DASH'
    elif 'ออกกำลังกาย' in text or 'exercise' in text:
        return 'การออกกำลังกายแบบแอโรบิกมีประโยชน์ต่อหลอดเลือด แต่ลด SBP ได้เฉลี่ย 4-9 mmHg ซึ่งอาจไม่เพียงพอหากไม่ได้ปรับการกินอาหาร'
    elif 'บุหรี่' in text:
        return 'การเลิกบุหรี่ช่วยลดความเสี่ยงการเกิดโรคหลอดเลือดหัวใจโดยรวม แต่ไม่มีผลโดยตรงต่อการลดระดับความดันโลหิต SBP ในระยะสั้น'
    elif 'แอลกอฮอล์' in text or 'alcohol' in text:
        return 'การจำกัดเครื่องดื่มแอลกอฮอล์ช่วยลด SBP ได้เพียง 2-4 mmHg ซึ่งน้อยกว่าประโยชน์ที่ได้จากการคุมอาหารแบบ DASH'
    elif 'praziquantel' in text:
        return 'Praziquantel ออกฤทธิ์เพิ่มความซึมผ่านของแคลเซียมที่ผนังเซลล์ของพยาธิ ทำให้พยาธิเกิดอาการหดเกร็งและตาย ไม่ใช่กลไกยับยั้ง Microtubule'
    elif 'niclosamide' in text:
        return 'Niclosamide ยับยั้งกระบวนการ Oxidative phosphorylation ของพยาธิ ทำให้ขาดพลังงาน ATP นำไปใช้รักษาพยาธิตัวตืดได้ดี'
    elif 'mebendazole' in text:
        return 'Mebendazole ยับยั้งการสร้าง Microtubule อย่างจำเพาะเจาะจงในพยาธิ และทำให้การดูดซึมกลูโคสของพยาธิลดลงจนตาย'
    elif 'pyrantel pamoate' in text:
        return 'Pyrantel pamoate มีฤทธิ์เป็น Depolarizing neuromuscular blocker กระตุ้น Nicotinic receptors ของพยาธิ ทำให้พยาธิอัมพาต'
    elif 'ivermectin' in text:
        return 'Ivermectin ออกฤทธิ์กระตุ้น Glutamate-gated chloride channels ที่ระบบประสาทพยาธิ ทำให้เซลล์เกิด Hyperpolarization เป็นอัมพาต'
    elif 'insulin' in text or 'lispro' in text or 'nph' in text or 'aspart' in text:
        return 'Insulin แต่ละชนิดมี Pharmacokinetics ต่างกัน NPH มีระยะเวลาออกฤทธิ์ปานกลางและไม่ได้ออกแบบมาให้บริหารทางหลอดเลือดดำในผู้ป่วย DKA'
    elif 'β-cell' in text or 'sulfonylurea' in text or 'glibenclamide' in text:
        return 'ยากลุ่ม Sulfonylureas กระตุ้นการหลั่งอินซูลินจากเบต้าเซลล์ของตับอ่อน เพิ่มความเสี่ยงของภาวะน้ำตาลในเลือดต่ำ (Hypoglycemia)'
    elif 'ดูดซึม' in text or 'acarbose' in text:
        return 'Acarbose ยับยั้งเอนไซม์ Alpha-glucosidase ที่ลำไส้ ชะลอการย่อยและดูดซึมคาร์โบไฮเดรต ช่วยลด Postprandial glucose'
    elif 'metformin' in text or 'ตับ' in text or 'egfr' in text:
        return 'Metformin ออกฤทธิ์หลักคือยับยั้ง Hepatic glucose production และห้ามใช้ในผู้ป่วย eGFR < 30 mL/min/1.73m2 เนื่องจากเสี่ยงต่อ Lactic acidosis'
    elif 'repaglinide' in text:
        return 'Repaglinide เป็นยากลุ่ม Meglitinides ออกฤทธิ์กระตุ้นการหลั่งอินซูลินในช่วงสั้นๆ สามารถนำมาใช้ในผู้ป่วยโรคไตเรื้อรังได้'
    elif 'cushing' in text or 'prader' in text or 'hyperthyroidism' in text:
        return 'Cushing\'s syndrome และ Prader-Willi syndrome เป็นสาเหตุของความอ้วนได้ ขณะที่ Hyperthyroidism มักทำให้มีอัตราการเผาผลาญสูงและน้ำหนักลด'
    elif 'reye' in text or 'airway hypersensitivity' in text or 'bleeding' in text:
        return 'การใช้ Aspirin ในเด็กที่ติดเชื้อไวรัสเพิ่มความเสี่ยงของการเกิด Reye\'s syndrome ซึ่งนำไปสู่ภาวะสมองบวมและตับล้มเหลว'
    elif 'ช่องแช่เย็น' in text or 'ตะแคง' in text or 'ละลาย' in text:
        return 'วิธีการเหน็บยาที่ถูกต้องควรนอนตะแคงค้างไว้อย่างน้อย 15-30 นาทีเพื่อให้ยาละลายและออกฤทธิ์เต็มที่ การนอนเพียง 5 นาทีอาจสั้นเกินไป'
    elif 'hydro' in text or 'demethylation' in text or 'reduction' in text:
        return 'ยากลุ่ม Nitroimidazole ต้องผ่านกระบวนการ Nitro-reduction ในเชื้อโปรโตซัวเพื่อสร้างอนุมูลอิสระที่เป็นพิษต่อ DNA ของเชื้อ'
    elif 'tinnitus' in text:
        return 'Tinnitus (หูอื้อ) เป็นผลข้างเคียงของยา Aspirin ในขนาดสูงที่ทำให้เกิด Salicylism แต่ไม่ใช่ข้อกังวลหลักที่ห้ามใช้ยาในเด็กที่ติดเชื้อไวรัส'
    else:
        return 'ข้อความในตัวเลือกนี้อธิบายกลไกทางพยาธิวิทยาหรือเภสัชวิทยาที่ไม่ถูกต้องสำหรับตัวยาหรือภาวะของโรคที่กล่าวถึงในกรณีศึกษา'

def process():
    try:
        with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\cardio_part4.json', encoding='utf-8') as f:
            data = json.load(f)
        
        out_dict = {}
        letters = {1: 'ก', 2: 'ข', 3: 'ค', 4: 'ง', 5: 'จ'}
        for d in data:
            c_idx = str(d['cardio_idx'])
            ans_str = str(d.get('ans', '')).strip()
            
            correct_num = None
            if ans_str.isdigit():
                correct_num = int(ans_str)
            
            distractors = {}
            if c_idx in exact_dict:
                for i in range(1, 6):
                    if i != correct_num:
                        char = letters[i]
                        if char in exact_dict[c_idx]:
                            distractors[char] = exact_dict[c_idx][char]
            else:
                for i in range(1, 6):
                    if i != correct_num:
                        choice_text = d.get(f'c{i}', '')
                        if choice_text:
                            distractors[letters[i]] = generate_rationale(choice_text)
            
            out_dict[c_idx] = {"distractors": distractors}
            
        with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\distractors_cardio_part4.json', 'w', encoding='utf-8') as f:
            json.dump(out_dict, f, ensure_ascii=False, indent=4)
            
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    process()
