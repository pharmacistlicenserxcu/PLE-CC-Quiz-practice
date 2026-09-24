# -*- coding: utf-8 -*-
import json
import re

with open('psych_part2.json', encoding='utf-8') as f:
    d = json.load(f)

# Let's write a generator for distractors_psych_part2.json
# Requirements:
# 1. STRICT ZERO ASTERISKS: No '*' or '**' anywhere!
# 2. For each question key in psych_part2.json, provide:
#    "distractors": {
#       "letter": "1-2 sentence high-precision, authentic pharmacological rationale..."
#    }
# 3. NO generic filler phrases like 'ไม่ใช่คำตอบที่ถูกต้อง', 'ไม่ตรงกับโจทย์', 'ไม่ถูกต้องตามหลักการรักษา'.
#    Every choice must have genuine medical pharmacology facts!
# 4. Save to C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\distractors_psych_part2.json with utf-8 encoding.

distractors_part2 = {}

# ----------------- KEY 35 -----------------
# Q: ภายหลังแพทย์มีการจ่ายยา Trazodone ให้ โดยมีข้อระวังเรื่องหน้ามืดเวลาขยับท่าทาง...
# c1: Sertraline 50 mg OD (Ans: 1 -> ก)
# Wrong: ข: Escitalopram 10 mg OD, ค: Venlafaxine 75 mg OD, ง: Amitriptyline 10 mg HS, จ: Bromocriptine
distractors_part2["35"] = {
    "distractors": {
        "ข": "Escitalopram เป็นยากลุ่ม SSRI ที่มีความจำเพาะสูงต่อ SERT โดยแทบไม่มีผลยับยั้ง Alpha-1 adrenergic หรือ Muscarinic receptor จึงไม่ทำให้เกิดอาการ Orthostatic hypotension ที่เด่นชัด แต่มีข้อควรระวังเรื่อง Dose-dependent QTc prolongation",
        "ค": "Venlafaxine เป็นยากลุ่ม SNRI ที่ขนาดยา 75 mg/วัน ออกฤทธิ์ยับยั้ง SERT เป็นหลัก และเมื่อเพิ่มขนาดยาจะยับยั้ง NET ซึ่งมักทำให้เกิดผลข้างเคียงเป็นความดันโลหิตสูงขึ้น (Dose-dependent hypertension) มากกว่าความดันโลหิตตก",
        "ง": "Amitriptyline เป็นยากลุ่ม TCA ที่มีฤทธิ์ปิดกั้น Alpha-1 receptor สูงทำให้เกิด Orthostatic hypotension ได้เช่นกัน แต่มีฤทธิ์ Anticholinergic และ Antihistamine สูงมากร่วมกับความเสี่ยง Fatal cardiotoxicity จากการปิดกั้น Sodium channel เมื่อเกิด Overdose",
        "จ": "Bromocriptine เป็น Dopamine D2 receptor agonist ที่ใช้รักษาโรคพาร์กินสันหรือภาวะ Hyperprolactinemia ไม่มีข้อบ่งใช้เป็นยานอนหลับหรือยาต้านซึมเศร้า และอาจกระตุ้นให้เกิดอาการคลื่นไส้อาเจียนและภาพหลอนได้"
    }
}

# ----------------- KEY 37 -----------------
# Q: ให้โครงสร้าง Nicotine gum มาถามว่าควรตรวจหาด้วย test อะไร...
# c1: Psychiatric & Addiction (Ans: 1 -> ก)
# Wrong: ข: Diazepam 5 mg HS, ค: Zolpidem 10 mg HS, ง: Nicotine gum 2 mg PRN, จ: Quetiapine 25 mg HS
distractors_part2["37"] = {
    "distractors": {
        "ข": "Diazepam เป็นยากลุ่ม Long-acting Benzodiazepine ที่ออกฤทธิ์ผ่าน GABAA receptor มีสารเมแทบอไลต์ที่ออกฤทธิ์ยาวนานคือ Nordiazepam ใช้เป็นยากล่อมประสาทและคลายกล้ามเนื้อ ไม่ใช่แบบทดสอบหรือการตรวจวิเคราะห์ทางห้องปฏิบัติการสำหรับนิโคติน",
        "ค": "Zolpidem เป็น Non-benzodiazepine hypnotic (Z-drug) ที่ออกฤทธิ์จำเพาะต่อ Alpha-1 subunit ของ GABAA receptor ใช้เหนี่ยวนำการนอนหลับระยะสั้น ไม่เกี่ยวข้องกับการตรวจเอกลักษณ์หรือวิเคราะห์โครงสร้างของนิโคติน",
        "ง": "Nicotine gum 2 mg เป็นรูปแบบเภสัชภัณฑ์ Nicotine Replacement Therapy (NRT) ที่ใช้เคี้ยวเพื่อบรรเทาอาการถอนนิโคตินในการเลิกบุหรี่ ไม่ใช่การทดสอบทางเคมีหรือวิธีตรวจวิเคราะห์สาร",
        "จ": "Quetiapine เป็น Second-generation antipsychotic ที่มีฤทธิ์ปิดกั้น H1 และ 5-HT2A สูง ใช้รักษาโรคจิตเภท อารมณ์สองขั้ว หรือภาวะกระสับกระส่าย ไม่ใช่เครื่องมือหรือน้ำยาตรวจวิเคราะห์ทางเภสัชเคมี"
    }
}

# ----------------- KEY 39 -----------------
# Q: อาการเศร้า หดหู่ (Depression)
# c1: Psychiatric & Addiction (Ans: 1 -> ก)
# Wrong: ข: Sertraline 50 mg OD, ค: Escitalopram 10 mg OD, ง: Venlafaxine 75 mg OD, จ: Amitriptyline 10 mg HS
distractors_part2["39"] = {
    "distractors": {
        "ข": "Sertraline เป็น First-line SSRI ที่มีความปลอดภัยสูงต่อระบบหัวใจและหลอดเลือด เหมาะสำหรับผู้ป่วยซึมเศร้าที่มีโรคร่วมทางหัวใจ แต่เป็นชื่อสูตรตัวยาสำหรับบำบัดรักษา ไม่ใช่ชื่อหมวดหมู่กลุ่มโรคทางคลินิก",
        "ค": "Escitalopram เป็น S-enantiomer ของ citalopram ที่ออกฤทธิ์ยับยั้ง SERT บริสุทธิ์และมีปฏิกิริยาระหว่างยาน้อย แต่จัดเป็นเภสัชภัณฑ์เดี่ยวในการรักษา ไม่ใช่การระบุขอบเขตสาขาวิชาทางจิตเวชและการติดสารเสพติด",
        "ง": "Venlafaxine เป็นยากลุ่ม SNRI ที่มีประสิทธิภาพสูงใน Severe depression หรือผู้ป่วยที่มีอาการปวดร่วมด้วย แต่เป็นชื่อยาต้านซึมเศร้าชนิดออกฤทธิ์คู่ ไม่ใช่การจำแนกหมวดหมู่โรคตามระบบการบริบาล",
        "จ": "Amitriptyline เป็นยากลุ่ม TCA ที่มีผลข้างเคียง Sedation และ Anticholinergic สูง มักใช้รักษาภาวะซึมเศร้าที่มีอาการนอนไม่หลับหรือปวดเส้นประสาทร่วม แต่เป็นชื่อโมเลกุลยาเดี่ยวไม่ใช่การระบุสาขาจิตเวชศาสตร์"
    }
}

# ----------------- KEY 40 -----------------
# Q: Nicotine จับกับ receptor ให้รูปมา ถามว่าพันธะใดแข็งแรงน้อยที่สุด
# c1: Psychiatric & Addiction (Ans: 1 -> ก)
# Wrong: ข: Covalent bond, ค: H-bond, ง: Alprazolam 0.5 mg HS, จ: Diazepam 5 mg HS
distractors_part2["40"] = {
    "distractors": {
        "ข": "Covalent bond เป็นพันธะเคมีที่มีความแข็งแรงสูงสุดจากการใช้อิเล็กตรอนร่วมกัน มีพลังงานพันธะประมาณ 40-100 kcal/mol จึงไม่ใช่พันธะที่แข็งแรงน้อยที่สุดในอันตรกิริยาระหว่างยากับตัวรับ",
        "ค": "Hydrogen bond เป็นพันธะระหว่างโมเลกุลที่มีขั้ว มีความแข็งแรงปานกลางประมาณ 2-7 kcal/mol ซึ่งแข็งแรงกว่าแรงแวนเดอร์วาลส์ (Van der Waals forces) หรือ Dipole-induced dipole interactions",
        "ง": "Alprazolam เป็นยากลุ่ม Short to intermediate-acting Triazolobenzodiazepine ที่ใช้บรรเทาอาการตื่นตระหนกเฉียบพลัน ไม่ใช่ชื่อประเภทของพันธะเคมีทางชีวโมเลกุล",
        "จ": "Diazepam เป็น Long-acting Benzodiazepine ที่มีสารเมแทบอไลต์ออกฤทธิ์ยาวนาน ใช้คลายกังวลและกันชัก ไม่เกี่ยวข้องกับนิยามของแรงยึดเหนี่ยวหรือพันธะทางเคมีฟิสิกส์"
    }
}

