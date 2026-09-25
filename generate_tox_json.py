#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generate 40 High-Yield Pristine Toxicology & Poisoning Exam Questions
for PLE-CC Licensure Exam Prep.
All questions adhere strictly to:
- No asterisks (* or **)
- Clean plain text format
- Authentic Guideline references (Ramathibodi Poison Center / Thai Society of Clinical Toxicology)
- Realistic distractors with thorough pharmacological rationales
"""

import json, sys

questions = [
    # 1. Paracetamol / APAP Toxicity
    {
        "q": "ผู้ป่วยหญิงไทยอายุ 22 ปี น้ำหนัก 50 กิโลกรัม ถูกนำส่งห้องฉุกเฉินหลังรับประทานยาพาราเซตามอล (500 มก./เม็ด) จำนวน 30 เม็ด (15 กรัม หรือ 300 มก./กก.) โดยรับประทานรวดเดียวเมื่อ 6 ชั่วโมงก่อนมาโรงพยาบาล ตรวจระดับ Serum Paracetamol ได้ 180 mcg/mL ข้อใดเป็นแนวทางการรักษาที่ถูกต้องและเหมาะสมที่สุด",
        "c1": "เริ่มให้ N-acetylcysteine (NAC) ทางหลอดเลือดดำทันทีตามเกณฑ์ Rumack-Matthew nomogram",
        "c2": "ให้ Activated charcoal 50 กรัม รับประทานทันทีเพื่อลดการดูดซึมยา",
        "c3": "รอตรวจซ้ำ Serum Paracetamol ที่ 12 ชั่วโมงหลังรับประทานยาก่อนตัดสินใจให้ยาต้านพิษ",
        "c4": "ให้การรักษาแบบประคับประคองและติดตามค่า AST/ALT ทุก 24 ชั่วโมงโดยไม่ต้องให้ยาต้านพิษ",
        "c5": "ทำ Gastric lavage ร่วมกับให้ Sodium bicarbonate ทางหลอดเลือดดำ",
        "ans": 1,
        "subtopic": "Paracetamol Toxicity",
        "cat": "Clinic",
        "note": "Rumack-Matthew Nomogram & NAC Protocol",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. เริ่มให้ N-acetylcysteine (NAC) ทางหลอดเลือดดำทันทีตามเกณฑ์ Rumack-Matthew nomogram

💡 Background:
ภาวะพิษจากพาราเซตามอลเกินขนาด (Paracetamol toxicity) เกิดจากกลไกการเกิดสารพิษ N-acetyl-p-benzoquinone imine (NAPQI) ผ่าน CYP2E1 เมื่อ Glutathione ในตับถูกใช้จนหมด NAPQI จะจับกับ hepatic macromolecules เกิด centrilobular hepatic necrosis การประเมินความเสี่ยงต่อตับอักเสบเฉียบพลันหลังกินยาเดี่ยวครั้งเดียว (single acute ingestion) ระหว่าง 4-24 ชั่วโมง ใช้ Rumack-Matthew nomogram โดย treatment line อยู่ที่ 150 mcg/mL ที่ 4 ชั่วโมง และ 75 mcg/mL ที่ 8 ชั่วโมง (เส้น 180 mcg/mL ที่ 6 ชั่วโมงอยู่เหนือ treatment line)

🎯 ทำไมข้อนี้ถึงถูก:
ระดับ Serum Paracetamol ของผู้ป่วยเท่ากับ 180 mcg/mL ที่ 6 ชั่วโมง ซึ่งอยู่เหนือเส้น Treatment line (ประมาณ 100-110 mcg/mL ที่ 6 ชั่วโมง) จึงมีข้อบ่งชี้ชัดเจนในการให้ N-acetylcysteine (NAC) ทันทีเพื่อเติมหมู่ Sulfhydryl เพิ่มการสังเคราะห์ Glutathione และเปลี่ยน NAPQI เป็นสารที่ไม่เป็นพิษ (Mercapturic acid) ป้องกันภาวะตับวายเฉียบพลัน

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Activated charcoal มีประโยชน์สูงสุดเมื่อให้ภายใน 1-2 ชั่วโมงหลังรับประทานยา การให้ที่ 6 ชั่วโมงมียาเคลื่อนผ่านกระเพาะอาหารไปแล้วและไม่มีประโยชน์ทางคลินิก
• ข้อ ค. การรอตรวจซ้ำที่ 12 ชั่วโมงทำให้การเริ่ม NAC ล่าช้า ประสิทธิภาพของ NAC จะสูงสุดเมื่อเริ่มให้ภายใน 8 ชั่วโมงแรกหลังกินยา
• ข้อ ง. ผู้ป่วยมีระดับยาอยู่ในเกณฑ์เสี่ยงสูงต่อตับวายเฉียบพลัน การรักษาแบบประคับประคองโดยไม่ให้ NAC ถือเป็นข้อผิดพลาดร้ายแรง
• ข้อ จ. Gastric lavage มีข้อบ่งชี้เฉพาะภายใน 1 ชั่วโมงแรกในกรณีที่รับประทานยาปริมาณสูงมากและไม่มีข้อห้าม และ Sodium bicarbonate ไม่มีบทบาทในการขับพาราเซตามอล

📖 Guideline อ้างอิง:
แนวทางการดูแลรักษาผู้ป่วยภาวะพิษจากพาราเซตามอล ศูนย์พิษวิทยารามาธิบดี และ American College of Medical Toxicology (ACMT) Practice Guideline

📌 จุดจำก่อนสอบ:
• Single acute overdose เกณฑ์เริ่มประเมิน nomogram ที่ 4 ชั่วโมง (treatment line: 150 mcg/mL at 4 hr)
• NAC มีประสิทธิภาพป้องกันตับวาย 100% หากได้รับภายใน 8 ชั่วโมงแรกหลังรับประทานยา
• ผู้ป่วย High-risk (พิษสุราเรื้อรัง, ทุพโภชนาการ, ใช้ยากระตุ้น CYP2E1 เช่น Isoniazid, Phenytoin) มีความเสี่ยงต่อตับวายสูงกว่าปกติ"""
    },
    {
        "q": "ผู้ป่วยชายอายุ 25 ปี รับประทานยา Paracetamol เกินขนาดและได้รับการรักษาด้วย Intravenous N-acetylcysteine (NAC) ขนาด 150 mg/kg ทางหลอดเลือดดำ ระหว่างเริ่มหยดยาได้ 15 นาที ผู้ป่วยมีอาการหน้าแดง คัน มีผื่นลมพิษ (Urticaria) ขึ้นตามแขนและลำตัว แต่ความดันโลหิตปกติ (120/80 mmHg) หายใจปกติ ไม่มีเสียง Wheezing ข้อใดคือการจัดการที่ถูกต้องที่สุด",
        "c1": "หยุดหยดยา NAC ชั่วคราว ให้ Chlorpheniramine ฉีดเข้าหลอดเลือดดำ และเริ่มหยด NAC ต่อในอัตราที่ช้าลงเมื่ออาการดีขึ้น",
        "c2": "หยุดยา NAC ถาวรทันทีและเปลี่ยนเป็น Activated charcoal ทางสายยาง",
        "c3": "ฉีด Adrenaline (Epinephrine) 0.5 mg เข้ากล้ามเนื้อทันทีเนื่องจากเป็น Anaphylaxis",
        "c4": "เพิ่มอัตราเร็วการหยดยา NAC ให้หมดเร็วขึ้นเพื่อรีบขับพิษออกจากร่างกาย",
        "c5": "ให้ Hydrocortisone 100 mg IV และส่งผู้ป่วยเข้าห้องผ่าตัดเพื่อปลูกถ่ายตับฉุกเฉิน",
        "ans": 1,
        "subtopic": "Paracetamol Toxicity",
        "cat": "Clinic",
        "note": "NAC Non-IgE Anaphylactoid Reaction",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. หยุดหยดยา NAC ชั่วคราว ให้ Chlorpheniramine ฉีดเข้าหลอดเลือดดำ และเริ่มหยด NAC ต่อในอัตราที่ช้าลงเมื่ออาการดีขึ้น

💡 Background:
อาการไม่พึงประสงค์จากการให้ Intravenous N-acetylcysteine ที่พบได้บ่อย (10-20%) คือ ปฏิกิริยาแบบ Non-IgE-mediated anaphylactoid reaction ซึ่งเกิดจากการหลั่ง Histamine โดยตรง มักเกิดขึ้นระหว่างการให้ Loading dose (ชั่วโมงแรก) อาการแสดงมีตั้งแต่ผื่นแดง คัน ลมพิษ ไปจนถึงหลอดลมหดเกร็งหรือความดันโลหิตต่ำ

🎯 ทำไมข้อนี้ถึงถูก:
ในผู้ป่วยที่มีอาการเพียงผื่นลมพิษและคัน (Mild to Moderate reaction) โดยไม่มีภาวะความดันโลหิตต่ำหรือหลอดลมหดเกร็ง แนวทางปฏิบัติมาตรฐานคือการหยุดหยดยาชั่วคราว ให้ยาแก้แพ้กลุ่ม H1-antihistamine (เช่น Chlorpheniramine IV) รอจนอาการสงบลง แล้วจึงเริ่มหยดยา NAC ต่อได้ด้วยอัตราเร็วที่ลดลงครึ่งหนึ่ง เนื่องจากประโยชน์ของการป้องกันตับวายจาก NAC มีความสำคัญยิ่งยวด

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. การหยุดยา NAC ถาวรจะทำให้ผู้ป่วยเสี่ยงต่อการเกิดภาวะตับวายเฉียบพลันและเสียชีวิต การเกิด Anaphylactoid reaction ไม่ใช่ข้อห้ามเด็ดขาดในการให้ NAC ต่อ
• ข้อ ค. Adrenaline มีข้อบ่งชี้เฉพาะ Severe anaphylaxis ที่มีระบบหายใจล้มเหลว (Wheezing, Stridor) หรือความดันโลหิตตก (Hypotension) ผู้ป่วยรายนี้มีเพียงอาการทางผิวหนังจึงยังไม่จำเป็นต้องใช้ Adrenaline
• ข้อ ง. การเพิ่มอัตราเร็วจะกระตุ้นการหลั่ง Histamine มากขึ้นและทำให้อาการแพ้รุนแรงขึ้นจนเกิดภาวะช็อกได้
• ข้อ จ. ผู้ป่วยรายนี้ยังไม่มีภาวะตับวายเฉียบพลัน (Hepatic encephalopathy หรือ Coagulopathy) จึงยังไม่มีข้อบ่งชี้ในการส่งปลูกถ่ายตับ

📖 Guideline อ้างอิง:
แนวทางการดูแลรักษาผู้ป่วยได้รับสารพิษ ศูนย์พิษวิทยารามาธิบดี และ European Association for the Study of the Liver (EASL) Clinical Practice Guidelines

📌 จุดจำก่อนสอบ:
• ปฏิกิริยาจาก IV NAC เป็น Anaphylactoid (Non-IgE mediated) สัมพันธ์กับอัตราการหยดยาที่เร็วเกินไป
• การจัดการ: หยุดยาชั่วคราว -> ให้ Antihistamine -> อาการทุเลาแล้วเริ่มให้ต่อในอัตราที่ช้าลง"""
    },
    # 2. Opioids Overdose
    {
        "q": "ผู้ป่วยชายอายุ 35 ปี มีประวัติใช้สารเสพติด ถูกพบนอนหมดสติข้างทาง หายใจช้าเพียง 4 ครั้งต่อนาที รูม่านตาหดเล็กเท่ารูเข็มทั้งสองข้าง (Pinpoint pupils: 1 mm) ตรวจพบรอยเข็มฉีดยาบริเวณแขน วัดสัญญาณชีพได้ BP 90/60 mmHg, PR 52 bpm, SpO2 78% ยาใดเป็น Antidote ทางเลือกแรกที่ต้องรีบให้เพื่อช่วยชีวิต",
        "c1": "Naloxone",
        "c2": "Flumazenil",
        "c3": "Atropine",
        "c4": "N-acetylcysteine",
        "c5": "Sodium bicarbonate",
        "ans": 1,
        "subtopic": "Opioid Toxicity",
        "cat": "Clinic",
        "note": "Opioid Toxidrome & Naloxone",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Naloxone

💡 Background:
อาการแสดงของผู้ป่วยรายนี้เป็นลักษณะคลาสสิกของ Opioid Toxidrome ซึ่งประกอบด้วยไตรแอด (Classic triad): 1) ซึมหมดสติ (CNS depression) 2) กดการหายใจ (Respiratory depression: RR < 8-10/min) และ 3) รูม่านตาหดเล็ก (Pinpoint pupils / Miosis) ภาวะแทรกซ้อนที่ทำให้เสียชีวิตทันทีคือการหยุดหายใจและภาวะพร่องออกซิเจนอย่างรุนแรง

🎯 ทำไมข้อนี้ถึงถูก:
Naloxone เป็น Pure opioid receptor competitive antagonist ที่ออกฤทธิ์แย่งจับกับ mu-opioid receptor อย่างจำเพาะ สามารถกู้คืนการหายใจและระดับความรู้สึกตัวได้อย่างรวดเร็วภายใน 1-2 นาทีหลังฉีดทางหลอดเลือดดำ (IV)

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Flumazenil เป็น Antidote สำหรับ Benzodiazepine overdose การให้ในผู้ป่วยที่อาจใช้สารเสพติดผสมเสี่ยงต่อการชักรุนแรง (Withdrawal seizure) และไม่ได้แก้อาการกดการหายใจจาก Opioid
• ข้อ ค. Atropine เป็น Anticholinergic drug ใช้รักษา Bradycardia หรือ Organophosphate poisoning ไม่มีผลต้านฤทธิ์กดการหายใจของ Opioid
• ข้อ ง. N-acetylcysteine เป็น Antidote สำหรับ Paracetamol toxicity
• ข้อ จ. Sodium bicarbonate ใช้รักษาพิษจาก Cyclic antidepressants หรือยาที่บล็อก Sodium channel

📖 Guideline อ้างอิง:
American Heart Association (AHA) Guidelines for Cardiopulmonary Resuscitation and Emergency Cardiovascular Care: Opioid-Associated Emergency

📌 จุดจำก่อนสอบ:
• Opioid triad: Unconscious + Respiratory depression + Pinpoint pupils
• Naloxone IV/IM/Intranasal: เป้าหมายการรักษาคือฟื้นฟูการหายใจให้เพียงพอ (RR > 10-12/min) ไม่จำเป็นต้องให้จนผู้ป่วยตื่นเต็มที่เพื่อป้องกัน Acute withdrawal syndrome
• Half-life ของ Naloxone สั้น (30-90 นาที) สั้นกว่า Opioids ส่วนใหญ่ (เช่น Morphine, Methadone) จึงต้องเฝ้าระวังการกลับมาหยุดหายใจซ้ำ (Renarcotization)"""
    },
    {
        "q": "หลังจากฉีด Naloxone 0.4 mg IV ให้ผู้ป่วยที่สงสัยว่าได้รับยา Methadone เกินขนาด ผู้ป่วยกลับมารู้สึกตัวดี หายใจ 16 ครั้ง/นาที SpO2 98% ญาติขอรับผู้ป่วยกลับบ้านทันที เภสัชกรควรให้คำแนะนำแก่ทีมแพทย์อย่างไรเกี่ยวกับระยะเวลาการเฝ้าระวังอาการ",
        "c1": "ต้องสังเกตอาการในโรงพยาบาลอย่างน้อย 24-48 ชั่วโมง เนื่องจาก Methadone มีค่าครึ่งชีวิตยาวนานกว่า Naloxone มาก ผู้ป่วยอาจกลับมากดการหายใจซ้ำได้",
        "c2": "สามารถอนุญาตให้กลับบ้านได้ทันทีหากเดินทรงตัวได้ดี",
        "c3": "สังเกตอาการต่อเพียง 1 ชั่วโมง หากไม่ง่วงซึมสามารถกลับบ้านได้",
        "c4": "ให้ยา Naloxone ชนิดรับประทานกลับไปกินที่บ้านต่อเนื่อง 3 วัน",
        "c5": "เปลี่ยนยาเป็น Naltrexone ฉีดเข้ากล้ามเนื้อก่อนจำหน่ายออกจากโรงพยาบาล",
        "ans": 1,
        "subtopic": "Opioid Toxicity",
        "cat": "Clinic",
        "note": "Renarcotization risk with Methadone",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. ต้องสังเกตอาการในโรงพยาบาลอย่างน้อย 24-48 ชั่วโมง เนื่องจาก Methadone มีค่าครึ่งชีวิตยาวนานกว่า Naloxone มาก ผู้ป่วยอาจกลับมากดการหายใจซ้ำได้

💡 Background:
Pharmacokinetics ของ Antidote เปรียบเทียบกับสารพิษมีความสำคัญยิ่งยวด Naloxone มี Elimination half-life สั้นมากเพียง 30-90 นาที ในขณะที่ Methadone มีค่าครึ่งชีวิตยาวนานถึง 15-60 ชั่วโมง (เฉลี่ย 24-36 ชั่วโมง)

🎯 ทำไมข้อนี้ถึงถูก:
เมื่อฤทธิ์ของ Naloxone หมดลง (ประมาณ 1-2 ชั่วโมง) Methadone ที่ยังค้างอยู่ในร่างกายจะกลับมาจับกับ Opioid receptors ซ้ำ ทำให้เกิดภาวะ Renarcotization ส่งผลให้ผู้ป่วยกลับมาหมดสติและหยุดหายใจซ้ำจนเสียชีวิตได้ ดังนั้นจำเป็นต้อง Admit เฝ้าระวังอาการอย่างใกล้ชิดอย่างน้อย 24-48 ชั่วโมง และอาจต้องพิจารณาให้ Naloxone continuous IV infusion

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. และ ค. การจำหน่ายผู้ป่วยกลับบ้านเร็วเกินไปเป็นอันตรายถึงแก่ชีวิตเนื่องจากการหยุดหายใจซ้ำ
• ข้อ ง. Naloxone ทางการรับประทานมี First-pass metabolism สูงมากเกือบ 100% ทำให้ระดับยาในกระแสเลือดไม่เพียงพอและไม่มีรูปแบบยากินสำหรับภาวะฉุกเฉิน
• ข้อ จ. Naltrexone เป็น Long-acting opioid antagonist หากฉีดในผู้ป่วยที่เพิ่งได้รับ Opioid เกินขนาดจะกระตุ้นให้เกิด Severe precipitated withdrawal syndrome ที่รุนแรงและควบคุมได้ยาก

📖 Guideline อ้างอิง:
Goldfrank's Toxicologic Emergencies และแนวทางการดูแลผู้ได้รับพิษเฉียบพลัน ศูนย์พิษวิทยารามาธิบดี

📌 จุดจำก่อนสอบ:
• Methadone half-life = 24-36 ชั่วโมง, Naloxone half-life = 1-1.5 ชั่วโมง
• ภาวะ Renarcotization เกิดขึ้นเมื่อ Naloxone หมดฤทธิ์ก่อนสารพิษ ต้องตั้ง Continuous infusion หรือติดตามนานกว่าปกติ"""
    },
    # 3. Organophosphates & Carbamates
    {
        "q": "เกษตรกรชายอายุ 50 ปี ถูกนำส่งโรงพยาบาลหลังจากพ่นสารกำจัดศัตรูพืชในสวน มีอาการน้ำลายไหลยืด เหงื่อออกท่วมตัว น้ำตาไหล ถ่ายเหลว กลั้นปัสสาวะไม่ได้ หายใจเหนื่อยหอบ มีเสียง Rhonchi และ Wheezing ทั่วปอดทั้งสองข้าง ม่านตาหดเล็กขนาด 1.5 มม. ชีพจร 48 ครั้ง/นาที ยาใดเป็น Antidote ตัวแรกที่ต้องรีบให้เพื่อแก้ไขภาวะ Bronchorrhea และช่วยการหายใจ",
        "c1": "Atropine sulfate",
        "c2": "Pralidoxime (2-PAM)",
        "c3": "Diphenhydramine",
        "c4": "Salbutamol nebulizer",
        "c5": "Succinylcholine",
        "ans": 1,
        "subtopic": "Organophosphate Toxicity",
        "cat": "Clinic",
        "note": "Cholinergic Toxidrome & Atropine",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Atropine sulfate

💡 Background:
อาการแสดงของผู้ป่วยเกิดจากภาวะ Cholinergic Toxidrome หรือ Cholinergic crisis จากการยับยั้งเอนไซม์ Acetylcholinesterase ทำให้เกิดการสะสมของ Acetylcholine ที่ Muscarinic และ Nicotinic receptors จำด้วยตัวย่อ DUMBELS (Defecation, Urination, Miosis, Bronchorrhea/Bronchospasm/Bradycardia, Emesis, Lacrimation, Salivation) สาเหตุการเสียชีวิตหลักเกิดจากการขาดอากาศหายใจจากเสมหะและสารคัดหลั่งในหลอดลมปริมาณมหาศาล (Bronchorrhea) ร่วมกับหลอดลมหดเกร็ง (Bronchospasm)

🎯 ทำไมข้อนี้ถึงถูก:
Atropine เป็น Competitive muscarinic receptor antagonist ออกฤทธิ์ยับยั้ง Muscarinic effects โดยเฉพาะการลดสารคัดหลั่งในทางเดินหายใจ (Drying of pulmonary secretions) และขยายหลอดลม ถือเป็น First-line antidote ที่ต้องให้ทันทีเพื่อกู้ระบบทางเดินหายใจ โดยให้ในขนาดเริ่มต้น 1.8-3 mg IV และเพิ่มขนาดยาทุก 3-5 นาทีจนกระทั่งเข้าสู่ภาวะ Atropinization

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Pralidoxime (2-PAM) เป็น Cholinesterase reactivator ออกฤทธิ์ช่วยฟื้นฟูเอนไซม์และแก้ไขอาการทาง Nicotinic (เช่น กล้ามเนื้ออ่อนแรง Fasciculation) แต่การออกฤทธิ์ช้ากว่า ไม่สามารถลดเสมหะในปอดได้ทันที ต้องให้ควบคู่หรือหลัง Atropine
• ข้อ ค. Diphenhydramine มีฤทธิ์ Anticholinergic อ่อนๆ ไม่สามารถต้านฤทธิ์รุนแรงของ Cholinergic crisis ได้
• ข้อ ง. Salbutamol ช่วยขยายหลอดลมแต่ไม่สามารถยับยั้งการหลั่ง Bronchorrhea มหาศาลได้
• ข้อ จ. Succinylcholine เป็นข้อห้ามใช้เด็ดขาดในผู้ป่วย Organophosphate poisoning เนื่องจากถูกกำจัดโดย Plasma cholinesterase ทำให้เกิด prolonged paralysis ยาวนานหลายชั่วโมง

📖 Guideline อ้างอิง:
WHO Guidelines for the Management of Organophosphorus Pesticide Poisoning และแนวทางการรักษาภาวะพิษจากสารกำจัดแมลงกลุ่มยับยั้งโคลีนเอสเตอเรส ศูนย์พิษวิทยารามาธิบดี

📌 จุดจำก่อนสอบ:
• Endpoints of Atropinization (เป้าหมายของการให้ Atropine): Clear lung secretions (ปอดแห้งไม่มีเสียง Rhonchi/Crepitation), HR > 80 bpm, Systolic BP > 80 mmHg, Dry axillae
• ห้ามใช้ Miosis เป็นเกณฑ์หยุด Atropine เพราะรูม่านตาจะขยายช้าที่สุด"""
    },
    {
        "q": "ข้อใดเป็นข้อบ่งชี้และหลักการที่ถูกต้องในการใช้ Pralidoxime (2-PAM) ในผู้ป่วยที่ได้รับสารพิษกลุ่ม Organophosphates",
        "c1": "ควรให้โดยเร็วที่สุดก่อนเกิดกระบวนการ Aging ของเอนไซม์ Acetylcholinesterase โดยเฉพาะเพื่อลดอาการกล้ามเนื้ออ่อนแรง (Nicotinic symptoms)",
        "c2": "ให้เดี่ยวๆ โดยไม่ต้องให้ Atropine ร่วมด้วย",
        "c3": "ใช้ได้ผลดีเลิศและจำเป็นต้องให้ในผู้ป่วยที่ได้รับสารพิษกลุ่ม Carbamates ทุกราย",
        "c4": "ให้เฉพาะเมื่อผู้ป่วยมีอาการน้ำลายไหลและม่านตาหดเล็กเท่านั้น",
        "c5": "สามารถให้ทดแทนการล้างตัว (Decontamination) ในผู้ป่วยที่สัมผัสทางผิวหนังได้",
        "ans": 1,
        "subtopic": "Organophosphate Toxicity",
        "cat": "Clinic",
        "note": "Pralidoxime & Aging of AChE",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. ควรให้โดยเร็วที่สุดก่อนเกิดกระบวนการ Aging ของเอนไซม์ Acetylcholinesterase โดยเฉพาะเพื่อลดอาการกล้ามเนื้ออ่อนแรง (Nicotinic symptoms)

💡 Background:
Organophosphates จับกับเอนไซม์ Acetylcholinesterase แบบ Phosphorylation หากปล่อยไว้นานจะเกิดปฏิกิริยา Dealkylation ของโมเลกุลยา เรียกว่า Aging ทำให้พันธะระหว่างยากับเอนไซม์กลายเป็นพันธะโควาเลนต์ถาวรที่ไม่สามารถคืนกลับได้ (Irreversible inhibition)

🎯 ทำไมข้อนี้ถึงถูก:
Pralidoxime (2-PAM) มีหมู่ Oxime ที่มีความสามารถในการแย่งจับหมู่ฟอสเฟตออกจากเอนไซม์ ทำให้ฟื้นฟูเอนไซม์กลับมาทำงานได้ (Enzyme reactivation) ซึ่งมีประโยชน์หลักในการต้าน Nicotinic effects เช่น กล้ามเนื้ออ่อนแรง, Muscle fasciculation และ Respiratory muscle paralysis โดยต้องให้โดยเร็วที่สุดก่อนที่จะเกิดกระบวนการ Aging (ซึ่งอาจเกิดภายในไม่กี่นาทีถึงหลายสิบชั่วโมงขึ้นกับชนิดของสาร เช่น Soman เกิด Aging ในหลักนาที ส่วน Parathion หลายสิบชั่วโมง)

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. ต้องให้ Atropine เสมอเพื่อรักษา Muscarinic toxicity ที่เป็นอันตรายถึงชีวิต ห้ามให้ 2-PAM เดี่ยวๆ
• ข้อ ค. สารกลุ่ม Carbamates ยับยั้งเอนไซม์แบบ Carbamylation ซึ่งเกิดการสลายตัวคืนกลับได้เองตามธรรมชาติ (Spontaneous hydrolysis) ภายใน 24-48 ชั่วโมง และไม่เกิด Aging ดังนั้น Atropine เพียงอย่างเดียวมักเพียงพอ ไม่แนะนำให้ 2-PAM ใน Carbamate toxicity เป็นกิจวัตร
• ข้อ ง. อาการน้ำลายไหลและม่านตาหดเป็น Muscarinic effects ซึ่งตอบสนองต่อ Atropine ไม่ใช่ข้อบ่งชี้หลักของ 2-PAM
• ข้อ จ. การล้างตัว (Decontamination) ถอดเสื้อผ้า ล้างสบู่มีความจำเป็นอย่างยิ่งเพื่อป้องกันการดูดซึมยาต่อเนื่อง ยาแก้พิษไม่สามารถทดแทนการล้างตัวได้

📖 Guideline อ้างอิง:
แนวทางเวชปฏิบัติการรักษาภาวะเป็นพิษจากสารกำจัดศัตรูพืช กระทรวงสาธารณสุข และ Ramathibodi Poison Center Guideline

📌 จุดจำก่อนสอบ:
• Atropine แก้ Muscarinic (DUMBELS)
• 2-PAM แก้ Nicotinic (Fasciculation, Weakness) ก่อนเกิด Aging
• Carbamate ไม่เกิด Aging การให้ Atropine เพียงอย่างเดียวมักเพียงพอ"""
    },
    # 4. Methanol & Ethylene Glycol
    {
        "q": "ผู้ป่วยชายอายุ 45 ปี ถูกนำส่งโรงพยาบาลหลังดื่มสุรากลั่นเอง (เหล้าเถื่อน) มีอาการเมา คลื่นไส้อาเจียน ตามัว มองเห็นภาพเป็นสีขาวโพลนเหมือนอยู่ในพายุหิมะ (Snowstorm vision) ผลตรวจทางห้องปฏิบัติการพบ High anion gap metabolic acidosis (pH 7.15, HCO3 8 mEq/L, Anion gap 26 mEq/L) และ High osmolar gap ยาใดเป็น Antidote จำเพาะที่ยับยั้งการเปลี่ยนสารพิษนี้ไปเป็น Formic acid",
        "c1": "Fomepizole หรือ Ethanol 10% IV infusion",
        "c2": "Methylene blue",
        "c3": "Dimercaprol (BAL)",
        "c4": "Thiamine IV",
        "c5": "Deferoxamine",
        "ans": 1,
        "subtopic": "Toxic Alcohol",
        "cat": "Clinic",
        "note": "Methanol toxicity & Alcohol dehydrogenase",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Fomepizole หรือ Ethanol 10% IV infusion

💡 Background:
อาการตามัว Snowstorm vision ร่วมกับ High anion gap metabolic acidosis และประวัติดื่มเหล้ากลั่นเอง เป็นลักษณะจำเพาะของ Methanol poisoning ตัว Methanol เองมีพิษน้อย แต่ถูกเปลี่ยนโดยเอนไซม์ Alcohol dehydrogenase (ADH) กลายเป็น Formaldehyde และกลายเป็น Formic acid โดย Formate จะยับยั้ง Cytochrome oxidase ในไมโทคอนเดรีย ทำให้เกิดพิษต่อจอประสาทตาและเส้นประสาทตา (Optic neuropathy / Retinal toxicity) ทำให้ตาบอดถาวรและเกิดภาวะกรดรุนแรง

🎯 ทำไมข้อนี้ถึงถูก:
Antidote ในการรักษาพิษจาก Methanol (และ Ethylene glycol) คือ สารที่ยับยั้งเอนไซม์ Alcohol dehydrogenase (ADH) ได้แก่ Fomepizole (4-methylpyrazole) ซึ่งเป็น Competitive ADH inhibitor โดยตรง หรือ Ethanol ซึ่งมี Affinity ต่อ ADH สูงกว่า Methanol ถึง 10-20 เท่า เพื่อป้องกันไม่ให้เกิดสารพิษ Formic acid

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Methylene blue เป็น Antidote สำหรับภาวะ Methemoglobinemia
• ข้อ ค. Dimercaprol เป็น Chelating agent สำหรับพิษโลหะหนัก (Arsenic, Mercury, Lead)
• ข้อ ง. Thiamine ใช้รักษา Wernicke-Korsakoff encephalopathy หรือเป็น Co-factor เสริมใน Ethylene glycol poisoning (ไม่ใช่ตัวต้านพิษหลักของ Methanol)
• ข้อ จ. Deferoxamine เป็น Chelating agent สำหรับพิษจากธาตุเหล็ก (Iron overdose)

📖 Guideline อ้างอิง:
American Academy of Clinical Toxicology (AACT) Practice Guidelines on the Treatment of Methanol Poisoning

📌 จุดจำก่อนสอบ:
• Methanol metabolite = Formic acid (ทำให้เกิด High anion gap acidosis + Blindness / Snowstorm vision)
• Ethylene glycol metabolite = Oxalic acid (ทำให้เกิด Calcium oxalate crystals ในปัสสาวะ + Acute kidney injury)
• ทั้งสองภาวะรักษาด้วยการบล็อก ADH ด้วย Fomepizole หรือ Ethanol + เสริม Folic acid (ใน Methanol เพื่อช่วยขับ Formate) หรือ Thiamine/Pyridoxine (ใน Ethylene glycol)"""
    },
    {
        "q": "ในการรักษาภาวะพิษจาก Methanol นอกจากให้ Fomepizole หรือ Ethanol เพื่อยับยั้งเอนไซม์ Alcohol dehydrogenase แล้ว วิตามินใดที่ต้องให้เสริมเพื่อเร่งการสลาย Formic acid ให้กลายเป็น Carbon dioxide และน้ำ",
        "c1": "Folic acid (หรือ Folinic acid / Leucovorin)",
        "c2": "Pyridoxine (Vitamin B6)",
        "c3": "Thiamine (Vitamin B1)",
        "c4": "Vitamin K1 (Phytomenadione)",
        "c5": "Ascorbic acid (Vitamin C)",
        "ans": 1,
        "subtopic": "Toxic Alcohol",
        "cat": "Clinic",
        "note": "Folic acid role in Methanol metabolism",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Folic acid (หรือ Folinic acid / Leucovorin)

💡 Background:
การขจัดสารพิษ Formic acid ในร่างกายมนุษย์อาศัยวิถี Folate-dependent pathway โดยเอนไซม์ 10-formyltetrahydrofolate dehydrogenase จะเปลี่ยน Formate ร่วมกับ Tetrahydrofolate ให้กลายเป็น Carbon dioxide (CO2) และน้ำ (H2O)

🎯 ทำไมข้อนี้ถึงถูก:
การให้ Folic acid หรือ Folinic acid (Leucovorin) 50 mg IV ทุก 4-6 ชั่วโมง จะช่วยเร่งกระบวนการ Metabolism ของ Formic acid ให้สลายตัวเร็วขึ้น จึงช่วยลดระดับสารพิษที่ทำลายจอประสาทตาและลดความรุนแรงของภาวะเลือดเป็นกรด

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. และ ค. Pyridoxine (B6) และ Thiamine (B1) เป็น Co-factors ที่ใช้เสริมในการรักษา Ethylene glycol poisoning เพื่อเปลี่ยน Glyoxylic acid ไปเป็น Glycine และ alpha-hydroxy-beta-ketoadipate ตามลำดับ ไม่ได้ใช้ใน Methanol
• ข้อ ง. Vitamin K1 ใช้ต้านฤทธิ์ของ Warfarin หรือ Superwarfarin (Rodenticides)
• ข้อ จ. Vitamin C มีบทบาทเป็น Antioxidant ทั่วไป ไม่มีผลต่อการสลาย Formic acid

📖 Guideline อ้างอิง:
AACT Practice Guidelines on the Treatment of Methanol Poisoning และคู่มือการดูแลผู้ป่วยได้รับสารพิษ ศูนย์พิษวิทยารามาธิบดี

📌 จุดจำก่อนสอบ:
• Methanol adjunctive cofactor = Folate / Folinic acid
• Ethylene glycol adjunctive cofactors = Thiamine + Pyridoxine"""
    },
    # 5. Cyanide Poisoning
    {
        "q": "ผู้ประสบภัยจากเหตุการณ์ไฟไหม้ในอาคารปิดทึบ ถูกนำส่งห้องฉุกเฉินด้วยอาการหมดสติ หายใจหอบลึก ผิวหนังมีสีแดงชมพู (Cherry red skin) มีกลิ่นอัลมอนด์ไหม้ (Bitter almond odor) จากลมหายใจ ผลก๊าซในเลือดพบ Severe lactic acidosis (Lactate 14 mmol/L) แม้จะได้รับ 100% High-flow oxygen ข้อใดเป็นชุดยาแก้พิษ (Antidote) ที่เหมาะสมและปลอดภัยที่สุดในปัจจุบัน",
        "c1": "Hydroxocobalamin (Cyanokit)",
        "c2": "Sodium nitrite + Sodium thiosulfate",
        "c3": "Methylene blue",
        "c4": "N-acetylcysteine",
        "c5": "Atropine + Pralidoxime",
        "ans": 1,
        "subtopic": "Cyanide Toxicity",
        "cat": "Clinic",
        "note": "Cyanide Poisoning in Smoke Inhalation",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Hydroxocobalamin (Cyanokit)

💡 Background:
ควันไฟจากการเผาไหม้วัสดุสังเคราะห์ (พลาสติก ยูรีเทน ไนลอน ขนสัตว์) ปลดปล่อยก๊าซ Hydrogen cyanide ไซยาไนด์จะจับกับ Fe3+ (Ferric ion) ใน Cytochrome c oxidase (Complex IV) ของกระบวนการ Electron transport chain ทำให้เซลล์ไม่สามารถใช้ออกซิเจนได้ เกิด Histotoxic hypoxia ส่งผลให้เซลล์เปลี่ยนไปหายใจแบบไม่ใช้ออกซิเจน เกิด Severe lactic acidosis และเลือดดำมีออกซิเจนค้างอยู่สูง ทำให้ผิวเป็นสีชมพูเชอร์รี่

🎯 ทำไมข้อนี้ถึงถูก:
Hydroxocobalamin (Cyanokit) เป็น Antidote ขนานแรกที่แนะนำในผู้ป่วยไฟไหม้ (Smoke inhalation) เนื่องจากโมเลกุลมี Cobalt atom ซึ่งจะจับกับ Cyanide ได้โดยตรง กลายเป็น Cyanocobalamin (Vitamin B12) ที่ไม่มีพิษและขับออกทางปัสสาวะ ที่สำคัญคือไม่ก่อให้เกิดภาวะ Methemoglobinemia และไม่ทำให้ความดันโลหิตตก จึงปลอดภัยอย่างยิ่งในผู้ป่วยไฟไหม้ที่อาจมี Carbon monoxide poisoning ร่วมด้วย

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Sodium nitrite ทำให้เกิด Methemoglobinemia (Fe2+ -> Fe3+) เพื่อแย่งจับ Cyanide แต่ในผู้ป่วยไฟไหม้ที่มี Carbon monoxide (COHb) อยู่แล้ว การเพิ่ม MetHb จะยิ่งทำให้ความสามารถในการขนส่งออกซิเจนของเลือดลดลงวิกฤตจนเสียชีวิตได้ จึงห้ามใช้ Nitrite ใน Smoke inhalation เว้นแต่แยก CO ได้ชัดเจน
• ข้อ ค. Methylene blue เป็นยารักษา Methemoglobinemia การให้จะต้านกลไกของ Nitrite
• ข้อ ง. N-acetylcysteine ไม่มีบทบาทในการจับไซยาไนด์
• ข้อ จ. Atropine + Pralidoxime ใช้รักษา Organophosphate ไม่เกี่ยวข้องกับ Cyanide

📖 Guideline อ้างอิง:
American College of Emergency Physicians (ACEP) Clinical Policy: Critical Issues in the Evaluation and Management of Adult Patients Presenting with Smoke Inhalation

📌 จุดจำก่อนสอบ:
• Cyanide poisoning: Histotoxic hypoxia, High venous oxygen, Severe lactic acidosis
• Fire victim with smoke inhalation: เลือก Hydroxocobalamin เสมอ (หลีกเลี่ยง Sodium nitrite เพราะเสี่ยงต่อการขาดออกซิเจนซ้ำซ้อนจาก Carbon monoxide)"""
    },
    {
        "q": "กลไกการออกฤทธิ์ของ Sodium thiosulfate ในการรักษาภาวะพิษจาก Cyanide คือข้อใด",
        "c1": "ทำหน้าที่เป็น Sulfur donor ให้แก่เอนไซม์ Rhodanese เพื่อเปลี่ยน Cyanide เป็น Thiocyanate ที่ไม่เป็นพิษและขับออกทางไต",
        "c2": "ออกซิไดซ์ฮีโมโกลบินให้กลายเป็น Methemoglobin เพื่อดึง Cyanide ออกจาก Cytochrome oxidase",
        "c3": "แย่งจับกับ Cytochrome c oxidase โดยตรงเพื่อป้องกันไม่ให้ Cyanide เข้าจับ",
        "c4": "กระตุ้นการทำงานของ Cytochrome P450 ในตับเพื่อสลายโมเลกุลของ Cyanide",
        "c5": "จับกับ Cyanide ในทางเดินอาหารและป้องกันการดูดซึม",
        "ans": 1,
        "subtopic": "Cyanide Toxicity",
        "cat": "Clinic",
        "note": "Sodium thiosulfate mechanism of action",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. ทำหน้าที่เป็น Sulfur donor ให้แก่เอนไซม์ Rhodanese เพื่อเปลี่ยน Cyanide เป็น Thiocyanate ที่ไม่เป็นพิษและขับออกทางไต

💡 Background:
ในร่างกายมีเอนไซม์ธรรมชาติชื่อ Rhodanese (Thiosulfate sulfurtransferase) อยู่ในตับและไมโทคอนเดรีย ทำหน้าที่เปลี่ยน Cyanide (CN-) ให้กลายเป็น Thiocyanate (SCN-) ซึ่งมีความเป็นพิษน้อยกว่ามากและละลายน้ำได้ดี ขับออกทางปัสสาวะได้ แต่กระบวนการนี้ถูกจำกัดด้วยปริมาณสารตั้งต้นกลุ่ม Sulfur (Endogenous sulfur donors) ภายในร่างกาย

🎯 ทำไมข้อนี้ถึงถูก:
Sodium thiosulfate ทำหน้าที่เป็น Substrate หรือ Sulfur donor จากภายนอกให้กับเอนไซม์ Rhodanese เพื่อเร่งปฏิกิริยาการเปลี่ยนสารพิษ Cyanide ให้เป็น Thiocyanate ได้อย่างรวดเร็วและขับถ่ายออกทางไตได้อย่างปลอดภัย

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. การออกซิไดซ์ฮีโมโกลบินเป็น Methemoglobin เป็นกลไกของ Amyl nitrite และ Sodium nitrite ไม่ใช่ Sodium thiosulfate
• ข้อ ค. ไม่มี Antidote ใดที่แย่งจับกับ Cytochrome c oxidase โดยตรง
• ข้อ ง. Cyanide ไม่ได้ถูกกำจัดผ่านเอนไซม์ CYP450 เป็นหลัก
• ข้อ จ. การจับในทางเดินอาหารเพื่อป้องกันการดูดซึมเป็นกลไกของ Activated charcoal ไม่ใช่ Sodium thiosulfate IV

📖 Guideline อ้างอิง:
Goldfrank's Toxicologic Emergencies Chapter on Cyanide and Hydrogen Sulfide

📌 จุดจำก่อนสอบ:
• Cyanide Antidote Kit แบบดั้งเดิม: 1) Amyl nitrite สูดดม 2) Sodium nitrite IV (สร้าง MetHb แย่งจับ CN) 3) Sodium thiosulfate IV (ให้ Sulfur donor ผ่าน Rhodanese -> Thiocyanate)
• ปัจจุบัน Hydroxocobalamin นิยมใช้เป็นทางเลือกแรกเพราะออกฤทธิ์เร็วและปลอดภัยกว่ามาก"""
    },
    # 6. Digoxin Toxicity
    {
        "q": "ผู้ป่วยหญิงอายุ 78 ปี เป็นโรคหัวใจล้มเหลวและหัวใจห้องบนสั่นพลิ้ว (AF) รับประทานยา Digoxin 0.25 mg OD และ Furosemide 40 mg OD มาด้วยอาการคลื่นไส้ อาเจียน เบื่ออาหาร มองเห็นภาพเป็นสีเหลืองเขียว (Xanthopsia) ตรวจ EKG พบ PVCs และ Junctional tachycardia ภาวะเกลือแร่ผิดปกติในข้อใดเป็นตัวกระตุ้นหลักที่ทำให้เกิด Digoxin toxicity",
        "c1": "Hypokalemia",
        "c2": "Hyperkalemia",
        "c3": "Hypernatremia",
        "c4": "Hypercalcemia เดี่ยวๆ โดยที่โปแทสเซียมปกติ",
        "c5": "Hyponatremia",
        "ans": 1,
        "subtopic": "Digoxin Toxicity",
        "cat": "Clinic",
        "note": "Hypokalemia predisposing to Digoxin toxicity",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Hypokalemia

💡 Background:
Digoxin ออกฤทธิ์ยับยั้งเอนไซม์ Na+/K+ ATPase pump ที่เยื่อหุ้มเซลล์กล้ามเนื้อหัวใจ โดยจะแย่งจับที่ตำแหน่งเดียวกับ Potassium ion (K+) ดังนั้น เมื่อผู้ป่วยเกิดภาวะ Hypokalemia (มักเกิดจากยาขับปัสสาวะ Furosemide ที่ผู้ป่วยรับประทานร่วมด้วย) โปแทสเซียมในเลือดต่ำจะทำให้ Digoxin จับกับ Na+/K+ ATPase pump ได้มากขึ้นและแน่นขึ้น ส่งผลให้เกิดพิษจากยา Digoxin ได้ง่ายขึ้นอย่างมากแม้ระดับยาในเลือดจะอยู่ในช่วงปกติหรือสูงเพียงเล็กน้อย

🎯 ทำไมข้อนี้ถึงถูก:
Hypokalemia (รวมถึง Hypomagnesemia และ Hypercalcemia) เป็นปัจจัยชักนำที่สำคัญที่สุดในการเพิ่มความไวและความเป็นพิษของ Digoxin ต่อหัวใจ ผู้ป่วยที่ได้รับ Loop diuretics มีความเสี่ยงสูงมากต่อภาวะนี้

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Hyperkalemia มักเป็น 'ผลลัพธ์' ที่เกิดขึ้นในภาวะ Acute massive Digoxin overdose (เนื่องจาก Na+/K+ ATPase ถูกยับยั้งอย่างรุนแรงทำให้ K+ ออกมานอกเซลล์) แต่ไม่ใช่ตัวชักนำให้เกิดพิษใน Chronic toxicity
• ข้อ ค. และ จ. ระดับ Sodium ในเลือดไม่มีผลโดยตรงต่อการจับของ Digoxin กับ Na+/K+ ATPase
• ข้อ ง. แม้ Hypercalcemia จะเพิ่มความเสี่ยงต่อ Arrhythmia แต่ Hypokalemia จาก Loop diuretics เป็นสาเหตุที่พบบ่อยและเป็นตัวกระตุ้นหลักในเวชปฏิบัติ

📖 Guideline อ้างอิง:
American Heart Association (AHA) Guidelines on Management of Heart Failure and Digoxin Toxicity

📌 จุดจำก่อนสอบ:
• ปัจจัยส่งเสริมให้เกิด Digoxin toxicity: Hypokalemia, Hypomagnesemia, Hypercalcemia, ภาวะไตเสื่อม (Digoxin ขับออกทางไต)
• อาการพิษทางตา: Xanthopsia (มองเห็นแสงสีเหลืองเขียวรอบดวงไฟ)
• คลื่นไฟฟ้าหัวใจจำเพาะ: Salvadore Dali sagging ST depression, PVCs, Bidirectional VT"""
    },
    {
        "q": "ผู้ป่วยมีภาวะ Acute Digoxin Overdose ระดับ Serum Potassium วัดได้ 6.5 mEq/L และมีภาวะ Life-threatening ventricular arrhythmias การรักษาด้วยยาใดเป็น Antidote จำเพาะที่มีประสิทธิภาพสูงสุด และยาใดเป็นข้อห้ามให้เนื่องจากอาจทำให้เกิด Stone heart",
        "c1": "ยาแก้พิษคือ Digoxin-specific Fab (Digibind) และห้ามฉีด Calcium gluconate/chloride",
        "c2": "ยาแก้พิษคือ Calcium chloride และห้ามให้ Digoxin-specific Fab",
        "c3": "ยาแก้พิษคือ Atropine และห้ามให้ Potassium chloride",
        "c4": "ยาแก้พิษคือ Sodium polystyrene sulfonate และห้ามให้ Magnesium",
        "c5": "ยาแก้พิษคือ Amiodarone และห้ามให้ Lidocaine",
        "ans": 1,
        "subtopic": "Digoxin Toxicity",
        "cat": "Clinic",
        "note": "Digibind & Avoid Calcium in Digoxin toxicity",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. ยาแก้พิษคือ Digoxin-specific Fab (Digibind) และห้ามฉีด Calcium gluconate/chloride

💡 Background:
ในภาวะ Acute massive Digoxin overdose เอนไซม์ Na+/K+ ATPase จะถูกยับยั้งทั่วร่างกายอย่างรุนแรง ส่งผลให้ K+ ไม่สามารถเข้าสู่เซลล์ได้ เกิดภาวะ Severe Hyperkalemia (> 5.5 mEq/L) ซึ่งระดับ K+ ที่สูงขึ้นจะสัมพันธ์โดยตรงกับอัตราการเสียชีวิตของผู้ป่วย

🎯 ทำไมข้อนี้ถึงถูก:
1) Digoxin-specific antibody fragments (Digoxin-specific Fab: Digibind หรือ DigiFab) เป็น Antidote จำเพาะ ออกฤทธิ์จับกับ Digoxin อิสระในกระแสเลือดอย่างแน่นหนาและขับออกทางไต
2) การให้ Calcium salts (เช่น Calcium gluconate หรือ Calcium chloride) ทางหลอดเลือดดำในภาวะ Digoxin toxicity ถือเป็นข้อห้ามหรือข้อควรระวังขั้นสูงตามทฤษฎี Stone heart เนื่องจากภายในเซลล์กล้ามเนื้อหัวใจมีระดับ Calcium สูงมากอยู่แล้วจากการทำงานของ Na+/Ca2+ exchanger ที่ผกผัน การเติม Calcium เข้าไปอาจทำให้กล้ามเนื้อหัวใจเกิด Tetany หรือหดเกร็งถาวรจนหยุดเต้นในระยะบีบตัว (Irreversible systolic arrest / Stone heart)

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Calcium ไม่ใช่ยาแก้พิษของ Digoxin และเป็นข้อห้ามใช้
• ข้อ ค. Atropine ใช้รักษา Bradycardia ชั่วคราว แต่ไม่ใช่ Definitive antidote สำหรับ Life-threatening ventricular arrhythmia
• ข้อ ง. Sodium polystyrene sulfonate (Kayexalate) ออกฤทธิ์ลด K+ ช้ามาก ไม่ทันท่วงทีในภาวะฉุกเฉิน
• ข้อ จ. Amiodarone เป็นยาที่เพิ่มระดับ Digoxin ในเลือดและอาจทำให้ Conduct block รุนแรงขึ้น

