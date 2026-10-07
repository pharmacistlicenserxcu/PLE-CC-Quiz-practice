/**
 * =========================================================================
 * 📝 PLE-CC Quiz Practice — Web App API (Code.gs)
 * =========================================================================
 * Script ID: 1LB8brFu49jQwb5xR3WeeyW2Su_M8e1X2XX3mxD6sxlO7yVwWpDPwG-tS
 * Sheet ID: 1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w
 * 
 * Standard Sheet Column Layout (A=ข้อที่, B-P = 15 data cols, row1=Banner, row2=Header):
 *  A: ข้อที่
 *  B: คำถาม (Question)
 *  C: รูปถาม (Question Image URL)
 *  D: ตัวเลือก 1 (Choice 1)
 *  E: ตัวเลือก 2 (Choice 2)
 *  F: ตัวเลือก 3 (Choice 3)
 *  G: ตัวเลือก 4 (Choice 4)
 *  H: ตัวเลือก 5 (Choice 5)
 *  I: เฉลย (Answer Key 1-5)
 *  J: คำอธิบายเฉลย (Explanation)
 *  K: รูปเฉลย (Answer Image URL)
 *  L: Filter หมวด/Subtopic
 *  M: Product / Clinic (Track)
 *  N: หมายเหตุ (Note)
 *  O: ประเภทข้อสอบ (Exam Type)
 *  P: ปี / เลขชุด (Exam Year/Set)
 * 
 * Quick Ingestion Sheet (📥 prefix) — Extra column:
 *  Q: หมวดวิชา/ชีตปลายทาง (Category Tag — routes question to correct category)
 * =========================================================================
 */

// ────────────────────────────────────────────────────────────────────────────
// HELPER: ตรวจสอบว่า sheet เป็น Quick Ingestion Tab หรือไม่
// ────────────────────────────────────────────────────────────────────────────
function isIngestionSheet_(name) {
  return name.startsWith('📥') || name.startsWith('QI_');
}

// ────────────────────────────────────────────────────────────────────────────
// HELPER: ตรวจสอบว่า sheet ควรถูกข้ามไป (Log, Report, Eval, สารบัญ, Config)
// ────────────────────────────────────────────────────────────────────────────
function isSystemSheet_(name) {
  return name.startsWith('Log_') || name.startsWith('Report_') ||
         name.startsWith('Eval_') || name === 'สารบัญ' ||
         name.startsWith('Config_') || name.startsWith('User_') ||
         name.startsWith('Community_') || name.startsWith('Question_');
}


// ────────────────────────────────────────────────────────────────────────────
// Custom Menu — แสดงขึ้นบน Google Sheets เมื่อเปิดไฟล์
// ────────────────────────────────────────────────────────────────────────────
function onOpen() {
  SpreadsheetApp.getUi()
    .createMenu('⚡ ระบบคลังข้อสอบ PLE')
    .addItem('📥 สร้าง/รีเซ็ต Tab นำเข้าข้อสอบด่วน', 'setupQuickIngestionTab')
    .addToUi();
}

