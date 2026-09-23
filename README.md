# 📝 PLE-CC Quiz Practice (Multiple Choices)

ระบบคลังข้อสอบปรนัยเตรียมสอบใบประกอบวิชาชีพเภสัชกรรม (PLE-CC) พัฒนาเพื่อนิสิตเภสัชศาสตร์ จุฬาลงกรณ์มหาวิทยาลัย

🌐 **Website (GitHub Pages):** [https://pharmacistlicenserxcu.github.io/PLE-CC-Quiz-practice/](https://pharmacistlicenserxcu.github.io/PLE-CC-Quiz-practice/)  
📊 **Google Sheet Database:** [Google Sheet คลังข้อสอบ](https://docs.google.com/spreadsheets/d/1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w/edit)  
⚡ **Google Apps Script ID:** `1LB8brFu49jQwb5xR3WeeyW2Su_M8e1X2XX3mxD6sxlO7yVwWpDPwG-tS`

---

## 🌟 ฟีเจอร์เด่น
1. **คลังข้อสอบ Multiple Choices 5 ตัวเลือก:**
   - ตรวจคำตอบทันที (ถูก = เขียว, ผิด = แดง)
   - แสดง **คำอธิบายเฉลยละเอียด** พร้อมภาพประกอบ (ถ้ามี)
   - คีย์ลัดแป้นพิมพ์: กดเลข `1-5` เพื่อเลือกตอบ, ลูกศร `←` `→` เพื่อเลื่อนข้อ, `Space` เพื่อไปข้อถัดไป
2. **โหมดการทำข้อสอบยืดหยุ่น:**
   - **เลือกทำตามหมวดโรค (By Category):** ฝึกเน้นเฉพาะหมวดโรคที่ต้องการ
   - **สุ่มข้อสอบ (Random Quiz):** เลือกจำนวนข้อที่ต้องการสุ่มได้ (10 / 20 / 30 / 50 ข้อ หรือทุกข้อ) พร้อมกรองตามสายวิชา Clinic / Product / SAP
3. **ระบบทบทวนข้อที่ผิด (Review Wrong Answers):**
   - เมื่อทำจบชุด มีหน้าสรุปคะแนน พร้อมปุ่มกดดูเฉลยและทบทวนเฉพาะข้อที่ตอบผิด
4. **โหมดสลับหน้าจอ (Desktop / Smartphone View):**
   - รองรับการใช้งานทั้งบนคอมพิวเตอร์ แท็บเล็ต และสมาร์ทโฟน
5. **ระบบ Offline 100% (PWA & Service Worker):**
   - ทำงานได้แม้อยู่ในโหมดออฟไลน์ หรือต่อเน็ตไม่ได้
   - อัปเดตข้อมูลอัตโนมัติเมื่อมีการเปลี่ยนแปลงใน Google Sheet

---

## 🛠️ โครงสร้างไฟล์
```
PLE CC Quiz/
├── index.html                  # Single-Page Web App
├── quiz-data-offline.js        # คลังข้อสอบ Offline สำรอง
├── manifest.json               # PWA Manifest
├── sw.js                       # Service Worker Offline Caching
├── compile_offline_db.py       # สคริปต์ดึงข้อมูลจาก Google Sheet -> JS
├── compile_offline_db.bat      # กดเพื่อคอมไพล์ฐานข้อมูล Offline
├── Push_to_GitHub.bat          # กดเพื่อคอมไพล์และ Push ขึ้น GitHub Pages อัตโนมัติ
├── images/                     # โฟลเดอร์เก็บรูปภาพประกอบข้อสอบ
└── google_apps_script/
    ├── Code.gs                 # API สำรองบน Google Apps Script
    ├── appsscript.json         # Manifest ของ Apps Script
    └── .clasp.json             # Clasp configuration
```
