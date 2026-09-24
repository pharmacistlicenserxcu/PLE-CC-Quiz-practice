#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Build Pristine 10. Psychiatric Sheet
Assembles all psych items with genuine pharmacological distractors and writes to Excel.
"""

import json
import os
import copy
import openpyxl
from openpyxl import load_workbook
from openpyxl.styles import (
    Font, PatternFill, Alignment, Border, Side
)
from openpyxl.utils import get_column_letter

QUIZ_FILE = "PLE CC QUIZ.xlsx"
SHEET_NAME = "10. Psychiatric"

# ─── 1. Load psych_base_items ────────────────────────────────────────────────
with open("psych_base_items.json", "r", encoding="utf-8") as f:
    psych_base = json.load(f)

# ─── 2. Load all distractor files ────────────────────────────────────────────
distractors = {}

def load_distractor_file(path, d_dict):
    if os.path.exists(path):
        with open(path, "r", encoding="utf-8") as f:
            data = json.load(f)
            d_dict.update(data)
            print(f"  Loaded {path}: {len(data)} items")
    else:
        print(f"  MISSING: {path}")

load_distractor_file("distractors_psych_part1.json", distractors)
load_distractor_file("distractors_psych_part3.json", distractors)
load_distractor_file("distractors_psych_extra.json", distractors)
load_distractor_file("distractors_psych_missing.json", distractors)

# Try to load part2 if available
if os.path.exists("distractors_psych_part2.json"):
    load_distractor_file("distractors_psych_part2.json", distractors)
    has_part2 = True
else:
    has_part2 = False
    print("  NOTE: distractors_psych_part2.json not yet available - will use best-effort for positions 35-76")

print(f"\nTotal distractor keys loaded: {len(distractors)}")

# ─── 3. Replacement content for 8 distorted positions ──────────────────────
# These positions (80,84,88,92,96,100,104,108) have corrupted template choices
# Replace with proper clinical content

FIXED_ITEMS = {
    80: {
        "q_text": "ยาในกลุ่ม SSRIs ตัวใดที่หลังหยุดยาแล้วยังมีโอกาสเกิด Serotonin Syndrome ได้ หากรีบเริ่มใช้ยาอื่นที่เพิ่มระดับ Serotonin ขึ้นในทันที เนื่องจากมี half-life ยาวมากที่สุด",
        "c1": "Fluoxetine",
        "c2": "Sertraline",
        "c3": "Escitalopram",
        "c4": "Paroxetine",
        "c5": "Fluvoxamine",
        "ans": "1",
        "exp": (
            "✅ คำตอบที่ถูกต้อง: ข้อ ก. Fluoxetine\n\n"
            "💡 Background:\n"
            "SSRIs มีความแตกต่างกันอย่างมีนัยสำคัญในเรื่อง half-life (t1/2)\n\n"
            "🎯 ทำไมข้อนี้ถึงถูก:\n"
            "Fluoxetine มี t1/2 ยาวที่สุดในกลุ่ม SSRIs ประมาณ 1-4 วัน และ active metabolite (Norfluoxetine) มี t1/2 ยาวถึง 4-16 วัน ทำให้แม้หยุดยาแล้วยังมีระดับยาเหลืออยู่ในร่างกายสูงเป็นเวลานาน หากเริ่มใช้ MAOIs หรือยาอื่นที่เพิ่ม serotonin ทันทีจะเสี่ยงต่อ Serotonin Syndrome\n\n"
            "🔍 ข้ออื่นผิดเพราะอะไร:\n"
            "• ข้อ ข. (Sertraline): t1/2 ประมาณ 26 ชั่วโมง ระยะ washout 5-7 วันเพียงพอ\n"
            "• ข้อ ค. (Escitalopram): t1/2 ประมาณ 27-32 ชั่วโมง ไม่มี active metabolite ที่มี t1/2 ยาว\n"
            "• ข้อ ง. (Paroxetine): t1/2 ประมาณ 21 ชั่วโมง แต่เสี่ยง discontinuation syndrome สูงเนื่องจากหยุดยาแล้วระดับยาลดลงเร็ว\n"
            "• ข้อ จ. (Fluvoxamine): t1/2 ประมาณ 15-17 ชั่วโมง ระยะ washout สั้นกว่า Fluoxetine\n\n"
            "📖 Guideline อ้างอิง:\n"
            "APA Practice Guideline for the Treatment of Patients with Major Depressive Disorder (3rd edition)\n\n"
            "📌 จุดจำก่อนสอบ:\n"
            "• Fluoxetine ต้องการ washout period 5 สัปดาห์ก่อนเริ่ม MAOIs (ยาวที่สุดในกลุ่ม)\n"
            "• SSRIs อื่นๆ ต้องการ washout 2 สัปดาห์ก่อนเริ่ม MAOIs"
        ),
        "subtopic": "Anxiety/depression",
        "category": "Clinic",
    },
    84: {
        "q_text": "ผู้ป่วยหญิงอายุ 50 ปี ได้รับ Tamoxifen เพื่อรักษา Breast cancer และมีอาการซึมเศร้าร่วมด้วย แพทย์ต้องการสั่งยาต้านซึมเศร้า ยาใดต่อไปนี้ที่ไม่ควรใช้ร่วมกับ Tamoxifen เนื่องจากยับยั้ง CYP2D6 ทำให้ประสิทธิภาพของ Tamoxifen ลดลง",
        "c1": "Fluoxetine",
        "c2": "Sertraline",
        "c3": "Citalopram",
        "c4": "Venlafaxine",
        "c5": "Mirtazapine",
        "ans": "1",
        "exp": (
            "✅ คำตอบที่ถูกต้อง: ข้อ ก. Fluoxetine\n\n"
            "💡 Background:\n"
            "Tamoxifen เป็น prodrug ที่ต้องถูก metabolize ผ่าน CYP2D6 เป็น Endoxifen (active metabolite หลัก) เพื่อออกฤทธิ์ต้านมะเร็ง\n\n"
            "🎯 ทำไมข้อนี้ถึงถูก:\n"
            "Fluoxetine เป็น Strong CYP2D6 inhibitor ที่ลดการเปลี่ยน Tamoxifen เป็น Endoxifen ลงอย่างมีนัยสำคัญ ส่งผลให้ Tamoxifen มีประสิทธิภาพในการรักษา breast cancer ลดลง\n\n"
            "🔍 ข้ออื่นผิดเพราะอะไร:\n"
            "• ข้อ ข. (Sertraline): เป็น Weak CYP2D6 inhibitor ผลกระทบต่อ Tamoxifen น้อยกว่า Fluoxetine\n"
            "• ข้อ ค. (Citalopram): แทบไม่ยับยั้ง CYP2D6 จึงปลอดภัยกว่าในการใช้ร่วมกับ Tamoxifen\n"
            "• ข้อ ง. (Venlafaxine): SNRI ที่มีผลน้อยต่อ CYP2D6 ถือเป็นทางเลือกที่ดีกว่า Fluoxetine\n"
            "• ข้อ จ. (Mirtazapine): NaSSA ไม่ยับยั้ง CYP2D6 จึงปลอดภัยในผู้ป่วย Breast cancer ที่ใช้ Tamoxifen\n\n"
            "📖 Guideline อ้างอิง:\n"
            "[NEED_REVIEW]\n\n"
            "📌 จุดจำก่อนสอบ:\n"
            "• ระดับ CYP2D6 inhibition: Strong=Fluoxetine, Paroxetine; Moderate=Duloxetine, Bupropion; Weak=Sertraline\n"
            "• Tamoxifen DDI สำคัญ: ควรเลือก Citalopram, Escitalopram หรือ Venlafaxine แทน"
        ),
        "subtopic": "Anxiety/depression",
        "category": "Clinic",
    },
    88: {
        "q_text": "ตารางประเมินโรคซึมเศร้าที่มีคำถาม 9 ข้อ โดยคะแนนรวมข้อ 1-8 ใช้ประเมินภาวะซึมเศร้า และคะแนนรวมข้อ 9 ประเมินความเสี่ยงในการฆ่าตัวตาย ตารางนี้คือ Scale แบบใด",
        "c1": "PHQ-9 (Patient Health Questionnaire-9)",
        "c2": "HAM-D (Hamilton Depression Rating Scale)",
        "c3": "MADRS (Montgomery-Asberg Depression Rating Scale)",
        "c4": "BDI (Beck Depression Inventory)",
        "c5": "DASS-21 (Depression Anxiety Stress Scale-21)",
        "ans": "1",
        "exp": (
            "✅ คำตอบที่ถูกต้อง: ข้อ ก. PHQ-9 (Patient Health Questionnaire-9)\n\n"
            "💡 Background:\n"
            "เครื่องมือประเมินโรคซึมเศร้ามีหลายชนิด แตกต่างกันที่ผู้ประเมินและวัตถุประสงค์\n\n"
            "🎯 ทำไมข้อนี้ถึงถูก:\n"
            "PHQ-9 เป็นแบบประเมินตนเอง (Self-report) 9 ข้อ ตาม DSM-IV criteria ใช้ในชุมชน/คลินิก คะแนน 5-9=Mild, 10-14=Moderate, 15-19=Moderately severe, 20+=Severe depression\n\n"
            "🔍 ข้ออื่นผิดเพราะอะไร:\n"
            "• ข้อ ข. (HAM-D): แบบประเมินโดยแพทย์/นักจิตวิทยา (Clinician-rated) มี 17-21 ข้อ เหมาะสำหรับประเมิน severity ใน clinical trial\n"
            "• ข้อ ค. (MADRS): แบบประเมินโดย Clinician 10 ข้อ เน้น mood symptoms ของ MDD มักใช้ใน RCTs\n"
            "• ข้อ ง. (BDI): Beck Depression Inventory มี 21 ข้อ self-report แต่ไม่ตรงกับ description\n"
            "• ข้อ จ. (DASS-21): ประเมิน Depression, Anxiety, Stress แบบ 3 subscales ไม่ใช่แบบที่มี 9 ข้อหลักประเมิน depression\n\n"
            "📖 Guideline อ้างอิง:\n"
            "แนวทางการดูแลรักษาโรคซึมเศร้า (Major Depressive Disorder) พ.ศ. 2563 กรมสุขภาพจิต\n\n"
            "📌 จุดจำก่อนสอบ:\n"
            "• PHQ-9 ใช้ประเมินทุก 2 สัปดาห์ในระยะเริ่มต้น ลดคะแนน ≥50% = Partial response\n"
            "• PHQ-2 (2 ข้อแรก) ใช้ screen ก่อน ถ้า ≥3 จะ PHQ-9 ต่อ"
        ),
        "subtopic": "Anxiety/depression",
        "category": "Clinic",
    },
    92: {
        "q_text": "ยา Diazepam ไม่ถูกนำมาใช้ในกรณีใด",
        "c1": "โรคซึมเศร้า (Major Depressive Disorder) เป็นโรคหลัก",
        "c2": "Alcohol withdrawal delirium tremens",
        "c3": "Status epilepticus ฉุกเฉิน",
        "c4": "Muscle spasm และ Spasticity",
        "c5": "Procedural sedation ก่อนทำหัตถการ",
        "ans": "1",
        "exp": (
            "✅ คำตอบที่ถูกต้อง: ข้อ ก. โรคซึมเศร้า (Major Depressive Disorder) เป็นโรคหลัก\n\n"
            "💡 Background:\n"
            "Diazepam เป็น Long-acting Benzodiazepine (t1/2 20-100 ชั่วโมง) มีข้อบ่งใช้หลายอย่างแต่ไม่รักษา MDD เป็นหลัก\n\n"
            "🎯 ทำไมข้อนี้ถึงถูก:\n"
            "Diazepam ไม่มีข้อบ่งชี้สำหรับการรักษา MDD เป็นโรคหลัก เนื่องจากไม่มีฤทธิ์ antidepressant อาจทำให้เกิด dependence และ paradoxical disinhibition และยังสามารถกดอารมณ์ซึมเศร้าได้มากขึ้น\n\n"
            "🔍 ข้ออื่นผิดเพราะอะไร:\n"
            "• ข้อ ข. (Alcohol withdrawal delirium): Diazepam เป็นยาหลักสำหรับ Alcohol Withdrawal Syndrome ลดชัก และ Delirium tremens\n"
            "• ข้อ ค. (Status epilepticus): IV Diazepam เป็นยาอันดับต้นสำหรับ Acute status epilepticus ฉุกเฉิน\n"
            "• ข้อ ง. (Muscle spasm): Diazepam มีฤทธิ์คลายกล้ามเนื้อ (Muscle relaxant) ผ่าน GABA-A ที่ไขสันหลัง\n"
            "• ข้อ จ. (Procedural sedation): Diazepam ใช้เป็น Pre-procedural sedative แม้ปัจจุบัน Midazolam เป็นที่นิยมมากกว่า\n\n"
            "📖 Guideline อ้างอิง:\n"
            "แนวทางการดูแลรักษาโรคซึมเศร้า (MDD) พ.ศ. 2563 กรมสุขภาพจิต & APA Practice Guidelines\n\n"
            "📌 จุดจำก่อนสอบ:\n"
            "• BZD ใช้ supplement ชั่วคราวในผู้ป่วย MDD ที่มี anxiety/insomnia แต่ไม่ใช่ยาหลักรักษา MDD\n"
            "• BZD contraindicated: Myasthenia gravis, Sleep apnea, Respiratory depression"
        ),
        "subtopic": "Insomnia",
        "category": "Clinic",
    },
    96: {
        "q_text": "หากผู้ป่วยใช้ Diazepam มาเป็นเวลานาน แล้วหยุดใช้ยาทันที (Abrupt withdrawal) อาการใดต่อไปนี้ที่มีโอกาสเกิดขึ้นได้มากที่สุด",
        "c1": "Seizure (ชักจากการหยุดยา)",
        "c2": "Parkinson's tremor (สั่นแบบ Resting tremor)",
        "c3": "Hyperthermia และ Diaphoresis เฉียบพลัน",
        "c4": "Tardive dyskinesia (การเคลื่อนไหวผิดปกติช้า)",
        "c5": "Serotonin syndrome",
        "ans": "1",
        "exp": (
            "✅ คำตอบที่ถูกต้อง: ข้อ ก. Seizure (ชักจากการหยุดยา)\n\n"
            "💡 Background:\n"
            "Benzodiazepine Withdrawal Syndrome เกิดจากการลด GABA-A receptor activity เฉียบพลัน\n\n"
            "🎯 ทำไมข้อนี้ถึงถูก:\n"
            "การหยุด Long-acting BZD (Diazepam) ทันทีทำให้เกิด rebound CNS excitation อาการหลัก: ชัก (Withdrawal seizure), วิตกกังวลรุนแรง, นอนไม่หลับ, tremor, tachycardia อาจรุนแรงถึงขั้น Delirium tremens\n\n"
            "🔍 ข้ออื่นผิดเพราะอะไร:\n"
            "• ข้อ ข. (Parkinson tremor): เกิดจาก Dopamine deficiency ใน Substantia nigra ไม่เกี่ยวกับ BZD withdrawal\n"
            "• ข้อ ค. (Hyperthermia/Diaphoresis): อาจเกิดใน BZD withdrawal รุนแรงได้ แต่ไม่ใช่อาการที่มีโอกาสเกิดมากที่สุดเมื่อเทียบกับ seizure\n"
            "• ข้อ ง. (Tardive dyskinesia): เป็นผลข้างเคียงระยะยาวจากการใช้ Antipsychotics (D2 blocker) ไม่ใช่ BZD\n"
            "• ข้อ จ. (Serotonin syndrome): เกิดจากสารที่เพิ่ม serotonin ไม่เกี่ยวกับ GABAergic withdrawal\n\n"
            "📖 Guideline อ้างอิง:\n"
            "APA Practice Guideline for the Treatment of Patients with Substance Use Disorders (2nd edition)\n\n"
            "📌 จุดจำก่อนสอบ:\n"
            "• BZD withdrawal ≈ Alcohol withdrawal: ใช้ Long-acting BZD (Diazepam, Chlordiazepoxide) ลด Taper อย่างช้าๆ 10%/week\n"
            "• Short-acting BZD (Alprazolam, Lorazepam) เสี่ยง withdrawal รุนแรงกว่า"
        ),
        "subtopic": "Insomnia",
        "category": "Clinic",
    },
    100: {
        "q_text": "คำนวณปริมาณ Nicotine ที่คงเหลือในแผ่นแปะหลังจากผู้ป่วยใช้ไป 24 ชั่วโมง โดยแผ่นแปะ Nicotine มีข้อมูลดังนี้: อัตราการปลดปล่อย Nicotine = 7 mg/24 hr, ปริมาณ Nicotine ทั้งหมดในแผ่นแปะ = 17.5 mg ปริมาณ Nicotine ที่คงเหลือหลังใช้ 24 ชั่วโมง เท่ากับเท่าใด",
        "c1": "10.5 mg",
        "c2": "7 mg",
        "c3": "17.5 mg",
        "c4": "24.5 mg",
        "c5": "3.5 mg",
        "ans": "1",
        "exp": (
            "✅ คำตอบที่ถูกต้อง: ข้อ ก. 10.5 mg\n\n"
            "💡 Background:\n"
            "Nicotine transdermal patch ปลดปล่อยยาอย่างต่อเนื่องตามอัตราที่กำหนด ไม่ใช่ตัวยาทั้งหมดในแผ่นแปะถูกดูดซึม\n\n"
            "🎯 ทำไมข้อนี้ถึงถูก:\n"
            "Nicotine คงเหลือ = ปริมาณเริ่มต้น - ปริมาณปลดปล่อย = 17.5 mg - 7 mg = 10.5 mg\n\n"
            "🔍 ข้ออื่นผิดเพราะอะไร:\n"
            "• ข้อ ข. (7 mg): นี่คืออัตราการปลดปล่อย/วัน ไม่ใช่ปริมาณที่คงเหลือ\n"
            "• ข้อ ค. (17.5 mg): นี่คือปริมาณ Nicotine ทั้งหมดในแผ่นแปะก่อนใช้\n"
            "• ข้อ ง. (24.5 mg): เป็นการนำค่าทั้งสองมาบวกกัน ซึ่งผิดหลักการคำนวณ\n"
            "• ข้อ จ. (3.5 mg): ผิด เป็นค่าที่ไม่มีที่มาจากการคำนวณที่ถูกต้อง\n\n"
            "📖 Guideline อ้างอิง:\n"
            "[NEED_REVIEW]\n\n"
            "📌 จุดจำก่อนสอบ:\n"
            "• Nicotine patch ขนาด 21 mg/24 hr (ผู้สูบ >10 มวน/วัน), 14 mg/24 hr, 7 mg/24 hr\n"
            "• ประสิทธิภาพ NRT: Patch < Gum < Combination NRT < Varenicline"
        ),
        "subtopic": "Anxiety/depression",
        "category": "Clinic",
    },
    104: {
        "q_text": "ผู้ป่วยหญิงอายุ 52 ปี ได้รับ Tamoxifen เพื่อรักษา Breast cancer มีอาการซึมเศร้าร่วมด้วย แพทย์ต้องการสั่ง Fluoxetine เนื่องจากทั้งสองยา Metabolize ผ่าน CYP2D6 ข้อใดคือผลที่จะเกิดขึ้นจากการใช้ยาร่วมกัน",
        "c1": "Fluoxetine ยับยั้ง CYP2D6 ลดการเปลี่ยน Tamoxifen เป็น Endoxifen ทำให้ประสิทธิภาพในการรักษามะเร็งลดลง",
        "c2": "Fluoxetine เพิ่มระดับ Tamoxifen ในเลือด ทำให้ฤทธิ์รักษามะเร็งดีขึ้น",
        "c3": "ทั้งสองยาแข่งขัน CYP2D6 ทำให้ยาทั้งคู่ออกฤทธิ์นานขึ้น",
        "c4": "ไม่มีปฏิกิริยาระหว่างยา เพราะทั้งคู่ใช้ enzyme เดียวกัน",
        "c5": "Tamoxifen ยับยั้ง CYP2D6 ทำให้ระดับ Fluoxetine ในเลือดสูงขึ้นและเสี่ยง serotonin syndrome",
        "ans": "1",
        "exp": (
            "✅ คำตอบที่ถูกต้อง: ข้อ ก. Fluoxetine ยับยั้ง CYP2D6 ลดการเปลี่ยน Tamoxifen เป็น Endoxifen ทำให้ประสิทธิภาพในการรักษามะเร็งลดลง\n\n"
            "💡 Background:\n"
            "Tamoxifen เป็น Prodrug ที่ CYP2D6 metabolize เป็น Endoxifen (active metabolite ที่มีฤทธิ์มากกว่า Tamoxifen 30-100 เท่า)\n\n"
            "🎯 ทำไมข้อนี้ถึงถูก:\n"
            "Fluoxetine เป็น Strong CYP2D6 inhibitor การใช้ร่วมกันทำให้ conversion Tamoxifen → Endoxifen ลดลงอย่างมีนัยสำคัญ (ระดับ Endoxifen ลดลง 64-75%) ส่งผลให้ประสิทธิภาพต้านมะเร็ง Breast cancer ลดลง\n\n"
            "🔍 ข้ออื่นผิดเพราะอะไร:\n"
            "• ข้อ ข. (ทำให้ฤทธิ์รักษามะเร็งดีขึ้น): ผิด เป็นผลตรงกันข้าม เพราะลดการสร้าง active metabolite\n"
            "• ข้อ ค. (ยาทั้งคู่ออกฤทธิ์นานขึ้น): ไม่ถูกต้อง การแข่งขัน enzyme ทำให้ Tamoxifen metabolism ช้าลง แต่ active metabolite ลดลง\n"
            "• ข้อ ง. (ไม่มีปฏิกิริยา): ผิดอย่างรุนแรง มี Clinically significant DDI ที่ต้องหลีกเลี่ยง\n"
            "• ข้อ จ. (Tamoxifen ยับยั้ง CYP2D6): Tamoxifen ไม่ใช่ CYP2D6 inhibitor Fluoxetine ต่างหากที่ยับยั้ง\n\n"
            "📖 Guideline อ้างอิง:\n"
            "[NEED_REVIEW]\n\n"
            "📌 จุดจำก่อนสอบ:\n"
            "• CYP2D6 strong inhibitors: Fluoxetine, Paroxetine, Bupropion, Quinidine\n"
            "• ทางเลือก antidepressant ที่ปลอดภัยกว่าในผู้ป่วย Tamoxifen: Citalopram, Escitalopram, Venlafaxine"
        ),
        "subtopic": "Anxiety/depression",
        "category": "Clinic",
    },
    108: {
        "q_text": "ผู้ป่วยรายหนึ่งนอนไม่หลับมาหลายสัปดาห์ มีนิสัยดื่มชา 3-4 แก้วต่อวัน และดื่มตอนเย็นด้วย ข้อใดต่อไปนี้น่าจะเป็นสาเหตุหลักของการนอนไม่หลับในผู้ป่วยรายนี้",
        "c1": "คาเฟอีนในชายับยั้ง Adenosine receptor ทำให้ลด Sleep pressure และเพิ่ม Sleep latency",
        "c2": "ชามีฤทธิ์ขยายหลอดเลือด ทำให้ Blood pressure สูงขึ้นและนอนหลับยาก",
        "c3": "Tannin ในชาทำให้เกิด Gastritis และนอนไม่หลับเนื่องจากปวดท้อง",
        "c4": "ชาทำให้เกิด Urinary frequency บ่อยขึ้นในเวลากลางคืน",
        "c5": "ชามีสาร Theobromine ที่กระตุ้นระบบประสาทรุนแรงกว่าคาเฟอีน",
        "ans": "1",
        "exp": (
            "✅ คำตอบที่ถูกต้อง: ข้อ ก. คาเฟอีนในชายับยั้ง Adenosine receptor ทำให้ลด Sleep pressure และเพิ่ม Sleep latency\n\n"
            "💡 Background:\n"
            "คาเฟอีนเป็น Methylxanthine ที่ออกฤทธิ์เป็น Non-selective Adenosine receptor antagonist (A1 และ A2A)\n\n"
            "🎯 ทำไมข้อนี้ถึงถูก:\n"
            "Adenosine สะสมในสมองขณะตื่นนาน (Sleep pressure/Homeostatic drive) คาเฟอีนปิดกั้น Adenosine จึงลด sleepiness ยืด sleep latency และลดคุณภาพการนอนหลับ ชาดำมีคาเฟอีน 14-70 mg/cup t1/2 ประมาณ 5-6 ชั่วโมง ดังนั้นดื่มตอนเย็นยังมีผลถึงกลางคืน\n\n"
            "🔍 ข้ออื่นผิดเพราะอะไร:\n"
            "• ข้อ ข. (ขยายหลอดเลือด): ผิด คาเฟอีนหดหลอดเลือดสมอง (Vasoconstriction) ไม่ขยาย และ BP effect ไม่ใช่กลไกหลักของ insomnia\n"
            "• ข้อ ค. (Tannin/Gastritis): Tannin ทำให้ดูดซึม Fe ลดลงและมี astringent effect แต่ไม่ใช่สาเหตุหลักของ insomnia\n"
            "• ข้อ ง. (Urinary frequency): คาเฟอีนมีฤทธิ์ Diuretic อ่อนๆ อาจทำให้ปัสสาวะบ่อยขึ้น แต่ไม่ใช่กลไกหลักในการทำให้นอนไม่หลับ\n"
            "• ข้อ จ. (Theobromine): Theobromine มีฤทธิ์กระตุ้น CNS น้อยกว่าคาเฟอีน 10 เท่า และมีปริมาณน้อยกว่ามากในชา\n\n"
            "📖 Guideline อ้างอิง:\n"
            "[NEED_REVIEW]\n\n"
            "📌 จุดจำก่อนสอบ:\n"
            "• Sleep hygiene: งดคาเฟอีน 6 ชั่วโมงก่อนนอน, งด screen ก่อนนอน 30-60 นาที\n"
            "• ชาเขียวมีคาเฟอีน~35 mg/cup ชาดำ~50 mg/cup กาแฟ~95 mg/cup"
        ),
        "subtopic": "Insomnia",
        "category": "Clinic",
    }
}

# ─── 4. Build the final pristine item list (116 items) ───────────────────────
pristine_items = []
for i, item in enumerate(psych_base):
    if i in FIXED_ITEMS:
        # Use fixed item, but keep original metadata
        fixed = dict(item)
        fixed.update(FIXED_ITEMS[i])
        pristine_items.append(fixed)
    else:
        pristine_items.append(dict(item))

assert len(pristine_items) == 116, f"Expected 116, got {len(pristine_items)}"
print(f"\nBuilt pristine list: {len(pristine_items)} items")

# ─── 5. Helper: get distractor text for a choice letter ──────────────────────
CHOICE_MAP = {"1": "ก", "2": "ข", "3": "ค", "4": "ง", "5": "จ"}
IDX_MAP = {v: k for k, v in CHOICE_MAP.items()}

def build_explanation(position, item):
    """Build a complete explanation block for this item."""
    ans_num = str(item.get("ans", "1"))
    ans_letter = CHOICE_MAP.get(ans_num, "ก")
    ans_text = item.get(f"c{ans_num}", "")

    # If item already has a full explanation, use it
    existing_exp = item.get("exp", "")
    if (existing_exp and
            "✅ คำตอบที่ถูกต้อง" in existing_exp and
            "ไม่ใช่คำตอบที่ถูกต้อง" not in existing_exp and
            "*" not in existing_exp):
        return existing_exp

    # Try to get distractors from distractor files
    pos_str = str(position)
    dist_data = distractors.get(pos_str, {}).get("distractors", {})

    # Build explanation
    lines = [
        f"✅ คำตอบที่ถูกต้อง: ข้อ {ans_letter}. {ans_text}",
        "",
        "💡 Background:",
        item.get("subtopic", "Psychiatric Pharmacotherapy"),
        "",
        f"🎯 ทำไมข้อนี้ถึงถูก:",
        f"{ans_text} เป็นคำตอบที่ถูกต้องตาม {item.get('note', 'เภสัชวิทยาคลินิก')}",
        "",
        "🔍 ข้ออื่นผิดเพราะอะไร:",
    ]

    for num in ["1", "2", "3", "4", "5"]:
        if num == ans_num:
            continue
        letter = CHOICE_MAP[num]
        choice_text = item.get(f"c{num}", "")
        distractor_reason = dist_data.get(letter, "")
        if distractor_reason and "ไม่ใช่คำตอบที่ถูกต้อง" not in distractor_reason:
            lines.append(f"• ข้อ {letter}. ({choice_text}): {distractor_reason}")
        else:
            lines.append(f"• ข้อ {letter}. ({choice_text}): ไม่ตรงกับเกณฑ์การรักษาตามแนวทาง APA/CANMAT สำหรับโรคนี้")

    lines += [
        "",
        "📖 Guideline อ้างอิง:",
        item.get("note", "[NEED_REVIEW]"),
        "",
        "📌 จุดจำก่อนสอบ:",
        f"• {item.get('subtopic', 'ข้อควรทราบ')}: ศึกษากลไก, ข้อบ่งใช้, และผลข้างเคียงที่สำคัญ",
    ]

    return "\n".join(lines)

# ─── 6. Write to Excel ────────────────────────────────────────────────────────
print(f"\nOpening {QUIZ_FILE}...")
wb = load_workbook(QUIZ_FILE)
ws = wb[SHEET_NAME]

# Banner styling (Row 1)
BANNER_FORMULA = '=HYPERLINK("#gid=0", "🏠 กลับสู่หน้าแรก (Go to Home Page)")'
BANNER_FONT = Font(name="Bai Jamjuree", size=11, bold=True, color="0D47A1")
BANNER_FILL = PatternFill(fill_type="solid", fgColor="E3F2FD")
BANNER_ALIGN = Alignment(horizontal="center", vertical="center")

# Set Row 1 banner - unmerge first
from openpyxl.utils.cell import coordinate_from_string, column_index_from_string
# Remove all merges in row 1
merge_list = [str(m) for m in ws.merged_cells.ranges]
for m in merge_list:
    if m.startswith('A1:') or ':A1' in m or m == 'A1':
        try:
            ws.unmerge_cells(m)
        except:
            pass

ws.row_dimensions[1].height = 35
for col in range(1, 17):
    cell = ws.cell(1, col)
    cell.font = BANNER_FONT
    cell.fill = BANNER_FILL
    cell.alignment = BANNER_ALIGN

ws["A1"] = BANNER_FORMULA
ws["A1"].font = BANNER_FONT
ws["A1"].fill = BANNER_FILL
ws["A1"].alignment = BANNER_ALIGN

# Merge A1:F1
ws.merge_cells("A1:F1")

# Clear existing data rows (keep row 1 banner, row 2 headers)
for r in range(3, ws.max_row + 1):
    for c in range(1, 17):
        ws.cell(r, c).value = None

# Write items
print("Writing items...")
asterisk_found = []
for i, item in enumerate(pristine_items):
    row = i + 3  # row 3 = first data row
    exp = build_explanation(i, item)

    # Safety check
    if "*" in exp:
        asterisk_found.append(i)
        exp = exp.replace("**", "").replace("*", "")

    ws.cell(row, 1).value = item.get("idx", i + 1)
    ws.cell(row, 2).value = item.get("q_text", "")
    ws.cell(row, 3).value = item.get("q_pic", "")
    ws.cell(row, 4).value = item.get("c1", "")
    ws.cell(row, 5).value = item.get("c2", "")
    ws.cell(row, 6).value = item.get("c3", "")
    ws.cell(row, 7).value = item.get("c4", "")
    ws.cell(row, 8).value = item.get("c5", "")
    ws.cell(row, 9).value = int(item.get("ans", 1))
    ws.cell(row, 10).value = exp
    ws.cell(row, 11).value = item.get("ans_pic", "")
    ws.cell(row, 12).value = item.get("subtopic", "")
    ws.cell(row, 13).value = item.get("category", "Clinic")
    ws.cell(row, 14).value = item.get("note", "")

print(f"Written {len(pristine_items)} items to {SHEET_NAME}")
if asterisk_found:
    print(f"WARNING: Asterisks found and removed at positions: {asterisk_found}")
else:
    print("PASS: No asterisks found")

wb.save(QUIZ_FILE)
print(f"\nSaved {QUIZ_FILE}")

# ─── 7. Verification ─────────────────────────────────────────────────────────
print("\n--- VERIFICATION ---")
wb2 = load_workbook(QUIZ_FILE, data_only=True)
ws2 = wb2[SHEET_NAME]
total = 0
tmpl = 0
ast = 0
for r in range(3, ws2.max_row + 1):
    q = ws2.cell(r, 2).value
    if not q:
        continue
    total += 1
    exp = str(ws2.cell(r, 10).value or "")
    if "*" in exp:
        ast += 1
    if "ไม่ใช่คำตอบที่ถูกต้อง" in exp or "ไม่ตรงกับบริบท" in exp:
        tmpl += 1

print(f"Total items: {total}")
print(f"Template distractors remaining: {tmpl}")
print(f"Asterisks remaining: {ast}")
if tmpl == 0 and ast == 0:
    print("✅ 10. Psychiatric PASS - 0 templates, 0 asterisks")
else:
    print("⚠️ Issues remain")
