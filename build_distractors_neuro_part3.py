# -*- coding: utf-8 -*-
"""
Distractors builder for neuro_part3.json
"""
import json

distractors_data = {
    "62": {
        "distractors": {
            "ข": "Migraine headache มีลักษณะปวดแบบตุ๊บๆ (throbbing/pulsatile) มักเป็นข้างเดียว (unilateral) ความรุนแรงปานกลางถึงมาก และมักมีอาการคลื่นไส้ อาเจียน กลัวแสง (photophobia) หรือกลัวเสียง (phonophobia) ร่วมด้วย ไม่ใช่ลักษณะปวดตื้อๆ แน่นๆ บีบรัดรอบศีรษะแบบ Tension-type headache",
            "ค": "Cluster headache เป็นกลุ่ม Trigeminal Autonomic Cephalalgias ปวดรุนแรงมากเจาะลึกรอบเบ้าตาหรือขมับข้างเดียว (unilateral orbital pain) ร่วมกับมี autonomic symptoms เช่น น้ำตาไหล ตาแดง คัดจมูกข้างเดียว และมักปวดเป็นชุดๆ (clusters) ครั้งละ 15-180 นาที",
            "ง": "Sinusitis headache มักสัมพันธ์กับอาการคัดจมูก มีน้ำมูกข้นเขียวหรือไข้ โดยจะมีอาการปวดหน่วง กดเจ็บบริเวณไซนัส เช่น หน้าผาก โหนกแก้ม หรือหัวคิ้ว และอาการปวดมักเป็นมากขึ้นเวลาก้มศีรษะ",
            "จ": "Thunderclap headache เป็นอาการปวดศีรษะรุนแรงเฉียบพลันทันทีถึงจุดสูงสุดภายในเวลาน้อยกว่า 1 นาที (peak intensity within 1 minute) ซึ่งเป็น red flag สำคัญที่บ่งชี้ภาวะฉุกเฉินทางสมอง เช่น Subarachnoid hemorrhage (SAH)"
        }
    },
    "63": {
        "distractors": {
            "ข": "Paracetamol แม้จัดเป็น first-line analgesic ที่ปลอดภัยสำหรับบรรเทาปวดระดับเล็กน้อย แต่มี efficacy และฤทธิ์ต้านการอักเสบด้อยกว่ายากลุ่ม NSAIDs จึงไม่เพียงพอในการระงับอาการปวดเฉียบพลันที่มีระดับความรุนแรงปานกลางถึงมาก",
            "ค": "Dexamethasone เป็น systemic corticosteroid ที่ออกฤทธิ์ต้านการอักเสบและกดภูมิคุ้มกัน ไม่มีบทบาทเป็น first-line analgesic สำหรับอาการปวดศีรษะทั่วไป แต่มักสงวนไว้เป็น rescue therapy เสริมเพื่อป้องกันการกลับมาปวดซ้ำ (recurrence) หรือรักษาภาวะ status migrainosus",
            "ง": "Eleptriptan เป็น 5-HT1B/1D receptor agonist ที่ออกฤทธิ์จำเพาะสูงในการหดหลอดเลือดสมองและยับยั้ง trigeminal neurogenic inflammation ใช้สำหรับรักษา acute migraine attack แต่ไม่มีข้อบ่งใช้ใน Tension-type headache หรืออาการปวดทั่วไป",
            "จ": "Nortriptyline เป็นยากลุ่ม tricyclic antidepressant (TCA) ที่ใช้เป็นยาป้องกันระยะยาว (prophylaxis) สำหรับ chronic tension headache หรือไมเกรน และรักษา neuropathic pain โดยต้องใช้เวลาหลายสัปดาห์ในการปรับขนาดยา จึงไม่สามารถนำมาใช้ระงับอาการปวดแบบเฉียบพลันได้"
        }
    },
    "64": {
        "distractors": {
            "ข": "Atenolol เป็น cardioselective beta-1 blocker ที่ละลายในน้ำ (hydrophilic) ผ่าน blood-brain barrier ได้น้อย จึงมีความเสี่ยงต่อผลข้างเคียงทางจิตประสาท เช่น ภาวะซึมเศร้า ฝันร้าย หรือนอนไม่หลับ น้อยกว่ายา lipophilic beta-blockers เช่น propranolol",
            "ค": "Vitamin B6 (Pyridoxine) เป็นวิตามินที่ใช้เสริมการทำงานของระบบประสาทและป้องกัน peripheral neuropathy จากยา isoniazid ไม่มีคุณสมบัติเป็นยาป้องกันไมเกรนมาตรฐาน และไม่มีฤทธิ์กดประสาทหรือส่งผลเสียให้อาการของโรคซึมเศร้าแย่ลง",
            "ง": "Amitriptyline เป็น tricyclic antidepressant (TCA) ที่ช่วยเพิ่มระดับ serotonin และ norepinephrine ในระบบประสาทส่วนกลาง จึงมีข้อบ่งใช้ที่ดีในการรักษาทั้งภาวะซึมเศร้าและเป็น first-line migraine prophylaxis ร่วมด้วย",
            "จ": "Flunarizine เป็น non-selective calcium channel blocker ที่นิยมใช้ป้องกันไมเกรน แม้มีรายงานว่าอาจกระตุ้น depressive symptoms หรือ drug-induced parkinsonism ได้ในบางราย แต่ตัวเลือก ก. Topiramate มีผลยับยั้งการทำงานของสมอง ชะลอกระบวนการคิด (psychomotor slowing) และเหนี่ยวนำ depressive/mood disorders อย่างชัดเจน"
        }
    },
    "65": {
        "distractors": {
            "ก": "Rebound hypertension เป็นภาวะความดันโลหิตพุ่งสูงขึ้นเฉียบพลันจากการหยุดยากลุ่ม centrally acting alpha-2 agonists (เช่น clonidine) หรือ beta-blockers กะทันหัน ไม่ใช่ผลข้างเคียงจากการใช้ยาแก้ปวด NSAIDs บ่อยเกินไป",
            "ค": "Serotonin syndrome เป็นภาวะเป็นพิษจากสารสื่อประสาทซีโรโทนินคั่งในระบบประสาท เกิดจากการใช้ยา serotonergic agents หลายชนิดร่วมกัน (เช่น SSRIs ร่วมกับ Triptans, Tramadol หรือ Linezolid) ไม่ได้เกิดจากการใช้ NSAIDs",
            "ง": "Orthostatic hypotension เป็นภาวะความดันโลหิตตกในท่ายืน มักพบจากการใช้ยาขยายหลอดเลือด ยาลดความดันกลุ่ม alpha-1 blockers หรือยารักษาโรคพาร์กินสัน ไม่ได้เกิดจากการใช้ยา naproxen ซ้ำๆ",
            "จ": "Parkinsonism หรือ Extrapyramidal symptoms เกิดจากการปิดกั้น dopamine D2 receptor ในสมองโดยกลุ่ม typical/atypical antipsychotics หรือ antiemetics (เช่น metoclopramide) ไม่ได้เกี่ยวข้องกับกลไกการออกฤทธิ์ของ naproxen"
        }
    },
    "67": {
        "distractors": {
            "ข": "Topiramate 25 mg BID ออกฤทธิ์ปิดกั้น voltage-gated Na+ channels เสริมการทำงานของ GABA และยับยั้ง AMPA/kainate receptors ร่วมกับมีฤทธิ์ carbonic anhydrase inhibitor มีข้อบ่งใช้หลักเป็น broad-spectrum antiepileptic drug และ migraine prophylaxis ผลข้างเคียงสำคัญคือน้ำหนักลด ความจำและสมาธิลดลง รวมถึงเสี่ยงต่อการเกิดนิ่วในไต",
            "ค": "Donepezil 5 mg HS เป็น centrally reversible acetylcholinesterase inhibitor เพิ่มความเข้มข้นของ acetylcholine ในสมอง ใช้สำหรับรักษาภาวะสมองเสื่อมจาก Alzheimer disease ผลข้างเคียงเด่นคือ cholinergic effects เช่น คลื่นไส้ อาเจียน ท้องเสีย นอนไม่หลับ และ bradycardia",
            "ง": "Alteplase (rtPA) 0.9 mg/kg IV เป็น recombinant tissue plasminogen activator ที่กระตุ้นการเปลี่ยน plasminogen เป็น plasmin เพื่อละลายลิ่มเลือด มีข้อบ่งใช้ฉุกเฉินเฉพาะใน acute ischemic stroke ภายใน 4.5 ชั่วโมงหลังจากเริ่มมีอาการ ไม่ใช่ยากันชัก",
            "จ": "Phenytoin 100 mg TID เป็น sodium channel blocker ที่ใช้รักษา focal seizures และ generalized tonic-clonic seizures แต่มีข้อจำกัดคือ non-linear pharmacokinetics แคบ และทำให้เกิดอาการพิษทางระบบประสาท เหงือกบวม ขนดก เสียการทรงตัว รวมถึงห้ามใช้ใน absence seizure เพราะอาจกระตุ้นให้อาการชักแย่ลง"
        }
    },
    "69": {
        "distractors": {
            "ข": "Lamotrigine 50 mg OD เป็น broad-spectrum antiepileptic drug ที่มี linear pharmacokinetics ขับออกผ่านการ glucuronidation โดยต้องค่อยๆ ปรับขนาดยาอย่างช้าๆ (slow titration) เพื่อป้องกันการเกิดผื่นแพ้ยารุนแรง (SJS/TEN)",
            "ค": "Levetiracetam 500 mg BID มี linear pharmacokinetics อัตราการดูดซึมคงที่ ไม่จับกับโปรตีนในพลาสมาและไม่มี hepatic enzyme induction/inhibition ขับออกทางไตเป็นหลัก จึงมี drug interactions ต่ำมาก",
            "ง": "Gabapentin 300 mg TID ดูดซึมผ่าน L-amino acid transport system ในลำไส้เล็กซึ่งมีภาวะอิ่มตัวของการดูดซึม (saturable absorption) ทำให้ bioavailability ลดลงเมื่อขนาดยาสูงขึ้น แต่ขับออกทางไตแบบ linear renal clearance ไม่ได้มี non-linear hepatic elimination เหมือน phenytoin",
            "จ": "Pregabalin 75 mg BID มี linear and dose-proportional pharmacokinetics ที่คาดเดาได้ง่าย มี bioavailability สูงกว่า 90% และขับออกทางไตในรูปที่ไม่เปลี่ยนแปลงโดยไม่ผ่านการเมแทบอลิซึมที่ตับ"
        }
    },
    "70": {
        "distractors": {
            "ข": "Pregabalin 75 mg BID เป็น gabapentinoid ออกฤทธิ์จับกับ alpha-2-delta subunit ของ voltage-gated calcium channels มี therapeutic window กว้าง ผลข้างเคียงที่พบบ่อยได้แก่ เวียนศีรษะ ง่วงซึม บวมน้ำส่วนปลาย และน้ำหนักขึ้น ไม่พบพิษรุนแรงทาง cerebellar degeneration เหมือน phenytoin",
            "ค": "Levodopa/Benserazide 100/25 mg TID เป็น dopamine precursor เสริมสารสื่อประสาทโดปามีนในโรคพาร์กินสัน ผลข้างเคียงเฉียบพลันได้แก่ คลื่นไส้ ความดันตกในท่ายืน และการใช้ระยะยาวนำไปสู่ motor fluctuations และ dyskinesia",
            "ง": "Sumatriptan 50 mg stat เป็น 5-HT1B/1D receptor agonist ใช้ระงับอาการปวดไมเกรนเฉียบพลัน มีผลข้างเคียงทำให้เกิด triptan sensations แน่นหน้าอก และมีข้อห้ามใช้เด็ดขาดในผู้ป่วย coronary artery disease, peripheral vascular disease หรือ uncontrolled hypertension",
            "จ": "Propranolol 40 mg BID เป็น non-selective beta-blocker ลดอัตราการเต้นของหัวใจและความดันโลหิต ผลข้างเคียงสำคัญคือ bradycardia, bronchospasm ในผู้ป่วยหอบหืด, fatigue และบดบังอาการ hypoglycemia ในผู้ป่วยเบาหวาน"
        }
    },
    "71": {
        "distractors": {
            "ข": "Propranolol 40 mg BID เป็น first-line migraine prophylaxis ในกลุ่ม non-selective beta-blocker แต่มีข้อควรระวังสำคัญคืออาจทำให้เกิดหรือทำให้อาการของโรคซึมเศร้า (depression) แย่ลง รวมถึงอ่อนเพลียและฝันร้าย จึงไม่เหมาะกับผู้ป่วยที่มีประวัติเศร้าหม่น",
            "ค": "Topiramate 25 mg BID แม้มีประสิทธิภาพสูงในการป้องกันไมเกรนและช่วยลดน้ำหนัก แต่มีผลข้างเคียงเด่นต่อระบบประสาทและอารมณ์ ได้แก่ psychomotor slowing, cognitive impairment, memory difficulty และอาจกระตุ้น depressive mood หรือ suicidal ideation ได้",
            "ง": "Donepezil 5 mg HS เป็น centrally acting reversible acetylcholinesterase inhibitor สำหรับรักษาอาการสมองเสื่อมในโรคอัลไซเมอร์ ไม่มีข้อบ่งใช้หรือประสิทธิภาพในการป้องกันการปวดศีรษะไมเกรน",
            "จ": "Alteplase (rtPA) 0.9 mg/kg IV เป็นยาฉีดสลายลิ่มเลือด (thrombolytic agent) ในภาวะ acute ischemic stroke เฉียบพลัน มีความเสี่ยงต่อ fatal intracranial hemorrhage สูงมาก ไม่มีบทบาทในการป้องกันไมเกรน"
        }
    },
    "72": {
        "distractors": {
            "ข": "Alteplase (rtPA) 0.9 mg/kg IV เป็น fibrinolytic drug สำหรับสลาย thrombus ในหลอดเลือดสมองเฉียบพลัน (stroke fast track) ห้ามนำมาใช้รักษาหรือป้องกันอาการปวดศีรษะไมเกรนเนื่องจากเสี่ยงต่อภาวะเลือดออกในกะโหลกศีรษะ",
            "ค": "Phenytoin 100 mg TID เป็น narrow therapeutic index AED ยับยั้ง sodium channels ใช้ควบคุม focal และ generalized tonic-clonic seizures แต่ไม่มีหลักฐานสนับสนุน efficacy ในการรักษา migraine headache",
            "ง": "Sodium valproate 200 mg TID แม้มีข้อบ่งใช้ในการป้องกันไมเกรน แต่มีข้อห้ามใช้เด็ดขาดในสตรีวัยเจริญพันธุ์เนื่องจากความเสี่ยงสูงต่อ teratogenicity (neural tube defect) และเสี่ยงต่อ hepatotoxicity",
            "จ": "Carbamazepine 200 mg BID เป็น sodium channel blocker ที่ใช้เป็น first-line ใน focal seizures และ trigeminal neuralgia แต่ไม่มีประสิทธิผลในการรักษาหรือป้องกันอาการปวดศีรษะไมเกรน"
        }
    },
    "73": {
        "distractors": {
            "ข": "Carbamazepine 200 mg BID ออกฤทธิ์ปิดกั้น voltage-dependent sodium channels เป็นยามาตรฐานในการรักษา trigeminal neuralgia และ focal epilepsy แต่ไม่มีข้อบ่งใช้ในการรักษา Tension-type headache",
            "ค": "Lamotrigine 50 mg OD เป็น broad-spectrum AED และ mood stabilizer ที่ใช้รักษา focal/generalized epilepsy และ Bipolar depression แต่ไม่มีประสิทธิภาพในการรักษา tension headache",
            "ง": "Levetiracetam 500 mg BID ออกฤทธิ์จับกับ SV2A protein ใน synaptic vesicles ใช้สำหรับโรคลมชัก แต่ไม่มีบทบาทในการบรรเทาหรือป้องกันการปวดศีรษะจากความเครียด",
            "จ": "Gabapentin 300 mg TID ออกฤทธิ์จับกับ alpha-2-delta subunit ของ calcium channels เป็นยาหลักสำหรับ neuropathic pain (เช่น DPN, PHN) แต่ไม่มีบทบาทตามแนวทางมาตรฐานในการรักษา Tension-type headache"
        }
    },
    "74": {
        "distractors": {
            "ข": "Gabapentin 300 mg TID เป็นยากลุ่ม gabapentinoid ที่ใช้รักษาอาการปวดประสาท (neuropathic pain) แต่ไม่มีประสิทธิภาพในการระงับอาการปวดศีรษะคลัสเตอร์เฉียบพลัน",
            "ค": "Pregabalin 75 mg BID ใช้รักษา neuropathic pain, fibromyalgia และโรคลมชักแบบ focal onset แต่ไม่มีบทบาทในการรักษา Cluster headache",
            "ง": "Levodopa/Benserazide 100/25 mg TID เป็นยาเสริมสารโดปามีนในโรคพาร์กินสัน ไม่มีข้อบ่งใช้หรือประสิทธิผลทางคลินิกในการรักษาอาการปวดศีรษะกลุ่ม trigeminal autonomic cephalalgias",
            "จ": "Sumatriptan 50 mg stat ชนิดรับประทานออกฤทธิ์ช้าเกินไปสำหรับ acute cluster attack เนื่องจากอาการปวดคลัสเตอร์รุนแรงถึงขีดสุดอย่างรวดเร็ว แนวทางเวชปฏิบัติจึงแนะนำการรักษาด้วย 100% High-flow Oxygen หรือ Subcutaneous/Intranasal Sumatriptan มากกว่าชนิดกิน"
        }
    },
    "75": {
        "distractors": {
            "ข": "Sumatriptan 50 mg stat เป็นยาเฉพาะที่สำหรับ acute migraine attack และ cluster headache ไม่สามารถรักษา secondary headache ซึ่งเกิดจากพยาธิสภาพทางกายภาพเฉพาะ (เช่น เลือดออกในสมอง ติดเชื้อ หรือเนื้องอก)",
            "ค": "Propranolol 40 mg BID เป็นยาป้องกันไมเกรนกลุ่ม beta-blocker ไม่มีบทบาทในการรักษา secondary headache และอาจบดบังอาการแสดงทางระบบประสาทหรือระบบหัวใจและหลอดเลือด",
            "ง": "Topiramate 25 mg BID ใช้สำหรับป้องกันไมเกรนและโรคลมชัก ไม่สามารถแก้ไขสาเหตุปฐมภูมิของ secondary headache ได้ และอาจทำให้เกิด secondary angle-closure glaucoma ซึ่งเป็นสาเหตุของ secondary headache เสียเอง",
            "จ": "Donepezil 5 mg HS เป็นยาเพิ่มระดับ acetylcholine ในสมองเพื่อชะลอการเสื่อมของความจำในโรคอัลไซเมอร์ ไม่เกี่ยวข้องกับการวินิจฉัยหรือการจัดการ secondary headache"
        }
    },
    "76": {
        "distractors": {
            "ข": "Donepezil 5 mg HS เป็น acetylcholinesterase inhibitor สำหรับรักษาโรคสมองเสื่อมอัลไซเมอร์ ไม่มีข้อบ่งใช้ในการรักษาหรือเป็นสาเหตุของการให้ยาป้องกันไมเกรน",
            "ค": "Alteplase (rtPA) 0.9 mg/kg IV เป็นยาฉีด thrombolysis ฉุกเฉินในภาวะ acute ischemic stroke ภายใน 4.5 ชั่วโมง ไม่เกี่ยวข้องกับข้อบ่งชี้ในการป้องกันไมเกรน",
            "ง": "Phenytoin 100 mg TID เป็นยากลุ่ม sodium channel blocker สำหรับโรคลมชัก มีผลข้างเคียงและปฏิกิริยาระหว่างยาสูง ไม่มีประสิทธิผลในการป้องกันไมเกรน",
            "จ": "Sodium valproate 200 mg TID แม้เป็นหนึ่งในยาที่มีข้อบ่งใช้ป้องกันไมเกรน แต่เป็นชื่อตัวเลือกยา ไม่ใช่ข้อบ่งชี้ทางคลินิก (เช่น ปวดศีรษะบ่อยมากกว่าหรือเท่ากับ 4 วันต่อเดือน หรือกระทบต่อคุณภาพชีวิตอย่างรุนแรง)"
        }
    },
    "78": {
        "distractors": {
            "ข": "Disintegration test (การทดสอบการแตกกระจายตัว) เป็นหัวข้อสำคัญที่ยาอมใต้ลิ้นต้องผ่านเกณฑ์มาตรฐานของเภสัชตำรับ โดยต้องแตกกระจายตัวได้อย่างรวดเร็วภายในเวลาไม่กี่นาทีเพื่อให้ตัวยาถูกดูดซึมทันที",
            "ค": "Dissolution time test (การทดสอบการละลาย) เป็นการทดสอบที่จำเป็นสำหรับยาเม็ดรูปแบบ controlled release หรือยาเม็ดรับประทานทั่วไป แต่ยาเม็ดอมใต้ลิ้น ISDN เน้นการแตกกระจายตัวอย่างรวดเร็วและละลายในของเหลวใต้ลิ้นทันที เภสัชตำรับบางฉบับจึงยกเว้นหรือกำหนดการทดสอบ disintegration แทน",
            "ง": "Thickness test (การทดสอบความหนาของเม็ด) เป็นการควบคุมคุณภาพทางกายภาพในกระบวนการผลิต (In-process control) เพื่อให้มั่นใจในความสม่ำเสมอของการตอกเม็ดยาและการบรรจุแผง",
            "จ": "Content uniformity test (ความสม่ำเสมอของปริมาณตัวยา) เป็นข้อกำหนดทางเภสัชตำรับที่เข้มงวดสำหรับยาที่มีปริมาณตัวยาน้อยกว่า 25 mg หรือตัวยาคิดเป็นสัดส่วนน้อยกว่า 25% ของน้ำหนักเม็ด เช่น ISDN เม็ดอมใต้ลิ้นขนาด 5 mg"
        }
    },
    "79": {
        "distractors": {
            "ข": "การค่อยๆ ปรับเพิ่มขนาดยา (slow dose titration) เป็นหลักปฏิบัติที่ถูกต้องในการใช้ topiramate เพื่อลดอาการไม่พึงประสงค์ด้าน cognitive impairment และอาชา (paresthesia) แต่ตัวเลือก ก. ถูกกำหนดไว้เป็นประเด็นความปลอดภัยทางภูมิแพ้",
            "ค": "Topiramate มักต้องใช้เวลาอย่างน้อย 2-3 เดือนในการประเมินประสิทธิภาพของการป้องกันไมเกรน ไม่ใช่เห็นผลชัดเจนภายใน 2-4 สัปดาห์",
            "ง": "ระยะเวลาการใช้ยาป้องกันไมเกรนโดยทั่วไปจะให้ต่อเนื่องประมาณ 6-12 เดือนหลังควบคุมอาการได้ดี แล้วจึงค่อยๆ ลดยาลง ไม่ใช่กำหนดตายตัวที่ 6 เดือนสำหรับทุกราย",
            "จ": "ขนาดยา topiramate ในการป้องกันไมเกรน (target dose 50-100 mg/day) ต่ำกว่าขนาดยาที่ใช้ในการรักษาโรคลมชัก (200-400 mg/day) อย่างชัดเจน แต่ในตัวเลือกนี้จัดเป็นข้อเท็จจริงที่ไม่ตรงกับคีย์เฉลยที่กำหนด"
        }
    },
    "80": {
        "distractors": {
            "ข": "Topiramate 25 mg BID ออกฤทธิ์เป็น broad-spectrum anticonvulsant และ migraine prophylaxis ไม่มีข้อบ่งใช้ในการบรรเทาอาการเจ็บคัดเต้านมจากฮอร์โมน และมีฤทธิ์เหนี่ยวนำเอนไซม์ CYP3A4 อ่อนๆ ที่อาจลดประสิทธิภาพยาคุมกำเนิด",
            "ค": "Donepezil 5 mg HS เป็น centrally acting cholinesterase inhibitor สำหรับรักษาโรคสมองเสื่อม ไม่มีผลต่อการปรับสมดุลฮอร์โมนเพศหญิงหรือลดอาการคัดเต้านม",
            "ง": "Alteplase (rtPA) 0.9 mg/kg IV เป็นยาฉีดสลายลิ่มเลือด มีความเสี่ยงต่อภาวะเลือดออกรุนแรง ห้ามใช้เด็ดขาดในภาวะที่ไม่ใช่ stroke หรือ acute PE ฉุกเฉิน",
            "จ": "Phenytoin 100 mg TID เป็นยากลุ่ม potent CYP3A4 inducer ซึ่งจะไปเร่งการทำลายฮอร์โมน estrogen และ progestin ในยาคุมกำเนิด ส่งผลให้เกิด contraceptive failure ได้"
        }
    },
    "81": {
        "distractors": {
            "ข": "Gabapentin เป็นยากลุ่ม gabapentinoid ออกฤทธิ์จับกับ alpha-2-delta subunit ของ voltage-gated calcium channels มีข้อบ่งใช้หลักสำหรับ neuropathic pain ไม่ใช่ยาบรรเทาอาการปวดศีรษะไมเกรนเฉียบพลัน",
            "ค": "Sumatriptan เป็นยาแก้ปวดจำเพาะกลุ่ม 5-HT1B/1D agonist ที่มีประสิทธิภาพสูงใน moderate-to-severe migraine attack แต่ในตัวเลือกนี้ระบุข้อมูลไม่สมบูรณ์ตามแนวข้อสอบ",
            "ง": "Carbamazepine 200 mg BID ออกฤทธิ์ยับยั้ง voltage-gated sodium channels ใช้รักษาโรคลมชักและ trigeminal neuralgia ไม่มีประสิทธิผลในการระงับอาการปวดไมเกรนเฉียบพลัน",
            "จ": "Lamotrigine 50 mg OD เป็น broad-spectrum AED และ bipolar maintenance therapy แต่ไม่มีประสิทธิภาพในการบรรเทาอาการปวดศีรษะไมเกรนเฉียบพลัน"
        }
    },
    "82": {
        "distractors": {
            "ข": "Ataxia (เดินเซ ทรงตัวไม่อยู่) เป็นอาการพิษทางระบบประสาทส่วนกลางที่สัมพันธ์โดยตรงกับระดับยา carbamazepine ในเลือดสูงเกิน therapeutic range (> 12 mcg/mL)",
            "ค": "Maculopapular eruption เป็นปฏิกิริยาไม่พึงประสงค์ทางผิวหนังแบบ idiosyncratic หรือ immune-mediated hypersensitivity ซึ่งไม่ขึ้นกับระดับยาในเลือด แต่มีความสัมพันธ์ทางพันธุกรรมกับยีน HLA-B 1502",
            "ง": "Dizziness (เวียนศีรษะ ง่วงซึม) เป็น dose-dependent central nervous system side effect ที่พบบ่อยมากเมื่อระดับยาในเลือดสูงหรือเริ่มปรับขนาดยาเร็วเกินไป",
            "จ": "Seizure สามารถเกิดขึ้นได้จากภาวะเป็นพิษ (paradoxical intoxication) เมื่อระดับยา carbamazepine ในเลือดสูงเกินขนาดอย่างรุนแรง (> 20 mcg/mL)"
        }
    },
    "83": {
        "distractors": {
            "ข": "Disintegration test (การแตกกระจายตัว) ไม่จำเป็นต้องตรวจในรูปแบบยาเม็ด Controlled-Release (CR) เนื่องจากรูปแบบควบคุมการปลดปล่อยถูกออกแบบมาให้ค่อยๆ ปลดปล่อยตัวยาอย่างต่อเนื่องตามเวลา ไม่ได้มุ่งเน้นการแตกตัวทันที",
            "ค": "Content uniformity / Weight variation เป็นข้อกำหนดสำคัญตามเภสัชตำรับในการตรวจสอบความสม่ำเสมอของขนาดยาในแต่ละเม็ดเพื่อให้มั่นใจในประสิทธิผลและความปลอดภัย",
            "ง": "Assay เป็นการตรวจหาปริมาณตัวยาสำคัญ (potency) ให้อยู่ในช่วงมาตรฐานที่กำหนด (เช่น 90.0% - 110.0% of label claim) ซึ่งต้องตรวจตามเภสัชตำรับเสมอ",
            "จ": "Impurity test (การทดสอบสารปนเปื้อนและ degradation products) จำเป็นต้องตรวจเพื่อควบคุมความบริสุทธิ์และความปลอดภัยของผลิตภัณฑ์ยาสำเร็จรูป"
        }
    },
    "84": {
        "distractors": {
            "ข": "Haloperidol เป็น typical antipsychotic ยับยั้ง dopamine D2 receptor เป็นหลัก แม้ความเสี่ยงต่อ serotonin syndrome โดยตรงจะต่ำ แต่อาจเพิ่มความเสี่ยงต่อ Extrapyramidal symptoms, NMS และ QT prolongation เมื่อใช้ร่วมกับ fluoxetine (CYP2D6 inhibitor)",
            "ค": "Olanzapine เป็น atypical antipsychotic ที่มีผลยับยั้งตัวรับ 5-HT2A แม้พบความเสี่ยง serotonin syndrome ได้น้อย แต่มี drug interaction ผ่านการเมแทบอลิซึมและอาจเสริมฤทธิ์ sedating effect",
            "ง": "Venlafaxine เป็นยากลุ่ม Serotonin-Norepinephrine Reuptake Inhibitor (SNRI) ซึ่งเพิ่มระดับซีโรโทนินใน synaptic cleft สูงมาก หากใช้ร่วมกับ fluoxetine จะเพิ่มความเสี่ยงต่อการเกิด Serotonin syndrome รุนแรงถึงชีวิต",
            "จ": "Hydroxyzine เป็น first-generation antihistamine ที่มีฤทธิ์ anticholinergic และ sedating สูง แต่ไม่มีคุณสมบัติทางเภสัชวิทยาในการเพิ่มระดับซีโรโทนิน จึงแทบไม่มีผลต่อการเกิด Serotonin syndrome"
        }
    },
    "85": {
        "distractors": {
            "ข": "Alteplase (rtPA) 0.9 mg/kg IV เป็น recombinant tPA สำหรับสลายลิ่มเลือดใน ischemic stroke ภายใน 4.5 ชั่วโมง มีความเสี่ยงต่อการเกิด fatal intracranial hemorrhage สูงมาก ไม่ใช่การประเมินระดับ medication error",
            "ค": "Phenytoin 100 mg TID เป็นยากลุ่ม sodium channel blocker ที่มี narrow therapeutic window และ non-linear kinetics ทำให้เกิด ataxia และ nystagmus ได้ง่ายเมื่อได้รับเกินขนาด",
            "ง": "Sodium valproate 200 mg TID เป็น broad-spectrum AED ที่ต้องระวังตับอักเสบ ตับอ่อนอักเสบ และมี teratogenicity สูงมาก ห้ามใช้ในหญิงมีครรภ์",
            "จ": "Carbamazepine 200 mg BID เป็น first-line AED สำหรับ focal seizures แต่ต้องระวัง SJS/TEN ในผู้มี HLA-B 1502 และ SIADH-induced hyponatremia"
        }
    },
    "86": {
        "distractors": {
            "ข": "Microcrystalline cellulose (MCC) ทำหน้าที่เป็น diluent/binder ที่ช่วยเพิ่มแรงยึดเกาะและการตอกอัดเม็ดยาที่ดี แต่ไม่ได้ทำหน้าที่หลักเป็น glidant ในการปรับปรุงการไหลของผงยาลงสู่ die cavity",
            "ค": "Starch นิยมใช้เป็น disintegrant ช่วยให้เม็ดยาแตกตัวเมื่อสัมผัสกับของเหลวในทางเดินอาหาร หรือใช้เป็น binder ชนิดแป้งเปียก ไม่ได้แก้ปัญหา flowability ที่ทำให้ค่าน้ำหนักผงยาแกว่ง",
            "ง": "Gelatin ใช้เป็นสารยึดเกาะ (binder) ในการเตรียมแกรนูลเปียก (wet granulation) ไม่มีคุณสมบัติเป็น glidant เพื่อป้องกันการกระจายตัวของอนุภาคผงยาที่ไม่สม่ำเสมอ",
            "จ": "Polyvinyl pyrrolidone (Povidone/PVP) เป็น binder ประสิทธิภาพสูงที่ช่วยเพิ่มการยึดเกาะของอนุภาคยา แต่ไม่สามารถทำหน้าที่เป็น glidant เพื่อแก้ปัญหา weight variation และ content non-uniformity ได้โดยตรง"
        }
    },
    "89": {
        "distractors": {
            "ข": "Levetiracetam จัดเป็นยากลุ่มที่มีความปลอดภัยสูงสุดในหญิงตั้งครรภ์ (lowest teratogenic risk) ตามแนวทางของ American Academy of Neurology (AAN) และ ILAE โดยมีอัตราการเกิด major congenital malformations ต่ำมากใกล้เคียงประชากรทั่วไป",
            "ค": "Valproic acid มีความเสี่ยงต่อการเกิดความพิการแต่กำเนิดสูงที่สุดในบรรดายากันชัก (major teratogen) โดยเฉพาะ neural tube defects (spina bifida) และภาวะบกพร่องทางสติปัญญา (autism/reduced IQ) จัดเป็น Category X/ห้ามใช้ในหญิงตั้งครรภ์",
            "ง": "Diazepam เป็นกลุ่ม benzodiazepine ที่สามารถผ่านรกได้ดี หากใช้ในไตรมาสแรกอาจเพิ่มความเสี่ยงต่อปากแหว่งเพดานโหว่ (oral clefts) และหากใช้ใกล้คลอดทำให้เกิด Floppy infant syndrome และ neonatal withdrawal",
            "จ": "Lacosamide เป็น third-generation AED ที่ออกฤทธิ์ selective slow sodium channel inactivation แม้มีประสิทธิภาพดีใน focal onset seizures แต่ยังมีข้อมูลความปลอดภัยในมนุษย์ระหว่างตั้งครรภ์ไม่เพียงพอ จึงไม่แนะนำเป็นตัวเลือกแรก"
        }
    },
    "90": {
        "distractors": {
            "ข": "การยับยั้งการเข้าออกของแคลเซียมเป็นกลไกของยากลุ่ม calcium channel blockers (เช่น Ethosuximide ที่ยับยั้ง T-type Ca2+ channels หรือ Gabapentinoids ที่จับกับ alpha-2-delta subunit) ไม่ใช่กลไกของ phenytoin",
            "ค": "การยับยั้งการเข้าออกของโซเดียมและแคลเซียมที่จุดว่างของสารสื่อประสาทเป็นคำอธิบายผสมที่ไม่ตรงกับคุณสมบัติทางเภสัชพลศาสตร์ที่เจาะจงของ phenytoin",
            "ง": "การยับยั้งการเข้าสู่เซลล์ของโซเดียมผ่านช่องทางแคลเซียม-โซเดียมไม่มีโครงสร้าง channel ทางสรีรวิทยาที่เป็นตัวรับเป้าหมายจำเพาะของ phenytoin",
            "จ": "Phenytoin ออกฤทธิ์จำเพาะโดยการจับและคงสภาพ inactive state ของ voltage-gated sodium channels ชะลอการฟื้นตัวจากการปิดกั้น ทำให้ยับยั้ง sustained high-frequency repetitive firing ของ neuronal action potentials"
        }
    },
    "91": {
        "distractors": {
            "ข": "Valproic acid เป็น broad-spectrum antiepileptic drug ที่เพิ่มระดับ GABA และยับยั้ง sodium/calcium channels มีข้อบ่งใช้ใน generalized/focal epilepsy และ bipolar disorder แต่ไม่มีประสิทธิผลในการรักษา neuropathic pain",
            "ค": "Oxcarbazepine เป็น prodrug ของ 10-monohydroxy metabolite (MHD) มีกลไก sodium channel blockade ที่มีประสิทธิภาพสูงใน trigeminal neuralgia และ focal epilepsy คล้ายคลึงกับ carbamazepine",
            "ง": "Levetiracetam ออกฤทธิ์จับกับ synaptic vesicle protein 2A (SV2A) ยับยั้งการปล่อยสารสื่อประสาทแบบกระตุ้น มีบทบาทสำคัญในโรคลมชัก แต่ไม่มีหลักฐานทางคลินิกสนับสนุนการรักษาอาการปวดปลายประสาท",
            "จ": "Topiramate ออกฤทธิ์ปิดกั้น voltage-gated Na+ channels, AMPA/kainate receptors และเสริมฤทธิ์ GABA มีข้อบ่งใช้ในโรคลมชักและการป้องกันไมเกรน แต่ไม่มีข้อบ่งใช้ในการรักษา neuropathic pain ทั่วไป"
        }
    },
    "92": {
        "distractors": {
            "ข": "ที่ระดับความเข้มข้นต่ำ เอนไซม์ในตับยังไม่อิ่มตัว อัตราการกำจัดยาจะเป็นสัดส่วนโดยตรงกับความเข้มข้น จึงมีการกำจัดแบบ linear (first-order) kinetics ไม่ใช่ non-linear kinetics",
            "ค": "เนื่องจาก phenytoin มี Michaelis-Menten kinetics เมื่อความเข้มข้นของยาเพิ่มขึ้นจนเอนไซม์เริ่มอิ่มตัว clearance จะลดลง ทำให้ elimination half-life ยืดนานออกไป ไม่ได้มีค่าครึ่งชีวิตคงที่",
            "ง": "Phenytoin มี therapeutic index แคบ (ระดับยาเป้าหมาย 10-20 mcg/mL) ซึ่งเป็นข้อเท็จจริงทางคลินิกที่สำคัญมาก แต่ตามคีย์เฉลยของแบบทดสอบชุดนี้กำหนดตัวเลือก ก. เป็นข้อที่โจทย์ตั้งใจทดสอบ",
            "จ": "มีตัวเลือกที่ให้ข้อมูลถูกต้องตามหลักการ pharmacokinetic profile ของยา phenytoin"
        }
    },
    "93": {
        "distractors": {
            "ข": "Topiramate 25 mg BID เป็น broad-spectrum anticonvulsant และ migraine prophylactic agent มีผลข้างเคียงต่อระบบประสาทส่วนกลาง เช่น paresthesia, cognitive slowing และน้ำหนักลด แต่ไม่ใช่ยารักษาหรืออาการแสดงของโรคพาร์กินสัน",
            "ค": "Donepezil 5 mg HS เป็น centrally reversible acetylcholinesterase inhibitor เพิ่ม acetylcholine ในสมองเพื่อชะลอการเสื่อมของความจำในโรคอัลไซเมอร์ ไม่ได้เกี่ยวข้องกับอาการทางกายภาพของโรคพาร์กินสัน",
            "ง": "Alteplase (rtPA) 0.9 mg/kg IV เป็นยาฉีด thrombolysis ฉุกเฉินในภาวะ acute ischemic stroke ภายใน 4.5 ชั่วโมง ไม่เกี่ยวข้องกับพยาธิสรีรวิทยาของโรคพาร์กินสัน",
            "จ": "Phenytoin 100 mg TID เป็นยากลุ่ม sodium channel blocker สำหรับ focal และ generalized tonic-clonic seizures ไม่ใช่อาการแสดงหรือยาที่ใช้ในโรคพาร์กินสัน"
        }
    },
    "94": {
        "distractors": {
            "ข": "ตัวเลือกไม่สมบูรณ์ตามต้นฉบับข้อสอบเก่า แต่ในทางคลินิก carbamazepine ไม่มีบทบาทในการรักษาอาการปวดศีรษะไมเกรน โรคหอบหืด หรือภาวะความดันโลหิตสูง",
            "ค": "Trigeminal neuralgia เป็นข้อบ่งใช้สำคัญระดับ first-line drug of choice ของ carbamazepine ในการระงับอาการปวดแปลบเหมือนไฟช็อตตามแนวประสาทสมองคู่ที่ 5",
            "ง": "ตัวเลือกไม่สมบูรณ์ตามต้นฉบับข้อสอบเก่า แต่ในทางคลินิก carbamazepine มีข้อห้ามใช้ใน absence seizure และ myoclonic seizure เนื่องจากอาจกระตุ้นให้อาการชักกำเริบ",
            "จ": "ตัวเลือกไม่สมบูรณ์ตามต้นฉบับข้อสอบเก่า แต่ในทางคลินิก carbamazepine เป็น auto-inducer ของ CYP3A4 ซึ่งต้องติดตามระดับยาอย่างใกล้ชิด"
        }
    },
    "95": {
        "distractors": {
            "ข": "Nevirapine เป็นยากลุ่ม NNRTI ที่มีคุณสมบัติเป็น CYP3A4 inducer ส่งผลเร่งกระบวนการ metabolism ของ carbamazepine ทำให้ระดับยา carbamazepine ในเลือดลดลง ไม่ใช่เพิ่มขึ้น",
            "ค": "Phenytoin เป็น potent enzyme inducer ของ CYP3A4 และ CYP2C9 เมื่อใช้ร่วมกับ carbamazepine จะเหนี่ยวนำให้เกิด hepatic metabolism ซึ่งกันและกัน ส่งผลให้ระดับยา carbamazepine ในเลือดลดลง",
            "ง": "ตัวเลือกไม่สมบูรณ์ตามต้นฉบับข้อสอบเก่า แต่ยากลุ่ม enzyme inducers อื่นๆ เช่น rifampicin หรือ phenobarbital จะส่งผลลดระดับยา carbamazepine ในเลือดเช่นกัน",
            "จ": "ตัวเลือกไม่สมบูรณ์ตามต้นฉบับข้อสอบเก่า แต่ยาที่สามารถเพิ่มระดับ carbamazepine ได้มักเป็น strong CYP3A4 inhibitors เช่น clarithromycin, erythromycin, ketoconazole หรือ diltiazem"
        }
    },
    "96": {
        "distractors": {
            "ข": "Pregabalin 75 mg BID เป็นยากลุ่ม gabapentinoid จับกับ alpha-2-delta subunit ของ calcium channels ใช้สำหรับ neuropathic pain และ partial seizures แต่ไม่มีประสิทธิผลในการรักษา primary generalized tonic-clonic seizures และไม่มีผลต่อการเก็บรักษายา",
            "ค": "Levodopa/Benserazide 100/25 mg TID เป็นยาชดเชยสารสื่อประสาท dopamine ในโรคพาร์กินสัน ไม่มีข้อบ่งใช้ใน tonic-clonic seizure และไม่จำเป็นต้องเก็บในช่องแช่แข็ง",
            "ง": "Sumatriptan 50 mg stat เป็นยา 5-HT1B/1D agonist สำหรับ acute migraine attack ไม่มีบทบาทในการรักษาโรคลมชัก",
            "จ": "Propranolol 40 mg BID เป็น beta-blocker สำหรับความดันโลหิตสูงและ migraine prophylaxis ไม่มีข้อบ่งใช้ในการควบคุมอาการชักแบบ tonic-clonic"
        }
    }
}

# Verification script
print(f"Total keys prepared: {len(distractors_data)}")
for k, v in distractors_data.items():
    wrong_choices = list(v["distractors"].keys())
    # Check zero asterisks
    for choice, text in v["distractors"].items():
        if "*" in text:
            print(f"WARNING: Asterisk found in key {k} choice {choice}")
print("Verification complete.")

with open('distractors_neuro_part3.json', 'w', encoding='utf-8') as f:
    json.dump(distractors_data, f, ensure_ascii=False, indent=2)

print("Saved to distractors_neuro_part3.json successfully.")