📖 Guideline อ้างอิง:
Management of Digoxin Toxicity, American College of Emergency Physicians & Ramathibodi Poison Center

📌 จุดจำก่อนสอบ:
• ข้อบ่งชี้ของ Digoxin-specific Fab: 1) Life-threatening arrhythmia 2) K+ > 5.0-5.5 mEq/L ใน acute overdose 3) Ingestion > 10 mg ในผู้ใหญ่ (> 4 mg ในเด็ก) 4) Serum Digoxin > 10-15 ng/mL
• ระวังการให้ Calcium IV ในผู้ป่วยที่สงสัย Digoxin toxicity เด็ดขาด"""
    },
    # 7. Iron Toxicity
    {
        "q": "เด็กชายอายุ 3 ขวบ น้ำหนัก 15 กิโลกรัม แอบรับประทานยาบำรุงโลหิต Ferrous sulfate (มี Elemental iron 60 มก./เม็ด) ของมารดาไปจำนวน 20 เม็ด (ได้รับ Elemental iron รวม 1,200 มก. หรือ 80 มก./กก.) หลังกิน 2 ชั่วโมง เด็กมีอาการปวดท้องรุนแรง อาเจียนเป็นเลือดสด ถ่ายดำ และความดันโลหิตตก ยาแก้พิษจำเพาะใดที่ต้องให้ทางหลอดเลือดดำเพื่อจับกับธาตุเหล็กส่วนเกิน",
        "c1": "Deferoxamine (Desferrioxamine)",
        "c2": "Dimercaprol (BAL)",
        "c3": "Calcium disodium EDTA",
        "c4": "Penicillamine",
        "c5": "Succimer (DMSA)",
        "ans": 1,
        "subtopic": "Iron Toxicity",
        "cat": "Clinic",
        "note": "Iron toxicity & Deferoxamine",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Deferoxamine (Desferrioxamine)

💡 Background:
ขนาดยา Elemental iron ที่เป็นพิษ:
• < 20 mg/kg: มักไม่มีอาการ
• 20-60 mg/kg: อาการพิษเล็กน้อยถึงปานกลางต่อทางเดินอาหาร
• > 60 mg/kg: อาการพิษรุนแรง (Severe toxicity) เสี่ยงต่อการเสียชีวิต
เด็กรายนี้ได้รับ 80 mg/kg ซึ่งเข้าสู่ Severe toxicity ทำให้เกิดการกัดกร่อนเยื่อบุกระเพาะอาหารและลำไส้อย่างรุนแรง (Hemorrhagic gastritis) ตามด้วยภาวะช็อก ตับวาย และ Metabolic acidosis

🎯 ทำไมข้อนี้ถึงถูก:
Deferoxamine เป็น Specific chelating agent ที่จับกับ Ferric iron (Fe3+) อย่างจำเพาะ กลายเป็นสารประกอบเชิงซ้อน Feroxamine ซึ่งไม่มีพิษ ละลายน้ำได้ดี และถูกขับออกทางไต การขับ Feroxamine ทางปัสสาวะจะทำให้ปัสสาวะเปลี่ยนเป็นสีไวน์แดงอมส้ม เรียกว่า Vin rosé urine

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Dimercaprol (BAL) ห้ามใช้ใน Iron poisoning โดยเด็ดขาด เพราะสารประกอบเชิงซ้อนระหว่าง BAL กับ Iron มีความเป็นพิษต่อตับและไตสูงกว่าตัวเหล็กอิสระ
• ข้อ ค. Calcium disodium EDTA ใช้สำหรับ Lead toxicity (พิษจากตะกั่ว)
• ข้อ ง. Penicillamine ใช้สำหรับ Copper (Wilson's disease) หรือ Arsenic/Lead
• ข้อ จ. Succimer (DMSA) เป็นยากินสำหรับ Lead, Mercury, Arsenic ไม่ใช้ใน Acute severe iron toxicity

📖 Guideline อ้างอิง:
AACT Practice Guidelines on the Treatment of Acute Iron Poisoning

📌 จุดจำก่อนสอบ:
• Elemental iron > 60 mg/kg = Severe toxicity
• Antidote = Deferoxamine IV infusion
• สัญญาณของการจับธาตุเหล็ก = Vin rosé urine (สีไวน์กุหลาบ)
• ห้ามใช้ BAL ในภาวะ Iron overload เด็ดขาด"""
    },
    # 8. Heavy Metals (Lead, Mercury, Arsenic)
    {
        "q": "คนงานโรงงานหลอมแบตเตอรี่ มีอาการปวดท้องรุนแรงแบบบิดเกร็ง (Colicky abdominal pain), ข้อมือตก (Wrist drop / Peripheral neuropathy), โลหิตจางแบบ Microcytic hypochromic ที่ตรวจพบ Basophilic stippling ในเม็ดเลือดแดง และตรวจพบเส้นสีน้ำเงินคล้ำที่ขอบเหงือก (Burton's line) ระดับสารพิษชนิดใดในเลือดที่ต้องตรวจยืนยัน และยาแก้พิษตัวใดที่เหมาะสมในผู้ใหญ่ที่มีอาการรุนแรง",
        "c1": "Lead (ตะกั่ว) — รักษาด้วย Dimercaprol (BAL) ร่วมกับ Calcium disodium EDTA",
        "c2": "Arsenic (สารหนู) — รักษาด้วย Deferoxamine",
        "c3": "Mercury (ปรอท) — รักษาด้วย Sodium thiosulfate",
        "c4": "Cadmium (แคดเมียม) — รักษาด้วย Penicillamine",
        "c5": "Iron (เหล็ก) — รักษาด้วย N-acetylcysteine",
        "ans": 1,
        "subtopic": "Heavy Metal Toxicity",
        "cat": "Clinic",
        "note": "Lead poisoning symptoms & Chelation",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Lead (ตะกั่ว) — รักษาด้วย Dimercaprol (BAL) ร่วมกับ Calcium disodium EDTA

💡 Background:
อาการแสดงของผู้ป่วยเป็นลักษณะเฉพาะของภาวะพิษจากตะกั่วเรื้อรัง (Lead toxicity / Plumbism) ได้แก่:
1) ทางเดินอาหาร: ปวดท้องบิดรุนแรง (Lead colic)
2) ระบบประสาท: Motor neuropathy โดยเฉพาะ Radial nerve palsy ทำให้ข้อมือตก (Wrist drop) และ Encephalopathy
3) ระบบเลือด: ขัดขวางการสังเคราะห์ Heme (ยับยั้งเอนไซม์ delta-ALA dehydratase และ Ferrochelatase) ทำให้เกิด Microcytic anemia ร่วมกับ Basophilic stippling
4) ช่องปาก: ตะกั่วทำปฏิกิริยากับแบคทีเรียเกิด Lead sulfide ตกตะกอนเป็นเส้นสีน้ำเงิน-ดำที่ขอบเหงือก (Burton's line)

🎯 ทำไมข้อนี้ถึงถูก:
การวินิจฉัยคือพิษจากตะกั่ว (Blood Lead Level) ในผู้ป่วยที่มีอาการรุนแรงหรือมี Lead encephalopathy การรักษามาตรฐานคือการให้ Chelating agents สองชนิดร่วมกัน ได้แก่ Dimercaprol (BAL) ฉีดเข้ากล้ามเนื้อ นำหน้าก่อนเริ่มให้ Calcium disodium EDTA ทางหลอดเลือดดำอย่างน้อย 4 ชั่วโมง เพื่อป้องกันไม่ให้ EDTA ดึงตะกั่วจากกระดูกไปสะสมในสมองเพิ่มขึ้น

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. พิษจาก Arsenic ทำให้เกิดกลิ่นกระเทียม, Mees' lines บนเล็บ, และอาการท้องร่วงเป็นน้ำซาวข้าว การรักษาใช้ BAL หรือ Succimer ไม่ใช่ Deferoxamine
• ข้อ ค. Sodium thiosulfate ใช้กับ Cyanide ไม่ใช่ปรอท (Mercury รักษาด้วย BAL หรือ Succimer)
• ข้อ ง. การรักษา Cadmium toxicity หลีกเลี่ยง Chelating agents เพราะเสี่ยงต่อไตวาย
• ข้อ จ. พิษจากธาตุเหล็กไม่ทำให้เกิด Wrist drop หรือ Burton's line

📖 Guideline อ้างอิง:
CDC Guidelines for the Identification and Management of Lead Exposure in Adults and Children

📌 จุดจำก่อนสอบ:
• Lead toxicity: Lead colic + Wrist drop + Basophilic stippling + Burton's line
• Severe Lead Encephalopathy: ให้ BAL ฉีด IM ก่อน ตามด้วย CaNa2-EDTA IV เสมอ
• ในเด็กหรือรายที่อาการไม่รุนแรง สามารถใช้ยากิน Succimer (DMSA) ได้"""
    },
    {
        "q": "ผู้ป่วยได้รับสารพิษ Inorganic Arsenic หรือ Inorganic Mercury ในระยะเฉียบพลัน ข้อใดถูกต้องเกี่ยวกับการเลือกใช้ยาขับโลหะหนัก (Chelating agent) และข้อห้ามใช้",
        "c1": "Dimercaprol (BAL) ฉีดเข้ากล้ามเนื้อเป็น Antidote ทางเลือกแรกสำหรับพิษจากสารหนูและเกลืออนินทรีย์ของปรอท แต่ห้ามใช้ใน Organic mercury (Methylmercury)",
        "c2": "Calcium disodium EDTA เป็นยาทางเลือกแรกสำหรับ Organic mercury",
        "c3": "Deferoxamine สามารถใช้ทดแทน BAL ได้ในกรณีที่ผู้ป่วยแพ้ถั่วลิสง",
        "c4": "Dimercaprol สามารถบริหารยาทางหลอดเลือดดำได้อย่างปลอดภัย",
        "c5": "Succimer (DMSA) ห้ามใช้ในเด็กเนื่องจากกดการเจริญเติบโต",
        "ans": 1,
        "subtopic": "Heavy Metal Toxicity",
        "cat": "Clinic",
        "note": "BAL in Arsenic/Mercury and peanut allergy precaution",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Dimercaprol (BAL) ฉีดเข้ากล้ามเนื้อเป็น Antidote ทางเลือกแรกสำหรับพิษจากสารหนูและเกลืออนินทรีย์ของปรอท แต่ห้ามใช้ใน Organic mercury (Methylmercury)

💡 Background:
Dimercaprol (British Anti-Lewisite: BAL) มีหมู่ Sulfhydryl (-SH) สองหมู่ที่จับกับโลหะหนักได้อย่างเหนียวแน่น มีประสิทธิภาพดีในการจับกับ Arsenic, Inorganic Mercury, Gold และ Lead (ร่วมกับ EDTA)

🎯 ทำไมข้อนี้ถึงถูก:
1) BAL เป็นยาหลักในการรักษาพิษเฉียบพลันจาก Arsenic และ Inorganic mercury salts
2) ข้อห้ามสำคัญ: ห้ามใช้ BAL ในการรักษาพิษจาก Organic mercury (เช่น Methylmercury จากปลาทะเลปนเปื้อนในโรคมินามาตะ) เด็ดขาด เนื่องจากสารประกอบเชิงซ้อนระหว่าง BAL กับ Methylmercury สามารถผ่าน Blood-Brain Barrier เข้าสู่สมองได้ดีขึ้น ทำให้ความเป็นพิษต่อระบบประสาทรุนแรงขึ้น (Redistribution of mercury to the brain) ในกรณี Organic mercury ให้เลือกใช้ Succimer (DMSA) หรือ N-acetylcysteine

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Calcium disodium EDTA ไม่มีประสิทธิภาพในการจับกับ Mercury และเสี่ยงต่อ Nephrotoxicity
• ข้อ ค. Deferoxamine จับเฉพาะธาตุเหล็ก ไม่สามารถจับ Arsenic หรือ Mercury ได้
• ข้อ ง. Dimercaprol ละลายในน้ำมันถั่วลิสง (Peanut oil) ต้องฉีดเข้ากล้ามเนื้อลึก (Deep IM) เท่านั้น ห้ามฉีดเข้าทางหลอดเลือดดำ (IV) โดยเด็ดขาดเพราะทำให้เกิดไขมันอุดกั้นหลอดเลือดและพิษร้ายแรง
• ข้อ จ. Succimer (DMSA) เป็น Chelating agent ชนิดรับประทานที่ได้รับการรับรองจาก US-FDA ให้ใช้ในเด็กได้อย่างปลอดภัย

📖 Guideline อ้างอิง:
Medical Toxicology: Diagnosis and Treatment of Heavy Metal Poisoning, WHO & Ramathibodi Poison Center

📌 จุดจำก่อนสอบ:
• BAL ละลายในน้ำมันถั่วลิสง -> ฉีด Deep IM เท่านั้น และระวังในผู้แพ้ถั่ว (Peanut allergy)
• BAL ห้ามใช้ใน Organic mercury (ห้ามใช้ใน Minamata disease)
• BAL ห้ามใช้ใน Iron, Cadmium, Selenium เพราะสารเชิงซ้อนมีพิษต่อไตสูงขึ้น"""
    },
    # 9. Beta-blockers & Calcium Channel Blockers Overdose
    {
        "q": "ผู้ป่วยหญิงอายุ 60 ปี รับประทานยา Propranolol ขนาด 40 มก. ไปจำนวน 30 เม็ด (1,200 มก.) เพื่อฆ่าตัวตาย ถูกนำส่งโรงพยาบาลด้วยอาการซึม ความดันโลหิต 70/40 mmHg อัตราการเต้นของหัวใจ 38 ครั้ง/นาที น้ำตาลในเลือด 55 mg/dL แม้จะได้รับการให้สารน้ำ Isotonic saline อย่างเต็มที่และฉีด Atropine 3 mg แล้ว ชีพจรและความดันโลหิตยังไม่ดีขึ้น ยาใดเป็น Antidote จำเพาะทางเลือกแรกที่ออกฤทธิ์เพิ่ม cAMP โดยไม่ผ่าน Beta-adrenergic receptor",
        "c1": "Glucagon IV bolus ตามด้วย continuous infusion",
        "c2": "Calcium gluconate IV bolus",
        "c3": "Insulin regular ในขนาดปกติ 5-10 units IV",
        "c4": "Norepinephrine infusion เดี่ยวๆ",
        "c5": "Dopamine infusion ขนาดต่ำ (Renal dose)",
        "ans": 1,
        "subtopic": "Cardiovascular Drug Overdose",
        "cat": "Clinic",
        "note": "Beta-blocker toxicity & Glucagon",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Glucagon IV bolus ตามด้วย continuous infusion

💡 Background:
Beta-blocker overdose ทำให้เกิดภาวะหัวใจเต้นช้า (Bradycardia), ความดันโลหิตต่ำ (Hypotension), หัวใจบีบตัวลดลง (Cardiogenic shock) และน้ำตาลในเลือดต่ำ (Hypoglycemia) โดยเฉพาะยาที่ละลายในไขมันสูงและมี Membrane stabilizing activity เช่น Propranolol จะทำให้เกิดการกดการนำไฟฟ้าในหัวใจและชักได้

🎯 ทำไมข้อนี้ถึงถูก:
Glucagon เป็น First-line antidote จำเพาะสำหรับ Beta-blocker overdose กลไกการออกฤทธิ์คือ Glucagon จะจับกับ G-protein coupled glucagon receptor บนกล้ามเนื้อหัวใจโดยตรง ซึ่งไปกระตุ้นเอนไซม์ Adenylate cyclase ให้เปลี่ยน ATP เป็น cyclic AMP (cAMP) ข้ามขั้นตอนการกระตุ้นผ่าน Beta-adrenergic receptors (Bypass blocked beta-receptors) ส่งผลให้ระดับ intracellular cAMP และ Calcium เพิ่มขึ้น เกิด Positive inotropic และ Chronotropic effects ทำให้หัวใจเต้นเร็วขึ้นและบีบตัวแรงขึ้น

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Calcium gluconate เป็น First-line สำหรับ Calcium channel blocker (CCB) toxicity แต่ใน Beta-blocker toxicity มีประสิทธิภาพด้อยกว่า Glucagon
• ข้อ ค. การรักษาด้วย High-dose Insulin Euglycemia Therapy (HIET) ต้องใช้ Insulin ขนาดสูงมาก (1 unit/kg bolus ตามด้วย 0.5-1 unit/kg/hr) ร่วมกับ 10-50% Dextrose ไม่ใช่การให้อินซูลินขนาดปกติ 5-10 units
• ข้อ ง. Norepinephrine เพียงอย่างเดียวมักไม่ได้ผลเนื่องจาก Beta-receptors ถูกยับยั้งอย่างสมบูรณ์
• ข้อ จ. Low-dose dopamine ไม่มีประโยชน์ในการกู้สัญญาณชีพในภาวะช็อกรุนแรง

📖 Guideline อ้างอิง:
American College of Medical Toxicology (ACMT) Guidance on the Treatment of Beta-Blocker and Calcium Channel Blocker Overdose

📌 จุดจำก่อนสอบ:
• Beta-blocker overdose antidote = Glucagon (Bypass beta-receptor -> เพิ่ม cAMP)
• ผลข้างเคียงเด่นของ Glucagon IV bolus คือ คลื่นไส้อาเจียนรุนแรง (Nausea & Vomiting) ต้องเตรียม Suction และระวังการสำลัก"""
    },
    {
        "q": "ผู้ป่วยชายอายุ 55 ปี รับประทานยา Amlodipine 10 มก. ไป 30 เม็ด (300 มก.) มาโรงพยาบาลด้วยภาวะ Refractory shock (BP 60/30 mmHg, HR 55 bpm, Blood glucose 280 mg/dL) ทีมแพทย์ตัดสินใจเริ่มการรักษาด้วย High-Dose Insulin Euglycemia Therapy (HIET) ข้อใดคือหลักการที่ถูกต้องของการรักษานี้",
        "c1": "ให้อินซูลิน Regular Insulin ในขนาดสูงมาก (1 unit/kg IV bolus ตามด้วย infusion 0.5-1 unit/kg/hr) ร่วมกับการให้ Glucose ทางหลอดเลือดดำและติดตามระดับ Potassium อย่างใกล้ชิด",
        "c2": "ให้อินซูลินขนาดต่ำ 0.1 unit/kg/hr เพื่อลดระดับน้ำตาลในเลือดที่สูงให้อยู่ในเกณฑ์ปกติเท่านั้น",
        "c3": "ห้ามให้สารละลายน้ำตาลกลูโคสร่วมด้วยเด็ดขาดเนื่องจากผู้ป่วยมีภาวะน้ำตาลในเลือดสูงอยู่แล้ว",
        "c4": "อินซูลินออกฤทธิ์โดยการบล็อกแคลเซียมแชนแนลเพื่อลดการทำงานของหัวใจ",
        "c5": "ต้องหยุดอินซูลินทันทีหากระดับ Serum Potassium ต่ำกว่า 4.0 mEq/L",
        "ans": 1,
        "subtopic": "Cardiovascular Drug Overdose",
        "cat": "Clinic",
        "note": "High-dose insulin in CCB overdose",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. ให้อินซูลิน Regular Insulin ในขนาดสูงมาก (1 unit/kg IV bolus ตามด้วย infusion 0.5-1 unit/kg/hr) ร่วมกับการให้ Glucose ทางหลอดเลือดดำและติดตามระดับ Potassium อย่างใกล้ชิด

💡 Background:
Calcium Channel Blocker (CCB) โดยเฉพาะชนิด Dihydropyridine ขนาดสูง (เช่น Amlodipine) หรือ Non-Dihydropyridine (Verapamil, Diltiazem) จะยับยั้ง L-type calcium channels บนหลอดเลือดและเซลล์กล้ามเนื้อหัวใจ และยับยั้งการหลั่งอินซูลินจากตับอ่อน (Beta-islet cells ต้องการแคลเซียมในการหลั่งอินซูลิน) ทำให้ผู้ป่วยมักมีภาวะ Hyperglycemia และกล้ามเนื้อหัวใจขาดพลังงาน เพราะในภาวะช็อกเซลล์หัวใจจะเปลี่ยนจากการใช้ Free fatty acids มาพึ่งพาการใช้น้ำตาลกลูโคสเป็นพลังงานหลัก

🎯 ทำไมข้อนี้ถึงถูก:
High-Dose Insulin Euglycemia Therapy (HIET หรือ HIE) ออกฤทธิ์เป็น Metabolic inotrope:
1) อินซูลินขนาดสูง (1 unit/kg IV loading + 0.5-1 unit/kg/hr infusion) ช่วยเปิดทางให้ Glucose เข้าสู่เซลล์กล้ามเนื้อหัวใจ เพิ่มการสร้าง ATP และเพิ่มการบีบตัวของหัวใจ (Inotropic effect) โดยไม่เพิ่มการใช้ออกซิเจนของกล้ามเนื้อหัวใจ
2) ต้องให้ Dextrose (10% หรือ 50%) หยดร่วมด้วยเสมอเพื่อป้องกันภาวะ Hypoglycemia (รักษาระดับน้ำตาลที่ 150-250 mg/dL)
3) ต้องเฝ้าระวัง Hypokalemia เนื่องจากอินซูลินดึง K+ เข้าเซลล์ โดยให้ K+ เสริมเมื่อระดับ K+ < 3.0 mEq/L

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. อินซูลินขนาดต่ำแบบที่ใช้รักษา DKA (0.1 unit/kg/hr) ไม่มีผลต่อ Inotropic effect ของกล้ามเนื้อหัวใจ
• ข้อ ค. แม้ช่วงแรกน้ำตาลจะสูง แต่อินซูลินขนาดมหาศาลจะทำให้น้ำตาลตกลงอย่างรวดเร็วและรุนแรง จึงต้องเตรียมให้ Glucose IV เสมอ
• ข้อ ง. อินซูลินไม่ได้ไปบล็อกแคลเซียม แต่ช่วยเรื่อง Cardiac energy metabolism
• ข้อ จ. ภาวะ Hypokalemia จากอินซูลินเป็นเพียงการเคลื่อนย้าย K+ เข้าเซลล์ ให้แก้ไขด้วยการเติม K+ IV โดยไม่จำเป็นต้องหยุดอินซูลิน

📖 Guideline อ้างอิง:
Extracorporeal Treatments in Poisoning (EXTRIP) workgroup and ACMT Guidelines on Calcium Channel Blocker Toxicity

📌 จุดจำก่อนสอบ:
• CCB Overdose Triad: Shock + Bradycardia/AV block + Hyperglycemia
• Antidotes: IV Calcium (Gluconate/Chloride), High-dose Insulin (HIET), Vasopressors (Norepinephrine), Intralipid (ILE)"""
    },
    # 10. Benzodiazepines Overdose
    {
        "q": "ผู้ป่วยหญิงอายุ 30 ปี ถูกนำส่งโรงพยาบาลหลังรับประทานยา Diazepam 5 mg จำนวน 40 เม็ดร่วมกับ Amitriptyline 25 mg จำนวน 30 เม็ดเพื่อทำร้ายตัวเอง มีอาการซึม ไม่รู้สึกตัว แต่ระบบหายใจยังคงเพียงพอ (RR 14 ครั้ง/นาที) ตรวจคลื่นไฟฟ้าหัวใจพบ Sinus tachycardia อัตรา 115 ครั้ง/นาที และ QRS complex กว้าง 130 msec เหตุใดแพทย์จึง 'ไม่ควร' ให้ยา Flumazenil ในผู้ป่วยรายนี้",
        "c1": "เสี่ยงต่อการชักรุนแรงที่ไม่สามารถควบคุมได้และภาวะหัวใจเต้นผิดจังหวะจากการปลดปล่อยฤทธิ์ของ Cyclic Antidepressants (TCAs)",
        "c2": "Flumazenil ออกฤทธิ์เสริมพิษของ Amitriptyline ทำให้ความดันโลหิตสูงวิกฤต",
        "c3": "Flumazenil มีข้อห้ามใช้เด็ดขาดในผู้ป่วยที่ได้รับ Diazepam เกินขนาด",
        "c4": "Flumazenil จะทำให้เกิดพิษต่อตับเฉียบพลันจากปฏิกิริยาเสริมฤทธิ์ของยา",
        "c5": "Diazepam ขับออกทางไตหมดแล้ว การให้ Flumazenil จึงไม่มีประโยชน์",
        "ans": 1,
        "subtopic": "Sedative-Hypnotic Toxicity",
        "cat": "Clinic",
        "note": "Flumazenil contraindications in mixed TCA overdose",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. เสี่ยงต่อการชักรุนแรงที่ไม่สามารถควบคุมได้และภาวะหัวใจเต้นผิดจังหวะจากการปลดปล่อยฤทธิ์ของ Cyclic Antidepressants (TCAs)

💡 Background:
Flumazenil เป็น Competitive antagonist ที่จำเพาะต่อ Benzodiazepine binding site บน GABAA receptor สามารถแก้ฤทธิ์ซึมของ Benzodiazepines ได้อย่างรวดเร็ว อย่างไรก็ตาม การใช้ Flumazenil มีข้อควรระวังและความเสี่ยงสูงมากในเวชปฏิบัติฉุกเฉิน

🎯 ทำไมข้อนี้ถึงถูก:
ในผู้ป่วยที่รับประทานยาเกินขนาดแบบผสม (Mixed overdose) โดยเฉพาะร่วมกับสารที่ทำให้เกิดอาการชัก เช่น Tricyclic antidepressants (TCAs: Amitriptyline ซึ่งผู้ป่วยมี QRS กว้าง > 100 msec แสดงถึงพิษจาก TCA ชัดเจน), Theophylline, Tramadol หรือในผู้ป่วยที่มีประวัติติด Benzodiazepine เรื้อรัง:
• ฤทธิ์ระงับประสาทของ Benzodiazepines ทำหน้าที่เป็นยากันชัก (Anticonvulsant shield) คอยกดฤทธิ์ชักของ TCA ไว้
• หากฉีด Flumazenil เข้าไป ฤทธิ์กันชักจะหายไปทันที ทำให้เกิด Intractable seizures (ชักต่อเนื่อง) และเกิด Ventricular arrhythmias เสียชีวิตได้ การรักษาผู้ป่วยรายนี้ต้องใช้ Sodium bicarbonate IV เพื่อรักษา TCA toxicity และรักษาแบบประคับประคองทางเดินหายใจโดยไม่ใช้ Flumazenil

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Flumazenil ไม่ได้ทำให้ความดันโลหิตสูงวิกฤต
• ข้อ ค. Flumazenil เป็น Antidote ของ Benzodiazepines โดยตรง ไม่ได้มีข้อห้ามใช้กับ Diazepam เดี่ยวๆ
• ข้อ ง. Flumazenil ไม่ได้ทำให้เกิดพิษต่อตับ
• ข้อ จ. Diazepam มี Half-life ยาวนาน 20-50 ชั่วโมง และมี Active metabolites การบอกว่าขับออกหมดแล้วไม่ถูกต้อง

📖 Guideline อ้างอิง:
American College of Emergency Physicians (ACEP) Clinical Policy for Sedative-Hypnotic and TCA Overdose

📌 จุดจำก่อนสอบ:
• ข้อห้ามใช้ Flumazenil: 1) Mixed overdose ร่วมกับสารกระตุ้นการชัก (โดยเฉพาะ TCAs) 2) ผู้ใช้ BZD เรื้อรัง (เสี่ยงต่อ Acute withdrawal seizure) 3) ผู้ป่วยโรคลมชัก (Epilepsy)
• การรักษา BZD overdose ทั่วไป: ประคับประคองทางเดินหายใจ (Supportive airway care) เป็นหลัก ปลอดภัยกว่าการให้ Flumazenil"""
    },
    # 11. Anticoagulant Reversal
    {
        "q": "ผู้ป่วยชายอายุ 72 ปี รับประทานยา Warfarin สำหรับรักษาภาวะลิ่มเลือดอุดกั้นในปอด (PE) เกิดอุบัติเหตุล้มศีรษะกระแทกพื้น ผลเอกซเรย์คอมพิวเตอร์สมอง (CT brain) พบ Intracranial hemorrhage (เลือดออกในกะโหลกศีรษะ) ผลตรวจเลือดพบ INR = 7.5 และผู้ป่วยยังมีเลือดออกต่อเนื่อง ข้อใดเป็นแนวทางการให้ยาต้านพิษเพื่อลดค่า INR และหยุดเลือดอย่างเร่งด่วนที่สุดตามแนวทางเวชปฏิบัติสากล",
        "c1": "ให้ 4-Factor Prothrombin Complex Concentrate (4F-PCC) ทางหลอดเลือดดำทันที ร่วมกับ Vitamin K1 10 mg IV infusion ช้าๆ",
        "c2": "ให้ Vitamin K1 10 mg รับประทานเพียงอย่างเดียว",
        "c3": "ให้ Fresh Frozen Plasma (FFP) เพียงอย่างเดียวโดยไม่ต้องให้ Vitamin K1",
        "c4": "ฉีด Protamine sulfate 50 mg ทางหลอดเลือดดำทันที",
        "c5": "ให้ Idarucizumab 5 g ทางหลอดเลือดดำ",
        "ans": 1,
        "subtopic": "Anticoagulant Reversal",
        "cat": "Clinic",
        "note": "Warfarin reversal in major bleeding (4F-PCC + Vit K1)",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. ให้ 4-Factor Prothrombin Complex Concentrate (4F-PCC) ทางหลอดเลือดดำทันที ร่วมกับ Vitamin K1 10 mg IV infusion ช้าๆ

💡 Background:
ภาวะเลือดออกรุนแรงที่เป็นอันตรายถึงชีวิต (Major life-threatening bleeding เช่น Intracranial hemorrhage) ในผู้ป่วยที่ได้รับ Warfarin ต้องการการแก้ไขภาวะการแข็งตัวของเลือดให้กลับมาเป็นปกติ (INR < 1.4-1.5) โดยเร็วที่สุดภายในระดับนาที

🎯 ทำไมข้อนี้ถึงถูก:
1) 4-Factor Prothrombin Complex Concentrate (4F-PCC) ประกอบด้วย Clotting factors สำคัญ 4 ตัว (II, VII, IX, X) และ Protein C, S ในรูปแบบเข้มข้น ปริมาตรน้อย สามารถบริหารยาทางหลอดเลือดดำได้รวดเร็ว และปรับลด INR ให้ลงมาปกติได้ภายใน 10-30 นาที ถือเป็น First-line treatment เหนือกว่า Fresh Frozen Plasma (FFP)
2) ต้องให้ Intravenous Vitamin K1 (Phytomenadione) 5-10 mg IV infusion ช้าๆ (ใน 30 นาที) ควบคู่ไปด้วยเสมอ เพื่อกระตุ้นให้ตับสังเคราะห์ Clotting factors ขึ้นมาใหม่ทดแทน เนื่องจาก 4F-PCC มีฤทธิ์อยู่ได้เพียง 6-8 ชั่วโมง (ตาม half-life ของ Factor VII) หากไม่ให้ Vitamin K1 ค่า INR จะเด้งกลับมาสูงขึ้นซ้ำอีก (Rebound anticoagulation)

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. การให้ Vitamin K1 แบบกินหรือฉีดเพียงอย่างเดียว ต้องใช้เวลาอย่างน้อย 12-24 ชั่วโมงในการสร้าง Clotting factors ใหม่ ซึ่งช้าเกินไปในภาวะเลือดออกในสมอง
• ข้อ ค. FFP ต้องใช้เวลาเตรียม ละลาย และให้ปริมาตรสารน้ำมาก (15-30 mL/kg) เสี่ยงต่อ Fluid overload (TACO) และใช้เวลาหลายชั่วโมงในการลด INR อีกทั้งหากไม่ให้ Vitamin K1 ร่วมด้วย ค่า INR จะกลับมาสูงขึ้นอีก
• ข้อ ง. Protamine sulfate เป็น Specific antidote สำหรับ Unfractionated Heparin ไม่ใช่ Warfarin
• ข้อ จ. Idarucizumab (Praxbind) เป็น Specific reversal agent สำหรับ Dabigatran (DOAC) ไม่ใช่ Warfarin

📖 Guideline อ้างอิง:
American College of Cardiology (ACC) Expert Consensus on Anticoagulation Reversal และ CHEST Guideline on Antithrombotic Therapy

📌 จุดจำก่อนสอบ:
• Warfarin Life-threatening bleed = 4F-PCC + IV Vitamin K1 (10 mg)
• IV Vitamin K1 ต้องเจือจางและหยดช้าๆ อย่างน้อย 30 นาที ป้องกัน Anaphylactoid shock
• ไม่ฉีด Vitamin K1 แบบ IM เดี่ยวๆ ในผู้ป่วย INR สูงเพราะเสี่ยงต่อ Hematoma ขนาดใหญ่"""
    },
    {
        "q": "ผู้ป่วยหญิงอายุ 65 ปี ได้รับยาต้านการแข็งตัวของเลือดชนิดรับประทานกลุ่มใหม่ (DOAC) ตัวใดตัวหนึ่ง และเกิดภาวะเลือดออกรุนแรงในทางเดินอาหารส่วนบน ข้อใดจับคู่ระหว่างยาต้านการแข็งตัวของเลือดและยาต้านพิษจำเพาะ (Specific reversal agent) ได้อย่างถูกต้อง",
        "c1": "Dabigatran คู่กับ Idarucizumab",
        "c2": "Rivaroxaban คู่กับ Protamine sulfate",
        "c3": "Apixaban คู่กับ Deferoxamine",
        "c4": "Enoxaparin คู่กับ Vitamin K1",
        "c5": "Warfarin คู่กับ Flumazenil",
        "ans": 1,
        "subtopic": "Anticoagulant Reversal",
        "cat": "Clinic",
        "note": "DOACs Specific Antidotes",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Dabigatran คู่กับ Idarucizumab

💡 Background:
การพัฒนายาต้านพิษจำเพาะสำหรับ Direct Oral Anticoagulants (DOACs) มีความสำคัญอย่างยิ่งในการจัดการภาวะเลือดออกรุนแรงหรือการผ่าตัดฉุกเฉิน

🎯 ทำไมข้อนี้ถึงถูก:
Idarucizumab (Praxbind) เป็น Humanized monoclonal antibody fragment (Fab) ที่จับกับ Dabigatran (Direct Thrombin Inhibitor) ได้อย่างจำเพาะเจาะจง โดยมีความสามารถในการจับ (Affinity) สูงกว่า Thrombin ถึง 350 เท่า สามารถต้านฤทธิ์ของ Dabigatran ได้อย่างสมบูรณ์ภายในไม่กี่นาที

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Rivaroxaban และ Apixaban (Factor Xa inhibitors) มี Specific reversal agent คือ Andexanet alfa (ไม่ใช่ Protamine sulfate ซึ่งใช้กับ Heparin)
• ข้อ ค. Deferoxamine ใช้กับพิษธาตุเหล็ก
• ข้อ ง. Enoxaparin (LMWH) แก้ฤทธิ์ได้บางส่วน (ประมาณ 60-75%) ด้วย Protamine sulfate (ไม่ใช่ Vitamin K1)
• ข้อ จ. Warfarin แก้ฤทธิ์ด้วย Vitamin K1 และ 4F-PCC (Flumazenil ใช้กับ Benzodiazepines)

📖 Guideline อ้างอิง:
ACC Expert Consensus Decision Pathway on Management of Bleeding in Patients on Oral Anticoagulants

📌 จุดจำก่อนสอบ:
• Dabigatran (Factor IIa inhibitor) -> Idarucizumab (Praxbind)
• Rivaroxaban / Apixaban / Edoxaban (Factor Xa inhibitors) -> Andexanet alfa (Andexxa) หรือ 4F-PCC (หากไม่มี Andexanet)
• Heparin (UFH) -> Protamine sulfate (1 mg ต่อน้ำยา UFH 100 units)"""
    },
    # 12. Snake Envenomation
    {
        "q": "ผู้ป่วยชายอายุ 40 ปี ถูกงูไม่ทราบชนิดกัดที่บริเวณหลังเท้าขวาขณะเดินในสวนผลไม้ เวลาผ่านไป 1 ชั่วโมง ผู้ป่วยมีอาการหนังตาตกทั้งสองข้าง (Bilateral ptosis) กลืนลำบาก พูดไม่ชัด เสียงอู้อี้ และเริ่มหายใจเหนื่อยหอบจากการอ่อนแรงของกล้ามเนื้อกระบังลม แต่บริเวณบาดแผลไม่มีอาการบวมพองหรือเนื้อตาย อาการดังกล่าวเป็นลักษณะพิษต่อระบบประสาท (Neurotoxic venom) ของงูชนิดใดในประเทศไทย",
        "c1": "งูเห่า (Cobra) หรือ งูจงอาง (King cobra) หรือ งูสามเหลี่ยม (Banded krait)",
        "c2": "งูกะปะ (Malayan pit viper)",
        "c3": "งูเขียวหางไหม้ (Green pit viper)",
        "c4": "งูแมวเซา (Russell's viper)",
        "c5": "งูเหลือม (Reticulated python)",
        "ans": 1,
        "subtopic": "Snake Envenomation",
        "cat": "Clinic",
        "note": "Neurotoxic snake envenomation in Thailand",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. งูเห่า (Cobra) หรือ งูจงอาง (King cobra) หรือ งูสามเหลี่ยม (Banded krait)

💡 Background:
งูพิษในประเทศไทยแบ่งตามลักษณะทางคลินิกเป็น 3 กลุ่มหลัก:
1) พิษต่อระบบประสาท (Neurotoxin): งูเห่า (Cobra), งูจงอาง (King cobra), งูสามเหลี่ยม (Banded krait), งูทับสมิงคลา (Malayan krait)
2) พิษต่อระบบการแข็งตัวของเลือด (Hematotoxin): งูเขียวหางไหม้ (Green pit viper), งูกะปะ (Malayan pit viper), งูแมวเซา (Russell's viper)
3) พิษต่อกล้ามเนื้อ (Myotoxin): งูทะเล (Sea snakes)

🎯 ทำไมข้อนี้ถึงถูก:
อาการกล้ามเนื้ออ่อนแรง เริ่มจากกล้ามเนื้อใบหน้า หนังตาตก (Ptosis) ตามด้วยพูดไม่ชัด กลืนลำบาก (Bulbar palsy) และสุดท้ายกล้ามเนื้อช่วยหายใจเป็นอัมพาต (Diaphragmatic paralysis / Respiratory failure) เป็นอาการแสดงเฉพาะของ Neurotoxic snake envenomation ซึ่งต้องรีบให้เซรุ่มต้านพิษงูจำเพาะ (Monovalent or Polyvalent neurotoxic antivenom) และเตรียมใส่ท่อช่วยหายใจ

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. และ ค. งูกะปะและงูเขียวหางไหม้ เป็นงูพิษต่อระบบโลหิต ทำให้เกิดรอยเขี้ยวบวมพอง เลือดออกไม่หยุด Bleeding tendencies หรือ VCT/20WBCT ผิดปกติ
• ข้อ ง. งูแมวเซา เป็นงูพิษต่อระบบโลหิตและทำให้เกิดไตวายเฉียบพลัน (Acute renal failure) และ Conduction defect
• ข้อ จ. งูเหลือม เป็นงูไม่มีพิษ (Non-venomous snake) กัดแล้วมีเฉพาะรอยฟันรูปเกือกม้า

📖 Guideline อ้างอิง:
แนวทางการดูแลรักษาผู้ป่วยถูกงูพิษกัด สถานเสาวภา สภากาชาดไทย และ กระทรวงสาธารณสุข

📌 จุดจำก่อนสอบ:
• งูพิษต่อระบบประสาท (Neurotoxic): เห่า, จงอาง, สามเหลี่ยม, ทับสมิงคลา (อาการแรกเริ่มคือ 'หนังตาตก Ptosis')
• งูพิษต่อระบบโลหิต (Hematotoxic): กะปะ, เขียวหางไหม้, แมวเซา (ประเมินด้วย 20-minute Whole Blood Clotting Time: 20WBCT)
• เซรุ่มแก้พิษงู (Antivenom) ให้เฉพาะเมื่อมี 'ข้อบ่งชี้ทางระบบ (Systemic envenomation)' เท่านั้น ไม่ฉีดพร่ำเพรื่อเพราะเสี่ยงต่อ Anaphylaxis และ Serum sickness"""
    },
    {
        "q": "หญิงอายุ 50 ปี ถูกงูเขียวหางไหม้กัดที่นิ้วมือ มีอาการบวมลามขึ้นมาถึงข้อศอกภายใน 4 ชั่วโมง การตรวจคัดกรองการแข็งตัวของเลือดด้วยวิธี 20-minute whole blood clotting time (20WBCT) พบว่าเลือดไม่แข็งตัว (Unclotted blood) ข้อใดเป็นข้อบ่งชี้ในการให้เซรุ่มต้านพิษงู (Antivenom) ในผู้ป่วยรายนี้",
        "c1": "ผล 20WBCT ไม่แข็งตัว (Systemic hematotoxicity) หรือมีอาการบวมลามเกินกว่า 1 ข้อต่อใหญ่ภายในเวลาอันรวดเร็ว",
        "c2": "ให้เฉพาะเมื่อมีเลือดออกในอวัยวะภายใน เช่น เลือดออกในสมอง เท่านั้น",
        "c3": "ฉีดเซรุ่มเข้าที่แผลที่ถูกกัดโดยตรงเพื่อสลายพิษเฉพาะที่",
        "c4": "ต้องทำ Intradermal skin test ก่อนให้เซรุ่มทุกครั้ง หากผลบวกห้ามให้เซรุ่มเด็ดขาด",
        "c5": "ให้เซรุ่มต้านพิษงูระบบประสาทร่วมด้วยเสมอเพื่อป้องกันอาการกลืนลำบาก",
        "ans": 1,
        "subtopic": "Snake Envenomation",
        "cat": "Clinic",
        "note": "Antivenom indications and administration",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. ผล 20WBCT ไม่แข็งตัว (Systemic hematotoxicity) หรือมีอาการบวมลามเกินกว่า 1 ข้อต่อใหญ่ภายในเวลาอันรวดเร็ว

💡 Background:
เซรุ่มต้านพิษงูผลิตจากม้า (Equine-derived immunoglobulin) มีความเสี่ยงต่อการแพ้แบบ Anaphylaxis (5-10%) และ Serum sickness (10-20%) ดังนั้นจึงต้องให้เมื่อมีข้อบ่งชี้ที่ชัดเจนเท่านั้น

🎯 ทำไมข้อนี้ถึงถูก:
ข้อบ่งชี้ในการให้เซรุ่มต้านพิษงูระบบโลหิต (Hematotoxic antivenom):
1) ข้อบ่งชี้ทางระบบ (Systemic indications): 20WBCT ไม่แข็งตัว (> 20 นาที), VCT > 30 นาที, Platelet < 50,000 /mm3, มีเลือดออกผิดปกติในร่างกาย (Systemic bleeding)
2) ข้อบ่งชี้เฉพาะที่ (Local indications): บวมลามอย่างรวดเร็ว (บวมเกินครึ่งหนึ่งของแขนขาที่ถูกกัด หรือลามผ่านข้อต่อใหญ่ เช่น ข้อมือ/ข้อศอก ภายในไม่กี่ชั่วโมง) หรือเสี่ยงต่อการเกิด Compartment syndrome

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. ไม่จำเป็นต้องรอให้เลือดออกในสมอง เพราะ 20WBCT ไม่แข็งตัวแสดงถึง Defibrination syndrome ซึ่งมีข้อบ่งชี้ให้ทันทีเพื่อป้องกันภาวะแทรกซ้อน
• ข้อ ค. เซรุ่มต้านพิษงูต้องให้ทางหลอดเลือดดำ (IV infusion) เท่านั้น ห้ามฉีดเฉพาะที่รอบแผล (Local infiltration) เพราะนอกจากไม่ได้ผลแล้วยังเพิ่มความดันในเนื้อเยื่อ เสี่ยงต่อเนื้อตายและ Compartment syndrome
• ข้อ ง. ปัจจุบันไม่แนะนำให้ทำ Skin test ก่อนให้เซรุ่มเป็นกิจวัตร เพราะการทำ Skin test มี False positive/negative สูง ไม่สามารถพยากรณ์การเกิด Anaphylaxis ได้แม่นยำ และทำให้การรักษาล่าช้า หากมีข้อบ่งชี้ให้เตรียมยา Adrenaline พร้อมไว้ข้างเตียงเสมอ
• ข้อ จ. ห้ามให้เซรุ่มข้ามกลุ่ม ให้เฉพาะเซรุ่มที่ตรงกับชนิดของงู (Monovalent) หรือ Polyvalent hematotoxic เท่านั้น