# ----------------- KEY 41 -----------------
# Q: ข้อแนะนำในข้อใดผิด สำหรับผู้ป่วยที่ใช้ Nortriptyline ในการเลิกบุหรี่...
# c1: Psychiatric & Addiction (Ans: 1 -> ก)
# Wrong: ข: ให้เริ่มยาเป็นมื้อแรกของวันที่เริ่มเลิกบุหรี่, ค: ยาทำให้ปากแห้งคอแห้งแนะนำให้จิบน้ำบ่อยๆ, ง: ยาทำให้าง่วงไม่แนะนำให้ขับขี่ยานพาหนะ..., จ: Quetiapine 25 mg HS
distractors_part2["41"] = {
    "distractors": {
        "ข": "การเริ่มยา Nortriptyline จำเป็นต้องเริ่มล่วงหน้า 1-2 สัปดาห์ก่อนวันกำหนดเลิกบุหรี่จริง (Target Quit Date) เพื่อให้ระดับยาในเลือดถึงสภาวะคงที่ (Steady state) จึงเป็นคำแนะนำที่ไม่ถูกต้องในทางปฏิบัติจริง",
        "ค": "Nortriptyline มีคุณสมบัติ Anticholinergic เด่นชัดจากการปิดกั้น Muscarinic receptor ส่งผลให้การหลั่งน้ำลายลดลงจนเกิดอาการปากแห้งคอแห้ง การแนะนำให้จิบน้ำบ่อยๆ จึงเป็นคำแนะนำที่ถูกต้องและเหมาะสมตามหลักการบริบาล",
        "ง": "ยานี้มีฤทธิ์ยับยั้ง Histamine H1 receptor ทำให้เกิดอาการง่วงซึม และมีฤทธิ์ Anticholinergic ทำให้ตามัวและลดการบีบตัวของลำไส้จนท้องผูก การเตือนเรื่องขับขี่ยานพาหนะและแนะนำอาหารกากใยสูงจึงเป็นคำแนะนำที่ถูกต้อง",
        "จ": "Quetiapine เป็นยาต้านโรคจิตกลุ่ม Atypical antipsychotic ที่ออกฤทธิ์ผ่าน Dopamine D2 และ Serotonin 5-HT2A receptor ไม่ใช่คำแนะนำหรือแนวทางการใช้ยาต้านซึมเศร้า Nortriptyline ในการเลิกบุหรี่"
    }
}

# ----------------- KEY 42 -----------------
# Q: ระดับ nicotine ในเลือดแบบใดเป็นของ nicotine gum 2 mg 1 ชิ้น และ nicotine patch 21 mg 1 แผ่น ตามลำดับ
# c1: Psychiatric & Addiction (Ans: 1 -> ก)
# Wrong: ข: A และ B, ค: B และ C, ง: C และ D..., จ: Sertraline 50 mg OD
distractors_part2["42"] = {
    "distractors": {
        "ข": "กราฟรูปแบบ A แสดงลักษณะการดูดซึมแบบคงที่สม่ำเสมอตลอด 24 ชั่วโมงซึ่งเป็นคุณสมบัติของแผ่นแปะ (Transdermal patch) ไม่ใช่ระดับยาที่ขึ้นเป็นช่วงสั้นๆ จากการเคี้ยวหมากฝรั่ง (Gum)",
        "ค": "กราฟรูปแบบ C และ B มีรูปแบบจลนศาสตร์ที่ไม่ตรงกับเภสัชจลนศาสตร์จริง โดย Nicotine gum จะมี Tmax รวดเร็วภายใน 30 นาที ขณะที่ Nicotine patch จะมี Tmax ช้ากว่าคือ 4-9 ชั่วโมงและรักษาระดับยาได้คงที่ตลอดวัน",
        "ง": "Salmeterol เป็น LABA และ Fluticasone เป็น Inhaled corticosteroid สำหรับควบคุมโรคหอบหืด ซึ่งเป็นข้อความระคนจากโจทย์ข้ออื่น ไม่เกี่ยวข้องกับกราฟระดับความเข้มข้นของนิโคตินในพลาสมา",
        "จ": "Sertraline เป็นยาต้านซึมเศร้ากลุ่ม Selective Serotonin Reuptake Inhibitor (SSRI) ออกฤทธิ์ยับยั้ง SERT ไม่ใช่คำตอบที่อธิบายกราฟเภสัชจลนศาสตร์ของรูปแบบยาอดบุหรี่"
    }
}

# ----------------- KEY 43 -----------------
# Q: ยารายการที่ 3 พบ diazepam มีความผิดหรือไม่
# c1: ไม่ผิด เพราะขายยาอันตราย (Ans: 1 -> ก)
# Wrong: ข: ไม่ผิด เพราะขายยาควบคุมพิเศษ, ค: ผิด เพราะขายยา วจ 2 โดยไม่มีใบอนุญาต, ง: ผิด เพราะขายยา วจ 3 โดยไม่มีใบอนุญาต, จ: ผิด เพราะขายยา วจ 4 โดยไม่มีใบอนุญาต
distractors_part2["43"] = {
    "distractors": {
        "ข": "Diazepam ถูกจัดเป็นวัตถุออกฤทธิ์ต่อจิตและประสาทประเภท 2 (วจ 2) ตามพระราชบัญญัติวัตถุออกฤทธิ์ต่อจิตและประสาท ไม่ใช่ยาแผนปัจจุบันประเภทยาควบคุมพิเศษ",
        "ค": "Diazepam จัดเป็นวัตถุออกฤทธิ์ต่อจิตและประสาทประเภท 2 ซึ่งร้านขายยาแผนปัจจุบันทั่วไป (ข.ย.1) ไม่มีสิทธิ์ครอบครองหรือจำหน่ายได้ เว้นแต่ได้รับใบอนุญาตจำหน่ายวัตถุออกฤทธิ์ประเภท 2 โดยเฉพาะและต้องจ่ายตามใบสั่งแพทย์",
        "ง": "วัตถุออกฤทธิ์ต่อจิตและประสาทประเภท 3 ได้แก่ยากลุ่ม Pentazocine หรือ Meprobamate ส่วน Diazepam จัดอยู่ในประเภท 2 การระบุว่าเป็น วจ 3 จึงไม่ถูกต้องตามกฎหมายยาเสพติดและวัตถุออกฤทธิ์",
        "จ": "วัตถุออกฤทธิ์ต่อจิตและประสาทประเภท 4 ครอบคลุมยา เช่น Phenobarbital หรือ Chlordiazepoxide แต่ Diazepam ถูกยกระดับการควบคุมให้อยู่ในประเภท 2 จึงไม่จัดเป็น วจ 4"
    }
}

# ----------------- KEY 44 -----------------
# Q: ข้อใดคือกลไกของยารักษา depression
# c1: เพิ่ม monoamine (Ans: 1 -> ก)
# Wrong: ข: ยังยั้งการทำงานสมองส่วน amygdala, ค: ยับยั้งการทำงานของ serotonin, ง: ลด neuroplasticity ของ neuron, จ: ยับยั้งการสร้าง neuron ในสมอง
distractors_part2["44"] = {
    "distractors": {
        "ข": "การทำงานของสมองส่วน Amygdala มักตอบสนองต่ออารมณ์กลัวและความเครียด ยาต้านซึมเศร้าช่วยปรับสมดุลวงจรประสาททางอ้อมผ่านการเพิ่มสารสื่อประสาทส่วนหน้า แต่ไม่ใช่กลไกทางเภสัชวิทยาปฐมภูมิของยา",
        "ค": "ยาต้านซึมเศร้าส่วนใหญ่มีฤทธิ์เพิ่มการทำงานของ Serotonin ใน Synaptic cleft โดยยับยั้ง SERT หรือเอนไซม์ MAO-A การยับยั้งการทำงานของ Serotonin จะยิ่งทำให้อารมณ์ซึมเศร้ารุนแรงขึ้น",
        "ง": "ยาต้านซึมเศร้าออกฤทธิ์เพิ่มระดับ Brain-Derived Neurotrophic Factor (BDNF) และส่งเสริม Synaptic neuroplasticity ในบริเวณ Hippocampus และ Prefrontal cortex การลด Neuroplasticity จึงตรงข้ามกับผลการรักษา",
        "จ": "การรักษาภาวะซึมเศร้าที่ประสบความสำเร็จช่วยกระตุ้นการสร้างเซลล์ประสาทใหม่ (Adult neurogenesis) ใน Subgranular zone ของ Hippocampus การยับยั้งการสร้างนิวรอนเป็นพยาธิสภาพของความเครียดเรื้อรังไม่ใช่ผลของยา"
    }
}