// ────────────────────────────────────────────────────────────────────────────
// setupQuickIngestionTab — สร้าง Tab "📥 รวมข้อสอบด่วน" พร้อม Dropdown
// รันฟังก์ชันนี้ครั้งเดียวจาก Apps Script Editor หรือผ่านเมนู
// ────────────────────────────────────────────────────────────────────────────
function setupQuickIngestionTab() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const TAB_NAME = '📥 รวมข้อสอบด่วน';

  // ──── สร้างหรือเปิด Tab ────
  let sheet = ss.getSheetByName(TAB_NAME);
  if (!sheet) {
    sheet = ss.insertSheet(TAB_NAME);
    // ย้ายให้เป็น Tab แรกหลังหน้าแรก (ถ้ามี)
    try { ss.moveActiveSheet(1); } catch(e) {}
  } else {
    sheet.clearContents();
    sheet.clearFormats();
  }

  // ──── ดึงรายชื่อชีตวิชาทั้งหมด (ใช้เป็น Category Tag dropdown) ────
  const allCategoryNames = ss.getSheets()
    .map(s => s.getName())
    .filter(n => !isSystemSheet_(n) && !isIngestionSheet_(n));

  // ──── Row 1: Banner กลับหน้าแรก ────
  const homeSheet = ss.getSheets()[0];
  const homeGid   = homeSheet.getSheetId();
  sheet.getRange('A1').setFormula(
    '=HYPERLINK("#gid=' + homeGid + '","🏠 กลับสู่หน้าแรก (Go to Home Page)")'
  );
  sheet.getRange('A1:Q1').merge()
    .setBackground('#E3F2FD')
    .setFontFamily('Bai Jamjuree')
    .setFontSize(11)
    .setFontWeight('bold')
    .setHorizontalAlignment('center')
    .setVerticalAlignment('middle')
    .setFontColor('#0D47A1');
  sheet.setRowHeight(1, 36);

  // ──── Row 2: Headers ────
  const headers = [
    'ข้อที่',
    'คำถาม',
    'รูปถาม',
    'ตัวเลือก 1 (ก)',
    'ตัวเลือก 2 (ข)',
    'ตัวเลือก 3 (ค)',
    'ตัวเลือก 4 (ง)',
    'ตัวเลือก 5 (จ)',
    'เฉลย (1-5)',
    'คำอธิบายเฉลย',
    'รูปเฉลย',
    'Filter หมวด/Subtopic',
    'Track (Product/Clinic/SAP)',
    'หมายเหตุ',
    'ประเภทข้อสอบ',
    'ปี / เลขชุด',
    'หมวดวิชา/ชีตปลายทาง ★'   // คอลัมน์ Q — Category Tag (ใช้ route ข้อสอบไปหมวดวิชาในเว็บ)
  ];
  sheet.getRange(2, 1, 1, headers.length).setValues([headers])
    .setBackground('#1565C0')
    .setFontColor('#FFFFFF')
    .setFontFamily('Bai Jamjuree')
    .setFontSize(10)
    .setFontWeight('bold')
    .setHorizontalAlignment('center')
    .setVerticalAlignment('middle');
  sheet.setRowHeight(2, 40);

  // ──── กำหนดความกว้างคอลัมน์ ────
  const colWidths = [50, 350, 100, 160, 160, 160, 160, 160, 80, 400, 100, 140, 100, 120, 120, 180, 220];
  colWidths.forEach((w, i) => sheet.setColumnWidth(i + 1, w));

  // ──── Data Validation Dropdowns (เริ่มที่ Row 3 ลงไป 200 แถว) ────
  const dataRows = sheet.getRange(3, 1, 200, 17);

  // Col M (13): Track
  sheet.getRange(3, 13, 200, 1).setDataValidation(
    SpreadsheetApp.newDataValidation()
      .requireValueInList(['Clinic', 'Product', 'SAP'], true)
      .setAllowInvalid(false)
      .build()
  );

  // Col O (15): ประเภทข้อสอบ
  sheet.getRange(3, 15, 200, 1).setDataValidation(
    SpreadsheetApp.newDataValidation()
      .requireValueInList(['Mock', 'ข้อสอบจริง', 'ข้อสอบเก่า', 'แบบฝึกหัด'], true)
      .setAllowInvalid(false)
      .build()
  );

  // Col P (16): ปี / เลขชุด
  sheet.getRange(3, 16, 200, 1).setDataValidation(
    SpreadsheetApp.newDataValidation()
      .requireValueInList([
        '2567', '2566', '2565', '2564', '2563', '2562', '2561',
        '2560', '2559', '2558', '2557',
        'เล่มม่วง (Pharma Plus)', 'Mock RxCU84', 'Mock RxCU85',
        'ข้อสอบรวม'
      ], true)
      .setAllowInvalid(true) // อนุญาตพิมพ์เองได้
      .build()
  );

  // Col Q (17): หมวดวิชา/ชีตปลายทาง (Category Tag) ★ สำคัญที่สุด
  if (allCategoryNames.length > 0) {
    sheet.getRange(3, 17, 200, 1).setDataValidation(
      SpreadsheetApp.newDataValidation()
        .requireValueInList(allCategoryNames, true)
        .setAllowInvalid(false)
        .build()
    );
  }

  // Col I (9): เฉลย (1-5)
  sheet.getRange(3, 9, 200, 1).setDataValidation(
    SpreadsheetApp.newDataValidation()
      .requireValueInList(['1', '2', '3', '4', '5'], true)
      .setAllowInvalid(false)
      .build()
  );

  // ──── Freeze แถว 1-2 ────
  sheet.setFrozenRows(2);
  // Freeze คอลัมน์ Q (17) — ไม่ freeze เพราะไม่ถือเป็น fixed column
  // แต่ freeze คอลัมน์ A (ข้อที่)
  sheet.setFrozenColumns(1);

  // ──── สีแถบ Tab ────
  sheet.setTabColor('#1E88E5');

  // ──── สร้างแถวตัวอย่างว่าง (Row 3) เพื่อให้เห็นโครงสร้าง ────
  sheet.getRange(3, 1, 1, 17)
    .setBackground('#F0F8FF')
    .setVerticalAlignment('middle');

  // ──── Conditional Formatting: ไฮไลต์แถวที่ยังไม่มี Category Tag (คอลัมน์ Q ว่าง) ────
  const cfRange = sheet.getRange('Q3:Q202');
  const cfRule  = SpreadsheetApp.newConditionalFormatRule()
    .whenTextEqualTo('')
    .setBackground('#FFF9C4') // สีเหลืองอ่อน = ยังไม่ได้ระบุหมวดวิชา
    .setRanges([sheet.getRange('A3:Q202')])
    .build();
  sheet.setConditionalFormatRules([cfRule]);

  SpreadsheetApp.getUi().alert(
    '✅ สร้าง Tab "' + TAB_NAME + '" สำเร็จแล้ว!\n\n' +
    'คำแนะนำการใช้งาน:\n' +
    '1. กรอกข้อสอบตั้งแต่แถวที่ 3 ลงไปได้เลย\n' +
    '2. คอลัมน์ Q "หมวดวิชา/ชีตปลายทาง ★" สำคัญมาก ต้องเลือกจาก Dropdown เสมอ\n' +
    '3. เว็บจะอ่านจาก Tab นี้และกระจายข้อสอบเข้าหมวดวิชาตามคอลัมน์ Q อัตโนมัติ\n' +
    '4. แถวที่สีเหลือง = ยังไม่ได้เลือกหมวดวิชา → เว็บจะยังไม่แสดง'
  );
}