📖 Guideline อ้างอิง:
แนวทางเวชปฏิบัติการดูแลรักษาผู้ป่วยถูกงูพิษกัด สถานเสาวภา สภากาชาดไทย

📌 จุดจำก่อนสอบ:
• การบริหารเซรุ่ม: IV infusion ใน NSS/D5W 100 mL หยดใน 30-60 นาที (ห้ามฉีดรอบแผล ห้ามฉีด IM)
• เตรียม Adrenaline 1:1000 ข้างเตียงเสมอเพื่อพร้อมรักษาภาวะ Anaphylaxis"""
    },
    # 13. Isoniazid Overdose
    {
        "q": "ผู้ป่วยหญิงอายุ 25 ปี กำลังรับประทานยารักษาวัณโรคปอด รับประทานยา Isoniazid (INH) ขนาด 100 มก. ไปจำนวน 50 เม็ด (5 กรัม) เพื่อประชดแฟน 2 ชั่วโมงต่อมาเกิดอาการชักเกร็งกระตุกทั้งตัว (Status epilepticus) ร่วมกับ Severe metabolic acidosis ที่ดื้อต่อการรักษาด้วยยาฉีด Diazepam และ Phenytoin ทางหลอดเลือดดำ ยาต้านพิษจำเพาะใดที่ต้องรีบให้ในขนาดมิลลิกรัมเท่ากับขนาดยา INH ที่ผู้ป่วยรับประทาน",
        "c1": "Pyridoxine (Vitamin B6) IV",
        "c2": "Thiamine (Vitamin B1) IV",
        "c3": "Folic acid IV",
        "c4": "Calcium gluconate IV",
        "c5": "Sodium bicarbonate IV",
        "ans": 1,
        "subtopic": "Antituberculosis Drug Overdose",
        "cat": "Clinic",
        "note": "Isoniazid toxicity & Pyridoxine gram-for-gram",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Pyridoxine (Vitamin B6) IV

💡 Background:
Isoniazid (INH) มีโครงสร้างคล้าย Pyridoxine เมื่อได้รับเกินขนาด INH จะเข้าจับและยับยั้งเอนไซม์ Pyridoxine phosphokinase ทำให้ไม่สามารถเปลี่ยน Pyridoxine เป็น Active form คือ Pyridoxal-5-phosphate (PLP) ได้ และ INH ยังเร่งการขับถ่าย Pyridoxine ออกทางไต เมื่อขาด PLP เอนไซม์ Glutamic acid decarboxylase (GAD) จะไม่สามารถทำงานได้ ทำให้การสังเคราะห์ Gamma-aminobutyric acid (GABA) ซึ่งเป็นสารสื่อประสาทชนิดยับยั้ง (Inhibitory neurotransmitter) ในสมองลดฮวบ ส่งผลให้เกิดอาการชักแบบควบคุมไม่ได้ (Refractory seizures) และชักต่อเนื่อง (Status epilepticus)

🎯 ทำไมข้อนี้ถึงถูก:
Pyridoxine (Vitamin B6) เป็น Specific antidote ขนานแท้สำหรับ INH overdose:
• ขนาดยาที่ให้: คำนวณแบบ Gram-for-gram คือ ให้ Vitamin B6 ทางหลอดเลือดดำในขนาดกรัมเท่ากับจำนวนกรัมของ INH ที่กินเข้าไป (ผู้ป่วยกิน INH 5 กรัม ให้ Pyridoxine 5 กรัม IV)
• หากไม่ทราบขนาด INH ที่แน่นอน ให้ขนาดเริ่มต้น 5 กรัม IV ในผู้ใหญ่ (70 mg/kg ในเด็ก) โดยให้ช้าๆ ทางหลอดเลือดดำ ยาจะไปฟื้นฟูระดับ GABA ในสมองและหยุดอาการชักได้ทันที

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Thiamine (B1) ใช้สำหรับ Wernicke's encephalopathy หรือ Beriberi
• ข้อ ค. Folic acid ใช้ใน Methanol poisoning
• ข้อ ง. Calcium gluconate ไม่สามารถแก้กลไกการขาด GABA ได้
• ข้อ จ. Sodium bicarbonate ช่วยลดภาวะกรดแต่ไม่สามารถหยุดอาการชักที่เกิดจากการขาด GABA ได้ และอาการชักจาก INH มักดื้อต่อ Phenytoin (ห้ามให้ Phenytoin ใน INH seizure เพราะไม่ได้ผลและเพิ่มพิษ)

📖 Guideline อ้างอิง:
ACMT Practice Guidelines: Management of Isoniazid Overdose และ Ramathibodi Poison Center

📌 จุดจำก่อนสอบ:
• Isoniazid Overdose Triad: Refractory seizures + Severe metabolic acidosis + Coma
• Antidote: Pyridoxine (Vit B6) บริหารแบบ Gram-for-gram IV
• ห้ามใช้ Phenytoin ในอาการชักจาก INH ให้ใช้ Benzodiazepines + Pyridoxine เท่านั้น"""
    },
    # 14. Carbon Monoxide Poisoning
    {
        "q": "ผู้ป่วย 3 รายในครอบครัวเดียวกัน ถูกนำส่งโรงพยาบาลเนื่องจากหมดสติในรถยนต์ที่จอดติดเครื่องยนต์นอนหลับ ตรวจร่างกายพบผิวหนังมีสีแดงระเรื่อ (Cherry-red lips) ผู้ป่วยรายหนึ่งรู้สึกตัวแล้วแต่บ่นปวดศีรษะตุบๆ คลื่นไส้ เวียนศีรษะ เครื่อง Pulse oximeter วัดค่า SpO2 ได้ 98% แต่ผลตรวจ Arterial Blood Gas ด้วยเครื่อง Co-oximeter พบระดับ Carboxyhemoglobin (COHb) สูงถึง 35% ข้อใดคือการจัดการที่ถูกต้องที่สุด",
        "c1": "ให้ออกซิเจนความเข้มข้น 100% ผ่าน Non-rebreather mask ทันที และพิจารณาส่งรับการบำบัดด้วย Hyperbaric Oxygen Therapy (HBOT)",
        "c2": "ให้ถอดหน้ากากออกซิเจนออกได้เนื่องจากค่า SpO2 ปกติ 98%",
        "c3": "ฉีด Methylene blue ทางหลอดเลือดดำทันที",
        "c4": "ให้ Sodium thiosulfate ทางหลอดเลือดดำ",
        "c5": "ให้การรักษาแบบประคับประคองโดยสูดอากาศปกติ (Room air) เนื่องจาก CO สลายตัวได้เอง",
        "ans": 1,
        "subtopic": "Inhalation Toxicology",
        "cat": "Clinic",
        "note": "Carbon monoxide poisoning & Pulse oximeter pitfall",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. ให้ออกซิเจนความเข้มข้น 100% ผ่าน Non-rebreather mask ทันที และพิจารณาส่งรับการบำบัดด้วย Hyperbaric Oxygen Therapy (HBOT)

💡 Background:
ก๊าซคาร์บอนมอนอกไซด์ (Carbon monoxide: CO) ไม่มีสี ไม่มีกลิ่น เกิดจากการเผาไหม้ไม่สมบูรณ์ (เช่น ควันไอเสียรถยนต์ การจุดเตาถ่านในห้องปิด) CO จะจับกับ Hemoglobin กลายเป็น Carboxyhemoglobin (COHb) โดยมีความสามารถในการจับแน่นกว่าออกซิเจนถึง 200-250 เท่า และทำให้ Oxygen-hemoglobin dissociation curve เบี่ยงไปทางซ้าย (Left shift) ปลดปล่อยออกซิเจนให้เนื้อเยื่อไม่ได้ เกิด Tissue hypoxia ทั่วร่างกาย

🎯 ทำไมข้อนี้ถึงถูก:
1) Pitfall สำคัญ: เครื่อง Standard pulse oximeter ทั่วไปแยกไม่ออกระหว่าง Oxyhemoglobin กับ Carboxyhemoglobin จึงอ่านค่า SpO2 สูงลวงตา (False normal/high) ต้องใช้เครื่อง Co-oximeter เท่านั้น
2) การรักษา: ออกซิเจนคือยาต้านพิษ (Oxygen is the antidote):
   • ที่ Room air (21% O2): ค่าครึ่งชีวิตของ COHb ประมาณ 300-320 นาที (4-5 ชั่วโมง)
   • ให้ 100% Normobaric Oxygen (NBO): ลด half-life เหลือ 60-90 นาที
   • ให้ Hyperbaric Oxygen (HBOT 2.5-3.0 atm): ลด half-life เหลือเพียง 20-30 นาที