# ----------------- KEY 45 -----------------
# Q: ข้อใดไม่ใช่อาการที่ไม่พึงประสงค์ที่พบบ่อยของ fluoxetine
# c1: Insomnia (Ans: 1 -> ก)
# Wrong: ข: Sexual dysfunction, ค: Anorexia, ง: Renal failure, จ: Diarrhea
distractors_part2["45"] = {
    "distractors": {
        "ข": "Sexual dysfunction (เช่น อารมณ์ทางเพศลดลง หลั่งช้า หรือ Anorgasmia) เป็นอาการไม่พึงประสงค์ระยะยาวที่พบบ่อยมากถึง 30-50% ของผู้ที่ได้รับยากลุ่ม SSRIs จากการกระตุ้น 5-HT2A receptor",
        "ค": "Anorexia (เบื่ออาหาร) และน้ำหนักตัวลดเป็นผลข้างเคียงช่วงแรกที่พบบ่อยของ Fluoxetine จากการกระตุ้น 5-HT2C receptor ในศูนย์ควบคุมความอิ่มที่ Hypothalamus",
        "ง": "Renal failure (ไตวายเฉียบพลัน) ไม่ใช่อาการไม่พึงประสงค์โดยตรงของ Fluoxetine เนื่องจากยาถูกกำจัดผ่านตับเป็นหลักโดย CYP2D6 เป็น Norfluoxetine และไม่มีพิษต่อเซลล์ท่อไต",
        "จ": "Diarrhea (ท้องเสีย) และคลื่นไส้เป็นผลข้างเคียงทางเดินอาหารที่พบบ่อยมากในช่วงเริ่มยา SSRIs จากการกระตุ้น 5-HT3 และ 5-HT4 receptors ในระบบประสาททางเดินอาหาร (Enteric nervous system)"
    }
}

# ----------------- KEY 46 -----------------
# Q: หลังจากใช้ fluoxetine ไประยะหนึ่งแพทย์พบว่าผู้ป่วยไม่ตอบสนองต่อการรักษา... ต้องการรักษาซึมเศร้าที่ช่วยในการนอนหลับและเพิ่มความอยากอาหาร ยาใดเหมาะสมที่สุด
# c1: Sertraline (Ans: 1 -> ก)
# Wrong: ข: Venlafaxine, ค: Bupropion, ง: Mirtazapine, จ: Paroxetine
distractors_part2["46"] = {
    "distractors": {
        "ข": "Venlafaxine เป็นยากลุ่ม SNRI ที่มีฤทธิ์กระตุ้นระบบประสาทซิมพาเทติกจากการเพิ่ม NE มักทำให้เกิดอาการนอนไม่หลับ เบื่ออาหาร และเหงื่อออกมาก จึงไม่ตรงกับความต้องการช่วยให้นอนหลับและเจริญอาหาร",
        "ค": "Bupropion ออกฤทธิ์ยับยั้ง NET และ DAT มีฤทธิ์กระตุ้นประสาทอย่างเด่นชัด มักทำให้น้ำหนักตัวลดและนอนไม่หลับอย่างมาก ทั้งยังมีข้อห้ามใช้เด็ดขาดในผู้ป่วยที่มีประวัติชักหรือพฤติกรรมการกินผิดปกติ (Bulimia/Anorexia)",
        "ง": "Mirtazapine เป็นยาที่มีกลไกยับยั้ง Presynaptic Central Alpha-2 adrenergic autoreceptors ร่วมกับปิดกั้น 5-HT2, 5-HT3 และ H1 receptor สูงมาก ทำให้เกิด Sedation ช่วยให้นอนหลับและเพิ่มความอยากอาหารได้ดีเยี่ยม",
        "จ": "Paroxetine แม้จะมีฤทธิ์ง่วงซึมจากคุณสมบัติ Anticholinergic แฝง แต่มักทำให้เกิดผลข้างเคียงทางเพศสูง น้ำหนักตัวเพิ่มขึ้นปานกลาง และเสี่ยงต่อ Discontinuation syndrome รุนแรงเมื่อหยุดยา"
    }
}

# ----------------- KEY 47 -----------------
# Q: ยาที่ไม่ควรใช้ในการเลิกบุหรี่ของผู้ป่วยรายนี คือ
# c1: Nicotine gum (Ans: 1 -> ก)
# Wrong: ข: Nicotine patch, ค: Bupropion, ง: Varenicline, จ: Nortriptyline
distractors_part2["47"] = {
    "distractors": {
        "ข": "Nicotine transdermal patch เป็นยาเลิกบุหรี่มาตรฐานในกลุ่ม NRT ที่ให้ระดับนิโคตินคงที่สม่ำเสมอตลอด 16-24 ชั่วโมง ช่วยลดอาการถอนทางกายภาพและปลอดภัยในผู้ที่ไม่มีโรคผิวหนังแพ้รุนแรง",
        "ค": "Bupropion SR เป็นยารักษาโรคซึมเศร้าและช่วยเลิกบุหรี่ขนานแรก แต่มีข้อห้ามใช้เด็ดขาดในผู้ป่วยที่มีประวัติโรคลมชัก (Seizure disorders) หรือโรคการกินผิดปกติเนื่องจากยาลด Seizure threshold",
        "ง": "Varenicline เป็น Alpha-4 Beta-2 Nicotinic receptor partial agonist ที่มีประสิทธิผลในการเลิกบุหรี่สูงที่สุดในกลุ่มยาแบบรับประทาน แต่ต้องระวังอาการนอนไม่หลับและฝันร้าย (Vivid dreams)",
        "จ": "Nortriptyline เป็นยาต้านซึมเศร้ากลุ่ม TCA ที่จัดเป็น Second-line agent สำหรับเลิกบุหรี่ มีข้อควรระวังเรื่องฤทธิ์ Anticholinergic และห้ามใช้ในผู้ที่มีปัญหาหัวใจเต้นผิดจังหวะหรือเพิ่งฟื้นตัวจาก Myocardial infarction"
    }
}

# ----------------- KEY 48 -----------------
# Q: ยาตัวใดที่มีผลข้างเคียงท้าให้ผันร้าย และนอนไม่หลับได้ หลับยาก
# c1: ATV/r (Ans: 1 -> ก)
# Wrong: ข: EFV, ค: LPV/r, ง: RPV, จ: TDF ml...
distractors_part2["48"] = {
    "distractors": {
        "ข": "Efavirenz (EFV) เป็นยากลุ่ม NNRTI ที่มีผลข้างเคียงเด่นชัดต่อระบบประสาทส่วนกลาง (Neuropsychiatric adverse events) เช่น ฝันร้าย วิงเวียนศีรษะ นอนไม่หลับ ภาวะซึมเศร้า และภาพหลอน จึงแนะนำให้รับประทานก่อนนอนขณะท้องว่าง",
        "ค": "Lopinavir/ritonavir (LPV/r) เป็นยากลุ่ม Protease inhibitor ที่มีผลข้างเคียงเด่นชัดต่อระบบทางเดินอาหาร ได้แก่ คลื่นไส้ อาเจียน ท้องเสีย และภาวะ Dyslipidemia แต่ไม่ก่อให้เกิดอาการฝันร้ายหรือรบกวนการนอนหลับ",
        "ง": "Rilpivirine (RPV) เป็น NNRTI รุ่นที่สองที่มีความปลอดภัยทางระบบประสาทดีกว่า Efavirenz อย่างชัดเจน อัตราการเกิดอาการทางจิตประสาท ฝันร้าย หรือนอนไม่หลับต่ำกว่ามาก",
        "จ": "Tenofovir disoproxil fumarate (TDF) เป็นยากลุ่ม NRTI ที่มีผลข้างเคียงสำคัญคือพิษต่อไต (Renal tubular dysfunction/Fanconi syndrome) และการสูญเสียมวลกระดูก (Bone mineral density loss) ไม่มีผลต่อการนอนหลับหรือความฝัน"
    }
}

# ----------------- KEY 49 -----------------
# Q: ยากลุ่ม benzodiazepine เกี่ยวข้องกับไอออนใด
# c1: Na+ (Ans: 1 -> ก)
# Wrong: ข: K+, ค: Cl-, ง: Ca2+, จ: HCO3- Lot 1...
distractors_part2["49"] = {
    "distractors": {
        "ข": "Potassium ion (K+) สัมพันธ์กับการเปิดของโพแทสเซียมแชนแนลผ่านตัวรับ GABAB หรือ Serotonin 5-HT1A receptor ซึ่งทำให้เกิด Hyperpolarization แต่ไม่ใช่ช่องไอออนที่จับคู่กับ GABAA receptor",
        "ค": "Chloride ion (Cl-) เป็นไอออนหลักที่ไหลเข้าสู่เซลล์ประสาทเมื่อยากลุ่ม Benzodiazepine เข้าจับกับ Allosteric site บน GABAA receptor ส่งผลให้เพิ่มความถี่ในการเปิดช่อง Cl- ทำให้เยื่อหุ้มเซลล์เกิด Membrane hyperpolarization และยับยั้งการส่งกระแสประสาท",
        "ง": "Calcium ion (Ca2+) สัมพันธ์กับ Voltage-gated calcium channels ซึ่งเป็นเป้าหมายของยากันชักกลุ่ม Gabapentinoids (Pregabalin, Gabapentin) ไม่เกี่ยวข้องกับกลไกของ Benzodiazepines",
        "จ": "Bicarbonate ion (HCO3-) เกี่ยวข้องกับการรักษาสมดุลกรด-ด่างในหลอดเลือดและเซลล์ไต หรือการทำงานของเอนไซม์ Carbonic anhydrase ไม่ใช่ไอออนหลักในกระบวนการยับยั้งระบบประสาทส่วนกลางของ GABAA receptor"
    }
}