function doGet(e) {

  try {
    const params = e ? e.parameter : {};
    const action = params.action || 'ping';
    const sheetName = params.sheet || '';

    // 1. Ping
    if (action === 'ping') {
      return jsonResponse_({
        success: true,
        message: 'PLE-CC Quiz API is Live 🚀',
        timestamp: new Date().toISOString()
      });
    }

    // 2. ดึงรายชื่อหมวดหมู่ / Tabs ทั้งหมด (ข้าม Log, Report, Eval, สารบัญ, Config และ 📥 Ingestion Tabs)
    if (action === 'getCategories' || action === 'getSheetList') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      const sheets = ss.getSheets();
      const categories = [];

      sheets.forEach(sheet => {
        const title = sheet.getName();
        // ข้าม System sheets และ Quick Ingestion tabs (📥) — ข้อสอบจาก 📥 จะกระจายเข้าหมวดวิชาอัตโนมัติผ่าน Category Tag
        if (isSystemSheet_(title) || isIngestionSheet_(title)) return;

        const lastRow = sheet.getLastRow();
        let count = 0;
        let track = 'Clinic';
        if (lastRow >= 3) {
          count = lastRow - 2; // ลบ banner row 1 และ header row 2
          try {
            // Track อยู่ที่คอลัมน์ M (index 13 = col 13)
            const sampleTrack = sheet.getRange(3, 13).getValue();
            if (sampleTrack) track = String(sampleTrack).trim();
          } catch(err) {}
        }

        categories.push({
          name: title,
          count: count,
          track: track
        });
      });

      return jsonResponse_({
        success: true,
        count: categories.length,
        categories: categories
      });
    }


    // 3. ดึงข้อสอบจาก Sheet ที่ระบุ หรือดึงทุก Sheet
    if (action === 'getQuestions') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      let targetSheets = [];

      if (sheetName && sheetName !== '__all__') {
        const s = ss.getSheetByName(sheetName);
        if (!s) return jsonResponse_({ success: false, error: 'Sheet not found: ' + sheetName });
        targetSheets = [s];
      } else {
        // รวมชีตข้อสอบปกติ + ชีต 📥 Quick Ingestion (เพื่อให้ข้อสอบจาก 📥 กระจายไปหมวดวิชาตาม Category Tag)
        // ข้ามเฉพาะ System sheets เช่น Log_, Report_, Eval_, สารบัญ, Config_, User_, Community_, Question_
        targetSheets = ss.getSheets().filter(s => !isSystemSheet_(s.getName()));
      }

      const allQuestions = [];
      const inCellImages = getCachedInCellImages_();

      targetSheets.forEach(sheet => {
        const sName = sheet.getName();
        const lastRow = sheet.getLastRow();
        if (lastRow < 3) return; // แถว 1=Banner, แถว 2=Header

        // Quick Ingestion Tab (📥) มีคอลัมน์ Q พิเศษสำหรับ Category Tag → อ่าน 17 คอลัมน์
        // Sheet ปกติอ่าน 16 คอลัมน์ (A-P)
        const isIngest = isIngestionSheet_(sName);
        const numCols  = isIngest ? 17 : 16;
        const values   = sheet.getRange(3, 1, lastRow - 2, numCols).getValues();

        values.forEach((row, idx) => {
          const rowNum   = idx + 3;
          const firstVal = String(row[0] || '').trim();

          let offset = 0;
          let itemNo = allQuestions.length + 1;
          if (/^\d+$/.test(firstVal) || (row.length >= numCols && firstVal.length <= 4)) {
            offset = 1;
            itemNo = parseInt(firstVal, 10) || (allQuestions.length + 1);
          }

          const questionText = String(row[offset + 0] || '').trim();
          const rawQImg      = row[offset + 1];
          const c1           = String(row[offset + 2] || '').trim();
          const c2           = String(row[offset + 3] || '').trim();
          const c3           = String(row[offset + 4] || '').trim();
          const c4           = String(row[offset + 5] || '').trim();
          const c5           = String(row[offset + 6] || '').trim();
          const answerKey    = parseInt(row[offset + 7], 10) || 1;
          const explanation  = String(row[offset + 8] || '').trim();
          const rawAImg      = row[offset + 9];
          const subtopic     = String(row[offset + 10] || '').trim();
          const track        = String(row[offset + 11] || 'Clinic').trim();
          const note         = String(row[offset + 12] || '').trim();
          const examType     = String(row[offset + 13] || '').trim();
          const examYear     = String(row[offset + 14] || '').trim();

          // ─── Quick Ingestion: อ่าน Category Tag จากคอลัมน์ Q (offset+16) ───
          // ถ้ามี Tag → ใช้ Tag เป็น category (ข้อสอบจะไปโผล่ในหมวดวิชานั้นในเว็บ)
          // ถ้าไม่มี Tag → ข้ามแถวนี้ (ยังไม่ได้จัดหมวด)
          let category = sName;
          if (isIngest) {
            const categoryTag = String(row[offset + 16] || '').trim();
            if (!categoryTag) return; // ข้ามแถวที่ยังไม่ได้ระบุหมวดวิชา
            category = categoryTag;
          }

          if (!questionText && !c1) return;

          const qImgColIdx  = offset + 1;
          const aImgColIdx  = offset + 9;
          const questionImg = resolveImageUrl_(rawQImg, sName, rowNum, qImgColIdx, inCellImages);
          const answerImg   = resolveImageUrl_(rawAImg, sName, rowNum, aImgColIdx, inCellImages);

          const choices = [c1, c2, c3, c4];
          if (c5) choices.push(c5);

          allQuestions.push({
            id:            sName + '::' + rowNum,
            itemNo:        itemNo,
            category:      category,                         // ← ใช้ Category Tag สำหรับ 📥, ชื่อชีตสำหรับชีตปกติ
            subtopic:      subtopic || category,
            track:         track,
            examType:      examType,
            examYear:      examYear,
            question:      questionText,
            questionImage: questionImg,
            choices:       choices,
            answer:        answerKey,
            explanation:   explanation,
            answerImage:   answerImg,
            note:          note,
            fromIngestion: isIngest                          // ← flag บอกว่ามาจาก 📥 tab
          });
        });
      });

      return jsonResponse_({
        success: true,
        sheet: sheetName || '__all__',
        count: allQuestions.length,
        questions: allQuestions
      });
    }


    // 4. ดึงข้อมูลตารางอันดับคนขยัน (Leaderboard Top 10) & สถิติจำนวนสมาชิก
    if (action === 'getLeaderboard') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      const sheet = ss.getSheetByName('User_Profiles');
      if (!sheet) {
        return jsonResponse_({ success: true, totalMembers: 0, totalAnsweredAll: 0, leaderboard: [] });
      }
      const lastRow = sheet.getLastRow();
      if (lastRow < 3) {
        return jsonResponse_({ success: true, totalMembers: 0, totalAnsweredAll: 0, leaderboard: [] });
      }

      const rows = sheet.getRange(3, 1, lastRow - 2, 7).getValues();
      let totalQuestionsAll = 0;
      const usersList = [];

      rows.forEach(r => {
        const u = String(r[0] || '').trim();
        if (!u) return;
        const dn = String(r[1] || u).trim();
        const ans = Number(r[2] || 0);
        const cor = Number(r[3] || 0);
        const acc = String(r[4] || '0%').trim();
        const streak = Number(r[5] || 0);
        const last = String(r[6] || '').trim();
        totalQuestionsAll += ans;

        usersList.push({
          username: u,
          displayName: dn,
          totalAnswered: ans,
          totalCorrect: cor,
          accuracy: acc,
          streak: streak,
          lastActive: last
        });
      });

      // เรียงลำดับจาก TotalCorrect มากไปน้อย
      usersList.sort((a, b) => b.totalCorrect - a.totalCorrect);
      const top10 = usersList.slice(0, 10);

      return jsonResponse_({
        success: true,
        totalMembers: usersList.length,
        totalAnsweredAll: totalQuestionsAll,
        leaderboard: top10
      });
    }

    // 5. ดึงข้อความแชทและกระดานสนทนาล่าสุด (Community Messages)
    if (action === 'getCommunityMessages') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      const sheet = ss.getSheetByName('Community_Chat');
      if (!sheet) {
        return jsonResponse_({ success: true, messages: [] });
      }
      const lastRow = sheet.getLastRow();
      if (lastRow < 3) {
        return jsonResponse_({ success: true, messages: [] });
      }

      const rows = sheet.getRange(3, 1, lastRow - 2, 7).getValues();
      const messages = [];

      rows.forEach(r => {
        const mId = String(r[0] || '').trim();
        const text = String(r[4] || '').trim();
        if (!mId && !text) return;
        messages.push({
          id: mId || ('msg_' + Math.random().toString(36).substr(2, 8)),
          timestamp: String(r[1] || new Date().toISOString()),
          username: String(r[2] || 'anonymous'),
          displayName: String(r[3] || 'Anonymous'),
          message: text,
          replyToId: String(r[5] || '').trim(),
          topicTag: String(r[6] || 'ทั่วไป').trim()
        });
      });

      // นำข้อความ 50 ข้อความล่าสุด
      const recent = messages.slice(-50);
      return jsonResponse_({
        success: true,
        count: recent.length,
        messages: recent
      });
    }

    // 6. ดึงข้อมูลจำนวนการยืนยันข้อสอบถูกต้อง (Question Validation Counts)
    if (action === 'getValidationCounts') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      const sheet = ss.getSheetByName('Question_Validation_Counts');
      const counts = {};
      if (sheet) {
        const lastRow = sheet.getLastRow();
        if (lastRow >= 2) {
          const rows = sheet.getRange(2, 1, lastRow - 1, 3).getValues();
          rows.forEach(r => {
            const qId = String(r[0] || '').trim();
            const cnt = Number(r[2] || 0);
            if (qId) {
              counts[qId] = cnt;
            }
          });
        }
      }
      return jsonResponse_({ success: true, counts: counts });
    }

    return jsonResponse_({ success: true, message: 'PLE-CC Quiz API ready.' });
  } catch (err) {
    return jsonResponse_({ success: false, error: err.toString() });
  }
}