ผู้ป่วยที่มีอาการทางระบบประสาท หมดสติ หรือ COHb > 25% มีข้อบ่งชี้ในการส่งทำ Hyperbaric Oxygen Therapy (HBOT) เพื่อลดภาวะแทรกซ้อนทางระบบประสาทระยะยาว (Delayed Neurological Sequelae: DNS)

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. เป็นข้อผิดพลาดร้ายแรง ค่า SpO2 98% เป็นค่าลวงตา
• ข้อ ค. Methylene blue ใช้สำหรับ Methemoglobinemia ไม่ใช่ CO poisoning (หากให้ใน CO จะยิ่งทำให้การขนส่งออกซิเจนแย่ลง)
• ข้อ ง. Sodium thiosulfate ใช้กับ Cyanide
• ข้อ จ. การปล่อยให้สูด Room air ทำให้เนื้อเยื่อสมองและหัวใจขาดออกซิเจนยาวนาน เกิดอันตรายถาวร

📖 Guideline อ้างอิง:
Undersea and Hyperbaric Medical Society (UHMS) Guidelines on Carbon Monoxide Poisoning

📌 จุดจำก่อนสอบ:
• Pulse oximeter ปกติไม่ได้แปลว่าไม่มี CO poisoning (ต้องตรวจ COHb ด้วย Co-oximeter)
• ออกซิเจนคือ Antidote: ให้ 100% O2 via Non-rebreather mask ทุกราย
• ข้อบ่งชี้ HBOT: หมดสติ, อาการทางสมองรุนแรง, ชัก, หัวใจขาดเลือด, สตรีตั้งครรภ์ที่มี COHb > 15-20%, หรือ COHb > 25%"""
    },
    # 15. Methemoglobinemia
    {
        "q": "ทารกอายุ 4 เดือน ได้รับยาชาเฉพาะที่ Benzocaine เจลทาเหงือกแก้ปวดฟัน ต่อมามีอาการเขียวคล้ำ (Cyanosis) ปลายมือปลายเท้าและริมฝีปากเป็นสีม่วงคล้ำ วัด SpO2 ได้ 85% ตลอดเวลาแม้จะให้ออกซิเจน 100% เลือดที่เจาะจากหลอดเลือดดำมีสีน้ำตาลช็อกโกแลต (Chocolate brown blood) และไม่เปลี่ยนเป็นสีแดงเมื่อสัมผัสอากาศ ยาต้านพิษจำเพาะใดที่ต้องให้ทางหลอดเลือดดำ และมีข้อห้ามใช้ในผู้ป่วยที่มีภาวะเอนไซม์ใดบกพร่อง",
        "c1": "Methylene blue — มีข้อห้ามใช้ในผู้ป่วย G6PD deficiency",
        "c2": "N-acetylcysteine — มีข้อห้ามใช้ในผู้ป่วยตับวาย",
        "c3": "Deferoxamine — มีข้อห้ามใช้ในผู้ป่วยโรคไต",
        "c4": "Atropine — มีข้อห้ามใช้ในผู้ป่วยโรคต้อหิน",
        "c5": "Sodium thiosulfate — มีข้อห้ามใช้ในผู้ป่วยแพ้อาหารทะเล",
        "ans": 1,
        "subtopic": "Methemoglobinemia",
        "cat": "Clinic",
        "note": "Methylene blue & G6PD contraindication",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Methylene blue — มีข้อห้ามใช้ในผู้ป่วย G6PD deficiency

💡 Background:
Methemoglobin เกิดจากธาตุเหล็กในโมเลกุลฮีโมโกลบินถูกออกซิไดซ์จาก Ferrous (Fe2+) ไปเป็น Ferric (Fe3+) ซึ่งไม่สามารถจับและขนส่งออกซิเจนได้ สารที่มักกระตุ้นให้เกิดภาวะนี้ ได้แก่ ยาชาเฉพาะที่ (Benzocaine, Prilocaine/EMLA), ยาแดปโซน (Dapsone), ยาซัลฟา (Sulfonamides), สารไนไตรต์/ไนเตรต (Nitrites ในน้ำบาดาลหรืออาหารหมักดอง) อาการทางคลินิกเด่นคือ สีผิวเขียวคล้ำ (Slate-gray cyanosis), SpO2 ค้างอยู่ที่ประมาณ 85% (Oxygen saturation gap) และเลือดเป็นสีช็อกโกแลต (Chocolate brown blood)

🎯 ทำไมข้อนี้ถึงถูก:
1) Methylene blue (1-2 mg/kg IV) เป็น Specific antidote ออกฤทธิ์เป็น Cofactor ให้กับเอนไซม์ NADPH-methemoglobin reductase เปลี่ยน Fe3+ กลับมาเป็น Fe2+ ได้อย่างรวดเร็ว
2) ข้อห้ามใช้ที่สำคัญยิ่ง: ห้ามใช้ Methylene blue ในผู้ป่วยภาวะพร่องเอนไซม์ G6PD (Glucose-6-Phosphate Dehydrogenase deficiency) เนื่องจากในผู้ป่วย G6PD เซลล์จะขาด NADPH ทำให้ Methylene blue ไม่สามารถออกฤทธิ์ได้ และตัวมันเองจะทำหน้าที่เป็น Oxidizing agent ซ้ำเติม ทำให้เกิดภาวะเม็ดเลือดแดงแตกเฉียบพลันอย่างรุนแรง (Severe acute hemolysis) หากผู้ป่วยเป็น G6PD deficiency ให้เลือกใช้วิตามินซีขนาดสูง (High-dose Ascorbic acid IV) หรือทำ Exchange transfusion แทน

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. ถึง จ. ไม่ใช่ Antidote สำหรับภาวะ Methemoglobinemia

📖 Guideline อ้างอิง:
AACT Practice Guidelines on the Treatment of Methemoglobinemia

📌 จุดจำก่อนสอบ:
• Methemoglobinemia Clues: Cyanosis refractory to O2 + Saturation gap (SpO2 ~85%) + Chocolate brown blood
• Antidote: Methylene blue 1-2 mg/kg IV slow infusion
• ข้อห้ามเด็ดขาด: G6PD Deficiency (ทำให้เกิด Severe hemolysis) -> ใช้ Ascorbic acid แทน"""
    },
    # 16. Sulfonylurea Overdose
    {
        "q": "หญิงอายุ 75 ปี เป็นโรคไตเรื้อรัง (CKD Stage 4) พลั้งเผลอรับประทานยา Glipizide ขนาด 5 มก. ผิดเป็น 10 เม็ด (50 มก.) เกิดอาการเหงื่อแตก ใจสั่น หมดสติจากภาวะ Hypoglycemia รุนแรง (DTX 28 mg/dL) หลังได้รับ 50% Dextrose 50 mL ทางหลอดเลือดดำ ผู้ป่วยรู้สึกตัวดี แต่น้ำตาลกลับตกลงซ้ำอีกหลายครั้ง (Recurrent hypoglycemia) ยาใดเป็น Antidote จำเพาะที่ยับยั้งการหลั่งอินซูลินจากตับอ่อนเพื่อป้องกันน้ำตาลตกซ้ำ",
        "c1": "Octreotide",
        "c2": "Glucagon",
        "c3": "Hydrocortisone",
        "c4": "Diazoxide เดี่ยวๆ แบบพ่นจมูก",
        "c5": "Metformin",
        "ans": 1,
        "subtopic": "Oral Hypoglycemic Overdose",
        "cat": "Clinic",
        "note": "Sulfonylurea-induced hypoglycemia & Octreotide",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Octreotide

💡 Background:
ยากลุ่ม Sulfonylureas (เช่น Glipizide, Glibenclamide) ออกฤทธิ์ปิด ATP-sensitive K+ channels บน Beta-cells ของตับอ่อน ทำให้เกิด Depolarization และเปิด Voltage-gated Ca2+ channels นำไปสู่การหลั่ง Insulin ออกมาอย่างต่อเนื่อง เมื่อเกิด Overdose การให้สารละลายกลูโคสเข้มข้น (Hypertonic dextrose) จะยิ่งไปกระตุ้นตับอ่อนให้หลั่งอินซูลินออกมาเพิ่มขึ้นอีก ทำให้เกิดวงจรอุบาทว์ของภาวะน้ำตาลตกซ้ำซาก (Rebound / Recurrent hypoglycemia)

🎯 ทำไมข้อนี้ถึงถูก:
Octreotide เป็น Synthetic somatostatin analog ออกฤทธิ์จับกับ Somatostatin receptor-2 (SSTR-2) บน Beta-cells ของตับอ่อน ยับยั้งการเปิด Voltage-gated calcium channels ทำให้หยุดการหลั่ง Insulin ได้อย่างมีประสิทธิภาพ ช่วยป้องกันการเกิด Recurrent hypoglycemia ได้อย่างยั่งยืน โดยบริหารยาในขนาด 50-100 mcg ฉีดใต้ผิวหนัง (SC) หรือเข้าหลอดเลือดดำ (IV) ทุก 6-12 ชั่วโมง

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Glucagon ออกฤทธิ์สลาย Glycogen ในตับ แต่ในผู้สูงอายุหรือผู้ที่ได้รับ Sulfonylurea ขนาดสูง ไกลโคเจนในตับมักถูกใช้จนหมดแล้ว อีกทั้ง Glucagon เองสามารถกระตุ้นการหลั่งอินซูลินจากตับอ่อนได้ จึงไม่เหมาะสำหรับการป้องกันภาวะน้ำตาลตกซ้ำ
• ข้อ ค. Hydrocortisone ออกฤทธิ์เพิ่มน้ำตาลได้ช้ามาก (หลายชั่วโมง) ไม่ทันท่วงที
• ข้อ ง. Diazoxide ชนิดรับประทานออกฤทธิ์เปิด K+ channel ยับยั้งอินซูลินได้ แต่มีผลข้างเคียงความดันต่ำ คลื่นไส้ และหาได้ยากในห้องฉุกเฉิน ไม่มีรูปแบบพ่นจมูก
• ข้อ จ. Metformin เป็นยาลดน้ำตาล ห้ามให้เด็ดขาด

📖 Guideline อ้างอิง:
American College of Medical Toxicology (ACMT) Practice Guideline on the Management of Sulfonylurea Poisoning

📌 จุดจำก่อนสอบ:
• Sulfonylurea Overdose: การให้ Glucose เพียงอย่างเดียวทำให้เกิด Rebound hypoglycemia (เพราะ Glucose ไปกระตุ้นการหลั่ง Insulin ซ้ำ)
• Antidote ทางเลือกแรกป้องกัน Hypoglycemia ซ้ำ: Octreotide SC/IV"""
    },
    # 17. Methotrexate Toxicity
    {
        "q": "ผู้ป่วยโรคมะเร็งได้รับยาเคมีบำบัด High-dose Methotrexate (HD-MTX) ทางหลอดเลือดดำ 48 ชั่วโมงต่อมาตรวจพบระดับ Serum Methotrexate สูงค้างในระดับที่เป็นพิษรุนแรงและมีภาวะไตวายเฉียบพลันร่วมด้วย ยาใดต้องให้เพื่อทำหน้าที่เป็น 'Leucovorin rescue' เพื่อแย่งจับและเติมเต็ม Folate pool ให้เซลล์ปกติ และหากต้องการทำลายโมเลกุลยา Methotrexate ในเลือดโดยตรงต้องใช้เอนไซม์ใด",
        "c1": "Leucovorin (Folinic acid) สำหรับ Rescue และใช้ Glucarpidase (Voraxaze) ในการสลาย Methotrexate",
        "c2": "Folic acid สำหรับ Rescue และใช้ Urate oxidase ในการสลาย",
        "c3": "N-acetylcysteine สำหรับ Rescue และใช้ Rasburicase ในการสลาย",
        "c4": "Thiamine สำหรับ Rescue และใช้ Deferoxamine ในการสลาย",
        "c5": "Pyridoxine สำหรับ Rescue และใช้ Pegloticase ในการสลาย",
        "ans": 1,
        "subtopic": "Oncology Antidotes",
        "cat": "Clinic",
        "note": "Leucovorin rescue and Glucarpidase in MTX toxicity",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Leucovorin (Folinic acid) สำหรับ Rescue และใช้ Glucarpidase (Voraxaze) ในการสลาย Methotrexate

💡 Background:
Methotrexate (MTX) ออกฤทธิ์ยับยั้งเอนไซม์ Dihydrofolate reductase (DHFR) ทำให้เซลล์ขาด Tetrahydrofolate (THF) ซึ่งจำเป็นต่อการสังเคราะห์ Purine และ Thymidylate นำไปสู่การหยุดชะงักของการสังเคราะห์ DNA และเซลล์ตาย ในการให้ High-dose MTX ร่างกายจะเกิดภาวะพิษต่อไขกระดูก (Myelosuppression), ทางเดินอาหาร (Mucositis) และพิษต่อไตจากการตกตะกอนของผลึก MTX ในท่อไต

🎯 ทำไมข้อนี้ถึงถูก:
1) Leucovorin (Folinic acid / 5-formyl-THF) เป็น Active form ของ Folate ที่สามารถเข้าสู่เซลล์และถูกเปลี่ยนเป็น THF ได้โดยตรงโดยไม่ต้องพึ่งพาเอนไซม์ DHFR จึงทำหน้าที่เป็น 'Leucovorin rescue' กู้ชีพเซลล์ปกติของไขกระดูกและเยื่อบุทางเดินอาหารไม่ให้ถูกทำลาย
2) ในกรณีที่เกิด Delayed MTX clearance ร่วมกับภาวะไตวายเฉียบพลัน (Severe MTX-induced renal failure) ยา Glucarpidase (Voraxaze) ซึ่งเป็น Recombinant bacterial carboxypeptidase G2 enzyme จะทำหน้าที่ย่อยสลายโมเลกุล Methotrexate ในกระแสเลือดให้กลายเป็นสารที่ไม่เป็นพิษ (DAMPA) และขับทิ้งทางตับอย่างรวดเร็วภายใน 15 นาที

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Folic acid ธรรมดาต้องอาศัยเอนไซม์ DHFR ในการเปลี่ยนเป็นรูปออกฤทธิ์ ซึ่งถูก MTX ยับยั้งอยู่ จึงไม่สามารถใช้ทำ Rescue ได้
• ข้อ ค. Rasburicase (Urate oxidase) ใช้สลาย Uric acid ในภาวะ Tumor Lysis Syndrome ไม่เกี่ยวข้องกับ MTX
• ข้อ ง. และ จ. Thiamine และ Pyridoxine ไม่เกี่ยวข้องกับวิถี Folate metabolism

📖 Guideline อ้างอิง:
Consensus Guidelines for the Management of Methotrexate Toxicity, Journal of Clinical Oncology & National Comprehensive Cancer Network (NCCN)

📌 จุดจำก่อนสอบ:
• High-dose MTX Rescue = Leucovorin (Folinic acid) ไม่ใช่ Folic acid
• MTX toxicity with acute renal failure = Glucarpidase (ย่อย MTX ในพลาสมาโดยตรง)
• การป้องกัน: Hydration + Alkalinization of urine (Sodium bicarbonate รักษาระดับ Urine pH > 7.0) เพื่อป้องกันผลึก MTX ตกตะกอนในไต"""
    },
    # 18. Salicylate Toxicity
    {
        "q": "ผู้ป่วยวัยรุ่นรับประทานยาแอสไพริน (Aspirin) ขนาด 500 มก. ไปจำนวน 40 เม็ด (20 กรัม) มีอาการหูอื้อ (Tinnitus), หายใจหอบลึกและเร็ว (Hyperventilation), คลื่นไส้อาเจียน, มีไข้ และผลเลือดพบ Mixed respiratory alkalosis ร่วมกับ High anion gap metabolic acidosis ข้อใดเป็นแนวทางการเร่งการขับถ่ายยาออกจากร่างกายที่มีประสิทธิภาพสูงสุด",
        "c1": "การทำ Urine alkalinization ด้วย Sodium bicarbonate ทางหลอดเลือดดำเพื่อรักษาระดับ pH ของปัสสาวะให้อยู่ที่ 7.5-8.5 (Ion trapping)",
        "c2": "การให้ Ammonium chloride เพื่อทำปัสสาวะให้เป็นกรดเร่งการขับยา",
        "c3": "การให้สารน้ำ Isotonic saline เพียงอย่างเดียวโดยไม่ต้องปรับความเป็นกรดด่าง",
        "c4": "การให้ Furosemide ขนาดสูงเพื่อเร่งการขับปัสสาวะ (Forced diuresis)",
        "c5": "การฉีด N-acetylcysteine เพื่อจับกับ Salicylate",
        "ans": 1,
        "subtopic": "Salicylate Toxicity",
        "cat": "Clinic",
        "note": "Aspirin toxicity & Urine alkalinization (Ion trapping)",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. การทำ Urine alkalinization ด้วย Sodium bicarbonate ทางหลอดเลือดดำเพื่อรักษาระดับ pH ของปัสสาวะให้อยู่ที่ 7.5-8.5 (Ion trapping)

💡 Background:
Salicylate มีคุณสมบัติเป็นกรดอ่อน (pKa ~3.5) และสามารถผ่าน Blood-Brain Barrier เข้าสู่สมองได้เมื่ออยู่ในรูปที่ไม่แตกตัว (Non-ionized form) พิษของ Salicylate จะไปกระตุ้นศูนย์ควบคุมการหายใจในสมองโดยตรง ทำให้เกิด Respiratory alkalosis และไปขัดขวางกระบวนการ Oxidative phosphorylation (Uncoupling of oxidative phosphorylation) ทำให้เกิดการสร้างความร้อน (Hyperthermia) และสร้างกรดแลกติก เกิด Anion gap metabolic acidosis

🎯 ทำไมข้อนี้ถึงถูก:
การทำ Urine alkalinization ด้วย Sodium bicarbonate IV:
1) เพิ่ม pH ของเลือดและปัสสาวะ: เมื่อปัสสาวะมีค่า pH 7.5-8.5 Salicylate ในท่อไตจะเปลี่ยนรูปไปเป็น Ionized form (แตกตัวมีประจุ) ไม่สามารถแพร่กลับผ่านผนังเซลล์ท่อไตเข้าสู่กระแสเลือดได้ เรียกว่าปรากฏการณ์ 'Ion trapping' ทำให้ขับถ่าย Salicylate ออกทางปัสสาวะเพิ่มขึ้นกว่า 10-20 เท่า
2) การเพิ่ม pH ในเลือดยังช่วยดึง Salicylate ออกจากเนื้อเยื่อสมองเข้าสู่กระแสเลือดอีกด้วย
3) ต้องรักษาระดับ Potassium ในเลือดให้ปกติ (> 4.0 mEq/L) เสมอ เพราะหากมีภาวะ Hypokalemia ไตจะขับ H+ แทน K+ ทำให้ปัสสาวะไม่เป็นด่าง (Paradoxical aciduria)

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. การทำปัสสาวะให้เป็นกรดจะทำให้ Salicylate อยู่ในรูปไม่แตกตัว ดูดซึมกลับเข้าเลือดและสมองมากขึ้น ส่งผลให้ผู้ป่วยเสียชีวิต
• ข้อ ค. สารน้ำธรรมดาไม่สามารถเปลี่ยนอัตราการขับถ่าย Salicylate ได้อย่างมีนัยสำคัญ
• ข้อ ง. Forced diuresis ไม่มีประโยชน์และเสี่ยงต่อการเกิดน้ำท่วมปอด (Pulmonary edema) และสมองบวม
• ข้อ จ. N-acetylcysteine เป็น Antidote ของ Paracetamol ไม่ใช่ Aspirin