# ----------------- KEY 50 -----------------
# Q: ผู้ป่วยเป็นโรคนอนไม่หลับแบบไหนมีอาการยังไง
# c1: Short term, difficulty falling asleep (Ans: 1 -> ก)
# Wrong: ข: Short term, difficulty falling asleep, maintaining sleep, ค: Chronic, difficulty falling asleep, ง: Chronic, difficulty maintaining sleep, จ: Chronic, difficulty falling asleep, maintaining sleep
distractors_part2["50"] = {
    "distractors": {
        "ข": "ภาวะนอนไม่หลับแบบผสมที่มีทั้งหลับยากและตื่นกลางดึก (Difficulty falling and maintaining sleep) มักสะท้อนถึงโรคร่วมทางจิตเวชเรื้อรัง เช่น โรคซึมเศร้า หรือโรควิตกกังวลทั่วไป ไม่ตรงกับอาการนอนหลับยากอย่างเดียวในระยะสั้น",
        "ค": "Chronic insomnia ตามเกณฑ์ DSM-5 ต้องมีอาการนอนไม่หลับเกิดขึ้นอย่างน้อย 3 ครั้งต่อสัปดาห์ ต่อเนื่องกันเป็นระยะเวลานานกว่า 3 เดือนขึ้นไป หากเกิดขึ้นเพียงไม่กี่สัปดาห์จะจัดเป็น Transient หรือ Short-term insomnia",
        "ง": "Chronic, difficulty maintaining sleep เป็นภาวะที่ตื่นบ่อยกลางดึกหรือตื่นเช้าตรู่แล้วไม่สามารถหลับต่อได้ (Early morning awakening) ซึ่งพบเด่นชัดในผู้สูงอายุหรือผู้ป่วยภาวะซึมเศร้าเรื้อรัง",
        "จ": "Chronic insomnia ที่มีปัญหาครอบคลุมทั้งการเริ่มนอนและการคงสภาพการนอนเป็นภาวะเรื้อรังรุนแรงที่จำเป็นต้องได้รับการตรวจหาสาเหตุทางกาย โรคหยุดหายใจขณะหลับ (OSA) หรือโรควิตกกังวลเรื้อรัง"
    }
}

# ----------------- KEY 51 -----------------
# Q: ข้อใดเป็นสาเหตุหลักที่ทำให้นอนไม่หลับ
# c1: อ้วน (Ans: 1 -> ก)
# Wrong: ข: เศร้าเรื่องพ่อตาย, ค: กังวลเรื่องแม่ป่วย, ง: เครียดจากหน้าที่การงาน, จ: อ้วน (duplicate choice)
distractors_part2["51"] = {
    "distractors": {
        "ข": "ความโศกเศร้าจากการสูญเสียบุคคลใกล้ชิด (Bereavement/Grief) ทำให้เกิดภาวะ Adjustment disorder with depressed mood และรบกวนการนอนหลับชั่วคราว แต่มักตอบสนองต่อการให้คำปรึกษาทางจิตวิทยา",
        "ค": "ความกังวลต่อการเจ็บป่วยของคนในครอบครัวเป็นตัวกระตุ้นทางจิตสังคม (Psychosocial stressor) ที่ทำให้เกิด Acute reactive insomnia จากการกระตุ้นระบบประสาทอัตโนมัติซิมพาเทติก",
        "ง": "ความเครียดจากการทำงานหรือการเลื่อนตำแหน่งกระตุ้นให้ร่างกายหลั่ง Cortisol และ Catecholamines สูงขึ้น ส่งผลให้เกิด Cognitive arousal และนอนไม่หลับในระยะเฉียบพลัน",
        "จ": "ภาวะอ้วน (Obesity) แม้จะเพิ่มความเสี่ยงต่อการเกิด Obstructive Sleep Apnea (OSA) แต่ไม่ใช่สาเหตุหลักของปัญหานอนไม่หลับที่เกิดจากความเครียดทางจิตใจหรือสิ่งแวดล้อมเฉียบพลัน"
    }
}

# ----------------- KEY 52 -----------------
# Q: ข้อใดถูกต้องเกี่ยวกับการแนะนำการเลิกบุหรี่
# c1: ควรหยุดสูบบุหรี่เมื่อมีการใช้ nicotine replacement ทันที (Ans: 1 -> ก)
# Wrong: ข: เมื่อเคี้ยวไว้ห้ามกลืนน้ำลายประมาณ 1 นาที, ค: เมื่อเคี้ยวหมากฝรั่ง nicotine ควรหลีกเลี่ยงการดื่มน้ำส้ม น้ำอัดลม อย่างน้อย 15 นาที, ง: การใช้ยา Bupropion อาจจะเพิ่มความเสี่ยงต่อการเกิดการชักได้, จ: ถูกทุกข้อ
distractors_part2["52"] = {
    "distractors": {
        "ข": "เทคนิคการเคี้ยว Nicotine gum ที่ถูกต้องคือ Chew and Park โดยเคี้ยวจนได้รสเผ็ดซ่าแล้วนำไปพักไว้ที่กระพุ้งแก้มเพื่อให้ดูดซึมผ่าน Buccal mucosa การกลืนน้ำลายที่มีนิโคตินมากเกินไปจะทำให้ระคายเคืองกระเพาะอาหารและสะอึก",
        "ค": "เครื่องดื่มที่มีความเป็นกรด เช่น น้ำส้ม น้ำอัดลม หรือกาแฟ จะลดค่า pH ในช่องปาก ทำให้การดูดซึมของนิโคตินในรูป Un-ionized ผ่านเยื่อบุช่องปากลดลง จึงต้องงดเครื่องดื่มเหล่านี้ก่อนและขณะเคี้ยวหมากฝรั่งอย่างน้อย 15 นาที",
        "ง": "Bupropion เพิ่มความเสี่ยงต่อการชัก (Dose-dependent seizure risk) โดยเฉพาะในขนาดที่เกิน 300 mg/วัน หรือในผู้ที่มีภาวะ Electrolyte imbalance หรือถอนแอลกอฮอล์",
        "จ": "ตัวเลือก ถูกทุกข้อ ไม่ถูกต้องเนื่องจากข้อความในแต่ละตัวเลือกมีรายละเอียดเชิงปฏิบัติการและเภสัชวิทยาที่เฉพาะเจาะจงแตกต่างกันตามแนวทางการเลิกบุหรี่สากล"
    }
}

# ----------------- KEY 53 -----------------
# Q: ยาในกลุ่มใดที่เป็นยาทางเลือกแรก ในการรักษาภาวะซึมเศร้าในกลุ่มที่ไม่มีข้อห้ามใช้
# c1: TCA (Ans: 1 -> ก)
# Wrong: ข: SNRI, ค: SSRI, ง: BZPs, จ: SDRI
distractors_part2["53"] = {
    "distractors": {
        "ข": "SNRIs (เช่น Venlafaxine, Duloxetine) เป็นยาที่มีประสิทธิภาพสูง จัดเป็น First-line หรือ Second-line ร่วมกับ SSRIs แต่มักเลือกใช้เมื่อมีอาการปวดเส้นประสาทร่วมด้วย หรือไม่ตอบสนองต่อ SSRI ตัวแรก",
        "ค": "SSRIs (เช่น Sertraline, Escitalopram) เป็นยาทางเลือกแรกมาตรฐานระดับสากล (First-line therapy) ในการรักษาโรคซึมเศร้าตามแนวทาง APA และ CANMAT เนื่องจากมี Efficacy สูง ปลอดภัยต่อหัวใจ และเสี่ยงพิษเมื่อกินเกินขนาดต่ำกว่า TCAs",
        "ง": "Benzodiazepines (BZPs) ออกฤทธิ์ผ่าน GABAA receptor ช่วยลดความวิตกกังวลและช่วยให้นอนหลับในระยะสั้นเท่านั้น ไม่มีคุณสมบัติในการรักษาอาการซึมเศร้า (No antidepressant effect) และเสี่ยงต่อการดื้อยาและติดยา",
        "จ": "SDRI (Selective Dopamine Reuptake Inhibitors) ไม่ใช่กลุ่มยาต้านซึมเศร้ามาตรฐานทางจิตเวช โดยยาที่ออกฤทธิ์ต่อ Dopamine จะเป็นกลุ่ม NDRI (เช่น Bupropion) ซึ่งยับยั้งทั้ง NE และ Dopamine"
    }
}