function doPost(e) {
  try {
    let data = {};
    if (e && e.postData && e.postData.contents) {
      try {
        data = JSON.parse(e.postData.contents);
      } catch (jsonErr) {
        data = e.parameter || {};
      }
    } else if (e && e.parameter) {
      data = e.parameter;
    }

    const action = data.action || '';

    // ════════════════════════════════════════════════════════════════════════
    // ✏️ อัปเดตและแก้ไขข้อสอบแบบ Real-time (Admin Only) พร้อม Audit Trail
    // ════════════════════════════════════════════════════════════════════════
    if (action === 'updateQuestion') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      const qId = String(data.questionId || '').trim();
      if (!qId || !qId.includes('::')) {
        return jsonResponse_({ success: false, error: 'Question ID รูปแบบไม่ถูกต้อง (ต้องมี SheetName::Row)' });
      }

      const parts = qId.split('::');
      const sheetName = parts[0].trim();
      const rowNum = parseInt(parts[1], 10);

      if (isNaN(rowNum) || rowNum < 3) {
        return jsonResponse_({ success: false, error: 'เลขแถวไม่ถูกต้อง (ต้องเป็นแถวที่ 3 ขึ้นไป): ' + rowNum });
      }

      const targetSheet = findSheetSafely_(ss, sheetName);
      if (!targetSheet) {
        return jsonResponse_({ success: false, error: 'ไม่พบชีตเป้าหมาย: ' + sheetName });
      }

      // ดึงข้อมูลเดิมเพื่อทำ Audit Snapshot
      const lastCol = Math.max(targetSheet.getLastColumn(), 16);
      const oldValues = targetSheet.getRange(rowNum, 1, 1, Math.min(lastCol, 17)).getValues()[0];

      // บันทึกลง Log_Question_Edits (Audit Trail)
      let logSheet = ss.getSheetByName('Log_Question_Edits');
      if (!logSheet) {
        logSheet = ss.insertSheet('Log_Question_Edits');
        logSheet.appendRow([
          "Timestamp (เวลาไทย)", "Editor", "Question ID", "Sheet Name", "Row Number",
          "Old Question", "New Question", "Old Answer", "New Answer",
          "Old Explanation", "New Explanation", "Status"
        ]);
        logSheet.getRange(1, 1, 1, 12).setFontWeight("bold").setBackground("#1e3a8a").setFontColor("#ffffff");
        logSheet.setFrozenRows(1);
      }

      const thaiTimestamp = Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
      const editor = String(data.editorName || 'Admin');
      const newQuestion = String(data.question || '').replace(/\*\*/g, '').trim();
      const newAns = parseInt(data.answer, 10) || 1;
      const newExplanation = String(data.explanation || '').replace(/\*\*/g, '').replace(/<br\s*\/?>/gi, '\n').trim();

      logSheet.appendRow([
        thaiTimestamp,
        editor,
        qId,
        sheetName,
        rowNum,
        String(oldValues[1] || '').substring(0, 200),
        newQuestion.substring(0, 200),
        String(oldValues[8] || ''),
        String(newAns),
        String(oldValues[9] || '').substring(0, 200),
        newExplanation.substring(0, 200),
        "Updated"
      ]);

      // เตรียมข้อมูลเขียนทับลงชีตเป้าหมาย (คอลัมน์ B ถึง P)
      const choices = Array.isArray(data.choices) ? data.choices : [];
      const c1 = String(choices[0] || '').replace(/\*\*/g, '').trim();
      const c2 = String(choices[1] || '').replace(/\*\*/g, '').trim();
      const c3 = String(choices[2] || '').replace(/\*\*/g, '').trim();
      const c4 = String(choices[3] || '').replace(/\*\*/g, '').trim();
      const c5 = String(choices[4] || '').replace(/\*\*/g, '').trim();

      const qImg = String(data.questionImage || '').trim();
      const aImg = String(data.answerImage || '').trim();
      const subtopic = String(data.subtopic || '').replace(/\*\*/g, '').trim();
      const track = String(data.track || '').trim();
      
      // Note: ถ้ามี caseGroupId ให้ผนวกแท็ก [CASE: ...] ลงไปใน Note ด้วย
      let note = String(data.note || '').replace(/\*\*/g, '').trim();
      if (data.caseGroupId) {
        const caseTag = `[CASE: ${data.caseGroupId}${data.caseOrder ? '_Q' + data.caseOrder : ''}]`;
        if (!note.includes('[CASE:')) {
          note = note ? `${note} ${caseTag}` : caseTag;
        }
      }

      const examType = String(data.examType || '').trim();
      const examYear = String(data.examYear || '').trim();

      // เขียนทับคอลัมน์ B ถึง P (15 คอลัมน์: col 2 ถึง 16)
      const updateData = [
        newQuestion,      // Col B (2)
        qImg,             // Col C (3)
        c1,               // Col D (4)
        c2,               // Col E (5)
        c3,               // Col F (6)
        c4,               // Col G (7)
        c5,               // Col H (8)
        newAns,           // Col I (9)
        newExplanation,   // Col J (10)
        aImg,             // Col K (11)
        subtopic,         // Col L (12)
        track,            // Col M (13)
        note,             // Col N (14)
        examType,         // Col O (15)
        examYear          // Col P (16)
      ];

      targetSheet.getRange(rowNum, 2, 1, 15).setValues([updateData]);

      // ถ้ามีการแก้ไขเลขข้อ (ItemNo) ในคอลัมน์ A
      if (data.itemNo != null && String(data.itemNo).trim() !== '') {
        const itemNo = parseInt(data.itemNo, 10);
        if (!isNaN(itemNo)) {
          targetSheet.getRange(rowNum, 1).setValue(itemNo);
        }
      }

      // ถ้าเป็นชีต Quick Ingestion (📥) และมีส่ง categoryTag
      if (isIngestionSheet_(sheetName) && data.categoryTag) {
        targetSheet.getRange(rowNum, 17).setValue(String(data.categoryTag).trim());
      }

      return jsonResponse_({
        success: true,
        message: `บันทึกข้อสอบลง Google Sheet แถวที่ ${rowNum} สำเร็จแล้ว`,
        questionId: qId,
        sheet: sheetName,
        row: rowNum
      });
    }

    // ════════════════════════════════════════════════════════════════════════
    // ➕ เพิ่มข้อสอบใหม่ลงในหมวดหมู่เป้าหมาย (Admin Only)
    // ════════════════════════════════════════════════════════════════════════
    if (action === 'addQuestion') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      const sheetName = String(data.sheetName || '').trim();
      if (!sheetName) {
        return jsonResponse_({ success: false, error: 'กรุณาระบุชื่อชีต / หมวดวิชาเป้าหมาย' });
      }

      const targetSheet = findSheetSafely_(ss, sheetName);
      if (!targetSheet) {
        return jsonResponse_({ success: false, error: 'ไม่พบชีตเป้าหมาย: ' + sheetName });
      }

      // คำนวณแถวใหม่และเลขข้อ
      const nextRow = targetSheet.getLastRow() + 1;
      let nextItemNo = 1;
      if (nextRow > 3) {
        const lastItemVal = targetSheet.getRange(nextRow - 1, 1).getValue();
        const parsed = parseInt(lastItemVal, 10);
        nextItemNo = isNaN(parsed) ? (nextRow - 2) : (parsed + 1);
      }
      if (data.itemNo != null && String(data.itemNo).trim() !== '') {
        const customItemNo = parseInt(data.itemNo, 10);
        if (!isNaN(customItemNo)) nextItemNo = customItemNo;
      }

      const choices = Array.isArray(data.choices) ? data.choices : [];
      const c1 = String(choices[0] || '').replace(/\*\*/g, '').trim();
      const c2 = String(choices[1] || '').replace(/\*\*/g, '').trim();
      const c3 = String(choices[2] || '').replace(/\*\*/g, '').trim();
      const c4 = String(choices[3] || '').replace(/\*\*/g, '').trim();
      const c5 = String(choices[4] || '').replace(/\*\*/g, '').trim();

      const newQuestion = String(data.question || '').replace(/\*\*/g, '').trim();
      const qImg = String(data.questionImage || '').trim();
      const aImg = String(data.answerImage || '').trim();
      const newAns = parseInt(data.correctAnswer || data.answer, 10) || 1;
      const newExplanation = String(data.explanation || '').replace(/\*\*/g, '').replace(/<br\s*\/?>/gi, '\n').trim();

      const subtopic = String(data.subtopic || '').replace(/\*\*/g, '').trim();
      const track = String(data.track || '').trim();

      let note = String(data.note || '').replace(/\*\*/g, '').trim();
      if (data.caseGroupId) {
        const caseTag = `[CASE: ${data.caseGroupId}${data.caseOrder ? '_Q' + data.caseOrder : ''}]`;
        if (!note.includes('[CASE:')) {
          note = note ? `${note} ${caseTag}` : caseTag;
        }
      }

      const examType = String(data.examType || '').trim();
      const examYear = String(data.examYear || '').trim();

      const rowData = [
        nextItemNo,       // Col A (1)
        newQuestion,      // Col B (2)
        qImg,             // Col C (3)
        c1,               // Col D (4)
        c2,               // Col E (5)
        c3,               // Col F (6)
        c4,               // Col G (7)
        c5,               // Col H (8)
        newAns,           // Col I (9)
        newExplanation,   // Col J (10)
        aImg,             // Col K (11)
        subtopic,         // Col L (12)
        track,            // Col M (13)
        note,             // Col N (14)
        examType,         // Col O (15)
        examYear          // Col P (16)
      ];

      targetSheet.appendRow(rowData);
      const actualRow = targetSheet.getLastRow();
      const newQId = `${sheetName}::${actualRow}`;

      // บันทึกลง Audit Trail
      let logSheet = ss.getSheetByName('Log_Question_Edits');
      if (logSheet) {
        const thaiTimestamp = Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
        logSheet.appendRow([
          thaiTimestamp,
          String(data.editorName || 'Admin'),
          newQId,
          sheetName,
          actualRow,
          "-",
          newQuestion.substring(0, 200),
          "-",
          String(newAns),
          "-",
          newExplanation.substring(0, 200),
          "Created"
        ]);
      }

      return jsonResponse_({
        success: true,
        message: `เพิ่มข้อสอบใหม่ลงในหมวด ${sheetName} แถวที่ ${actualRow} สำเร็จแล้ว`,
        questionId: newQId,
        sheet: sheetName,
        row: actualRow,
        itemNo: nextItemNo
      });
    }

    // ════════════════════════════════════════════════════════════════════════
    // 🗑️ ลบข้อสอบออกจากชีต (Admin Only) พร้อมบันทึก Snapshot กู้คืนได้
    // ════════════════════════════════════════════════════════════════════════
    if (action === 'deleteQuestion') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      const qId = String(data.questionId || '').trim();
      if (!qId || !qId.includes('::')) {
        return jsonResponse_({ success: false, error: 'Question ID ไม่ถูกต้อง' });
      }

      const parts = qId.split('::');
      const sheetName = parts[0].trim();
      const rowNum = parseInt(parts[1], 10);

      if (isNaN(rowNum) || rowNum < 3) {
        return jsonResponse_({ success: false, error: 'เลขแถวไม่ถูกต้อง (ต้อง >= 3): ' + rowNum });
      }

      const targetSheet = findSheetSafely_(ss, sheetName);
      if (!targetSheet) {
        return jsonResponse_({ success: false, error: 'ไม่พบชีตเป้าหมาย: ' + sheetName });
      }

      // Snapshot ข้อมูลก่อนลบ
      const lastCol = Math.max(targetSheet.getLastColumn(), 16);
      const oldValues = targetSheet.getRange(rowNum, 1, 1, Math.min(lastCol, 17)).getValues()[0];

      let logSheet = ss.getSheetByName('Log_Question_Edits');
      if (logSheet) {
        const thaiTimestamp = Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
        logSheet.appendRow([
          thaiTimestamp,
          String(data.editorName || 'Admin'),
          qId,
          sheetName,
          rowNum,
          String(oldValues[1] || '').substring(0, 200),
          "[DELETED]",
          String(oldValues[8] || ''),
          "-",
          String(oldValues[9] || '').substring(0, 200),
          "-",
          "Deleted"
        ]);
      }

      // ลบแถวออกจากชีต
      targetSheet.deleteRow(rowNum);

      return jsonResponse_({
        success: true,
        message: `ลบข้อสอบรหัส ${qId} ออกจาก Google Sheet สำเร็จแล้ว`,
        questionId: qId,
        sheet: sheetName,
        row: rowNum
      });
    }

    // ════════════════════════════════════════════════════════════════════════
    // 📦 ย้ายข้อสอบข้ามหมวดหมู่ใหญ่ (Move Category / Sheet) (Admin Only)
    // ════════════════════════════════════════════════════════════════════════
    if (action === 'moveQuestion') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      const qId = String(data.questionId || data.sourceQuestionId || '').trim();
      const targetSheetName = String(data.targetSheetName || data.destSheetName || '').trim();

      if (!qId || !qId.includes('::') || !targetSheetName) {
        return jsonResponse_({ success: false, error: 'ข้อมูลสำหรับย้ายหมวดไม่ครบถ้วน' });
      }

      const parts = qId.split('::');
      const sourceSheetName = parts[0].trim();
      const sourceRowNum = parseInt(parts[1], 10);

      if (sourceSheetName === targetSheetName) {
        return jsonResponse_({ success: false, error: 'ชีตปลายทางตรงกับชีตต้นทาง ไม่จำเป็นต้องย้าย' });
      }

      const sourceSheet = findSheetSafely_(ss, sourceSheetName);
      const destSheet = findSheetSafely_(ss, targetSheetName);

      if (!sourceSheet || !destSheet) {
        return jsonResponse_({ success: false, error: 'ไม่พบชีตต้นทางหรือปลายทาง' });
      }

      // อ่านข้อมูลจากชีตต้นทาง
      const lastCol = Math.max(sourceSheet.getLastColumn(), 16);
      const rowValues = sourceSheet.getRange(sourceRowNum, 1, 1, Math.min(lastCol, 17)).getValues()[0];

      // คำนวณ Item No ในชีตปลายทาง
      const destNextRow = destSheet.getLastRow() + 1;
      let destItemNo = 1;
      if (destNextRow > 3) {
        const lastItemVal = destSheet.getRange(destNextRow - 1, 1).getValue();
        const parsed = parseInt(lastItemVal, 10);
        destItemNo = isNaN(parsed) ? (destNextRow - 2) : (parsed + 1);
      }

      // ปรับปรุง Item No สำหรับชีตใหม่
      rowValues[0] = destItemNo;

      // ถ้ามีการส่งข้อมูลแก้ไขล่าสุดมาด้วย ให้ใช้ข้อมูลใหม่
      if (data.question) rowValues[1] = String(data.question).replace(/\*\*/g, '').trim();
      if (data.questionImage != null) rowValues[2] = String(data.questionImage).trim();
      if (Array.isArray(data.choices)) {
        for (let c = 0; c < 5; c++) {
          rowValues[3 + c] = String(data.choices[c] || '').replace(/\*\*/g, '').trim();
        }
      }
      if (data.correctAnswer != null) rowValues[8] = parseInt(data.correctAnswer, 10) || 1;
      if (data.explanation) rowValues[9] = String(data.explanation).replace(/\*\*/g, '').replace(/<br\s*\/?>/gi, '\n').trim();
      if (data.answerImage != null) rowValues[10] = String(data.answerImage).trim();
      if (data.subtopic != null) rowValues[11] = String(data.subtopic).replace(/\*\*/g, '').trim();
      if (data.track != null) rowValues[12] = String(data.track).trim();
      if (data.note != null) rowValues[13] = String(data.note).replace(/\*\*/g, '').trim();
      if (data.examType != null) rowValues[14] = String(data.examType).trim();
      if (data.examYear != null) rowValues[15] = String(data.examYear).trim();

      // เขียนลงชีตปลายทาง
      destSheet.appendRow(rowValues.slice(0, 16));
      const newRowNum = destSheet.getLastRow();
      const newQId = `${targetSheetName}::${newRowNum}`;

      // ลบแถวเดิมออกจากชีตต้นทาง
      sourceSheet.deleteRow(sourceRowNum);

      // บันทึกลง Log_Question_Edits
      let logSheet = ss.getSheetByName('Log_Question_Edits');
      if (logSheet) {
        const thaiTimestamp = Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
        logSheet.appendRow([
          thaiTimestamp,
          String(data.editorName || 'Admin'),
          qId,
          sourceSheetName,
          sourceRowNum,
          String(rowValues[1] || '').substring(0, 100),
          `[MOVED to ${newQId}]`,
          "-",
          "-",
          "-",
          `Moved from ${sourceSheetName}::${sourceRowNum} to ${newQId}`,
          "Moved"
        ]);
      }

      return jsonResponse_({
        success: true,
        message: `ย้ายข้อสอบจาก ${sourceSheetName} ไปยัง ${targetSheetName} แถวที่ ${newRowNum} สำเร็จแล้ว`,
        oldQuestionId: qId,
        newQuestionId: newQId,
        sheet: targetSheetName,
        row: newRowNum,
        itemNo: destItemNo
      });
    }

    // บันทึกรายงานข้อสอบผิดพลาด
    if (action === 'reportIssue') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      let sheet = ss.getSheetByName('Report_Quiz_Issues');
      if (!sheet) {
        sheet = ss.insertSheet('Report_Quiz_Issues');
        sheet.appendRow([
          "Timestamp (เวลาไทย)", "User", "Category", "Question ID", "Question Text",
          "Issue Type", "Detail", "Status"
        ]);
        sheet.getRange(1, 1, 1, 8).setFontWeight("bold").setBackground("#991b1b").setFontColor("#ffffff");
        sheet.setFrozenRows(1);
      }

      const thaiTimestamp = data.timestamp || Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
      sheet.appendRow([
        thaiTimestamp,
        String(data.user || 'Anonymous'),
        String(data.category || ''),
        String(data.questionId || ''),
        String(data.question || '').substring(0, 150),
        String(data.issueType || 'ทั่วไป'),
        String(data.detail || ''),
        "Pending (รอดำเนินการ)"
      ]);

      return jsonResponse_({ success: true, message: 'บันทึกรายงานปัญหาเรียบร้อย' });
    }

    // บันทึกการยืนยันข้อสอบถูกต้อง (Question Validation / Upvote)
    if (action === 'validateQuestion') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      let sheet = ss.getSheetByName('Log_Question_Validations');
      if (!sheet) {
        sheet = ss.insertSheet('Log_Question_Validations');
        sheet.appendRow([
          "Timestamp (เวลาไทย)", "User", "Category", "Question ID", "Question Text"
        ]);
        sheet.getRange(1, 1, 1, 5).setFontWeight("bold").setBackground("#059669").setFontColor("#ffffff");
        sheet.setFrozenRows(1);
      }

      const thaiTimestamp = data.timestamp || Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
      const qId = String(data.questionId || '').trim();
      sheet.appendRow([
        thaiTimestamp,
        String(data.user || 'Anonymous'),
        String(data.category || ''),
        qId,
        String(data.question || '').substring(0, 150)
      ]);

      // อัปเดตชีตสรุปยอด Validate สะสมต่อข้อ (Question_Validation_Counts)
      let countSheet = ss.getSheetByName('Question_Validation_Counts');
      if (!countSheet) {
        countSheet = ss.insertSheet('Question_Validation_Counts');
        countSheet.appendRow(["Question ID", "Category", "Validation Count", "Last Validated"]);
        countSheet.getRange(1, 1, 1, 4).setFontWeight("bold").setBackground("#047857").setFontColor("#ffffff");
        countSheet.setFrozenRows(1);
      }

      let newCount = 1;
      const lastRow = countSheet.getLastRow();
      let foundRow = -1;
      if (lastRow >= 2) {
        const ids = countSheet.getRange(2, 1, lastRow - 1, 1).getValues();
        for (let i = 0; i < ids.length; i++) {
          if (String(ids[i][0]).trim() === qId) {
            foundRow = i + 2;
            break;
          }
        }
      }

      if (foundRow > 0) {
        const curCount = Number(countSheet.getRange(foundRow, 3).getValue()) || 0;
        newCount = curCount + 1;
        countSheet.getRange(foundRow, 3).setValue(newCount);
        countSheet.getRange(foundRow, 4).setValue(thaiTimestamp);
      } else {
        countSheet.appendRow([qId, String(data.category || ''), 1, thaiTimestamp]);
        newCount = 1;
      }

      return jsonResponse_({ success: true, count: newCount, message: 'บันทึกการยืนยันข้อสอบถูกต้องเรียบร้อย' });
    }

    // บันทึกสถิติการทำข้อสอบ (Exam Log)
    if (action === 'submitQuizResult') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      let sheet = ss.getSheetByName('Log_Quiz_Results');
      if (!sheet) {
        sheet = ss.insertSheet('Log_Quiz_Results');
        sheet.appendRow([
          "Timestamp (เวลาไทย)", "User", "Category/Mode", "Score", "Total",
          "Percentage", "TimeSpentSeconds"
        ]);
        sheet.getRange(1, 1, 1, 7).setFontWeight("bold").setBackground("#0E7490").setFontColor("#ffffff");
        sheet.setFrozenRows(1);
      }

      const thaiLogTime = Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
      sheet.appendRow([
        thaiLogTime,
        String(data.user || 'Anonymous'),
        String(data.category || 'All'),
        Number(data.score || 0),
        Number(data.total || 0),
        Number(data.percentage || 0) + '%',
        Number(data.timeSpent || 0)
      ]);

      return jsonResponse_({ success: true, message: 'บันทึกผลการทำข้อสอบเรียบร้อย' });
    }

    // ซิงค์โปรไฟล์และคะแนนสะสมของผู้ใช้ (User Profile & Leaderboard)
    if (action === 'syncUserProfile') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      let sheet = ss.getSheetByName('User_Profiles');
      if (!sheet) {
        return jsonResponse_({ success: false, error: 'User_Profiles sheet not found' });
      }

      const u = String(data.username || '').trim().toLowerCase();
      if (!u) return jsonResponse_({ success: false, error: 'Username required' });
      const dn = String(data.displayName || u).trim();
      const track = String(data.track || 'Clinic').trim();
      const totalAns = Number(data.totalAnswered != null ? data.totalAnswered : (data.answeredCount || 0));
      const totalCor = Number(data.totalCorrect != null ? data.totalCorrect : (data.correctCount || 0));
      const accPct = totalAns > 0 ? Math.round((totalCor / totalAns) * 100) + '%' : (data.accuracy ? String(data.accuracy) + '%' : '0%');

      const lastRow = sheet.getLastRow();
      let userRowIdx = -1;
      let existingStreak = 1;

      if (lastRow >= 3) {
        // Read Column A (Username)
        const usernames = sheet.getRange(3, 1, lastRow - 2, 1).getValues();
        for (let i = 0; i < usernames.length; i++) {
          if (String(usernames[i][0] || '').toLowerCase() === u) {
            userRowIdx = i + 3;
            try {
              existingStreak = Number(sheet.getRange(userRowIdx, 6).getValue()) || 1;
            } catch(e) {}
            break;
          }
        }
      }

      const nowIso = new Date().toISOString();
      if (userRowIdx > 0) {
        // Update B to G (Display Name, Total Answered, Total Correct, Accuracy, Streak, Last Active)
        sheet.getRange(userRowIdx, 2, 1, 6).setValues([[
          dn,
          totalAns,
          totalCor,
          accPct,
          existingStreak,
          nowIso
        ]]);
      } else {
        sheet.appendRow([
          u,
          dn,
          totalAns,
          totalCor,
          accPct,
          1,
          nowIso
        ]);
      }

      return jsonResponse_({ success: true, message: 'ซิงค์ข้อมูลโปรไฟล์เรียบร้อย' });
    }

    // บันทึกข้อความแชท Community ใหม่
    if (action === 'postCommunityMessage') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      let sheet = ss.getSheetByName('Community_Chat');
      if (!sheet) {
        return jsonResponse_({ success: false, error: 'Community_Chat sheet not found' });
      }

      const msg = String(data.message || '').trim();
      if (!msg) return jsonResponse_({ success: false, error: 'Message cannot be empty' });

      const msgId = 'msg_' + Date.now();
      const u = String(data.username || 'anonymous').trim();
      const dn = String(data.displayName || 'Anonymous').trim();
      const rep = String(data.replyToId || '').trim();
      const tag = String(data.categoryTag || data.topicTag || 'ทั่วไป').trim();

      sheet.appendRow([
        msgId,
        new Date().toISOString(),
        u,
        dn,
        msg,
        rep,
        tag
      ]);

      return jsonResponse_({
        success: true,
        message: 'ส่งข้อความเรียบร้อย',
        messageId: msgId
      });
    }

    return jsonResponse_({ success: false, error: 'Unknown action: ' + action });
  } catch (err) {
    return jsonResponse_({ success: false, error: err.toString() });
  }
}