📖 Guideline อ้างอิง:
EXTRIP Workgroup Recommendations for Salicylate Poisoning และแนวทางการดูแลผู้ป่วยได้รับพิษจาก Salicylate ศูนย์พิษวิทยารามาธิบดี

📌 จุดจำก่อนสอบ:
• Salicylate Toxicity Triad: Tinnitus + Hyperventilation + Mixed acid-base disorder
• Key treatment: Urine alkalinization (Target Urine pH 7.5-8.5) ด้วย NaHCO3 IV + ให้ K+ เสริม
• ข้อบ่งชี้ Hemodialysis ใน Salicylate: ระดับยา > 90-100 mg/dL, ไตวาย, ปอดบวมน้ำ, สมองบวม, ชัก หรืออาการทางคลินิกแย่ลงแม้ทำ alkalinization แล้ว"""
    },
    # 19. Extravasation Antidotes
    {
        "q": "พยาบาลแจ้งว่าเกิดเหตุน้ำยาเคมีบำบัดรั่วซึมออกนอกหลอดเลือดดำ (Extravasation) ของยา Doxorubicin (Adriamycin) ซึ่งเป็นยาเคมีบำบัดกลุ่ม Anthracycline จัดเป็น Vesicant drug ที่ทำให้เนื้อเยื่อตายอย่างรุนแรง ยาต้านพิษจำเพาะชนิดใดที่ได้รับการรับรองจาก US-FDA ให้ฉีดเข้าหลอดเลือดดำเพื่อป้องกันเนื้อเยื่อเน่าตายจาก Anthracycline extravasation",
        "c1": "Dexrazoxane (Totect / Savene)",
        "c2": "Hyaluronidase",
        "c3": "Sodium thiosulfate",
        "c4": "Dimercaprol",
        "c5": "Phentolamine",
        "ans": 1,
        "subtopic": "Chemotherapy Extravasation",
        "cat": "Clinic",
        "note": "Anthracycline extravasation antidote (Dexrazoxane)",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Dexrazoxane (Totect / Savene)

💡 Background:
Doxorubicin, Daunorubicin, Epirubicin (กลุ่ม Anthracyclines) เป็นยาเคมีบำบัดกลุ่ม DNA-binding vesicants เมื่อรั่วซึมออกนอกหลอดเลือด ตัวยาจะถูกเซลล์เนื้อเยื่อรอบข้างจับไว้และทำให้เซลล์ตายอย่างต่อเนื่อง เกิดแผลเปื่อยลึก เนื้อตายลุกลาม (Progressive tissue necrosis) ที่รักษาไม่หายและอาจต้องผ่าตัดตัดแขนขา

🎯 ทำไมข้อนี้ถึงถูก:
Dexrazoxane เป็น Specific antidote ที่ออกฤทธิ์ยับยั้งเอนไซม์ Topoisomerase II และทำหน้าที่เป็น Intracellular iron chelator ป้องกันการสร้าง Reactive oxygen species (Free radicals) ที่ทำลายเนื้อเยื่อ ได้รับการรับรองให้ใช้รักษา Anthracycline extravasation โดยให้ทางหลอดเลือดดำวันละครั้ง ติดต่อกัน 3 วัน โดยต้องเริ่มให้เร็วที่สุดภายใน 6 ชั่วโมงหลังเกิดเหตุ

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Hyaluronidase ฉีดใต้ผิวหนังรอบแผล ใช้สำหรับยาเคมีบำบัดกลุ่ม Vinca alkaloids (Vincristine, Vinblastine) และ Taxanes เพื่อสลายสาร Hyaluronic acid ในเนื้อเยื่อเกี่ยวพัน ช่วยให้ยากระจายตัวและดูดซึมออกไปเจือจาง
• ข้อ ค. Sodium thiosulfate ใช้ฉีดใต้ผิวหนังเฉพาะที่สำหรับ Mechlorethamine (Nitrogen mustard) และ Cisplatin extravasation
• ข้อ ง. Dimercaprol ใช้สำหรับพิษโลหะหนัก
• ข้อ จ. Phentolamine (Alpha-receptor blocker) ใช้สำหรับ Vasopressor extravasation (เช่น Norepinephrine, Dopamine) เพื่อขยายหลอดเลือดป้องกันเนื้อตายจากการขาดเลือด

📖 Guideline อ้างอิง:
European Society for Medical Oncology (ESMO) and Oncology Nursing Society (ONS) Guidelines on Management of Chemotherapy Extravasation

📌 จุดจำก่อนสอบ:
• Anthracyclines (Doxorubicin) Extravasation -> Dexrazoxane IV + ประคบเย็น (Cold pack)
• Vinca alkaloids (Vincristine) Extravasation -> Hyaluronidase SC + ประคบร้อน (Warm pack)
• Vasopressors (Norepinephrine) Extravasation -> Phentolamine SC รอบแผล"""
    },
    # 20. Serotonin Syndrome & Cyproheptadine
    {
        "q": "ผู้ป่วยหญิงอายุ 28 ปี รับประทานยา Sertraline 100 mg OD สำหรับรักษาโรคซึมเศร้า ไปซื้อยาแก้ปวด Tramadol 50 mg มารับประทานเองวันละ 4 ครั้ง ร่วมกับยาแก้หวัด Dextromethorphan 3 วันต่อมาถูกนำส่งโรงพยาบาลด้วยอาการกระสับกระส่าย สับสน ตัวร้อนจัด (Temp 39.5 C) เหงื่อแตกท่วมตัว หัวใจเต้นเร็ว (HR 130 bpm) ตรวจร่างกายพบ Hyperreflexia, มี Clonus (ทั้ง Inducible และ Spontaneous clonus) ชัดเจนที่ข้อเท้าทั้งสองข้าง เข้าได้กับเกณฑ์ Hunter Serotonin Toxicity Criteria หากการรักษาประคับประคองและ Benzodiazepines ไม่สามารถควบคุมอาการได้ ยาใดเป็น Serotonin antagonist จำเพาะที่สามารถใช้รักษาได้",
        "c1": "Cyproheptadine",
        "c2": "Bromocriptine",
        "c3": "Dantrolene",
        "c4": "Flumazenil",
        "c5": "Naloxone",
        "ans": 1,
        "subtopic": "Serotonin Syndrome",
        "cat": "Clinic",
        "note": "Hunter Criteria & Cyproheptadine",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Cyproheptadine

💡 Background:
Serotonin Syndrome (Serotonin Toxicity) เกิดจากการใช้ยาที่เสริมฤทธิ์การทำงานของ Serotonin ในระบบประสาทส่วนกลางร่วมกัน (ในผู้ป่วยรายนี้คือ SSRI: Sertraline + Tramadol ซึ่งยับยั้ง Serotonin reuptake + Dextromethorphan ซึ่งเป็น Serotonin reuptake inhibitor) เกณฑ์การวินิจฉัยมาตรฐานใช้ Hunter Serotonin Toxicity Criteria โดยอาการแสดงที่มีความจำเพาะสูงสุดคือภาวะ Clonus (Spontaneous, Inducible, หรือ Ocular clonus) ร่วมกับ Agitation, Diaphoresis, Hyperthermia และ Hyperreflexia

🎯 ทำไมข้อนี้ถึงถูก:
Cyproheptadine เป็นยาแก้แพ้รุ่นแรกที่มีคุณสมบัติเป็น Potent 5-HT1A and 5-HT2A receptor antagonist ที่ออกฤทธิ์ต้านการทำงานของ Serotonin โดยตรง ใช้เป็น Specific antidote ชนิดรับประทานในผู้ป่วย Serotonin syndrome ระดับปานกลางถึงรุนแรงที่ตอบสนองไม่เพียงพอต่อการรักษาด้วย Benzodiazepines

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Bromocriptine เป็น Dopamine agonist ใช้รักษา Neuroleptic Malignant Syndrome (NMS) ที่เกิดจากการขาด Dopamine (การใช้ใน Serotonin syndrome อาจทำให้อาการแย่ลง)
• ข้อ ค. Dantrolene เป็น Ryanodine receptor antagonist ใช้สำหรับ Malignant Hyperthermia จากยาดมสลบ ไม่ใช่ยาหลักสำหรับ Serotonin syndrome
• ข้อ ง. Flumazenil ใช้กับ Benzodiazepines
• ข้อ จ. Naloxone ใช้กับ Opioids แม้ Tramadol จะเป็น Opioid แต่อาการของผู้ป่วยรายนี้เกิดจาก Serotonin toxicity ซึ่ง Naloxone ไม่สามารถรักษาได้และอาจกระตุ้นให้อาการชักรุนแรงขึ้น

📖 Guideline อ้างอิง:
The New England Journal of Medicine (NEJM) Clinical Practice: The Serotonin Syndrome, and Hunter Criteria

📌 จุดจำก่อนสอบ:
• Serotonin Syndrome: Clonus (อาการเด่นสุด), Hyperreflexia, Agitation, Shivering, Diaphoresis
• Neuroleptic Malignant Syndrome (NMS): Lead-pipe rigidity (กล้ามเนื้อเกร็งแข็งเหมือนท่อตะกั่ว), Hyporeflexia, ค่อยๆ เกิดในหลักสัปดาห์
• Antidote Serotonin syndrome: Benzodiazepines + Cyproheptadine
• Antidote NMS: Bromocriptine + Amantadine + Dantrolene"""
    }
]

# We will supplement questions 21-40 with equally high-yield tox items
more_questions = [
    # 21. Warfarin Non-bleeding High INR Management
    {
        "q": "ผู้ป่วยชายอายุ 65 ปี รับประทานยา Warfarin ตรวจติดตามผลเลือดตามนัดพบว่าค่า INR = 8.5 โดยที่ผู้ป่วยไม่มีอาการเลือดออกผิดปกติใดๆ (No bleeding) สัญญาณชีพปกติ ข้อใดเป็นแนวทางการจัดการที่ถูกต้องตามแนวทางเวชปฏิบัติ CHEST 2012 / ACC 2017",
        "c1": "หยุดยา Warfarin ชั่วคราว 1-2 ครั้ง ให้รับประทาน Oral Vitamin K1 ขนาดต่ำ 1-2.5 mg และตรวจติดตามค่า INR อย่างใกล้ชิด",
        "c2": "ฉีด Vitamin K1 10 mg ทางหลอดเลือดดำทันที",
        "c3": "ให้ 4-Factor Prothrombin Complex Concentrate (PCC) ทันที",
        "c4": "ให้ Fresh Frozen Plasma (FFP) 2 ยูนิต",
        "c5": "รับประทานยา Warfarin ในขนาดเดิมต่อไปโดยไม่ต้องปรับยาเนื่องจากไม่มีอาการเลือดออก",
        "ans": 1,
        "subtopic": "Anticoagulant Reversal",
        "cat": "Clinic",
        "note": "Asymptomatic high INR management",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. หยุดยา Warfarin ชั่วคราว 1-2 ครั้ง ให้รับประทาน Oral Vitamin K1 ขนาดต่ำ 1-2.5 mg และตรวจติดตามค่า INR อย่างใกล้ชิด

💡 Background:
การจัดการผู้ป่วยที่ได้รับยา Warfarin แล้วมีค่า INR สูงผิดปกติโดยไม่มีอาการเลือดออก (Asymptomatic high INR) ต้องชั่งน้ำหนักระหว่างความเสี่ยงต่อการเกิดเลือดออกกับความเสี่ยงต่อการเกิดลิ่มเลือดอุดตันจากการลด INR ลงเร็วเกินไป (Warfarin resistance)

🎯 ทำไมข้อนี้ถึงถูก:
ตามคำแนะนำของ CHEST Guidelines:
• INR 4.5 - 10.0 โดยไม่มีอาการเลือดออก: แนะนำให้หยุดยา Warfarin 1-2 มื้อ ไม่จำเป็นต้องให้ Vitamin K1 เป็นกิจวัตร ยกเว้นผู้ป่วยมีความเสี่ยงสูงต่อการเกิดเลือดออก สามารถให้ Oral Vitamin K1 ขนาดต่ำ (1 - 2.5 mg) รับประทาน
• การให้ Vitamin K1 ชนิดรับประทานมีความปลอดภัย ปรับลด INR ได้อย่างนุ่มนวลภายใน 24 ชั่วโมง และไม่ทำให้เกิดภาวะต้านทานต่อยาวาร์ฟารินเหมือนการฉีดขนาดสูง

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. การฉีด Vitamin K1 10 mg IV มีข้อบ่งชี้เฉพาะในผู้ป่วยที่มี Major/Life-threatening bleeding เท่านั้น การให้ใน asymptomatic 환자 จะทำให้ค่า INR ตกฮวบและไม่สามารถให้ Warfarin ได้ผลนานหลายสัปดาห์
• ข้อ ค. และ ง. 4F-PCC และ FFP มีข้อบ่งชี้เฉพาะ Major life-threatening bleeding ไม่ใช้ในผู้ป่วยที่ไม่มีอาการเลือดออกเด็ดขาด
• ข้อ จ. ค่า INR 8.5 มีความเสี่ยงต่อภาวะเลือดออกในสมองสูงมาก การไม่หยุดยาเป็นอันตรายอย่างยิ่ง

📖 Guideline อ้างอิง:
CHEST Guidelines on Antithrombotic Therapy and Prevention of Thrombosis 9th/10th ed, and ACC Expert Consensus

📌 จุดจำก่อนสอบ:
• No bleeding + INR 4.5 - 10: หยุดยา 1-2 วัน (พิจารณา Oral Vit K1 1-2.5 mg เฉพาะรายที่เสี่ยงเลือดออกสูง)
• No bleeding + INR > 10: หยุดยา + ให้ Oral Vit K1 2.5 - 5 mg
• Serious / Life-threatening bleeding: 4F-PCC + IV Vit K1 5-10 mg เสมอ (ไม่ว่าค่า INR จะเป็นเท่าใด)"""
    },
    # 22. Ethylene Glycol / Oxalate crystals
    {
        "q": "ผู้ป่วยชายอายุ 30 ปี ถูกพบหมดสติหลังจากดื่มน้ำยาหล่อเย็นหม้อน้ำรถยนต์ (Antifreeze) ตรวจปัสสาวะด้วยกล้องจุลทรรศน์พบผลึกรูปซองจดหมาย (Envelope-shaped crystals) ปริมาณมาก และตรวจพบปัสสาวะเรืองแสงภายใต้แสง Wood's lamp ผลเลือดพบ High anion gap metabolic acidosis และภาวะไตวายเฉียบพลัน ผลึกดังกล่าวคือสารประกอบชนิดใด และสารตั้งต้นคืออะไร",
        "c1": "Calcium oxalate crystals เกิดจากสารพิษ Ethylene glycol",
        "c2": "Hippuric acid crystals เกิดจากสารพิษ Toluene",
        "c3": "Uric acid crystals เกิดจากสารพิษ Allopurinol",
        "c4": "Struvite crystals เกิดจากการติดเชื้อ Proteus mirabilis",
        "c5": "Cysteine crystals เกิดจากภาวะ Cystinuria",
        "ans": 1,
        "subtopic": "Toxic Alcohol",
        "cat": "Clinic",
        "note": "Calcium oxalate crystals in Ethylene glycol poisoning",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Calcium oxalate crystals เกิดจากสารพิษ Ethylene glycol

💡 Background:
น้ำยาหล่อเย็นหม้อน้ำรถยนต์ (Antifreeze coolant) มีส่วนผสมหลักคือ Ethylene glycol ซึ่งเป็นสารไม่มีสี ไม่มีกลิ่น แต่มีรสหวาน เมื่อรับประทานเข้าไปจะถูกเปลี่ยนโดย ADH และ Aldehyde dehydrogenase กลายเป็น Glycolic acid, Glyoxylic acid และสุดท้ายกลายเป็น Oxalic acid (Oxalate)

🎯 ทำไมข้อนี้ถึงถูก:
1) Oxalic acid จะเข้าจับกับ Calcium ในกระแสเลือดกลายเป็น Calcium oxalate monohydrate (รูปดัมเบลล์) หรือ Calcium oxalate dihydrate (รูปซองจดหมาย envelope-shaped crystals) ซึ่งตกตะกอนในท่อไต ทำให้เกิด Acute tubular necrosis และไตวายเฉียบพลัน
2) การจับกับแคลเซียมยังทำให้เกิดภาวะ Hypocalcemia รุนแรง
3) ในน้ำยาหล่อเย็นมักใส่สารเรืองแสง Sodium fluorescein ทำให้ปัสสาวะเรืองแสงสีเขียวภายใต้แสงอัลตราไวโอเลต (Wood's lamp) ได้ในช่วงแรก

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. ถึง จ. ไม่สอดคล้องกับประวัติดื่มน้ำยาหล่อเย็นและภาพผลึกรูปซองจดหมาย

📖 Guideline อ้างอิง:
AACT Practice Guidelines on the Treatment of Ethylene Glycol Poisoning

📌 จุดจำก่อนสอบ:
• Ethylene glycol Triad: High anion gap acidosis + Envelope-shaped Calcium oxalate crystals in urine + Acute kidney injury
• Antidote: Fomepizole หรือ Ethanol IV + Hemodialysis (หากไตวาย) + เสริม Thiamine และ Pyridoxine"""
    },
    # 23. Local Anesthetic Systemic Toxicity (LAST)
    {
        "q": "หญิงอายุ 25 ปี เข้ารับการผ่าตัดศัลยกรรมความงาม หลังได้รับการฉีดยาชาเฉพาะที่ Bupivacaine ในขนาดสูง เกิดอาการหูอื้อ ชาลิ้น ชักเกร็งกระตุก ตามด้วยหมดสติ หัวใจเต้นผิดจังหวะแบบกว้างรุนแรง (Ventricular fibrillation) และระบบไหลเวียนโลหิตล้มเหลว ยาต้านพิษทางหลอดเลือดดำชนิดใดที่ต้องรีบให้ทันทีเพื่อทำหน้าที่เป็น 'Lipid sink' ดึงยาชากลับเข้าสู่หลอดเลือด",
        "c1": "20% Intravenous Lipid Emulsion (Intralipid)",
        "c2": "Sodium bicarbonate",
        "c3": "Calcium chloride",
        "c4": "Flumazenil",
        "c5": "Methylene blue",
        "ans": 1,
        "subtopic": "Local Anesthetic Toxicity",
        "cat": "Clinic",
        "note": "LAST & 20% Lipid Emulsion",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. 20% Intravenous Lipid Emulsion (Intralipid)

💡 Background:
ภาวะพิษทั่วร่างจากยาชาเฉพาะที่ (Local Anesthetic Systemic Toxicity: LAST) มักเกิดจากการฉีดยาชาเข้าหลอดเลือดดำโดยไม่ได้ตั้งใจ หรือใช้ยาชาขนาดสูงเกินกำหนด โดยเฉพาะยาชาที่ละลายในไขมันสูง เช่น Bupivacaine ซึ่งจับกับ Cardiac sodium channels อย่างแน่นหนา ทำให้เกิดภาวะหัวใจหยุดเต้นที่ดื้อต่อการฟื้นคืนชีพ

🎯 ทำไมข้อนี้ถึงถูก:
20% Lipid Emulsion (Intralipid) เป็น First-line specific antidote สำหรับภาวะ LAST ตามแนวทางของสมาคมวิสัญญีแพทย์สากล (ASRA)
กลไกหลัก:
1) 'Lipid Sink' theory: อนุภาคไขมันในกระแสเลือดจะทำหน้าที่เป็นถังดึงยาชาที่มีคุณสมบัติละลายในไขมันสูง (Lipophilic drugs อย่าง Bupivacaine) ออกจากเนื้อเยื่อหัวใจและสมองเข้าสู่หลอดเลือด
2) Metabolic effect: เพิ่มพลังงานให้กล้ามเนื้อหัวใจโดยตรงผ่านการส่งเสริม Fatty acid oxidation
ขนาดยา: ให้ 20% Lipid emulsion 1.5 mL/kg IV bolus ใน 1 นาที ตามด้วย continuous infusion 0.25 mL/kg/min

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. ถึง จ. ไม่สามารถดึง Bupivacaine ออกจากกล้ามเนื้อหัวใจได้ และไม่ใช่ Antidote ของ LAST

📖 Guideline อ้างอิง:
American Society of Regional Anesthesia and Pain Medicine (ASRA) Practice Advisory on Local Anesthetic Systemic Toxicity

📌 จุดจำก่อนสอบ:
• LAST Signs: ชารอบปาก ลิ้นชา หูอื้อ โลหะในปาก -> ชัก -> Cardiovascular collapse / VF
• Antidote: 20% Intralipid IV ทันที ร่วมกับการทำ CPR คุณภาพสูง (ลดขนาด Epinephrine เหลือ < 1 mcg/kg และหลีกเลี่ยง Vasopressin, Beta-blockers, CCB)"""
    },
    # 24. TCA Poisoning & Sodium Bicarbonate
    {
        "q": "ผู้ป่วยชายอายุ 35 ปี รับประทานยา Amitriptyline 50 มก. ไปจำนวน 40 เม็ด (2,000 มก.) มีอาการซึม ม่านตาขยาย ปากแห้ง ผิวแห้ง ตรวจ EKG พบ Sinus tachycardia อัตรา 125 bpm, QRS complex กว้าง 140 msec และพบ Terminal R wave สูง > 3 mm ใน lead aVR ยาใดเป็น First-line treatment ที่ต้องให้ทางหลอดเลือดดำทันทีเพื่อลดความเสี่ยงต่อการเกิด Ventricular arrhythmia และชัก",
        "c1": "Sodium bicarbonate (NaHCO3) 8.4% IV push",
        "c2": "Amiodarone IV infusion",
        "c3": "Physostigmine IV",
        "c4": "Phenytoin IV infusion",
        "c5": "Procainamide IV",
        "ans": 1,
        "subtopic": "Antidepressant Toxicity",
        "cat": "Clinic",
        "note": "TCA toxicity & Sodium bicarbonate (QRS narrowing)",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Sodium bicarbonate (NaHCO3) 8.4% IV push

💡 Background:
Tricyclic Antidepressants (TCAs เช่น Amitriptyline, Imipramine) มีกลไกความเป็นพิษหลายระบบ:
1) ยับยั้ง Fast sodium channels ในกล้ามเนื้อหัวใจ (Quinidine-like / Class Ia antiarrhythmic effect) ทำให้การนำไฟฟ้าช้าลง เกิด QRS prolongation (> 100 msec เสี่ยงชัก, > 160 msec เสี่ยง Ventricular arrhythmia) และ Terminal R wave in aVR > 3 mm
2) ต้าน Muscarinic receptor (Anticholinergic toxidrome)
3) ต้าน Alpha-1 receptor (ความดันโลหิตต่ำ)
4) ต้าน GABA receptor ในสมอง (ชัก)