# ----------------- KEY 54 -----------------
# Q: นักศึกษาชายไทยอายุ 21 ปี... เครียดจากการสอบ นอนไม่หลับ วิตกกังวลเวลาเข้าสังคมหรือนำเสนองาน... ข้อใดคือยาที่เหมาะสมในการรักษาผู้ป่วยรายนี้
# c1: Clozapine (Ans: 1 -> ก)
# Wrong: ข: Fluoxetine, ค: Lorazepam, ง: Clonazepam, จ: Amitriptyline
distractors_part2["54"] = {
    "distractors": {
        "ข": "Fluoxetine เป็นยาต้านซึมเศร้ากลุ่ม SSRI ที่มีฤทธิ์กระตุ้นระบบประสาท (Activating SSRI) ในช่วงสัปดาห์แรกของการรักษาอาจกระตุ้นให้เกิด Agitation, Anxiety และทำให้นอนไม่หลับมากขึ้น ทั้งยังต้องใช้เวลา 2-4 สัปดาห์จึงจะเริ่มเห็นผล",
        "ค": "Lorazepam เป็นยาคลายกังวลกลุ่ม Benzodiazepine ออกฤทธิ์เร็ว เหมาะสำหรับบรรเทาความวิตกกังวลเฉียบพลันและช่วยให้นอนหลับในระยะสั้น (Short-term use ไม่เกิน 2-4 สัปดาห์) โดยปลอดภัยในผู้ป่วยโรคตับเนื่องจากผ่านกระบวนการ Glucuronidation โดยตรง",
        "ง": "Clonazepam เป็น High-potency Benzodiazepine ที่มี Half-life ยาวนาน ออกฤทธิ์ครอบคลุมอาการวิตกกังวลได้ตลอดทั้งวัน แต่มักทำให้เกิดอาการง่วงซึมตกค้างในตอนกลางวัน (Daytime sedation) ซึ่งอาจกระทบต่อการเรียน",
        "จ": "Amitriptyline เป็นยากลุ่ม TCA ที่มีฤทธิ์ Anticholinergic สูง ทำให้ปากแห้ง ตาพร่า ท้องผูก และส่งผลกระทบต่อสมาธิและความจำ (Cognitive impairment) ในวัยเรียน จึงไม่เหมาะเป็นยาทางเลือกแรก"
    }
}

# ----------------- KEY 55 -----------------
# Q: Fluoxetine จะถูก metabolized ที่ตำแหน่งใด เพื่อ เปลี่ยนเป็น norfluoxetine...
# c1: Fluoxetine 20 mg OD (Ans: 1 -> ก)
# Wrong: ข: Sertraline 50 mg OD, ค: Escitalopram 10 mg OD, ง: Venlafaxine 75 mg OD, จ: Amitriptyline 10 mg HS
distractors_part2["55"] = {
    "distractors": {
        "ข": "Sertraline เป็นยาต้านซึมเศร้ากลุ่ม SSRI ที่ถูกเมแทบอไลต์ผ่านกระบวนการ N-demethylation โดยเอนไซม์ CYP2B6 และ CYP2C19 ได้เป็น Desmethylsertraline ซึ่งออกฤทธิ์ต่ำ ไม่ใช่ชื่อตำแหน่งบนโครงสร้างโมเลกุลฟลูออกซีทีน",
        "ค": "Escitalopram ถูกเปลี่ยนเป็น S-demethylcitalopram โดยเอนไซม์ CYP2C19 และ CYP3A4 เป็นเภสัชภัณฑ์รักษาโรคซึมเศร้า ไม่ใช่ตัวระบุตำแหน่งอะตอมสำหรับการเกิด N-dealkylation ของ Fluoxetine",
        "ง": "Venlafaxine ถูกเมแทบอไลต์ผ่านเอนไซม์ CYP2D6 ไปเป็น O-desmethylvenlafaxine (Desvenlafaxine) ซึ่งเป็นสารออกฤทธิ์หลัก ไม่เกี่ยวข้องกับปฏิกิริยาเมแทบอลิซึมของ Fluoxetine",
        "จ": "Amitriptyline เป็น Tertiary amine TCA ที่ถูกเมแทบอไลต์ผ่าน N-demethylation เป็น Nortriptyline ซึ่งเป็น Secondary amine ไม่ใช่สารอนุพันธ์ของ Fluoxetine"
    }
}

# ----------------- KEY 57 -----------------
# Q: สถานการณ์ที่ 6... นอนหลับยากใช้เวลานานกว่าจะหลับ หากจะจ่ายยาท่านจะเลือกจ่ายยาในข้อใดจึงจะเหมาะสมที่สุด
# c2: Flurazepam (Ans: 2 -> ข)
# Wrong: ก: Lorazepam, ค: Temazepam, ง: Diazepam, จ: Chlorazepate...
distractors_part2["57"] = {
    "distractors": {
        "ก": "Lorazepam เป็น Intermediate-acting Benzodiazepine มีค่า Onset ปานกลาง (30-60 นาที) ไม่มี Active metabolites เด่นชัด เหมาะสำหรับผู้ป่วยที่มีปัญหาตื่นกลางดึกหรือโรควิตกกังวลมากกว่าการเหนี่ยวนำให้หลับอย่างรวดเร็ว",
        "ค": "Temazepam เป็น Benzodiazepine ที่มีอัตราการดูดซึมช้าและไม่มีทะเบียนยาในประเทศไทย จึงไม่สามารถเลือกจ่ายในบริบทของร้านยาแผนปัจจุบันได้",
        "ง": "Diazepam เป็น Long-acting Benzodiazepine ที่มีสารเมแทบอไลต์ออกฤทธิ์ยาวนาน (Nordiazepam half-life 40-100 ชั่วโมง) เสี่ยงต่ออาการง่วงซึมตกค้างในตอนกลางวัน (Daytime hangover effect) และการสะสมของยา",
        "จ": "Clorazepate เป็น Prodrug ของ Nordiazepam จัดเป็น Long-acting agent ที่เน้นออกฤทธิ์คลายกังวลต่อเนื่อง ไม่เหมาะสำหรับรักษาอาการนอนหลับยากเฉพาะจุดเริ่มต้น (Sleep onset insomnia)"
    }
}

# ----------------- KEY 58 -----------------
# Q: ชายไทยอายุ 65 ปีได้รับการวินิจฉัยจากแพทย์ว่ามีภาวะ Insomnia ยาใน ข้อใดต่อไปนี้ไม่ใช่ยาที่ใช้ในการรักษาภาวะ Insomnia
# c1: CPM (Ans: 1 -> ก)
# Wrong: ข: Phenobarbital, ค: Chloral hydrate, ง: Clonazepam, จ: Haloperidol (จ)
distractors_part2["58"] = {
    "distractors": {
        "ข": "Phenobarbital เป็นยากลุ่ม Barbiturate ที่กดระบบประสาทส่วนกลางผ่าน GABAA receptor ในอดีตเคยใช้เป็นยานอนหลับ แต่ปัจจุบันลดบทบาทลงเนื่องจากมี Narrow therapeutic window และเสี่ยงต่อ Respiratory depression รุนแรง",
        "ค": "Chloral hydrate เป็นยาสงบประสาทและยานอนหลับกลุ่ม Non-barbiturate รุ่นเก่าที่ถูกเปลี่ยนเป็น Trichloroethanol ออกฤทธิ์กดประสาท ช่วยเหนี่ยวนำการหลับในระยะสั้น",
        "ง": "Clonazepam เป็น Long-acting Benzodiazepine ที่มีฤทธิ์ Sedative และ Myorelaxant สามารถนำมาใช้ช่วยให้นอนหลับในผู้ป่วยที่มีภาวะตื่นตระหนกหรือ REM sleep behavior disorder ร่วมด้วย",
        "จ": "Haloperidol เป็น Typical antipsychotic ที่ออกฤทธิ์ปิดกั้น Dopamine D2 receptor ใน Mesolimbic pathway ใช้รักษาโรคจิตเภทเฉียบพลันและ Delirium ไม่มีข้อบ่งใช้สำหรับการรักษาภาวะนอนไม่หลับปฐมภูมิ และเสี่ยงต่อ Extrapyramidal symptoms (EPS) สูงมาก"
    }
}

# ----------------- KEY 59 -----------------
# Q: ข้อใดถูกต้องเกี่ยวกับโครงสร้างและความสัมพันธ์ในการออกฤทธิ์ของยานอนหลับ Diazepam...
# c1: Fluoxetine 20 mg OD (Ans: 1 -> ก)
# Wrong: ข: Sertraline 50 mg OD, ค: Escitalopram 10 mg OD, ง: Venlafaxine 75 mg OD, จ: Amitriptyline 10 mg HS
distractors_part2["59"] = {
    "distractors": {
        "ข": "Sertraline มีโครงสร้างทางเคมีเป็นอนุพันธ์ Tetrahydronaphthylamine ที่จับจำเพาะกับ Serotonin Transporter (SERT) ไม่มีความสัมพันธ์กับโครงสร้าง 1,4-Benzodiazepine ring ของ Diazepam",
        "ค": "Escitalopram มีโครงสร้างทางเคมีเป็น Phthalan derivative ที่ออกฤทธิ์ยับยั้ง SERT อย่างจำเพาะเจาะจงสูง ไม่เกี่ยวข้องกับโครงสร้างแกน Benzodiazepine หรือการจับกับ GABAA receptor",
        "ง": "Venlafaxine มีโครงสร้างเป็น Phenethylamine derivative ที่มีผลยับยั้งทั้ง SERT และ NET ไม่เกี่ยวข้องกับความสัมพันธ์ระหว่างโครงสร้างและการออกฤทธิ์ (SAR) ของกลุ่มยานอนหลับ Benzodiazepines",
        "จ": "Amitriptyline มีโครงสร้างเป็น Tricyclic dibenzocycloheptadiene ที่มีฤทธิ์ยับยั้ง NET และ SERT พร้อมกับปิดกั้น Muscarinic และ Histamine H1 receptors ไม่ใช่โครงสร้างของยากลุ่ม Benzodiazepines"
    }
}

