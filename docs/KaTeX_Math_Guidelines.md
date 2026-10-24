# คู่มือมาตรฐานการบันทึกสมการและสูตรคำนวณ KaTeX (KaTeX Equation Guidelines)
สำหรับทีมวิชาการและผู้จัดทำคลังข้อสอบใบประกอบวิชาชีพเภสัชกรรม (PLE-CC)

---

## 1. หลักการสำคัญ (Core Principles)
1. การใส่สัญลักษณ์สมการ:
- ครอบสมการด้วยเครื่องหมาย Dollar Sign ($ ... $) เสมอ เพื่อให้ระบบ Quiz แสดงผลเป็นสูตรคณิตศาสตร์สวยงาม
- หากเป็นสมการแบบบล็อกกึ่งกลาง (Display mode) ให้ครอบด้วย $$ ... $$
2. การหลีกเลี่ยงข้อความผิดเพี้ยน:
- ห้ามพิมพ์ $it; หรือ $lt; หรือ &lt; เด็ดขาด หากต้องการพิมพ์เครื่องหมายน้อยกว่าให้พิมพ์ < ตามปกติ
- ห้ามพิมพ์ /sqrt หรือ sqrt(...) ลอยๆ ในเฉลยหรือโจทย์ ให้ใช้ \sqrt{...} เสมอ

---

## 2. ตัวอย่างสูตรคำนวณที่พบบ่อยในข้อสอบสภาเภสัชกรรม

### ก. กลุ่ม Oncology & Clinical Calculations
1. พื้นที่ผิวร่างกาย Mosteller (Body Surface Area, BSA):
- รูปแบบ KaTeX:
  $BSA = \sqrt{\frac{Height (cm) \times Weight (kg)}{3600}}$
2. การคำนวณ Carboplatin (Calvert Formula):
- รูปแบบ KaTeX:
  $Dose (mg) = Target\ AUC \times (GFR + 25)$
3. การคำนวณ Creatinine Clearance (Cockcroft-Gault Equation):
- รูปแบบ KaTeX:
  $CrCl = \frac{(140 - Age) \times Weight}{72 \times sCr} \times 0.85\ (\text{if female})$

### ข. กลุ่ม Pharmacokinetics & Biopharmaceutics
1. ค่าคงที่การกำจัดยา (Elimination rate constant, Ke):
- รูปแบบ KaTeX:
  $k_e = \frac{0.693}{t_{1/2}}$
2. ค่าครึ่งชีวิตของการกำจัดยา (Half-life):
- รูปแบบ KaTeX:
  $t_{1/2} = \frac{0.693}{k_e}$
3. Clearance (Cl) และ Volume of Distribution (Vd):
- รูปแบบ KaTeX:
  $Cl = \frac{Dose}{AUC} = k_e \times V_d$
  $V_d = \frac{Dose}{C_0}$
4. Loading Dose (LD) และ Maintenance Dose (MD):
- รูปแบบ KaTeX:
  $LD = \frac{C_{ss} \times V_d}{F}$
  $MD = \frac{C_{ss} \times Cl \times \tau}{F}$

### ค. กลุ่ม Physical Pharmacy & Preformulation
1. Henderson-Hasselbalch Equation (pH, pKa):
- กรดอ่อน:
  $pH = pKa + \log\left(\frac{[A^-]}{[HA]}\right)$
- ด่างอ่อน:
  $pH = pKw - pKb + \log\left(\frac{[B]}{[BH^+]}\right)$
2. Noyes-Whitney Equation (Dissolution rate):
- รูปแบบ KaTeX:
  $\frac{dC}{dt} = \frac{D \cdot A \cdot (C_s - C)}{h}$
3. Stokes' Law (Sedimentation rate):
- รูปแบบ KaTeX:
  $v = \frac{2 r^2 (\rho_s - \rho_f) g}{9 \eta}$

### ง. กลุ่ม Research & Biostatistics
1. Relative Risk (RR) / Odds Ratio (OR) / Hazard Ratio (HR):
- รูปแบบ KaTeX:
  $95\%\ CI = e^{\ln(RR) \pm 1.96 \times SE}$
2. Number Needed to Treat (NNT):
- รูปแบบ KaTeX:
  $NNT = \frac{1}{ARR} = \frac{1}{|EER - CER|}$
3. Chi-square:
- รูปแบบ KaTeX:
  $\chi^2 = \sum \frac{(O - E)^2}{E}$

---

## 3. สรุปตารางสัญลักษณ์และรหัส KaTeX

- เครื่องหมายคูณ: \times (ตัวอย่าง: $5 \times 10 = 50$)
- เครื่องหมายบวกลบ: \pm (ตัวอย่าง: $120 \pm 10\ mmHg$)
- เครื่องหมายน้อยกว่าหรือเท่ากับ: \leq (ตัวอย่าง: $eGFR \leq 30$)
- เครื่องหมายมากกว่าหรือเท่ากับ: \geq (ตัวอย่าง: $HbA1c \geq 6.5\%$)
- เครื่องหมายประมาณ: \approx (ตัวอย่าง: $Ke \approx 0.063\ hr^{-1}$)
- สัญลักษณ์สแควร์รูท: \sqrt{...} (ตัวอย่าง: $\sqrt{25} = 5$)
- เศษส่วน: \frac{ตัวเศษ}{ตัวส่วน} (ตัวอย่าง: $\frac{A}{B}$)
- ตัวห้อย (Subscript): _{...} (ตัวอย่าง: $C_{max}$, $t_{1/2}$, $AUC_{0-\infty}$)
- ตัวยก (Superscript): ^{...} (ตัวอย่าง: $m^2$, $kg/m^2$)
- ตัวอักษรกรีก:
  - แอลฟา: \alpha ($\alpha$)
  - บีตา: \beta ($\beta$)
  - มิว: \mu ($\mu$, $\mu g/mL$)
  - ซิกมา: \sigma ($\sigma$)
  - อีตา: \eta ($\eta$)
  - ไค: \chi ($\chi^2$)