🎯 ทำไมข้อนี้ถึงถูก:
Sodium bicarbonate (NaHCO3) ออกฤทธิ์แก้พิษหัวใจผ่าน 2 กลไกสำคัญ:
1) เพิ่มระดับ Sodium ในกระแสเลือด (Sodium load) เพื่อแย่งจับชนะการบล็อก Sodium channel ของ TCA
2) ปรับค่า pH ของเลือดให้เป็นด่าง (Serum alkalinization: Target pH 7.45 - 7.55) ซึ่งจะทำให้โมเลกุล TCA เปลี่ยนเป็นรูปไม่แตกตัว (Neutral form) หลุดออกจาก Sodium channels บนเยื่อหุ้มเซลล์หัวใจ ส่งผลให้ QRS แคบลงและป้องกันการเต้นผิดจังหวะ

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข., ข้อ ด., ข้อ จ. Class Ia (Procainamide), Class Ic, และ Class III (Amiodarone) antiarrhythmics เป็น 'ข้อห้ามใช้เด็ดขาด' ใน TCA poisoning เนื่องจากยาเหล่านี้บล็อก Sodium/Potassium channels จะยิ่งทำให้ QRS กว้างขึ้นและหัวใจเต้นผิดจังหวะรุนแรงถึงชีวิต
• ข้อ ค. Physostigmine แม้จะแก้ Anticholinergic ได้ แต่เป็น 'ข้อห้ามใช้ใน TCA overdose' เพราะอาจทำให้เกิด Asystole และชักรุนแรง
• ข้อ ง. Phenytoin ไม่ได้ผลในการกันชักจาก TCA และเพิ่มอัตราการเต้นผิดจังหวะของหัวใจ

📖 Guideline อ้างอิง:
ACMT Guidelines for the Management of Tricyclic Antidepressant Toxicity

📌 จุดจำก่อนสอบ:
• EKG clues in TCA toxicity: QRS > 100 msec, Right axis deviation, Terminal R in aVR > 3 mm
• Treatment: Sodium bicarbonate 8.4% 1-2 mEq/kg IV push จนกว่า QRS จะแคบลง (< 100 msec)
• ห้ามใช้ Class Ia, Ic, III antiarrhythmics และ Physostigmine เด็ดขาด"""
    },
    # 25. Valproate / L-carnitine
    {
        "q": "ผู้ป่วยหญิงอายุ 22 ปี รับประทานยา Sodium valproate ขนาด 200 มก. ไป 50 เม็ด (10,000 มก.) เกิดอาการซึม สับสน ตรวจเลือดพบ Serum Ammonia สูงถึง 180 mcg/dL (Hyperammonemic encephalopathy) และระดับ Valproic acid ในเลือดสูงเกินเกณฑ์การรักษา ยาใดเป็น Antidote จำเพาะที่ช่วยเร่งการขจัดแอมโมเนียและเมแทบอลิซึมของ Valproic acid",
        "c1": "L-carnitine (Levocarnitine)",
        "c2": "N-acetylcysteine",
        "c3": "Lactulose ร่วมกับ Neomycin เท่านั้น",
        "c4": "Thiamine",
        "c5": "Pyridoxine",
        "ans": 1,
        "subtopic": "Antiepileptic Drug Overdose",
        "cat": "Clinic",
        "note": "Valproate-induced hyperammonemia & L-carnitine",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. L-carnitine (Levocarnitine)

💡 Background:
Sodium valproate เมื่อได้รับเกินขนาดจะขัดขวางกระบวนการ Beta-oxidation ของกรดไขมันในไมโทคอนเดรีย และทำให้เกิดการพร่อง Carnitine ภายในเซลล์ นอกจากนี้ Metabolite ของยากลุ่ม Valproate ยังไปยับยั้งเอนไซม์ Carbamoyl phosphate synthetase I (CPS I) ใน Urea cycle ของตับ ส่งผลให้ร่างกายไม่สามารถเปลี่ยน Ammonia เป็น Urea ได้ เกิดภาวะแอมโมเนียในเลือดสูง (Valproate-induced Hyperammonemic Encephalopathy: VHE) ซึ่งทำให้สมองบวมและโคม่า

🎯 ทำไมข้อนี้ถึงถูก:
L-carnitine (Levocarnitine) เป็น Specific antidote สำหรับ Valproic acid toxicity ที่มีภาวะ Hyperammonemia, Encephalopathy หรือ Hepatotoxicity โดย L-carnitine จะเข้าไปฟื้นฟู Carnitine pool ในไมโทคอนเดรีย ส่งเสริม Beta-oxidation และช่วยฟื้นฟูการทำงานของ Urea cycle ทำให้ระดับแอมโมเนียในเลือดลดลงสู่ระดับปกติอย่างรวดเร็ว

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. N-acetylcysteine อาจใช้เสริมในกรณีตับวาย แต่ไม่ใช่ Antidote หลักในการลดแอมโมเนียจาก Valproate
• ข้อ ค. Lactulose ช่วยขับแอมโมเนียในทางเดินอาหารจาก Cirrhosis แต่ไม่สามารถแก้ความผิดปกติของ Urea cycle ในไมโทคอนเดรียจาก Valproate ได้
• ข้อ ง. และ จ. Thiamine และ Pyridoxine ไม่เกี่ยวข้องกับกลไกความเป็นพิษของ Valproic acid

📖 Guideline อ้างอิง:
ACMT Practice Guidelines on the Use of L-Carnitine in Valproic Acid Toxicity

📌 จุดจำก่อนสอบ:
• Valproate Toxicity: Encephalopathy + Hyperammonemia (แม้ค่าตับ AST/ALT อาจปกติ)
• Antidote: L-carnitine IV (Loading 100 mg/kg ตามด้วย 50 mg/kg ทุก 8 ชั่วโมง)"""
    },
    # 26. Caustic Ingestion (Contraindication of Emesis/Lavage/Neutralization)
    {
        "q": "เด็กชายอายุ 4 ขวบ แอบดื่มน้ำยาล้างห้องน้ำชนิดกรดรุนแรง (Hydrochloric acid) เข้าไป 1 อึก มารดานำส่งห้องฉุกเฉินทันที เด็กมีอาการร้องไห้กระวนกระวาย น้ำลายไหล เจ็บคอมาก ริมฝีปากและช่องปากมีแผลไหม้ขาว การจัดการในข้อใดเป็น 'ข้อห้ามทำเด็ดขาด' ในการปฐมพยาบาลเบื้องต้น",
        "c1": "การทำให้อาเจียน, การล้างกระเพาะอาหาร (Gastric lavage), การให้สารสะเทินกรด (Neutralization ด้วยด่าง), และการให้ Activated charcoal",
        "c2": "การให้ผู้ป่วยงดน้ำและอาหาร (NPO) ทางปาก",
        "c3": "การให้สารน้ำทางหลอดเลือดดำและยาแก้ปวดอย่างเหมาะสม",
        "c4": "การปรึกษาแพทย์ศัลยกรรมหรือทางเดินอาหารเพื่อส่องกล้อง Esophagogastroduodenoscopy (EGD) ภายใน 24-48 ชั่วโมง",
        "c5": "การตรวจประเมินทางเดินหายใจอย่างใกล้ชิด",
        "ans": 1,
        "subtopic": "Corrosive / Caustic Ingestion",
        "cat": "Clinic",
        "note": "Contraindications in caustic ingestion",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. การทำให้อาเจียน, การล้างกระเพาะอาหาร (Gastric lavage), การให้สารสะเทินกรด (Neutralization ด้วยด่าง), และการให้ Activated charcoal

💡 Background:
สารกัดกร่อน (Caustic substances) แบ่งเป็น กรดแก่ (Strong acids เช่น น้ำยาล้างห้องน้ำ ทำให้เกิด Coagulation necrosis) และ ด่างแก่ (Strong alkalis เช่น โซดาไฟ น้ำยาฟอกขาว ทำให้เกิด Liquefaction necrosis ซึ่งแทรกซึมลึกและทะลุง่ายกว่า)

🎯 ทำไมข้อนี้ถึงถูก:
ข้อห้ามเด็ดขาด (Absolute Contraindications) ใน Caustic ingestion:
1) ห้ามทำให้อาเจียน (No emesis): สารกัดกร่อนจะไหลย้อนกลับมากัดซ้ำทางเดินอาหารส่วนบน กล่องเสียง และเสี่ยงต่อการสำลักลงปอด (Aspiration)
2) ห้ามล้างกระเพาะ (No gastric lavage / NG tube): เสี่ยงต่อการแทงทะลุหลอดอาหารหรือกระเพาะอาหาร (Esophageal/Gastric perforation)
3) ห้ามให้สารสะเทิน (No chemical neutralization): การให้สารด่างไปสะเทินกรดจะเกิดปฏิกิริยาคายความร้อน (Exothermic reaction) ทำให้เกิดแผลไหม้จากความร้อน (Thermal injury) ซ้ำเติมเนื้อเยื่อ
4) ห้ามให้ Activated charcoal: ไม่สามารถดูดซับกรด/ด่างได้ และจะบดบังทัศนวิสัยของแพทย์ในการส่องกล้อง EGD

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. ถึง จ. ล้วนเป็นการดูแลรักษาที่ถูกต้องและจำเป็นตามมาตรฐาน (NPO, IV fluids, Pain control, Airway assessment, Early EGD within 24-48 hr)

📖 Guideline อ้างอิง:
World Society of Emergency Surgery (WSES) Guidelines on Caustic Ingestion and Ramathibodi Poison Center