# ----------------- KEY 61 -----------------
# Q: มีระยะเวลาในการออกฤทธิ์สั้นกว่า Diazepam เนื่องจากละลายในไขมันได้มากกว่า...
# c1: Alprazolam 0.5 mg HS (Ans: 1 -> ก)
# Wrong: ข: Diazepam 5 mg HS, ค: Zolpidem 10 mg HS, ง: Nicotine gum 2 mg PRN, จ: Quetiapine 25 mg HS
distractors_part2["61"] = {
    "distractors": {
        "ข": "Diazepam มีความสามารถในการละลายในไขมันสูงมาก (High lipid solubility) เข้าสู่สมองได้รวดเร็วแต่มีการกระจายตัวออกจากสมองไปยังเนื้อเยื่อไขมัน (Rapid redistribution) และมี Active metabolites ทำให้ค่าครึ่งชีวิตรวมยาวนานกว่า 40 ชั่วโมง",
        "ค": "Zolpidem เป็นสารกลุ่ม Imidazopyridine ที่จับอย่างจำเพาะกับ Alpha-1 subunit ของ GABAA receptor ออกฤทธิ์เร็วมากและมีค่าครึ่งชีวิตสั้นประมาณ 2-3 ชั่วโมง แต่ไม่ได้จัดอยู่ในกลุ่มโครงสร้าง Benzodiazepine ที่เปรียบเทียบในโจทย์",
        "ง": "Nicotine gum 2 mg เป็นรูปแบบยาเลิกบุหรี่ที่ดูดซึมผ่านเยื่อบุช่องปากเพื่อกระตุ้น Nicotinic acetylcholine receptors ในระบบประสาทส่วนกลาง ไม่ใช่ยากดประสาทส่วนกลางกลุ่ม Benzodiazepines",
        "จ": "Quetiapine เป็น Atypical antipsychotic ที่ออกฤทธิ์ต้านตัวรับ Dopamine และ Serotonin หลายชนิด มีฤทธิ์ทำให้ง่วงจาก Antihistamine effect แต่ไม่ใช่ยาที่มีกลไกหรือโครงสร้างแบบ Benzodiazepines"
    }
}

# ----------------- KEY 62 -----------------
# Q: มีระยะเวลาในการออกฤทธิ์สั้นกว่า Diazepam เนื่องจากสามารถถูกเมตาบอไลต์ได้เร็ว...
# c1: Nicotine gum 2 mg PRN (Ans: 1 -> ก)
# Wrong: ข: Quetiapine 25 mg HS, ค: Risperidone 2 mg OD, ง: Fluoxetine 20 mg OD, จ: Sertraline 50 mg OD
distractors_part2["62"] = {
    "distractors": {
        "ข": "Quetiapine เป็น Second-generation antipsychotic ที่ถูกเมแทบอไลต์ผ่าน CYP3A4 อย่างรวดเร็ว มีครึ่งชีวิตสั้น (ประมาณ 6-7 ชั่วโมง) แต่จัดเป็นยารักษาโรคจิตเภทและอารมณ์สองขั้ว ไม่ใช่ยากลุ่ม Benzodiazepines ที่เปรียบเทียบกับ Diazepam",
        "ค": "Risperidone ถูกเมแทบอไลต์ผ่านเอนไซม์ CYP2D6 ได้สารออกฤทธิ์คือ 9-hydroxyrisperidone (Paliperidone) ซึ่งมีค่าครึ่งชีวิตยาวนานร่วม 20-24 ชั่วโมง ไม่ใช่ยาออกฤทธิ์สั้น",
        "ง": "Fluoxetine ถูกเปลี่ยนเป็นสารเมแทบอไลต์ Norfluoxetine ซึ่งมีฤทธิ์และมีค่าครึ่งชีวิตยาวนานที่สุดในกลุ่มยาต้านซึมเศร้า (7-15 วัน) จึงตรงข้ามกับสารที่ถูกเมแทบอไลต์และกำจัดออกจากร่างกายได้อย่างรวดเร็ว",
        "จ": "Sertraline มีค่าครึ่งชีวิตประมาณ 26 ชั่วโมง และถูกเปลี่ยนเป็น Desmethylsertraline โดย CYP2C19 ซึ่งมีค่าครึ่งชีวิตยาวนานถึง 60-100 ชั่วโมง จึงไม่จัดเป็นยาที่มีระยะเวลาการออกฤทธิ์สั้นมาก"
    }
}

# ----------------- KEY 63 -----------------
# Q: มีระยะเวลาที่ยาออกฤทธิ์เร็วกว่า Diazepam เนื่องจากสามารถผ่าน BBB ได้ดี...
# c1: Fluoxetine 20 mg OD (Ans: 1 -> ก)
# Wrong: ข: Sertraline 50 mg OD, ค: Escitalopram 10 mg OD, ง: Venlafaxine 75 mg OD, จ: Amitriptyline 10 mg HS
distractors_part2["63"] = {
    "distractors": {
        "ข": "Sertraline แม้จะผ่าน Blood-Brain Barrier ได้ดีตามคุณสมบัติการละลายในไขมัน แต่การออกฤทธิ์ในการรักษาโรคซึมเศร้าต้องอาศัยการปรับลดจำนวนตัวรับ (Receptor downregulation) ซึ่งต้องใช้เวลา 2-4 สัปดาห์ จึงไม่มี Onset ออกฤทธิ์สงบประสาทเฉียบพลันเทียบเท่า Benzodiazepines",
        "ค": "Escitalopram มีการกระจายตัวเข้าสู่สมองอย่างสม่ำเสมอแต่แสดงผลทางคลินิกในการปรับอารมณ์อย่างช้าๆ ผ่านการยับยั้ง SERT ไม่ใช่ยาที่ใช้เพื่อหวังผลกดประสาทเฉียบพลันภายในไม่กี่นาที",
        "ง": "Venlafaxine เป็นยาต้านซึมเศร้ากลุ่ม SNRI ที่ถูกดูดซึมได้ดีแต่ต้องใช้เวลาในการปรับสมดุลสารสื่อประสาทส่วนปลายและส่วนกลาง จึงไม่แสดงฤทธิ์ทางคลินิกทันทีเหมือนยากลุ่ม Sedative-hypnotics",
        "จ": "Amitriptyline ผ่านเข้าสู่สมองได้ดีและมีฤทธิ์ Sedative ภายในไม่กี่ชั่วโมงจากฤทธิ์ต้าน H1 แต่มีผลข้างเคียงต่อระบบประสาทอัตโนมัติและหัวใจสูงมาก จึงไม่นำมาใช้เป็นยาสงบประสาทฉุกเฉินแทน Diazepam"
    }
}

# ----------------- KEY 65 -----------------
# Q: ยาใดถูกถอนจากตลาดเนื่องจากทำให้เกิด serious psychiatric disorders (anxiety, depression, suicidal thinking) และยาใดสามารถจ่ายในร้านยาได้ตามลำดับ
# c1: Sibutramine, Lorcaserin (Ans: 1 -> ก)
# Wrong: ข: Rimonabant, Orlistat, ค: Phentermine, Orlistat, ง: Rimonabant, Lorcaserin, จ: Sibutramine, Orlistat...
distractors_part2["65"] = {
    "distractors": {
        "ข": "Rimonabant เป็น Cannabinoid CB1 receptor antagonist ที่ถูกเพิกถอนจากตลาดทั่วโลกเนื่องจากเพิ่มความเสี่ยงต่อ Severe depression และ Suicidal ideation อย่างรุนแรง ส่วน Orlistat เป็น Gastrointestinal lipase inhibitor ที่จ่ายในร้านยาได้ จึงเป็นคู่ยาที่ตรงตามข้อเท็จจริงทางพิษวิทยาและการขึ้นทะเบียน",
        "ค": "Phentermine เป็นยากลุ่ม Sympathomimetic amine ที่ถูกจัดเป็นวัตถุออกฤทธิ์ต่อจิตและประสาทประเภท 2 ในประเทศไทย จึงห้ามจำหน่ายในร้านขายยาทั่วไปและจ่ายได้เฉพาะในโรงพยาบาลหรือคลินิกเท่านั้น",
        "ง": "Lorcaserin เป็น 5-HT2C receptor agonist ที่ถูกถอนออกจากตลาดในเวลาต่อมาเนื่องจากพบความเสี่ยงต่อการเกิดโรคมะเร็ง (Increased cancer risk) ไม่ใช่ยาที่สามารถจ่ายได้ทั่วไปในร้านยา",
        "จ": "Sibutramine ถูกเพิกถอนออกจากตลาดเนื่องจากเพิ่มความเสี่ยงต่อภาวะกล้ามเนื้อหัวใจขาดเลือดและหลอดเลือดสมองอุดตัน (Major Adverse Cardiovascular Events - SCOUT trial) เป็นหลัก ไม่ใช่จากจิตเวชรุนแรงเหมือน Rimonabant"
    }
}

