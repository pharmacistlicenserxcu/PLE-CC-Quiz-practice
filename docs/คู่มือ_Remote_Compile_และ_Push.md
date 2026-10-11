# คู่มือการใช้งานระบบ Remote Compile & Push (GitHub Actions)
**ระบบคลังข้อสอบและแบบฝึกหัด PLE-CC Quiz Practice (RxCU84/85)**  
**จัดทำโดย:** ประธานโครงการเตรียมสอบใบประกอบวิชาชีพ ปีการศึกษา 2569

---

## 1. ประโยชน์ของระบบ Remote Compile & Push
- **ไม่ต้องเปิดคอมพิวเตอร์ส่วนตัว:** สามารถสั่งอัปเดตระบบข้อสอบผ่านสมาร์ตโฟน แท็บเล็ต หรือคอมพิวเตอร์เครื่องใดก็ได้ผ่านเบราว์เซอร์
- **เลือกรันเฉพาะเรื่องที่ต้องการได้ (Selective Mode):** ไม่จำเป็นต้องรอโหลดครบทั้ง 34 หมวดวิชา สามารถเลือกอัปเดตเฉพาะหมวดวิชาที่เพิ่งลงข้อสอบเสร็จได้ ใช้เวลาเพียง **10–20 วินาที**
- **Smart Incremental Merge:** ระบบจะนำข้อสอบเฉพาะหมวดที่อัปเดตไปผสานเข้ากับฐานข้อมูลเดิมอย่างปลอดภัย โดยข้อสอบหมวดอื่น ๆ ยังคงอยู่ครบถ้วน 100%
- **Auto Cache Invalidation:** เมื่อประมวลผลเสร็จ ระบบจะอัปเดตหมายเลขแคชของ Service Worker (`sw.js`) ให้ทันที ทำให้เพื่อนนิสิตที่เปิดหน้าเว็บได้รับข้อสอบเวอร์ชันใหม่โดยไม่ต้องเคลียร์แคชเอง

---

## 2. การตั้งค่าเริ่มต้นบน GitHub (ทำครั้งแรกเพียงครั้งเดียว)