📌 จุดจำก่อนสอบ:
• Caustic ingestion: Do NOT induce vomiting, Do NOT lavage, Do NOT neutralize, Do NOT give charcoal!
• Early endoscopy (EGD) ภายใน 24-48 ชั่วโมง เพื่อประเมินความรุนแรง (Zargar's classification)"""
    },
    # 27. Anticholinergic Toxicity & Physostigmine
    {
        "q": "วัยรุ่นชายอายุ 18 ปี ไปเที่ยวงานวัดและรับประทานเมล็ดต้นลำโพง (Datura stramonium) เนื่องจากอยากรู้รสชาติ 2 ชั่วโมงต่อมาเกิดอาการเพ้อคลั่ง ประสาทหลอน เอื้อมมือคว้าสิ่งของในอากาศ (Delirium) ม่านตาขยายกว้างและไม่ตอบสนองต่อแสง ผิวหนังแห้งแดงและร้อนจัด ไม่มีเหงื่อ ปัสสาวะไม่ออก ท้องอืด ไม่มีเสียงลำไส้เคลื่อนไหว เข้าได้กับ Anticholinergic Toxidrome ยาต้านพิษชนิดใดเป็น Acetylcholinesterase inhibitor ที่สามารถผ่านเข้าสู่ระบบประสาทส่วนกลางเพื่อรักษาอาการเพ้อคลั่งได้",
        "c1": "Physostigmine",
        "c2": "Neostigmine",
        "c3": "Pyridostigmine",
        "c4": "Atropine",
        "c5": "Pralidoxime",
        "ans": 1,
        "subtopic": "Plant Toxicology",
        "cat": "Clinic",
        "note": "Anticholinergic toxidrome & Physostigmine",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Physostigmine

💡 Background:
ต้นลำโพง (Datura stramonium) มีสารสำคัญคือ Belladonna alkaloids ได้แก่ Scopolamine (Hyoscine) และ Atropine ซึ่งออกฤทธิ์เป็น Anticholinergic (Antimuscarinic) agent อาการแสดงจำด้วยคำคล้องจองคลาสสิก:
• 'Blind as a bat' (Mydriasis / Blurry vision)
• 'Mad as a hatter' (Delirium / Hallucinations)
• 'Red as a beet' (Flushing)
• 'Hot as a hare' (Hyperthermia / Anhidrosis)
• 'Dry as a bone' (Dry mouth / Urinary retention / Ileus)

🎯 ทำไมข้อนี้ถึงถูก:
Physostigmine เป็นสารกลุ่ม Tertiary amine reversible acetylcholinesterase inhibitor ด้วยความที่เป็น Tertiary amine (โมเลกุลไม่มีประจุ) จึงสามารถซึมผ่าน Blood-Brain Barrier (BBB) เข้าสู่สมองได้ แตกต่างจาก Neostigmine และ Pyridostigmine ซึ่งเป็น Quaternary amines (มีประจุ ไม่ผ่าน BBB) ดังนั้น Physostigmine จึงเป็น Antidote เพียงตัวเดียวที่สามารถแก้ไขอาการสับสน เพ้อคลั่ง และกระสับกระส่ายรุนแรง (Central anticholinergic symptoms) ได้อย่างมีประสิทธิภาพ

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. และ ค. Neostigmine และ Pyridostigmine ไม่สามารถผ่าน BBB เข้าสมองได้ จึงแก้ได้เฉพาะ Peripheral symptoms
• ข้อ ง. Atropine เป็นสารพิษชนิดเดียวกับที่มีในต้นลำโพง การให้จะยิ่งเพิ่มความเป็นพิษ
• ข้อ จ. Pralidoxime ใช้ฟื้นฟูเอนไซม์ใน Organophosphate ไม่เกี่ยวข้องกับ Anticholinergic

📖 Guideline อ้างอิง:
ACMT Position Statement: The Use of Physostigmine in Anticholinergic Toxicity

📌 จุดจำก่อนสอบ:
• Anticholinergic Toxidrome: Mydriasis + Anhidrosis + Hyperthermia + Delirium + Urinary retention
• Antidote: Physostigmine (Tertiary amine ผ่าน BBB ได้)
• ระวัง: ห้ามใช้ Physostigmine หากสงสัย TCA overdose หรือมี QRS กว้างเด็ดขาด (เสี่ยง Asystole)"""
    },
    # 28. Cyanide vs Hydrogen Sulfide
    {
        "q": "คนงานลอกท่อระบายน้ำหมดสติลงไปในบ่อเกรอะบำบัดน้ำเสียทันทีที่เปิดฝาท่อ มีกลิ่นไข่เน่า (Rotten egg odor) รุนแรงในบริเวณเกิดเหตุ สารพิษชนิดใดเป็นสาเหตุ และยาแก้พิษกลุ่มใดที่สามารถให้เพื่อเหนี่ยวนำให้เกิด Sulfmethemoglobin ดึงสารพิษออกจาก Cytochrome oxidase",
        "c1": "Hydrogen sulfide (H2S) — รักษาด้วย Sodium nitrite หรือ Amyl nitrite (ห้ามให้ Sodium thiosulfate)",
        "c2": "Methane — รักษาด้วย ออกซิเจน 100%",
        "c3": "Carbon monoxide — รักษาด้วย Methylene blue",
        "c4": "Ammonia — รักษาด้วย Sodium bicarbonate",
        "c5": "Chlorine — รักษาด้วย N-acetylcysteine",
        "ans": 1,
        "subtopic": "Inhalation Toxicology",
        "cat": "Clinic",
        "note": "Hydrogen sulfide poisoning & Nitrites",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Hydrogen sulfide (H2S) — รักษาด้วย Sodium nitrite หรือ Amyl nitrite (ห้ามให้ Sodium thiosulfate)

💡 Background:
ก๊าซไฮโดรเจนซัลไฟด์ (Hydrogen sulfide: H2S หรือก๊าซไข่เน่า) เกิดจากการย่อยสลายสารอินทรีย์โดยแบคทีเรีย มักพบในบ่อเกรอะ ท่อระบายน้ำ โรงงานฟอกหนัง หรือบ่อขยะ ก๊าซนี้มีกลิ่นไข่เน่าที่ความเข้มข้นต่ำ แต่ที่ความเข้มข้นสูงจะทำให้ประสาทรับกลิ่นเป็นอัมพาตทันที (Olfactory fatigue) และทำให้ผู้สูดดมหมดสติล้มลงทันที เรียกว่า 'Knockdown effect'

🎯 ทำไมข้อนี้ถึงถูก:
1) กลไกความเป็นพิษของ H2S คล้ายกับ Cyanide มาก โดยไปจับกับ Fe3+ ใน Cytochrome c oxidase ยับยั้ง Cellular respiration ทำให้เกิด Histotoxic hypoxia
2) การรักษา: ให้ Sodium nitrite หรือสูดดม Amyl nitrite เพื่อเปลี่ยน Hemoglobin เป็น Methemoglobin (MetHb) ซึ่ง Fe3+ ใน MetHb จะไปแย่งจับกับ Sulfide กลายเป็น Sulfmethemoglobin ปลดปล่อย Cytochrome oxidase ให้กลับมาทำงานได้
3) ข้อแตกต่างสำคัญจาก Cyanide: 'ห้ามให้ Sodium thiosulfate' ใน Hydrogen sulfide poisoning เนื่องจากร่างกายมีระดับ Thiosulfate สูงอยู่แล้ว และเอนไซม์ Rhodanese ไม่ได้ใช้ในการขจัด Sulfide

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Methane เป็นก๊าซเฉื่อยที่แทนที่ออกซิเจน (Simple asphyxiant) ไม่มีกลิ่นไข่เน่า
• ข้อ ค. CO ไม่มีกลิ่นไข่เน่า และ Methylene blue ไม่ใช่ยารักษา
• ข้อ ง. และ จ. ไม่ตรงกับสารเคมีและอาการแสดง

📖 Guideline อ้างอิง:
Medical Toxicology of Hazardous Materials, ATSDR Guidelines on Hydrogen Sulfide

📌 จุดจำก่อนสอบ:
• H2S (ก๊าซไข่เน่า): Knockdown effect ในบ่อบำบัดน้ำเสีย/ท่อระบายน้ำ
• Antidote: Sodium nitrite IV (เหนี่ยวนำ MetHb ดึง Sulfide ออก)
• จำ: ไซยาไนด์ให้ Nitrite + Thiosulfate แต่ ไฮโดรเจนซัลไฟด์ให้เฉพาะ Nitrite (ไม่ให้ Thiosulfate)"""
    },
    # 29. Whole Bowel Irrigation
    {
        "q": "การล้างลำไส้ทั้งระบบ (Whole Bowel Irrigation: WBI) ด้วยสารละลาย Polyethylene Glycol-Electrolyte Solution (PEG-ELS) ทางสายยางให้อาหาร มีข้อบ่งชี้ที่ชัดเจนและมีประโยชน์สูงสุดในกรณีใดต่อไปนี้",
        "c1": "ผู้ลักลอบกลืนห่อยาเสพติดเข้าสู่ร่างกาย (Body packers) หรือการกลืนยาเม็ดชนิดออกฤทธิ์เนิ่นปริมาณมาก (Sustained-release drugs เช่น Verapamil SR)",
        "c2": "การรับประทานยานอนหลับ Diazepam ชนิดน้ำ",
        "c3": "การกลืนสารกัดกร่อนกรดกำมะถันรุนแรง",
        "c4": "ผู้ป่วยที่มีภาวะลำไส้อุดตัน (Bowel obstruction) หรือลำไส้ทะลุ",
        "c5": "การรับประทานยาพาราเซตามอลชนิดเม็ดธรรมดาภายใน 1 ชั่วโมง",
        "ans": 1,
        "subtopic": "Gastrointestinal Decontamination",
        "cat": "Product",
        "note": "Whole bowel irrigation indications & contraindications",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. ผู้ลักลอบกลืนห่อยาเสพติดเข้าสู่ร่างกาย (Body packers) หรือการกลืนยาเม็ดชนิดออกฤทธิ์เนิ่นปริมาณมาก (Sustained-release drugs เช่น Verapamil SR)

💡 Background:
Whole Bowel Irrigation (WBI) เป็นวิธีการขจัดสารพิษออกจากระบบทางเดินอาหารโดยการให้สารละลาย Polyethylene glycol-electrolyte solution (PEG-ELS เช่น Klean-Prep, Fortrans) ในอัตราเร็วสูง (1-2 ลิตร/ชั่วโมงในผู้ใหญ่) ทางสาย Nasogastric tube เพื่อชะล้างทางเดินอาหารตั้งแต่กระเพาะอาหารจนถึงทวารหนักโดยไม่ทำให้เกิดการสูญเสียหรือดูดซึมน้ำและเกลือแร่

🎯 ทำไมข้อนี้ถึงถูก:
ข้อบ่งชี้จำเพาะของ Whole Bowel Irrigation ตาม AACT/EAPCCT Guidelines:
1) การลักลอบกลืนห่อถุงยางบรรจุยาเสพติด เช่น เฮโรอีนหรือโคเคน (Body packers / Body stuffers) เพื่อเร่งการขับถ่ายออกมาก่อนที่ห่อจะแตกทะลุ
2) การรับประทานยาเม็ดรูปแบบออกฤทธิ์เนิ่นหรือควบคุมการปลดปล่อย (Sustained-release หรือ Extended-release) ปริมาณมาก เช่น Calcium channel blockers SR, Beta-blockers SR
3) การรับประทานสารพิษที่ไม่ถูกดูดซับด้วย Activated charcoal ในปริมาณมาก เช่น ธาตุเหล็ก (Iron) หรือ ลิเทียม (Lithium)

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. ยาน้ำดูดซึมเร็วมาก WBI ไม่มีประโยชน์
• ข้อ ค. Caustic ingestion เป็นข้อห้ามเด็ดขาดของการล้างท้องทุกชนิด
• ข้อ ง. ภาวะลำไส้อุดตัน (Ileus/Obstruction), ลำไส้ทะลุ (Perforation), เลือดออกในทางเดินอาหาร เป็น 'ข้อห้ามใช้เด็ดขาด' ของ WBI
• ข้อ จ. พาราเซตามอลเม็ดธรรมดาดูดซึมเร็ว ให้ Activated charcoal ภายใน 1-2 ชั่วโมงก็เพียงพอ ไม่ต้องทำ WBI

📖 Guideline อ้างอิง:
American Academy of Clinical Toxicology (AACT) and European Association of Poisons Centres and Clinical Toxicologists (EAPCCT) Position Paper on Whole Bowel Irrigation

📌 จุดจำก่อนสอบ:
• ข้อบ่งชี้ WBI: Body packers, Sustained-release tablets (CCB SR), Heavy metals (Iron, Lithium)
• น้ำยาที่ใช้: PEG-ELS (Iso-osmolar ปลอดภัยต่อ Electrolytes)
• อัตราเร็ว: ผู้ใหญ่ 1.5 - 2 L/hr, เด็ก 25 - 40 mL/kg/hr จนกว่าน้ำที่ถ่ายออกมาจะใส"""
    },
    # 30. Activated Charcoal Pitfalls (Substances NOT absorbed)
    {
        "q": "ผงถ่านกัมมันต์ (Activated Charcoal) มีคุณสมบัติในการดูดซับสารพิษในทางเดินอาหารได้ดีมาก อย่างไรก็ตาม สารในกลุ่มใดต่อไปนี้เป็นสารที่ 'ไม่ถูกดูดซับ' หรือดูดซับได้น้อยมากด้วย Activated Charcoal จึงไม่มีประโยชน์ในการบริหารยา",
        "c1": "โลหะหนัก (Iron, Lead, Lithium), แอลกอฮอล์ (Ethanol, Methanol), กรดแก่-ด่างแก่, และเกลือแร่โพแทสเซียม",
        "c2": "Paracetamol, Carbamazepine, Theophylline, Phenobarbital",
        "c3": "Dapsone, Quinine, Digoxin, Amitriptyline",
        "c4": "Aspirin, Propranolol, Phenytoin, Diazepam",
        "c5": "Chlorpheniramine, Dextromethorphan, Tramadol",
        "ans": 1,
        "subtopic": "Gastrointestinal Decontamination",
        "cat": "Product",
        "note": "Substances NOT absorbed by Activated Charcoal (PHAILS mnemonic)",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. โลหะหนัก (Iron, Lead, Lithium), แอลกอฮอล์ (Ethanol, Methanol), กรดแก่-ด่างแก่, และเกลือแร่โพแทสเซียม

💡 Background:
Activated Charcoal (AC) มีพื้นที่ผิวในการดูดซับสูงมาก (1,000-2,000 ตารางเมตรต่อกรัม) แต่การดูดซับต้องอาศัยแรง Van der Waals forces และ Hydrogen bonding สารประกอบที่มีขั้วสูง โมเลกุลเล็ก แตกตัวเป็นไอออนสูง หรือเป็นโลหะหนัก จะไม่สามารถจับกับผงถ่านกัมมันต์ได้

🎯 ทำไมข้อนี้ถึงถูก:
สารที่ไม่จับกับ Activated Charcoal จำด้วยตัวย่อ 'PHAILS':
• P: Pesticides, Potassium
• H: Heavy metals (Iron, Lead, Arsenic, Mercury), Hydrocarbons (น้ำมันก๊าด น้ำมันเบนซิน)
• A: Acids, Alkalis, Alcohols (Ethanol, Methanol, Ethylene glycol)
• I: Iron
• L: Lithium
• S: Solvents
การให้ Activated charcoal ในสารกลุ่มนี้ไม่ได้ประโยชน์ และในกลุ่ม Hydrocarbons หรือ Caustics ยังเพิ่มความเสี่ยงต่อการอาเจียนและสำลักเข้าปอด (Chemical pneumonitis)

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. ถึง จ. ล้วนเป็นสารที่ถูกดูดซับด้วย Activated charcoal ได้ดีมาก และยาบางชนิด (เช่น Carbamazepine, Theophylline, Phenobarbital, Dapsone) ยังมีข้อบ่งชี้ในการให้แบบหลายขนาด (Multiple-dose activated charcoal: MDAC) อีกด้วย

📖 Guideline อ้างอิง:
AACT/EAPCCT Position Paper: Single-Dose Activated Charcoal

📌 จุดจำก่อนสอบ:
• ไม่ดูดซับด้วย Charcoal (PHAILS): เหล็ก, ลิเทียม, แอลกอฮอล์, กรด-ด่าง, โพแทสเซียม, ไฮโดรคาร์บอน
• ขนาดยา Activated Charcoal: 1 g/kg (ผู้ใหญ่ 50-100 g) ละลายน้ำอัตราส่วน 1:4 หรือ 1:8
• มีประโยชน์สูงสุดภายใน 1 ชั่วโมงแรกหลังรับประทานสารพิษ"""
    }
]

questions.extend(more_questions)

# Questions 31-40 to make exactly 40 pristine questions
final_ten = [
    # 31. Multiple-Dose Activated Charcoal (MDAC)
    {
        "q": "การให้ผงถ่านกัมมันต์ซ้ำหลายขนาด (Multiple-Dose Activated Charcoal: MDAC หรือ 'Gastrointestinal Dialysis') ช่วยเพิ่มการขจัดยาออกจากร่างกายทางเดินอาหารได้อย่างมีนัยสำคัญ มีข้อบ่งชี้ที่ชัดเจนตามหลักฐานทางการแพทย์สำหรับยาในข้อใดต่อไปนี้",
        "c1": "Theophylline, Carbamazepine, Phenobarbital, Dapsone, Quinine",
        "c2": "Paracetamol, Iron, Lithium, Methanol",
        "c3": "Diazepam, Lorazepam, Midazolam, Alprazolam",
        "c4": "Amlodipine, Enalapril, Losartan, Hydrochlorothiazide",
        "c5": "Amoxicillin, Ciprofloxacin, Ceftriaxone, Azithromycin",
        "ans": 1,
        "subtopic": "Gastrointestinal Decontamination",
        "cat": "Clinic",
        "note": "Indications for MDAC (ABCDQ)",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Theophylline, Carbamazepine, Phenobarbital, Dapsone, Quinine

💡 Background:
Multiple-Dose Activated Charcoal (MDAC) คือการให้ Activated charcoal ขนาดเริ่มต้น 50-100 g ตามด้วยขนาด 25-50 g ทุก 2-4 ชั่วโมง กลไกคือการรบกวนกระบวนการ Enterohepatic circulation และดึงโมเลกุลยาจากกระแสเลือดผ่านเยื่อบุลำไส้กลับสู่โพรงลำไส้ตามความแตกต่างของความเข้มข้น (Back-diffusion / Gastrointestinal dialysis)

🎯 ทำไมข้อนี้ถึงถูก:
ยาที่มีข้อบ่งชี้ชัดเจนสำหรับการทำ MDAC ตามเกณฑ์ AACT/EAPCCT:
• Theophylline
• Carbamazepine
• Phenobarbital
• Dapsone
• Quinine
คุณสมบัติของยาที่เหมาะกับ MDAC คือ: 1) ปริมาตรการกระจายตัวต่ำ (Low Volume of distribution: Vd < 1 L/kg) 2) มีการจับกับโปรตีนต่ำถึงปานกลาง 3) มี Enterohepatic หรือ Enteroenteric recirculation 4) การขับยาตามปกติเกิดขึ้นช้า

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Paracetamol ใช้ NAC ส่วน Iron/Lithium/Methanol ไม่จับกับถ่านกัมมันต์
• ข้อ ค. Benzodiazepines มีการกระจายตัวสูง (High Vd) การทำ MDAC ไม่ช่วยลดระยะเวลาการรักษา
• ข้อ ง. และ จ. ยาความดันและยาปฏิชีวนะไม่มีข้อบ่งชี้ของ MDAC

📖 Guideline อ้างอิง:
AACT/EAPCCT Position Paper on Multiple-Dose Activated Charcoal

📌 จุดจำก่อนสอบ:
• ยาที่ทำ MDAC แล้วได้ผลดีที่สุด (จำ: 'The Car Daps Phen Quine'): Theophylline, Carbamazepine, Dapsone, Phenobarbital, Quinine
• ข้อควรระวัง: ต้องตรวจสอบ Bowel sounds ก่อนให้ทุกครั้ง ห้ามให้หากผู้ป่วยมี Ileus หรือ Bowel obstruction"""
    },
    # 32. Hydrocarbon Ingestion
    {
        "q": "เด็กหญิงอายุ 3 ขวบ สำลักน้ำมันก๊าด (Kerosene) ที่ผู้ปกครองแบ่งใส่ขวดน้ำดื่มไว้ มีอาการไอ สำลัก หายใจเหนื่อย และได้ยินเสียงเสมหะในคอ การจัดการในข้อใด 'ถูกต้องและปลอดภัยที่สุด'",
        "c1": "ห้ามทำให้อาเจียนและห้ามล้างกระเพาะอาหารเด็ดขาด ให้ออกซิเจนและถ่ายภาพรังสีทรวงอก (Chest X-ray) ติดตามภาวะ Chemical pneumonitis",
        "c2": "ให้กินไข่ขาวดิบหรือนมสดเพื่อเคลือบกระเพาะอาหาร",
        "c3": "ล้างกระเพาะอาหารทันทีด้วยสายยางขนาดใหญ่",
        "c4": "ให้ Activated charcoal 50 กรัมทันทีเพื่อดูดซับน้ำมันก๊าด",
        "c5": "ให้ยาขับปัสสาวะ Furosemide เพื่อเร่งการขับถ่ายสารพิษออกทางไต",
        "ans": 1,
        "subtopic": "Hydrocarbon Toxicology",
        "cat": "Clinic",
        "note": "Hydrocarbon ingestion & Aspiration chemical pneumonitis",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. ห้ามทำให้อาเจียนและห้ามล้างกระเพาะอาหารเด็ดขาด ให้ออกซิเจนและถ่ายภาพรังสีทรวงอก (Chest X-ray) ติดตามภาวะ Chemical pneumonitis

💡 Background:
สารกลุ่มไฮโดรคาร์บอน (Hydrocarbons เช่น น้ำมันก๊าด, น้ำมันเบนซิน, ทินเนอร์) มีคุณสมบัติ: ความหนืดต่ำ (Low viscosity), แรงตึงผิวต่ำ (Low surface tension), และความดันไอสูง (High volatility) สารที่มีคุณสมบัติเหล่านี้จะแพร่กระจายและสำลักเข้าสู่ทางเดินหายใจได้ง่ายมาก ทำให้เกิดปอดอักเสบจากสารเคมีอย่างรุนแรง (Chemical pneumonitis) และทำลายสารลดแรงตึงผิวในปอด (Surfactant)

🎯 ทำไมข้อนี้ถึงถูก:
การดูแลรักษาผู้ป่วยที่ดื่มสารกลุ่ม Hydrocarbons:
1) 'ห้ามทำให้อาเจียนและห้ามล้างท้องเด็ดขาด' เพราะจะยิ่งเพิ่มความเสี่ยงของการสำลักสารไฮโดรคาร์บอนเข้าสู่ปอด
2) ไม่ให้ Activated charcoal เพราะถ่านไม่ดูดซับไฮโดรคาร์บอนและทำให้อาเจียนสำลัก
3) การรักษาหลักคือ ประคับประคองระบบหายใจ ให้ออกซิเจน และติดตามอาการทางปอดอย่างน้อย 6 ชั่วโมงร่วมกับตรวจ Chest X-ray หากไม่มีอาการผิดปกติและภาพถ่ายรังสีปอดปกติหลังจาก 6 ชั่วโมงจึงสามารถกลับบ้านได้

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. การให้นมหรือไข่ขาวอาจทำให้อาเจียนและสำลักซ้ำเติม
• ข้อ ค. และ ง. การล้างท้องและผงถ่านกัมมันต์เป็นข้อห้ามเพราะเพิ่มความเสี่ยงปอดอักเสบ
• ข้อ จ. ไฮโดรคาร์บอนไม่ถูกขับทางไต ยาขับปัสสาวะไม่มีประโยชน์

📖 Guideline อ้างอิง:
AAP (American Academy of Pediatrics) Policy on Hydrocarbon Ingestion and Ramathibodi Poison Center

📌 จุดจำก่อนสอบ:
• Hydrocarbons ingestion: อันตรายสูงสุดคือ 'Aspiration chemical pneumonitis' ไม่ใช่ความเป็นพิษต่อกระเพาะ
• ห้ามทำให้อาเจียน ห้ามล้างท้อง ห้ามให้ Charcoal สังเกตอาการทางปอดอย่างน้อย 6 ชั่วโมง"""
    },
    # 33. Rodenticide (Superwarfarin) Poisoning
    {
        "q": "เด็กชายอายุ 5 ขวบ แอบรับประทานยาเบื่อหนูชนิดเม็ดข้าวโพดสีฟ้า-แดงที่มีสาร Brodifacoum (Long-acting anticoagulant rodenticide หรือ Superwarfarin) ไป 1 กำมือ เมื่อ 4 วันก่อน มาโรงพยาบาลด้วยอาการปัสสาวะเป็นเลือด (Hematuria) และมีจ้ำเลือดตามตัว ตรวจค่า INR พบว่ายาวนานผิดปกติ (> 10) การรักษาด้วย Vitamin K1 ในผู้ป่วยรายนี้มีความแตกต่างจากการรักษาพิษจาก Warfarin ทั่วไปอย่างไร",
        "c1": "ต้องให้ Vitamin K1 ในขนาดสูงและต่อเนื่องเป็นเวลานานหลายสัปดาห์ถึงหลายเดือน เนื่องจาก Brodifacoum มีค่าครึ่งชีวิตยาวนานมากและสะสมในตับ",
        "c2": "ให้ Vitamin K1 เพียงครั้งเดียวขนาด 10 mg ก็เพียงพอเนื่องจากยาขับออกทางไตอย่างรวดเร็ว",
        "c3": "Brodifacoum ไม่ตอบสนองต่อ Vitamin K1 ต้องใช้การฟอกเลือด (Hemodialysis) เท่านั้น",
        "c4": "ใช้ Protamine sulfate ฉีดเข้าหลอดเลือดดำแทน Vitamin K1",
        "c5": "ให้หยุดการรักษาทันทีที่ค่า INR กลับมาเป็นปกติใน 24 ชั่วโมงแรก",
        "ans": 1,
        "subtopic": "Rodenticide Toxicity",
        "cat": "Clinic",
        "note": "Superwarfarin poisoning & Prolonged Vitamin K1 therapy",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. ต้องให้ Vitamin K1 ในขนาดสูงและต่อเนื่องเป็นเวลานานหลายสัปดาห์ถึงหลายเดือน เนื่องจาก Brodifacoum มีค่าครึ่งชีวิตยาวนานมากและสะสมในตับ

💡 Background:
ยาเบื่อหนูกลุ่ม Superwarfarin (LAARs: Long-acting anticoagulant rodenticides เช่น Brodifacoum, Diphacinone, Bromadiolone) มีฤทธิ์ยับยั้งเอนไซม์ Vitamin K epoxide reductase เช่นเดียวกับ Warfarin แต่มีความแรง (Potency) สูงกว่า Warfarin ถึง 100 เท่า และละลายในไขมันสูงมาก มีค่าครึ่งชีวิตในร่างกายยาวนานถึง 20-60 วัน (หลายสัปดาห์ถึงหลายเดือน)

🎯 ทำไมข้อนี้ถึงถูก:
เนื่องจาก Superwarfarin สะสมในตับและออกฤทธิ์ยับยั้งการสังเคราะห์ Clotting factors อย่างยาวนาน การรักษาจึงต้องให้ Vitamin K1 (Phytomenadione) ในขนาดสูง (ผู้ใหญ่ 50-200 mg/day, เด็ก 1-5 mg/kg/day ชนิดรับประทาน) ต่อเนื่องเป็นเวลานานหลายสัปดาห์ถึงหลายเดือนจนกว่าสารพิษจะถูกกำจัดหมด โดยต้องตรวจติดตามค่า INR สม่ำเสมอหลังจากหยุด Vitamin K1

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. และ จ. การให้ระยะสั้นเพียงครั้งเดียวหรือหยุดยาทันทีที่ INR ปกติ จะทำให้ค่า INR เด้งกลับมาสูงวิกฤตและเกิดเลือดออกรุนแรงซ้ำในสัปดาห์ถัดไป
• ข้อ ค. Superwarfarin มี Volume of distribution สูงและจับกับโปรตีนสูง ไม่สามารถกำจัดด้วย Hemodialysis ได้ และตอบสนองต่อ Vitamin K1 ได้ดีมาก
• ข้อ ง. Protamine sulfate ใช้กับ Heparin ไม่เกี่ยวข้องกับ Superwarfarin

📖 Guideline อ้างอิง:
Management of Long-Acting Anticoagulant Rodenticide Poisoning, American College of Medical Toxicology (ACMT)

📌 จุดจำก่อนสอบ:
• Superwarfarin (Brodifacoum): Half-life นานหลายสัปดาห์ (Lipophilic)
• การรักษา: Oral Vitamin K1 ขนาดสูง ต่อเนื่อง 'หลายสัปดาห์ถึงหลายเดือน' (ห้ามหยุดยาเร็ว)"""
    },
    # 34. Paraquat Toxicity
    {
        "q": "ชาวสวนดื่มสารกำจัดวัชพืช พาราควอต (Paraquat: 27.6% W/V) เข้าไปประมาณ 1 ฝาขวด (15-20 mL) หลังดื่มมีอาการแสบร้อนในปากและลำคอรุนแรง เยื่อบุช่องปากเปื่อยลอก การจัดการในข้อใดเป็น 'ข้อควรระวังสำคัญที่สุด' ที่ห้ามทำหากผู้ป่วยยังไม่มีภาวะ Hypoxia รุนแรง",
        "c1": "การให้ออกซิเจนเสริม (Oxygen therapy) โดยไม่จำเป็น เนื่องจากออกซิเจนจะเร่งปฏิกิริยา Redox cycling สร้าง Reactive Oxygen Species (ROS) ทำลายเนื้อเยื่อปอดจนเกิด Pulmonary fibrosis รวดเร็วขึ้น",
        "c2": "การให้สารดูดซับดิน Fuller's earth หรือดินขาว Kaolin",
        "c3": "การให้ยาแก้ปวดกลุ่ม Opioids ทางหลอดเลือดดำ",
        "c4": "การให้สารน้ำทางหลอดเลือดดำอย่างเพียงพอ",
        "c5": "การบ้วนปากด้วยน้ำสะอาดปริมาณมาก",
        "ans": 1,
        "subtopic": "Pesticide Toxicology",
        "cat": "Clinic",
        "note": "Paraquat toxicity & Avoid Oxygen therapy",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. การให้ออกซิเจนเสริม (Oxygen therapy) โดยไม่จำเป็น เนื่องจากออกซิเจนจะเร่งปฏิกิริยา Redox cycling สร้าง Reactive Oxygen Species (ROS) ทำลายเนื้อเยื่อปอดจนเกิด Pulmonary fibrosis รวดเร็วขึ้น

💡 Background:
พาราควอต (Paraquat) เป็นสารกำจัดวัชพืชที่มีความเป็นพิษเฉียบพลันร้ายแรงมาก อัตราการเสียชีวิตสูงถึง 60-80% ตัวยาจะถูกดูดซึมและสะสมในเซลล์ถุงลมปอด (Alveolar type I & II cells) ผ่าน Polyamine uptake pathway ภายในเซลล์ Paraquat จะเกิดปฏิกิริยา Redox cycling รับอิเล็กตรอนจาก NADPH แล้วส่งต่อให้ออกซิเจน เกิดเป็น Superoxide radicals, Hydrogen peroxide และ Hydroxyl radicals ทำลายเยื่อหุ้มเซลล์ (Lipid peroxidation) นำไปสู่การเกิดพังผืดในปอดอย่างรวดเร็ว (Pulmonary fibrosis) และระบบหายใจล้มเหลว

🎯 ทำไมข้อนี้ถึงถูก:
การให้ออกซิเจนเสริม (Supplemental oxygen) จะทำหน้าที่เป็นสารตั้งต้นเร่งปฏิกิริยา Redox cycling ของ Paraquat ให้สร้าง Free radicals มากขึ้นอย่างมหาศาล ทำให้เนื้อเยื่อปอดถูกทำลายเร็วขึ้น ดังนั้น 'ห้ามให้ออกซิเจนเสริม' แก่ผู้ป่วย Paraquat poisoning เว้นแต่ผู้ป่วยจะมีภาวะ Severe hypoxia (PaO2 < 40 mmHg หรือ SpO2 < 85%) โดยให้ตั้งเป้าหมาย SpO2 เพียงแค่พอประคับประคองชีวิต (Low target SpO2 ~85-88%)

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. การให้ Fuller's earth (ดินฟูลเลอร์ 15%) หรือ Bentonite หรือ Activated charcoal เป็นการรักษามาตรฐานในการดูดซับพาราควอตในทางเดินอาหาร
• ข้อ ค., ง., จ. เป็นการดูแลประคับประคองที่ถูกต้อง

📖 Guideline อ้างอิง:
WHO and Ramathibodi Poison Center Clinical Practice Guidelines for the Management of Paraquat Poisoning

📌 จุดจำก่อนสอบ:
• Paraquat toxicity: สะสมที่ปอด เกิด Redox cycling -> Pulmonary fibrosis
• กฎเหล็ก: 'DO NOT give oxygen' เว้นแต่ Hypoxia วิกฤตจริงๆ
• สารดูดซับ: Fuller's earth 15% หรือ Activated charcoal เร็วที่สุด"""
    },
    # 35. Lithium Toxicity & Hemodialysis
    {
        "q": "ผู้ป่วยโรคไบโพลาร์รับประทานยา Lithium carbonate เกิดภาวะ Acute-on-chronic lithium toxicity ตรวจระดับ Serum Lithium ได้ 4.2 mEq/L ผู้ป่วยมีอาการสับสน สั่น กระตุก (Myoclonus), เดินเซ (Ataxia), ไตวายเฉียบพลัน และคลื่นไฟฟ้าหัวใจผิดปกติ การรักษาใดเป็นวิธีที่มีประสิทธิภาพสูงสุดในการกำจัด Lithium ออกจากร่างกายอย่างเร่งด่วน",
        "c1": "การฟอกเลือดด้วยเครื่องไตเทียม (Intermittent Hemodialysis)",
        "c2": "การให้ Activated charcoal ทางสายยาง",
        "c3": "การทำ Urine alkalinization ด้วย Sodium bicarbonate",
        "c4": "การให้ยาขับปัสสาวะ Furosemide",
        "c5": "การให้ Sodium polystyrene sulfonate (Kayexalate) ชนิดสวนทวาร",
        "ans": 1,
        "subtopic": "Psychiatric Drug Overdose",
        "cat": "Clinic",
        "note": "Lithium toxicity & Hemodialysis indications",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. การฟอกเลือดด้วยเครื่องไตเทียม (Intermittent Hemodialysis)

💡 Background:
Lithium เป็น Monovalent cation ที่มีโมเลกุลขนาดเล็กมาก (MW 7 Da), ไม่จับกับโปรตีนในพลาสมา (0% Protein binding), มี Volume of distribution ปานกลาง (0.7-0.9 L/kg) และถูกขับออกทางไตเป็นหลัก คุณสมบัติเหล่านี้ทำให้ Lithium เป็นยาที่สามารถกำจัดผ่านการฟอกเลือด (Hemodialysis) ได้ดีเยี่ยม

🎯 ทำไมข้อนี้ถึงถูก:
เกณฑ์การทำ Hemodialysis ในภาวะ Lithium Toxicity ตาม EXTRIP Workgroup:
1) ระดับ Serum Lithium > 4.0 mEq/L ไม่ว่าจะมีอาการหรือไม่
2) ระดับ Serum Lithium > 2.5 mEq/L ร่วมกับมีอาการทางระบบประสาทรุนแรง (ชัก, โคม่า, สับสน), ภาวะไตวาย, หรือมีโรคร่วมที่ไม่สามารถขับยาได้
3) ข้อควรจำ: หลังทำ Hemodialysis ระดับ Lithium จะเด้งกลับสูงขึ้นได้ (Post-dialysis rebound) จากการที่ลิเทียมเคลื่อนออกจากเซลล์สู่กระแสเลือด จึงต้องตรวจระดับซ้ำหลังฟอกเลือด 6-8 ชั่วโมง และอาจต้องฟอกเลือดซ้ำ

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Activated charcoal ไม่ดูดซับลิเทียม
• ข้อ ค. Urine alkalinization ไม่ได้ช่วยเพิ่มการขับถ่ายลิเทียมอย่างมีนัยสำคัญ
• ข้อ ง. Diuretics (โดยเฉพาะ Thiazides) ลดการขับลิเทียมและทำให้พิษรุนแรงขึ้น
• ข้อ จ. Kayexalate ไม่ใช่การรักษามาตรฐานสำหรับ Lithium toxicity