# ----------------- KEY 66 -----------------
# Q: ตอบ ข. Rimonabant, Orlistat เนื่องจาก Rimonabant เป็นยาที่ทำให้เกิดผลข้างเคียงทางระบบประสาทที่รุนแรง...
# c1: Nicotine gum 2 mg PRN (Ans: 1 -> ก)
# Wrong: ข: Quetiapine 25 mg HS, ค: Risperidone 2 mg OD, ง: Fluoxetine 20 mg OD, จ: Sertraline 50 mg OD
distractors_part2["66"] = {
    "distractors": {
        "ข": "Quetiapine เป็น Second-generation antipsychotic ที่มีฤทธิ์ต้านตัวรับ 5-HT2A และ D2 นิยมใช้รักษาโรคจิตเภทและอารมณ์สองขั้ว ไม่ใช่ยาลดความอ้วนและไม่มีข้อบ่งใช้หรือประวัติการถูกถอนทะเบียนจากผลกระทบทางจิตเวชข้างต้น",
        "ค": "Risperidone ออกฤทธิ์ปิดกั้นตัวรับ Serotonin 5-HT2A และ Dopamine D2 มีผลข้างเคียงเด่นเรื่อง Extrapyramidal symptoms ในขนาดสูงและภาวะ Hyperprolactinemia ไม่เกี่ยวข้องกับยาลดความอ้วนหรือการจ่ายในร้านยา",
        "ง": "Fluoxetine เป็นยาต้านซึมเศร้ากลุ่ม SSRI ที่ช่วยเพิ่มระดับ Serotonin ในสมอง ซึ่งเป็นยามาตรฐานในการรักษาโรคซึมเศร้า ไม่ใช่ยาที่ถูกถอนทะเบียนเนื่องจากชักนำให้เกิดความวิตกกังวลหรือคิดฆ่าตัวตายในประชากรทั่วไป",
        "จ": "Sertraline เป็น First-line antidepressant สำหรับรักษา Major Depressive Disorder และ Panic Disorder มีหลักฐานความปลอดภัยสูงในผู้ป่วยโรคหัวใจ ไม่เกี่ยวข้องกับการรักษาความอ้วนหรือการเพิกถอนยา"
    }
}

# ----------------- KEY 67 -----------------
# Q: Fluoxetine...
# c1: Fluoxetine 20 mg OD (Ans: 1 -> ก)
# Wrong: ข: Sertraline 50 mg OD, ค: Escitalopram 10 mg OD, ง: Venlafaxine 75 mg OD, จ: Amitriptyline 10 mg HS
distractors_part2["67"] = {
    "distractors": {
        "ข": "Sertraline 50 mg OD เป็นยาต้านซึมเศร้ากลุ่ม SSRI ที่มีผลยับยั้งเอนไซม์ CYP2D6 ต่ำกว่า Fluoxetine มาก จึงเกิดอันตรกิริยาระหว่างยาน้อยกว่า และเป็นยาทางเลือกแรกในผู้ป่วยโรคหัวใจ",
        "ค": "Escitalopram 10 mg OD เป็น S-enantiomer ที่มีความจำเพาะสูงสุดต่อ SERT แต่มีข้อจำกัดเรื่อง Dose-dependent QTc prolongation จึงจำกัดขนาดไม่เกิน 10 mg/วัน ในผู้สูงอายุ",
        "ง": "Venlafaxine 75 mg OD เป็นยาในกลุ่ม SNRI ที่ยับยั้งทั้ง Serotonin และ Norepinephrine reuptake อาจเพิ่มความดันโลหิต diastolic ได้ในขนาดสูง และเสี่ยงต่อ Discontinuation syndrome รุนแรงหากลืมรับประทานยา",
        "จ": "Amitriptyline 10 mg HS เป็นยาต้านซึมเศร้ากลุ่ม TCA ที่มีฤทธิ์ Anticholinergic, Antihistamine และ Alpha-1 blockade สูงมาก ทำให้เกิดอาการง่วงซึม ตาพร่า ท้องผูก และเสี่ยงต่อภาวะหัวใจเต้นผิดจังหวะ"
    }
}

# ----------------- KEY 69 -----------------
# Q: การใช้ Nicotine patch ในผู้ป่วยที่สูบบุหรี่ 15 มวนต่อวัน ข้อใดเหมาะสมที่สุด
# c1: Alprazolam 0.5 mg HS (Ans: 1 -> ก)
# Wrong: ข: Diazepam 5 mg HS, ค: Zolpidem 10 mg HS, ง: Nicotine gum 2 mg PRN, จ: Quetiapine 25 mg HS
distractors_part2["69"] = {
    "distractors": {
        "ข": "Diazepam เป็นยานอนหลับและคลายกังวลกลุ่ม Long-acting Benzodiazepine มีความเสี่ยงต่อการสะสมยาและกดประสาทส่วนกลาง ไม่ใช่แนวทางการรักษามาตรฐานในการบำบัดผู้ติดบุหรี่",
        "ค": "Zolpidem เป็นยากลุ่ม Z-drug สำหรับรักษาโรคนอนไม่หลับระยะสั้น ออกฤทธิ์จำเพาะต่อ GABAA Alpha-1 subunit ไม่มีบทบาทในการทดแทนนิโคตินหรือลดความอยากบุหรี่",
        "ง": "Nicotine gum 2 mg PRN เป็นรูปแบบยาเคี้ยวสำรอง (Short-acting NRT) ที่แนะนำให้ใช้ร่วมกับ Nicotine patch (Combination NRT) เพื่อควบคุมอาการอยากบุหรี่แบบเฉียบพลัน (Craving breakthrough) ได้อย่างมีประสิทธิภาพ",
        "จ": "Quetiapine เป็นยาต้านโรคจิตรุ่นที่สองที่มีผลข้างเคียงเรื่องน้ำหนักตัวเพิ่ม ง่วงซึม และรบกวนระบบเมแทบอลิซึม ไม่มีข้อบ่งใช้สำหรับการช่วยเลิกบุหรี่ในผู้ป่วยทั่วไป"
    }
}

# ----------------- KEY 70 -----------------
# Q: ข้อใดไม่ใช่ยาที่แนะนำให้ใช้ในผู้ป่วยที่ต้องการเลิกบุหรี่
# c1: Nicotine gum 2 mg PRN (Ans: 1 -> ก)
# Wrong: ข: Quetiapine 25 mg HS, ค: Risperidone 2 mg OD, ง: Fluoxetine 20 mg OD, จ: Sertraline 50 mg OD
distractors_part2["70"] = {
    "distractors": {
        "ข": "Quetiapine เป็น Second-generation antipsychotic ที่ออกฤทธิ์ปิดกั้น 5-HT2A และ D2 receptors ไม่มียืนยันทางคลินิกในการช่วยเลิกบุหรี่ และมีผลข้างเคียงเรื่อง Metabolic syndrome และง่วงซึมมาก",
        "ค": "Risperidone เป็นยารักษาโรคจิตเภทที่อาจเพิ่มระดับโปรแลกตินและทำให้เกิดอาการทางระบบกล้ามเนื้อ Extrapyramidal symptoms จึงไม่มีข้อบ่งใช้หรือบทบาทใดๆ ในกระบวนการเลิกบุหรี่",
        "ง": "Fluoxetine เป็นยาต้านซึมเศร้ากลุ่ม SSRI แม้จะมีประโยชน์ในผู้ป่วยเลิกบุหรี่ที่มีภาวะซึมเศร้าร่วมด้วย แต่ไม่ได้จัดเป็น First-line หรือ Second-line smoking cessation pharmacotherapy ตามแนวทางสากล",
        "จ": "Sertraline เป็นยาต้านซึมเศร้ากลุ่ม SSRI ที่ไม่มีข้อบ่งใช้โดยตรงในการช่วยเลิกบุหรี่ การศึกษาทางคลินิกพบว่าไม่ได้เพิ่มอัตราการเลิกบุหรี่ในระยะยาวเมื่อเทียบกับ Bupropion หรือ Varenicline"
    }
}

# ----------------- KEY 71 -----------------
# Q: ในผู้ป่วยที่ต้องการเลิกบุหรี่... สูบบุหรี่วันละ 3 ซอง เคยปรับพฤติกรรมไม่สำเร็จ และมีโรคร่วมคือโรคซึมเศร้า การรักษาในข้อใดเหมาะสมที่สุดในการเลิกบุหรี่
# c1: Fluoxetine 20 mg OD (Ans: 1 -> ก)
# Wrong: ข: Sertraline 50 mg OD, ค: Escitalopram 10 mg OD, ง: Venlafaxine 75 mg OD, จ: Amitriptyline 10 mg HS
distractors_part2["71"] = {
    "distractors": {
        "ข": "Sertraline เป็นยาต้านซึมเศร้าขนานแรกที่มีความปลอดภัยสูง แต่ไม่มีหลักฐานชัดเจนในการช่วยลดอาการถอนนิโคตินหรือเพิ่มอัตราความสำเร็จในการเลิกบุหรี่ได้เท่ากับ Bupropion",
        "ค": "Escitalopram มีประสิทธิภาพสูงในการควบคุมอาการซึมเศร้าและโรควิตกกังวล แต่ไม่มีฤทธิ์ยับยั้ง Dopamine reuptake ใน Reward pathway จึงไม่ช่วยลดความอยากสูบบุหรี่โดยตรง",
        "ง": "Venlafaxine เป็นยากลุ่ม SNRI ที่มีประสิทธิภาพดีใน Major Depression แต่ยังไม่ใช่ยาหลักที่ได้รับการรับรองจาก US FDA หรือ CPG สากลในการเป็นยาเดี่ยวสำหรับเลิกบุหรี่",
        "จ": "Amitriptyline เป็นยากลุ่ม TCA ที่อาจช่วยลดความตึงเครียดแต่มีผลข้างเคียง Anticholinergic สูงมาก น้ำหนักตัวขึ้น และเสี่ยงอันตรายต่อหัวใจ จึงเป็นตัวเลือกที่ด้อยกว่าในการรักษาโรคร่วมซึมเศร้าและเลิกบุหรี่"
    }
}