function findSheetSafely_(ss, sheetName) {
  if (!sheetName) return null;
  const direct = ss.getSheetByName(sheetName);
  if (direct) return direct;
  
  const allSheets = ss.getSheets();
  const cleanName = String(sheetName).trim().toLowerCase();
  
  // 1. Try matching by exact number prefix (e.g. "1." or "12.")
  const prefixMatch = cleanName.match(/^(\d+)\./);
  if (prefixMatch) {
    const numPrefix = prefixMatch[1] + '.';
    const match = allSheets.find(s => s.getName().trim().toLowerCase().startsWith(numPrefix));
    if (match) return match;
  }
  
  // 2. Try substring match
  const subMatch = allSheets.find(s => {
    const sn = s.getName().trim().toLowerCase();
    return sn.includes(cleanName) || cleanName.includes(sn);
  });
  if (subMatch) return subMatch;
  
  return null;
}

function jsonResponse_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}

/**
 * ดึง Image URL อย่างฉลาด (รองรับทั้ง Object CellImage, URL ตรง, และ In-Cell Image Map จาก XLSX)
 */
function resolveImageUrl_(val, sheetName, rowNum, colIdx, inCellImages) {
  if (!val) return (inCellImages && inCellImages[sheetName + '_r' + rowNum + '_c' + colIdx]) || '';
  
  // 1. ถ้าเป็น CellImage Object ใน Google Apps Script
  if (typeof val === 'object') {
    try {
      if (val.getContentUrl) {
        const directUrl = val.getContentUrl();
        if (directUrl) return directUrl;
      }
      if (val.getUrl) {
        const u = val.getUrl();
        if (u) return u;
      }
    } catch(e) {}
    return (inCellImages && inCellImages[sheetName + '_r' + rowNum + '_c' + colIdx]) || '';
  }

  const sVal = String(val).trim();
  if (sVal === 'CellImage') {
    return (inCellImages && inCellImages[sheetName + '_r' + rowNum + '_c' + colIdx]) || '';
  }

  // 2. ถ้าเป็น URL หรือ Path หรือ Base64 ตรง
  if (sVal.indexOf('http') === 0 || sVal.indexOf('data:image/') === 0 || sVal.indexOf('images/') === 0 || sVal.indexOf('drive.google') !== -1) {
    return sVal;
  }

  return (inCellImages && inCellImages[sheetName + '_r' + rowNum + '_c' + colIdx]) || '';
}