📖 Guideline อ้างอิง:
EXTRIP (Extracorporeal Treatments in Poisoning) Workgroup Guidelines for Lithium Poisoning

📌 จุดจำก่อนสอบ:
• Lithium toxicity: ระดับ > 4.0 mEq/L หรือ > 2.5 mEq/L + Neuro symptoms/Renal failure -> ทำ Hemodialysis
• ระวัง Post-dialysis rebound ของระดับลิเทียมหลังฟอกเลือด"""
    },
    # 36. Amphetamine / Sympathomimetic Toxidrome
    {
        "q": "ชายอายุ 24 ปี ถูกนำส่งโรงพยาบาลโดยเจ้าหน้าที่ตำรวจเนื่องจากมีอาการคลุ้มคลั่ง เอะอะโวยวาย หวาดระแวง เหงื่อแตกท่วมตัว หัวใจเต้นเร็ว (HR 145 bpm) ความดันโลหิตสูง (BP 190/110 mmHg) อุณหภูมิร่างกาย 39.2 องศาเซลเซียส ม่านตาขยายทั้งสองข้าง (Mydriasis 6 mm) สัมพันธ์กับภาวะ Sympathomimetic Toxidrome จากการเสพยาบ้า (Methamphetamine) ยาทางเลือกแรกในการควบคุมอาการกระสับกระส่าย ลดความดันโลหิต และป้องกันภาวะ Rhabdomyolysis คือข้อใด",
        "c1": "Benzodiazepines ทางหลอดเลือดดำ (เช่น Diazepam หรือ Lorazepam)",
        "c2": "Beta-blocker ชนิดไม่คัดเลือก เช่น Propranolol IV",
        "c3": "Haloperidol ฉีดเข้ากล้ามเนื้อเดี่ยวๆ",
        "c4": "Aspirin หรือ Paracetamol ทางปากเพื่อลดไข้",
        "c5": "Norepinephrine infusion",
        "ans": 1,
        "subtopic": "Substance Abuse Toxicology",
        "cat": "Clinic",
        "note": "Sympathomimetic toxidrome & Benzodiazepines",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Benzodiazepines ทางหลอดเลือดดำ (เช่น Diazepam หรือ Lorazepam)

💡 Background:
Methamphetamine และยากลุ่ม Amphetamines กระตุ้นการหลั่งสาร Catecholamines (Dopamine, Norepinephrine, Serotonin) เข้าสู่ Synaptic cleft ทำให้เกิด Sympathomimetic Toxidrome อาการแสดง: หัวใจเต้นเร็ว, ความดันโลหิตสูง, ม่านตาขยาย, เหงื่อออกมาก (Diaphoresis แตกต่างจาก Anticholinergic ที่ผิวจะแห้ง), ไข้สูง, กล้ามเนื้อเกร็ง และกระสับกระส่าย ภาวะแทรกซ้อนอันตรายคือ ความดันโลหิตสูงวิกฤต, ภาวะกล้ามเนื้อลายสลาย (Rhabdomyolysis), ไตวาย และเลือดออกในสมอง

🎯 ทำไมข้อนี้ถึงถูก:
Benzodiazepines (Diazepam 5-10 mg IV ทุก 5-10 นาที จนกว่าจะสงบ) เป็น First-line therapy สำหรับ Sympathomimetic toxicity ทุกชนิด:
• เพิ่มการทำงานของ GABA ในสมอง ช่วยลดความตื่นตัวของระบบประสาทส่วนกลาง (CNS agitation)
• ลด Sympathetic outflow ส่งผลให้ความดันโลหิตและอัตราการเต้นของหัวใจลดลง
• ลดการเกร็งตัวของกล้ามเนื้อ ช่วยลดความร้อนในร่างกายและป้องกัน Rhabdomyolysis

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Beta-blockers (เช่น Propranolol, Labetalol) มีความเสี่ยงต่อปรากฏการณ์ 'Unopposed alpha-adrenergic stimulation' คือเมื่อปิด Beta-2 receptor จะทำให้ Alpha-1 receptor ทำงานเดี่ยวๆ ส่งผลให้หลอดเลือดหดเกร็งรุนแรง ความดันโลหิตพุ่งสูงวิกฤตและหลอดเลือดหัวใจตีบตันได้ จึงห้ามให้ Pure beta-blockers
• ข้อ ค. Haloperidol ลด Threshold การชัก ขัดขวางการระบายความร้อนของร่างกาย (Anticholinergic side effect) และเพิ่มความเสี่ยงต่อ QTc prolongation และ Arrhythmias
• ข้อ ง. ไข้จาก Sympathomimetic เกิดจากกล้ามเนื้อทำงานหนัก ไม่ได้เกิดจาก Pyrogen ในสมอง ยาลดไข้พาราเซตามอล/แอสไพรินไม่ได้ผล ต้องใช้ External cooling ร่วมกับ Benzodiazepines

📖 Guideline อ้างอิง:
American Heart Association (AHA) and ACMT Guidelines on Management of Methamphetamine and Cocaine Toxicity

📌 จุดจำก่อนสอบ:
• Sympathomimetic (เหงื่อแตก) vs Anticholinergic (ผิวแห้ง ไม่มีเหงื่อ)
• First-line: Benzodiazepines IV ขนาดสูงจนสงบ
• ห้ามใช้ Beta-blockers เดี่ยวๆ (Unopposed alpha stimulation)"""
    },
    # 37. Theophylline Toxicity & Hemoperfusion
    {
        "q": "ผู้ป่วยหญิงอายุ 68 ปี รับประทานยาขยายหลอดลม Theophylline เกินขนาด เกิดภาวะ Severe acute toxicity ตรวจ EKG พบ Supraventricular tachycardia และ Multifocal Atrial Tachycardia (MAT) ร่วมกับมีอาการชักเกร็ง (Intractable seizures) และระดับ Theophylline ในเลือดสูงถึง 110 mcg/mL ข้อใดเป็นแนวทางการรักษาเพื่อกำจัดสารพิษออกจากร่างกายอย่างเร่งด่วน",
        "c1": "การทำ Charcoal Hemoperfusion หรือ Hemodialysis ร่วมกับการให้ Multiple-Dose Activated Charcoal (MDAC)",
        "c2": "การให้สารสะเทินกรดในกระเพาะอาหาร",
        "c3": "การฉีด Flumazenil เพื่อหยุดอาการชัก",
        "c4": "การให้ยาขับปัสสาวะ Thiazides",
        "c5": "การล้างกระเพาะอาหารด้วยน้ำเย็นจัด",
        "ans": 1,
        "subtopic": "Respiratory Drug Overdose",
        "cat": "Clinic",
        "note": "Theophylline toxicity & Extracorporeal removal",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. การทำ Charcoal Hemoperfusion หรือ Hemodialysis ร่วมกับการให้ Multiple-Dose Activated Charcoal (MDAC)

💡 Background:
Theophylline ยับยั้งเอนไซม์ Phosphodiesterase (เพิ่ม cAMP) และยับยั้ง Adenosine receptors กระตุ้นการหลั่ง Catecholamines มหาศาล ในภาวะเป็นพิษรุนแรง (Serum level > 80-100 mcg/mL ใน Acute หรือ > 40-60 mcg/mL ใน Chronic) จะทำให้เกิด Refractory ventricular arrhythmias, Severe hypokalemia, Hyperglycemia, Metabolic acidosis และ Status epilepticus ซึ่งมักดื้อต่อยากันชักทั่วไปและมีอัตราการเสียชีวิตสูง

🎯 ทำไมข้อนี้ถึงถูก:
1) Theophylline มี Volume of distribution ต่ำ (0.5 L/kg) และจับกับโปรตีนปานกลาง สามารถกำจัดออกจากเลือดได้อย่างมีประสิทธิภาพสูงด้วย Charcoal Hemoperfusion หรือ High-flux Hemodialysis
2) ในระหว่างรอเตรียมเครื่องไตเทียม ให้ Multiple-Dose Activated Charcoal (MDAC) ทางเดินอาหารเพื่อเร่งการขจัดยาผ่าน Gastrointestinal dialysis
3) สำหรับอาการหัวใจเต้นเร็วผิดจังหวะ ยาที่เลือกใช้คือ Short-acting Beta-blockers เช่น Esmolol

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข., ข้อ ง., ข้อ จ. ไม่มีบทบาทในการขจัด Theophylline
• ข้อ ค. Flumazenil เป็นข้อห้ามใช้เนื่องจากอาจกระตุ้นให้ชักมากขึ้น (อาการชักจาก Theophylline ให้รักษาด้วย Benzodiazepines และ Barbiturates)

📖 Guideline อ้างอิง:
EXTRIP Workgroup Recommendations for the Management of Theophylline Poisoning

📌 จุดจำก่อนสอบ:
• Theophylline Toxicity: Arrhythmias + Seizures + Hypokalemia + Hyperglycemia
• Extracorporeal clearance: Hemoperfusion / Hemodialysis เมื่อระดับยา > 100 mcg/mL (Acute) หรือชัก/หัวใจเต้นผิดจังหวะรุนแรง"""
    },
    # 38. Pyrethroid Toxicity
    {
        "q": "แม่บ้านมีอาการแสบร้อน ชา คันยิบๆ ที่ใบหน้าและผิวหนัง (Paresthesia) หลังจากฉีดสเปรย์กำจัดยุงและแมลงสาบสูตรที่มีสาร ไพรีทรอยด์ (Pyrethroids เช่น Cypermethrin, Permethrin) สารชนิดใดที่แนะนำให้ทาบริเวณผิวหนังเพื่อบรรเทาอาการชาแสบร้อนจากพิษของสารไพรีทรอยด์ได้อย่างมีประสิทธิภาพ",
        "c1": "Topical Vitamin E (DL-alpha-tocopheryl acetate cream)",
        "c2": "Topical Corticosteroid cream (Triamcinolone acetonide)",
        "c3": "Calamine lotion",
        "c4": "Silver sulfadiazine cream",
        "c5": "Alcohol 70%",
        "ans": 1,
        "subtopic": "Pesticide Toxicology",
        "cat": "Product",
        "note": "Pyrethroid paresthesia & Vitamin E cream",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Topical Vitamin E (DL-alpha-tocopheryl acetate cream)

💡 Background:
สารเคมีกำจัดแมลงกลุ่มไพรีทรินและไพรีทรอยด์ (Pyrethrins and Pyrethroids) สังเคราะห์เลียนแบบสารสกัดจากดอกเบญจมาศ ออกฤทธิ์ยืดเวลาการเปิดของ Voltage-gated sodium channels ในเซลล์ประสาท ทำให้เกิด Repetitive nerve discharge เมื่อสัมผัสทางผิวหนังจะทำให้เกิดอาการระคายเคือง ชา แสบร้อน คันยิบๆ (Cutaneous paresthesia / Stinging sensation) ซึ่งมักถูกน้ำชะล้างออกยากเนื่องจากละลายในไขมันสูง

🎯 ทำไมข้อนี้ถึงถูก:
การทาครีมที่มีส่วนผสมของ Vitamin E (DL-alpha-tocopheryl acetate cream หรือ oil) ได้รับการพิสูจน์ทางการแพทย์แล้วว่าเป็นยาเฉพาะที่ที่สามารถยับยั้งการกระตุ้นที่ปลายประสาทและบรรเทาอาการ Cutaneous paresthesia จาก Pyrethroid ได้อย่างรวดเร็วและมีประสิทธิภาพสูงสุด

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Topical steroids ไม่ได้ช่วยยับยั้ง Sodium channel activity ที่ปลายประสาท จึงไม่ช่วยลดอาการชาแสบร้อน
• ข้อ ค. Calamine lotion ให้ความเย็นชั่วคราวแต่ไม่สามารถแก้กลไกของไพรีทรอยด์ได้
• ข้อ ง. Silver sulfadiazine ใช้รักษาแผลไฟไหม้ติดเชื้อ
• ข้อ จ. แอลกอฮอล์จะยิ่งชะล้างไขมันผิวหนัง ทำให้ระคายเคืองและดูดซึมสารเคมีเพิ่มขึ้น

📖 Guideline อ้างอิง:
EPA (United States Environmental Protection Agency) Guidelines on Recognition and Management of Pesticide Poisonings: Pyrethrins and Pyrethroids

📌 จุดจำก่อนสอบ:
• Pyrethroids dermal exposure: Cutaneous paresthesia (ชาแสบคันยิบๆ)
• Specific topical remedy: Vitamin E acetate cream / oil"""
    },
    # 39. Botulism / Antitoxin
    {
        "q": "ชาวบ้าน 5 คนในหมู่บ้านเดียวกัน มีอาการหนังตาตก มองเห็นภาพซ้อน (Diplopia), กลืนลำบาก พูดไม่ชัด ลิ้นแข็ง, ปากแห้ง ม่านตาขยาย และกล้ามเนื้อแขนขาอ่อนแรงแบบสมมาตร โดยเริ่มจากศีรษะลงมาสู่ส่วนล่างของร่างกาย (Symmetrical descending flaccid paralysis) โดยที่ระดับความรู้สึกตัวยังปกติ หลังจากรับประทานหน่อไม้ปี๊บที่ผลิตเองในครัวเรือน ภาวะนี้เกิดจากสารพิษชนิดใด และยาต้านพิษที่ต้องให้คือข้อใด",
        "c1": "Botulinum neurotoxin จาก Clostridium botulinum — รักษาด้วย Equine Botulinum Antitoxin (Heptavalent หรือ Trivalent)",
        "c2": "Tetrodotoxin จากปลาปักเป้า — รักษาด้วย Atropine",
        "c3": "Ciguatoxin จากปลาทะเล — รักษาด้วย Mannitol",
        "c4": "Aflatoxin จากถั่วลิสง — รักษาด้วย N-acetylcysteine",
        "c5": "Saxitoxin จากหอยทะเล — รักษาด้วย Sodium thiosulfate",
        "ans": 1,
        "subtopic": "Foodborne Toxicology",
        "cat": "Clinic",
        "note": "Foodborne Botulism & Equine Botulinum Antitoxin",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. Botulinum neurotoxin จาก Clostridium botulinum — รักษาด้วย Equine Botulinum Antitoxin (Heptavalent หรือ Trivalent)

💡 Background:
โรคโบทูลิซึม (Foodborne Botulism) มักเกิดจากการรับประทานอาหารหมักดองหรืออาหารกระป๋องที่ผลิตไม่ได้มาตรฐาน (ในประเทศไทยพบประวัติคลาสสิกจากการรับประทานหน่อไม้ปี๊บต้มที่ไม่ผ่านความร้อนฆ่าเชื้อสปอร์) เชื้อ Clostridium botulinum เจริญในสภาวะไร้ออกซิเจนและสร้าง Botulinum neurotoxin ซึ่งเป็นโปรตีนที่ทนกรดในกระเพาะอาหาร สารพิษจะเข้าจับกับ Presynaptic cholinergic nerve terminals และทำลาย SNARE proteins (เช่น SNAP-25, Synaptobrevin) ทำให้ถุงเก็บ Acetylcholine ไม่สามารถหลอมรวมกับเยื่อหุ้มเซลล์เพื่อหลั่งสารสื่อประสาทได้ (Inhibition of acetylcholine release)

🎯 ทำไมข้อนี้ถึงถูก:
1) อาการแสดงคลาสสิกของ Botulism:
   • 4Ds: Diplopia (เห็นภาพซ้อน), Dysarthria (พูดไม่ชัด), Dysphagia (กลืนลำบาก), Dysphonia (เสียงเปลี่ยน)
   • Symmetrical descending flaccid paralysis: กล้ามเนื้ออ่อนแรงแบบสมมาตร เริ่มจากเส้นประสาทสมอง (Cranial nerves) ลงสู่แขน ขา และกล้ามเนื้อกระบังลม
   • Sensory ปกติ และไม่มีไข้
2) การรักษา: ต้องรีบให้ Equine Botulinum Antitoxin (เช่น Heptavalent BAT types A-G หรือ Trivalent types A, B, E) โดยเร็วที่สุด เพื่อจับกับสารพิษที่ยังลอยอยู่ในกระแสเลือดก่อนที่สารพิษจะเข้าสู่เซลล์ประสาท (สารพิษที่เข้าเซลล์ประสาทไปแล้วแอนติท็อกซินไม่สามารถดึงกลับมาได้ ต้องรอให้สร้าง Nerve terminal ใหม่ซึ่งใช้เวลาหลายเดือน)

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. Tetrodotoxin เกิดจากปลาปักเป้า บล็อก Sodium channel ไม่มีแอนติท็อกซินจำเพาะ
• ข้อ ค. Ciguatoxin เกิดจากปลาแนวปะการัง ทำให้เกิด Cold allodynia
• ข้อ ง. และ จ. ไม่ตรงกับเชื้อก่อโรคและอาการอัมพาตจากหน่อไม้ปี๊บ

📖 Guideline อ้างอิง:
CDC Guidance for the Management of Botulism and Bureau of Epidemiology, Department of Disease Control, Thailand

📌 จุดจำก่อนสอบ:
• Botulism: หน่อไม้ปี๊บ / อาหารกระป๋อง -> Descending flaccid paralysis + 4Ds (Diplopia, Dysarthria, Dysphagia, Dysphonia)
• กลไก: บล็อกการหลั่ง Acetylcholine ที่ปลายประสาท
• Antidote: Equine Botulinum Antitoxin (ต้องให้โดยเร็วที่สุดก่อนสารพิษเข้าเซลล์ประสาท)"""
    },
    # 40. Lead Chelation in Children (Succimer / DMSA)
    {
        "q": "เด็กชายอายุ 3 ขวบ อาศัยอยู่ในบ้านเก่าที่มีการทาสีลอกร่อน ผลการตรวจคัดกรอง Blood Lead Level (BLL) ได้เท่ากับ 35 mcg/dL เด็กไม่มีอาการแสดงของ Lead encephalopathy (ไม่มีอาการชัก ซึม หรืออาเจียนพุ่ง) ข้อใดเป็นแนวทางการรักษาด้วยยาขับโลหะหนัก (Chelation therapy) ที่แนะนำสำหรับเด็กรายนี้ตามแนวทางของ CDC และ AAP",
        "c1": "ให้ยาขับโลหะหนักชนิดรับประทาน Succimer (Dimercaptosuccinic acid: DMSA) ร่วมกับการขจัดแหล่งปนเปื้อนสารตะกั่วในบ้าน",
        "c2": "ให้ Dimercaprol (BAL) ฉีดเข้ากล้ามเนื้อลึกทันที",
        "c3": "ให้ Calcium disodium EDTA ทางหลอดเลือดดำทันที",
        "c4": "ไม่จำเป็นต้องรักษาด้วยยาใดๆ ให้ดื่มนมสดวันละ 1 ลิตร",
        "c5": "ให้ Penicillamine ชนิดฉีดเข้าหลอดเลือดดำ",
        "ans": 1,
        "subtopic": "Pediatric Heavy Metal Chelation",
        "cat": "Clinic",
        "note": "Succimer (DMSA) for pediatric lead poisoning",
        "exp": """✅ คำตอบที่ถูกต้อง: ข้อ ก. ให้ยาขับโลหะหนักชนิดรับประทาน Succimer (Dimercaptosuccinic acid: DMSA) ร่วมกับการขจัดแหล่งปนเปื้อนสารตะกั่วในบ้าน

💡 Background:
สารตะกั่ว (Lead) มีผลทำลายระบบประสาทและพัฒนาการทางสมองของเด็กอย่างถาวร (ทำให้ IQ ลดลง, สมาธิสั้น, พฤติกรรมก้าวร้าว) แหล่งที่พบบ่อยคือ สีทาบ้านที่มีสารตะกั่ว (Lead-based paint) ในบ้านเก่าที่หลุดลอกเป็นฝุ่นผง

🎯 ทำไมข้อนี้ถึงถูก:
เกณฑ์การให้ Chelation therapy ในเด็กตามแนวทาง CDC / AAP:
1) Blood Lead Level (BLL) 45 mcg/dL ขึ้นไป (หรือ BLL 20-44 mcg/dL ที่มีอาการหรือระดับตะกั่วค้างสูงต่อเนื่อง): มีข้อบ่งชี้ในการเริ่มให้ Chelation therapy
2) Succimer (DMSA: Dimercaptosuccinic acid) เป็น Water-soluble analog ของ Dimercaprol ที่สามารถรับประทานได้ (Oral form) ได้รับการรับรองจาก US-FDA สำหรับรักษาภาวะพิษจากตะกั่วในเด็กที่มี BLL > 45 mcg/dL (และมักใช้ในราย 20-44 mcg/dL ที่แพทย์พิจารณา) โดยมีผลข้างเคียงต่ำกว่า BAL และไม่จำเป็นต้องนอนโรงพยาบาลฉีดยา
3) การรักษาต้องทำควบคู่กับการค้นหาและกำจัดแหล่งสัมผัสสารตะกั่วในสภาพแวดล้อมของผู้ป่วยเสมอ

🔍 ข้ออื่นผิดเพราะอะไร:
• ข้อ ข. และ ค. การฉีด BAL ร่วมกับ CaNa2-EDTA สงวนไว้สำหรับ Severe lead poisoning (BLL >= 70 mcg/dL) หรือผู้ป่วยที่มีอาการของ Lead encephalopathy เท่านั้น ไม่ใช้เป็นตัวเลือกแรกในเด็กที่ไม่มีอาการ
• ข้อ ง. การไม่รักษาและปล่อยให้เด็กสัมผัสตะกั่วจะส่งผลเสียต่อสมองอย่างถาวร
• ข้อ จ. Penicillamine ปัจจุบันเป็นเพียงยาทางเลือกรองเนื่องจากมีผลข้างเคียงต่อไตและการแพ้ยาสูง

📖 Guideline อ้างอิง:
CDC Recommendations for the Management of Childhood Lead Exposure and Prevention, and AAP Guidelines

📌 จุดจำก่อนสอบ:
• Pediatric Lead Poisoning: ยาทางเลือกแรกคือ Oral Succimer (DMSA)
• Severe Lead Encephalopathy (BLL >= 70 mcg/dL): ใช้ BAL IM ตามด้วย CaNa2-EDTA IV
• กุญแจสำคัญที่สุด: ต้องกำจัดแหล่งปนเปื้อน (Environmental remediation) เสมอ มิฉะนั้นกินยาขับไปเด็กก็ดูดซึมซ้ำ"""
    }
]

questions.extend(final_ten)

with open('pristine_toxicology_40.json', 'w', encoding='utf-8') as f:
    json.dump(questions, f, ensure_ascii=False, indent=2)

print(f"Generated {len(questions)} pristine toxicology questions successfully!")