เพื่อให้ระบบ GitHub Actions สามารถเชื่อมต่อ Google Sheets API ได้:
1. เปิด Repository: [pharmacistlicenserxcu/PLE-CC-Quiz-practice](https://github.com/pharmacistlicenserxcu/PLE-CC-Quiz-practice)
2. ไปที่เมนู **Settings** -> แถบด้านซ้ายเลือก **Secrets and variables** -> คลิก **Actions**
3. คลิกปุ่ม **New repository secret**
4. กำหนดค่า:
   - **Name:** `GCP_SA_KEY`
   - **Secret:** คัดลอกข้อความ JSON ทั้งหมดจากไฟล์ Service Account (`gemini-sheets-editor-497118-060a7f15daf9.json`) มาวางในช่องนี้
5. คลิก **Add secret** เป็นอันเสร็จสิ้น

---

## 3. ขั้นตอนการใช้งานผ่าน GitHub บนเบราว์เซอร์ (มือถือ / คอมพิวเตอร์)

### ขั้นที่ 1: เข้าสู่หน้าระบบ GitHub Actions
1. เปิดเบราว์เซอร์และล็อกอินบัญชี GitHub
2. ไปที่แท็บ **Actions** ของคลังข้อสอบ:  
   👉 [https://github.com/pharmacistlicenserxcu/PLE-CC-Quiz-practice/actions](https://github.com/pharmacistlicenserxcu/PLE-CC-Quiz-practice/actions)

### ขั้นที่ 2: เลือกเวิร์กโฟลว์
1. ที่แถบเมนูด้านซ้าย ให้คลิกเลือก:  
   **🚀 Remote Compile Quiz Offline Database**
2. จะเห็นแถบแจ้งเตือนทางขวาบนพร้อมปุ่มสีฟ้า:  
   **Run workflow**

### ขั้นที่ 3: กำหนดตัวเลือกและกดสั่งรัน (Run workflow)
เมื่อคลิกปุ่ม **Run workflow** จะมีกล่องหน้าต่างปรากฏขึ้นมาให้กรอกข้อมูล:

1. **Use workflow from:**  
   เลือก Branch `main` (ค่าเริ่มต้น)

2. **เลือกโหมดการ Compile (`filter_mode`):**
   - 🎯 **`category`** : อัปเดตเฉพาะหมวดวิชาที่ระบุ (เร็วที่สุด แนะนำเมื่อแก้ไขรายวิชา)
   - 🏷️ **`track`** : อัปเดตแยกตามสายวิชา (`Clinic`, `Product`, หรือ `SAP`)
   - 🌐 **`all`** : ดึงข้อมูลและคอมไพล์ใหม่ครบทุกหมวด 34 หมวด (เหมาะสำหรับ Rebuild ประจำสัปดาห์)

3. **คำค้นหา/ชื่อหมวด (`filter_query`):**
   - หากเลือกโหมด `all`: ช่องนี้ปล่อยว่างไว้ได้เลย
   - หากเลือกโหมด `category`: พิมพ์ชื่อย่อหรือชื่อหมวดวิชา เช่น:
     - `Musculo` (วิชา Musculoskeletal)
     - `Cardio` (วิชา Cardiovascular)
     - `Endocrine` (วิชา Endocrine)
     - `Pulmo` (วิชา Pulmonary)
     - `Titration` (วิชา Titrations)
     - `Calc` (วิชา Pharmaceutical Calculations)
     - `Solid` (วิชา Solid Dosage Forms)
     - `Laws` (วิชา Pharmacy Laws & Ethics)
   - หากเลือกโหมด `track`: พิมพ์สายวิชา เช่น `Clinic`, `Product`, หรือ `SAP`

4. **ข้อความกำกับ Git Commit (`commit_msg`):**
   ใส่ข้อความสั้น ๆ ระบุสิ่งที่เราแก้ไข เช่น `Update Cardio set 2567` หรือปล่อยว่างเพื่อใช้ค่ามาตรฐาน

5. **คลิกปุ่มสีเขียว Run workflow:**
   ระบบคลาวด์ของ GitHub จะเริ่มรันงานทันที (ใช้เวลาประมาณ 10–25 วินาที สำหรับหมวดเดี่ยว และ 1–2 นาที สำหรับทุกหมวด)

---

## 4. ตารางตัวอย่างคำค้นหาสำหรับ Compile แยกเรื่อง (`mode: category`)

| หมวดวิชาใน Google Sheet | คำค้นหาที่แนะนำ (`filter_query`) | สายวิชา (Track) |
| :--- | :--- | :--- |
| `1. Musculoskeleton` | `Musculo` | Clinic |
| `2. Cardiovascular` | `Cardio` | Clinic |
| `3. Dermatologic` | `Derma` | Clinic |
| `4. Endocrine` | `Endo` | Clinic |
| `5. Gastrointestinal` | `Gastro` หรือ `GI` | Clinic |
| `6. Hematologic` | `Hemato` | Clinic |
| `7. Immunologic` | `Immuno` | Clinic |
| `8. Infectious diseases` | `Infect` | Clinic |
| `9. Neurologic` | `Neuro` | Clinic |
| `10. Psychiatric` | `Psych` | Clinic |
| `11. Pulmonary` | `Pulmo` | Clinic |
| `12. GynaecologicGenitourinary`| `Gynae` หรือ `GU` | Clinic |
| `13. Eye disorder` | `Eye` | Clinic |
| `14. Oncologic` | `Onco` | Clinic |
| `15. Renal` | `Renal` | Clinic |
| `16. Toxicology & Poisoning` | `Toxic` | Clinic |
| `17. Herbal Medicine` | `Herbal Med` | Clinic |
| `18. Clinical Nutrition` | `Nutrition` | Clinic |
| `1. Titrations` | `Titration` | Product |
| `2. Chromatography` | `Chromato` | Product |
| `3. Spectroscopy & Optics` | `Spectro` | Product |
| `4. Preformulation & GMP` | `Preform` หรือ `GMP` | Product |
| `5. Pharmaceutical Calc` | `Calc` | Product |
| `6. Solid Dosage Forms` | `Solid` | Product |
| `7. Liquid & Semisolids` | `Liquid` | Product |
| `8. Biopharm & Drug Release` | `Biopharm` | Product |
| `9. Sterile & Special Forms` | `Sterile` | Product |
| `10. Biotech Products` | `Biotech` | Product |
| `11. Herbal Products` | `Herbal Prod` | Product |
| `12. Food Products & QA` | `Food` | Product |
| `13. Medicinal Chemistry` | `Medchem` หรือ `Medicinal` | Product |
| `1. Pharmacy Laws & Ethics` | `Laws` | SAP |
| `2. Pharmacy Administration & Sy` | `Admin` | SAP |
| `3. Research & Biostats` | `Biostat` หรือ `Research` | SAP |

---

## 5. การตรวจสอบผลลัพธ์
1. หลังกด **Run workflow** ให้รีเฟรชหน้ารายการ Actions จะเห็นงานกำลังรัน (ไอคอนสีเหลืองหมุน)
2. เมื่องานเสร็จสิ้น ไอคอนจะเปลี่ยนเป็น **เครื่องหมายถูกสีเขียว (Green Checkmark)**
3. เปิดหน้าเว็บหลัก PLE-CC Quiz Practice จะพบว่าข้อสอบของหมวดวิชาดังกล่าวได้รับการอัปเดตเป็นข้อมูลล่าสุดทันที