/**
 * ดึง In-Cell Images Map พร้อมแคชใน CacheService (อายุ 6 ชั่วโมง)
 */
function getCachedInCellImages_() {
  const cache = CacheService.getScriptCache();
  const cachedJson = cache.get('quiz_in_cell_images_map');
  if (cachedJson) {
    try { return JSON.parse(cachedJson); } catch(e) {}
  }

  const freshMap = extractInCellImagesFromXlsx_();
  try {
    cache.put('quiz_in_cell_images_map', JSON.stringify(freshMap), 21600); // 6 hours
  } catch(e) {
    // ถ้าขนาดข้อมูลใหญ่เกินแคช ให้ข้าม
  }
  return freshMap;
}

/**
 * สกัดภาพที่แทรกในเซลล์ทั้งหมดผ่าน XLSX Stream
 */
function extractInCellImagesFromXlsx_() {
  const imagesMap = {};
  try {
    const ss = SpreadsheetApp.getActiveSpreadsheet();
    const url = 'https://docs.google.com/spreadsheets/d/' + ss.getId() + '/export?format=xlsx';
    const res = UrlFetchApp.fetch(url, {
      headers: { 'Authorization': 'Bearer ' + ScriptApp.getOAuthToken() },
      muteHttpExceptions: true
    });
    if (res.getResponseCode() !== 200) return imagesMap;

    const zipBlobs = Utilities.unzip(res.getBlob().setContentType('application/zip'));
    const zipMap = {};
    for (let i = 0; i < zipBlobs.length; i++) zipMap[zipBlobs[i].getName()] = zipBlobs[i];

    const sheetFilesMap = {};
    if (zipMap['xl/workbook.xml'] && zipMap['xl/_rels/workbook.xml.rels']) {
      const wbDoc = XmlService.parse(zipMap['xl/workbook.xml'].getDataAsString());
      const wbRelsDoc = XmlService.parse(zipMap['xl/_rels/workbook.xml.rels'].getDataAsString());
      const sheets = wbDoc.getRootElement().getDescendants();
      const rIdToName = {};
      for (let i = 0; i < sheets.length; i++) {
        const el = sheets[i].asElement();
        if (el && el.getName() === 'sheet') {
          rIdToName[el.getAttribute('id', el.getNamespace('r')).getValue()] = el.getAttribute('name').getValue();
        }
      }
      const rels = wbRelsDoc.getRootElement().getDescendants();
      for (let i = 0; i < rels.length; i++) {
        const el = rels[i].asElement();
        if (el && el.getName() === 'Relationship') {
          const rId = el.getAttribute('Id').getValue();
          if (rIdToName[rId]) sheetFilesMap[el.getAttribute('Target').getValue()] = rIdToName[rId];
        }
      }
    }

    const drawingToSheet = {};
    for (const path in zipMap) {
      if (path.indexOf('xl/worksheets/_rels/') === 0 && path.indexOf('.rels') !== -1) {
        const sheetXmlPath = 'worksheets/' + path.replace('xl/worksheets/_rels/', '').replace('.rels', '');
        const sheetName = sheetFilesMap[sheetXmlPath];
        if (!sheetName) continue;
        const relsDoc = XmlService.parse(zipMap[path].getDataAsString());
        const rels = relsDoc.getRootElement().getDescendants();
        for (let i = 0; i < rels.length; i++) {
          const el = rels[i].asElement();
          if (el && el.getName() === 'Relationship') {
            const target = el.getAttribute('Target').getValue();
            if (target.indexOf('drawing') !== -1) drawingToSheet[target.split('/').pop()] = sheetName;
          }
        }
      }
    }

    for (const dName in drawingToSheet) {
      const sheetName = drawingToSheet[dName];
      const dPath = 'xl/drawings/' + dName;
      const dRelsPath = 'xl/drawings/_rels/' + dName + '.rels';
      if (!zipMap[dPath] || !zipMap[dRelsPath]) continue;

      const dRelsDoc = XmlService.parse(zipMap[dRelsPath].getDataAsString());
      const dRels = dRelsDoc.getRootElement().getDescendants();
      const mediaMap = {};
      for (let i = 0; i < dRels.length; i++) {
        const el = dRels[i].asElement();
        if (el && el.getName() === 'Relationship') {
          mediaMap[el.getAttribute('Id').getValue()] = 'xl/' + el.getAttribute('Target').getValue().replace('../', '');
        }
      }

      const dDoc = XmlService.parse(zipMap[dPath].getDataAsString());
      const anchors = dDoc.getRootElement().getChildren();
      for (let i = 0; i < anchors.length; i++) {
        let col = null, row = null, embedId = null;
        const descendants = anchors[i].getDescendants();
        for (let j = 0; j < descendants.length; j++) {
          const el = descendants[j].asElement();
          if (!el) continue;
          if (el.getName() === 'col' && col === null) col = parseInt(el.getText(), 10);
          else if (el.getName() === 'row' && row === null) row = parseInt(el.getText(), 10) + 1;
          else if (el.getName() === 'blip') {
            const attr = el.getAttribute('embed', el.getNamespace('r'));
            if (attr) embedId = attr.getValue();
          }
        }
        if (col !== null && row !== null && embedId && mediaMap[embedId]) {
          const blob = zipMap[mediaMap[embedId]];
          if (blob) {
            imagesMap[sheetName + '_r' + row + '_c' + col] = 'data:' + (blob.getContentType() || 'image/png') + ';base64,' + Utilities.base64Encode(blob.getBytes());
          }
        }
      }
    }
  } catch (err) {
    Logger.log('In-cell error: ' + err);
  }
  return imagesMap;
}