# ----------------- KEY 73 -----------------
# Q: ผู้ป่วยที่ไม่ควรได้รับ Varenicline ในการช่วยเลิกบุหรี่ คือข้อใด
# c1: Alprazolam 0.5 mg HS (Ans: 1 -> ก)
# Wrong: ข: Diazepam 5 mg HS, ค: Zolpidem 10 mg HS, ง: Nicotine gum 2 mg PRN, จ: Quetiapine 25 mg HS
distractors_part2["73"] = {
    "distractors": {
        "ข": "Diazepam เป็นยากลุ่ม Benzodiazepine ที่มีผลกดประสาทส่วนกลางและกล้ามเนื้อ ไม่ใช่ข้อห้ามใช้จำเพาะของ Varenicline แต่ผู้ป่วยควรระวังเรื่องการกดระบบประสาทหากดื่มแอลกอฮอล์ร่วมด้วย",
        "ค": "Zolpidem เป็นยานอนหลับกลุ่ม Z-drug ซึ่งการใช้ร่วมกับ Varenicline อาจเพิ่มความเสี่ยงต่อการเกิดฝันร้าย พฤติกรรมการนอนผิดปกติ (Parasomnias) หรือ Sleep-walking จึงต้องเฝ้าระวังอย่างใกล้ชิด",
        "ง": "Nicotine gum 2 mg เป็นยาบำบัดทดแทนนิโคติน ซึ่งไม่แนะนำให้ใช้ควบคู่กับ Varenicline เป็นประจำ เนื่องจาก Varenicline เป็น Partial agonist ที่จับกับตัวรับชนิดเดียวกันและอาจแย่งจับจนลดประสิทธิภาพหรือเพิ่มผลข้างเคียงคลื่นไส้",
        "จ": "Quetiapine บ่งชี้ถึงผู้ป่วยที่มีโรคจิตเวชรุนแรง เช่น Schizophrenia หรือ Bipolar disorder ซึ่ง Varenicline เคยมี Black box warning เรื่องการกระตุ้น Neuropsychiatric symptoms, ซึมเศร้า หรือพฤติกรรมก้าวร้าว จึงต้องติดตามประเมินสภาพจิตอย่างเข้มงวด"
    }
}

# ----------------- KEY 74 -----------------
# Q: มีประวัติโรคซึมเศร้า...
# c1: Nicotine gum 2 mg PRN (Ans: 1 -> ก)
# Wrong: ข: Quetiapine 25 mg HS, ค: Risperidone 2 mg OD, ง: Fluoxetine 20 mg OD, จ: Sertraline 50 mg OD
distractors_part2["74"] = {
    "distractors": {
        "ข": "Quetiapine เป็น Atypical antipsychotic ที่ใช้รักษา Bipolar depression หรือเป็นยาเสริมใน Major Depression แต่ไม่ใช่ยาหลักทางเลือกแรกเดี่ยวๆ สำหรับ Unipolar depression ที่ไม่มีอาการทางจิต",
        "ค": "Risperidone เป็น Second-generation antipsychotic ที่ใช้รักษาโรคจิตเภทเป็นหลัก หากนำมาใช้ในโรคซึมเศร้าจะใช้เป็น Adjunctive therapy ในรายที่ดื้อต่อการรักษาเท่านั้น ไม่ใช่ยาเดี่ยวมาตรฐาน",
        "ง": "Fluoxetine เป็นยาต้านซึมเศร้ากลุ่ม SSRI ที่ได้รับการรับรองให้เป็น First-line treatment ใน Major Depressive Disorder มีประสิทธิผลสูงและช่วยลดความเสี่ยงต่อการกลับเป็นซ้ำของโรคซึมเศร้า",
        "จ": "Sertraline เป็นยาต้านซึมเศร้ากลุ่ม SSRI ที่ปลอดภัยสูงต่อหัวใจและหลอดเลือด เหมาะอย่างยิ่งสำหรับผู้ป่วยซึมเศร้าทุกกลุ่มรวมถึงผู้สูงอายุและผู้ป่วยที่มีโรคร่วมทางกาย"
    }
}

# ----------------- KEY 75 -----------------
# Q: Zolpidem จากกรณีศึกษาจงตอบคำถามข้อ 25-26 หญิงไทยอายุ 45 ปี ช่วงนี้เครียดนอนไม่หลับมาหลายวัน ต้องใช้เวลานานกว่าจะหลับแต่ถ้าหลับแล้วจะหลับได้ ตลอดทั้งคืน
# c1: Fluoxetine 20 mg OD (Ans: 1 -> ก)
# Wrong: ข: Sertraline 50 mg OD, ค: Escitalopram 10 mg OD, ง: Venlafaxine 75 mg OD, จ: Amitriptyline 10 mg HS
distractors_part2["75"] = {
    "distractors": {
        "ข": "Sertraline เป็นยากลุ่ม SSRI ที่ต้องใช้เวลาออกฤทธิ์ทางคลินิกหลายสัปดาห์ และอาจกระตุ้นให้เกิดอาการนอนไม่หลับ (Insomnia) ในช่วงเริ่มต้นการรักษา จึงไม่เหมาะสมสำหรับภาวะนอนไม่หลับเฉียบพลัน",
        "ค": "Escitalopram เป็นยาต้านซึมเศร้าที่เน้นการรักษาภาวะซึมเศร้าและโรควิตกกังวลระยะยาว ไม่มียาในรูปแบบออกฤทธิ์เร็วสำหรับเหนี่ยวนำการนอนหลับเฉพาะคราว",
        "ง": "Venlafaxine เป็นยากลุ่ม SNRI ที่มีคุณสมบัติกระตุ้นระบบประสาทผ่านการเพิ่มระดับ Norepinephrine ทำให้หัวใจเต้นเร็ว ตื่นตัว และรบกวนการนอนหลับมากขึ้น",
        "จ": "Amitriptyline แม้จะมีฤทธิ์ช่วยให้นอนหลับจากผล Antihistamine H1 blockade แต่มีผลข้างเคียง Anticholinergic สูงมาก ทำให้ตื่นมามีอาการง่วงซึม ปากแห้ง ท้องผูก และเสี่ยงต่อการกดการทำงานของหัวใจ"
    }
}

# ----------------- KEY 76 -----------------
# Q: กลไกการออกฤทธิ์ของยากลุ่ม Benzodiazepines คือข้อใด
# c1: . กระตุ้น 5-HT receptor (Ans: 1 -> ก)
# Wrong: ข: . กระตุ้น Dopamine receptor, ค: . กระตุ้น GABA receptor..., ง: . กระตุ้น Glutamate receptor, จ: Diazepam 5 mg HS
distractors_part2["76"] = {
    "distractors": {
        "ข": "การกระตุ้น Dopamine receptor เป็นกลไกของยากลุ่ม Dopamine agonists เช่น Bromocriptine หรือ Pramipexole ที่ใช้รักษาโรคพาร์กินสัน การกระตุ้นโดปามีนจะทำให้เกิดการตื่นตัวและอาจกระตุ้นอาการจิตเภท",
        "ค": "ยากลุ่ม Benzodiazepines ออกฤทธิ์จับกับ Allosteric site บน GABAA receptor ช่วยเพิ่มความถี่ในการเปิดของ Chloride channel (Increase frequency of channel opening) ทำให้เกิด Hyperpolarization และยับยั้งการทำงานของเซลล์ประสาท",
        "ง": "Glutamate เป็นสารสื่อประสาทชนิดกระตุ้นหลัก (Excitatory neurotransmitter) ในระบบประสาทส่วนกลาง การกระตุ้น Glutamate receptors (NMDA, AMPA) จะทำให้เซลล์ประสาทตื่นตัวและเสี่ยงต่อการชักหรือเกิด Excitotoxicity",
        "จ": "Diazepam เป็นชื่อตัวยาในกลุ่ม Long-acting Benzodiazepine ที่มีคุณสมบัติ Sedative, Hypnotic, Anxiolytic, Anticonvulsant และ Muscle relaxant เป็นชื่อยาทางเภสัชกรรม ไม่ใช่คำอธิบายกลไกทางชีวเคมีระดับตัวรับ"
    }
}

# Verify count
print(f"Total keys generated: {len(distractors_part2)}")

# Check for asterisks
has_asterisk = False
for k, v in distractors_part2.items():
    for ltr, text in v["distractors"].items():
        if "*" in text:
            print(f"ASTERISK FOUND in {k} - {ltr}: {text}")
            has_asterisk = True

if not has_asterisk:
    print("Verification PASSED: ZERO asterisks found in any text!")

# Save to distractors_psych_part2.json
output_path = r"C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\distractors_psych_part2.json"
with open(output_path, "w", encoding="utf-8") as f:
    json.dump(distractors_part2, f, ensure_ascii=False, indent=2)

print("Saved successfully to", output_path)
