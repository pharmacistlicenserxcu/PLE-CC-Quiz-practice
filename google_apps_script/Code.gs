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
    .addSeparator()
    .addItem('🤖 ตั้งค่าชีตรายงานปัญหา (Setup Report_Quiz_Issues)', 'setupReportIssuesSheet')
    .addItem('🔑 กดที่นี่เพื่ออนุญาตสิทธิ์และทดสอบ AI (Authorize & Test Gemini)', 'testGeminiConnectionManual')
    .addItem('⚡ ประมวลผล AI ข้อที่ยังค้างอยู่ (Process Pending Reports)', 'processPendingReports')
    .addItem('✅ อนุมัติข้อที่เลือกทั้งหมดลงชีตจริง (Apply All Approved Reports)', 'applyAllApprovedReports')
    .addToUi();
}

/**
 * onEdit — ดักจับเหตุการณ์การเลือก Dropdown สถานะในชีต Report_Quiz_Issues
 * เมื่อเลือก "✅ อนุมัติ (Approved)" จะนำข้อมูลไปอัปเดตลงชีตข้อสอบจริงทันที
 */
function onEdit(e) {
  if (!e || !e.range) return;
  try {
    const sheet = e.range.getSheet();
    if (!sheet || sheet.getName() !== 'Report_Quiz_Issues') return;

    const startCol = e.range.getColumn();
    const endCol = startCol + e.range.getNumColumns() - 1;
    // คอลัมน์ 17 คือ Status (สถานะการอนุมัติ)
    if (startCol > 17 || endCol < 17) return;

    const startRow = Math.max(2, e.range.getRow());
    const numRows = e.range.getNumRows();

    for (let r = 0; r < numRows; r++) {
      const currentRow = startRow + r;
      const statusVal = String(sheet.getRange(currentRow, 17).getValue() || '').trim();
      if (statusVal.includes('อนุมัติ') || statusVal.includes('Approved')) {
        applyReportIssueApproved(currentRow);
      }
    }
  } catch (err) {
    Logger.log('onEdit error: ' + err.toString());
  }
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
  sheet.getRange('A1:S1').merge()
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
    'หัวข้อโรคสภาฯ (Topic)',
    'หัวข้อย่อย (Subtopic)',
    'Product / Clinic (Track)',
    'หมายเหตุ',
    'ประเภทข้อสอบ',
    'ปี / เลขชุด',
    'Case ID (รหัสเคส)',
    'หมวดวิชา/ชีตปลายทาง ★'   // คอลัมน์ S — Category Tag
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
      .requireValueInList(['ข้อสอบจริง', 'ข้อสอบจำลอง', 'Mock', 'ข้อสอบเก่า', 'แบบฝึกหัด'], true)
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

    // Set Gemini API Key
    if (action === 'setGeminiApiKey') {
      const key = String(params.key || '').trim();
      if (key) {
        PropertiesService.getScriptProperties().setProperty('GEMINI_API_KEY', key);
        return jsonResponse_({ success: true, message: 'บันทึก GEMINI_API_KEY ใน Script Properties เรียบร้อย' });
      }
      return jsonResponse_({ success: false, error: 'ไม่พบ parameter key' });
    }

    // Test Gemini Direct Call
    if (action === 'testGemini') {
      const apiKey = getGeminiApiKey_();
      const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent?key=' + apiKey;
      try {
        const response = UrlFetchApp.fetch(url, {
          method: 'post',
          contentType: 'application/json',
          payload: JSON.stringify({
            contents: [{ parts: [{ text: 'Hello' }] }]
          }),
          muteHttpExceptions: true
        });
        return jsonResponse_({
          apiKeyLen: apiKey ? apiKey.length : 0,
          apiKeyPrefix: apiKey ? apiKey.substring(0, 8) : '',
          status: response.getResponseCode(),
          body: response.getContentText()
        });
      } catch (e) {
        return jsonResponse_({ error: e.toString() });
      }
    }

    // Trigger Process Pending Reports
    if (action === 'processReports') {
      const count = processPendingReportsInternal_();
      return jsonResponse_({ success: true, processedCount: count });
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

        const isIngest = isIngestionSheet_(sName);
        const colMap = resolveSheetColumnMap_(sheet);
        const lastCol = Math.max(sheet.getLastColumn(), 19);
        const values = sheet.getRange(3, 1, lastRow - 2, lastCol).getValues();

        values.forEach((row, idx) => {
          const rowNum = idx + 3;
          const firstVal = String(row[0] || '').trim();
          const itemNo = parseInt(firstVal, 10) || (allQuestions.length + 1);

          const caseContext = colMap.caseContext ? String(row[colMap.caseContext - 1] || '').trim() : '';
          let questionText = colMap.question ? String(row[colMap.question - 1] || '').trim() : '';
          if (!questionText && caseContext) {
            questionText = caseContext;
          }

          const rawQImg = colMap.imgQ ? row[colMap.imgQ - 1] : '';
          const c1 = colMap.c1 ? String(row[colMap.c1 - 1] || '').trim() : '';
          const c2 = colMap.c2 ? String(row[colMap.c2 - 1] || '').trim() : '';
          const c3 = colMap.c3 ? String(row[colMap.c3 - 1] || '').trim() : '';
          const c4 = colMap.c4 ? String(row[colMap.c4 - 1] || '').trim() : '';
          const c5 = colMap.c5 ? String(row[colMap.c5 - 1] || '').trim() : '';
          const answerKey = colMap.answer ? (parseInt(row[colMap.answer - 1], 10) || 1) : 1;
          const explanation = colMap.explanation ? String(row[colMap.explanation - 1] || '').trim() : '';
          const rawAImg = colMap.imgA ? row[colMap.imgA - 1] : '';
          const topic = colMap.topic ? String(row[colMap.topic - 1] || '').trim() : '';
          const subtopic = colMap.subtopic ? String(row[colMap.subtopic - 1] || '').trim() : '';
          const track = colMap.track ? String(row[colMap.track - 1] || '').trim() : '';
          const note = colMap.note ? String(row[colMap.note - 1] || '').trim() : '';
          const examType = colMap.examType ? String(row[colMap.examType - 1] || '').trim() : '';
          const examYear = colMap.examYear ? String(row[colMap.examYear - 1] || '').trim() : '';
          const caseIdRaw = colMap.caseId ? String(row[colMap.caseId - 1] || '').trim() : '';

          let category = sName;
          if (isIngest) {
            const categoryTag = colMap.caseId && row[colMap.caseId] ? String(row[colMap.caseId] || '').trim() : '';
            category = categoryTag || topic || sName;
          }

          if (!questionText && !c1) return;

          const questionImg = resolveImageUrl_(rawQImg, sName, rowNum, colMap.imgQ, inCellImages);
          const answerImg = resolveImageUrl_(rawAImg, sName, rowNum, colMap.imgA, inCellImages);

          const choices = [c1, c2, c3, c4];
          if (c5) choices.push(c5);

          let caseGroupId = '';
          let caseOrder = 0;
          let caseType = '';
          if (caseIdRaw && caseIdRaw.toLowerCase() !== 'null' && caseIdRaw !== '-') {
            const rawTrim = caseIdRaw.trim();
            if (/^CASE[_\-]/i.test(rawTrim) || /^\[CASE:/i.test(rawTrim)) {
              const cleanCase = rawTrim.replace(/^\[CASE:\s*/i, '').replace(/\]$/, '').replace(/\s+/g, '').toUpperCase();
              const mQ = cleanCase.match(/^(.*?)(?:[_\-]Q(\d+))?$/i);
              if (mQ && mQ[2]) {
                caseGroupId = mQ[1];
                caseOrder = parseInt(mQ[2], 10);
              } else {
                caseGroupId = cleanCase;
                caseOrder = 0;
              }
              if (caseGroupId.includes('_INT_') || caseGroupId.startsWith('CASE_INT') || caseGroupId.startsWith('CASE-INT')) {
                caseType = 'INT';
              } else if (caseGroupId.includes('_CLN_') || caseGroupId.startsWith('CASE_CLN') || caseGroupId.startsWith('CASE-CLN')) {
                caseType = 'CLN';
              } else if (caseGroupId.includes('_PRD_') || caseGroupId.startsWith('CASE_PRD') || caseGroupId.startsWith('CASE-PRD')) {
                caseType = 'PRD';
              } else if (caseGroupId.includes('_SAP_') || caseGroupId.startsWith('CASE_SAP') || caseGroupId.startsWith('CASE-SAP')) {
                caseType = 'SAP';
              } else {
                caseType = 'STD';
              }
            }
          }

          allQuestions.push({
            id: sName + '::' + rowNum,
            itemNo: itemNo,
            category: category,
            topic: topic || category,
            subtopic: subtopic || topic || category,
            track: track || 'Clinic',
            caseContext: caseContext,
            caseStem: caseContext,
            question: questionText,
            questionImage: questionImg,
            choices: choices,
            answer: answerKey,
            explanation: explanation,
            answerImage: answerImg,
            note: note,
            examType: examType,
            examYear: examYear,
            caseGroupId: caseGroupId,
            caseOrder: caseOrder,
            caseType: caseType,
            fromIngestion: isIngest
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

      const colMap = resolveSheetColumnMap_(targetSheet);
      const lastCol = Math.max(targetSheet.getLastColumn(), 19);
      const oldValues = targetSheet.getRange(rowNum, 1, 1, lastCol).getValues()[0];

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
      const newCaseContext = String(data.caseContext || data.caseStem || '').replace(/\*\*/g, '').trim();
      const newQuestion = String(data.question || '').replace(/\*\*/g, '').trim();
      const newAns = parseInt(data.correctAnswer != null ? data.correctAnswer : data.answer, 10) || 1;
      const newExplanation = String(data.explanation || '').replace(/\*\*/g, '').replace(/<br\s*\/?>/gi, '\n').trim();

      logSheet.appendRow([
        thaiTimestamp,
        editor,
        qId,
        sheetName,
        rowNum,
        String(oldValues[colMap.question - 1] || '').substring(0, 200),
        newQuestion.substring(0, 200),
        String(oldValues[colMap.answer - 1] || ''),
        String(newAns),
        String(oldValues[colMap.explanation - 1] || '').substring(0, 200),
        newExplanation.substring(0, 200),
        "Updated"
      ]);

      const choices = Array.isArray(data.choices) ? data.choices : [];
      const cleanChoices = choices.map(c => String(c || '').replace(/\*\*/g, '').trim());

      let qImg = String(data.questionImage || '').trim();
      let aImg = String(data.answerImage || '').trim();

      if (qImg.startsWith('data:image/')) {
        qImg = saveBase64ImageToDrive_(qImg, sheetName, rowNum, 'Q');
      }
      if (aImg.startsWith('data:image/')) {
        aImg = saveBase64ImageToDrive_(aImg, sheetName, rowNum, 'A');
      }

      const qImgCellValue = (qImg && qImg.startsWith('http')) ? `=IMAGE("${qImg}")` : qImg;
      const aImgCellValue = (aImg && aImg.startsWith('http')) ? `=IMAGE("${aImg}")` : aImg;

      const subtopic = String(data.subtopic || '').replace(/\*\*/g, '').trim();
      const track = String(data.track || '').trim();

      let note = String(data.note || '').replace(/\*\*/g, '').trim();
      if (data.caseGroupId) {
        const caseTag = `[CASE: ${data.caseGroupId}${data.caseOrder ? '_Q' + data.caseOrder : ''}]`;
        if (!note.includes('[CASE:')) {
          note = note ? `${note} ${caseTag}` : caseTag;
        }
      }

      const topic = String(data.topic || '').trim();
      const examType = String(data.examType || '').trim();
      const examYear = String(data.examYear || '').trim();
      const caseId = String(data.caseId || data.caseGroupId || '').trim();

      const updates = {
        itemNo: (data.itemNo != null && String(data.itemNo).trim() !== '') ? parseInt(data.itemNo, 10) : undefined,
        caseContext: newCaseContext,
        question: newQuestion,
        imgQ: qImgCellValue,
        choices: cleanChoices,
        answer: newAns,
        explanation: newExplanation,
        imgA: aImgCellValue,
        topic: topic,
        subtopic: subtopic,
        track: track,
        note: note,
        examType: examType,
        examYear: examYear,
        caseId: caseId
      };

      applyUpdatesToRowValues_(targetSheet, rowNum, colMap, updates);

      if (qImg && qImg.startsWith('http') && colMap.imgQ) {
        try { targetSheet.getRange(rowNum, colMap.imgQ).setNote(qImg); } catch(e) {}
      }
      if (aImg && aImg.startsWith('http') && colMap.imgA) {
        try { targetSheet.getRange(rowNum, colMap.imgA).setNote(aImg); } catch(e) {}
      }

      return jsonResponse_({
        success: true,
        message: `บันทึกข้อสอบลง Google Sheet แถวที่ ${rowNum} สำเร็จแล้ว`,
        questionId: qId,
        sheet: sheetName,
        row: rowNum,
        questionImage: qImg,
        answerImage: aImg
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
      let qImg = String(data.questionImage || '').trim();
      let aImg = String(data.answerImage || '').trim();

      const nextRowEstimate = targetSheet.getLastRow() + 1;
      if (qImg.startsWith('data:image/')) {
        qImg = saveBase64ImageToDrive_(qImg, sheetName, nextRowEstimate, 'Q');
      }
      if (aImg.startsWith('data:image/')) {
        aImg = saveBase64ImageToDrive_(aImg, sheetName, nextRowEstimate, 'A');
      }

      const qImgCellValue = (qImg && qImg.startsWith('http')) ? `=IMAGE("${qImg}")` : qImg;
      const aImgCellValue = (aImg && aImg.startsWith('http')) ? `=IMAGE("${aImg}")` : aImg;

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

      const colMap = resolveSheetColumnMap_(targetSheet);
      const addData = {
        itemNo: nextItemNo,
        caseContext: String(data.caseContext || data.caseStem || '').replace(/\*\*/g, '').trim(),
        question: newQuestion,
        imgQ: qImgCellValue,
        choices: [c1, c2, c3, c4, c5],
        answer: newAns,
        explanation: newExplanation,
        imgA: aImgCellValue,
        topic: String(data.topic || '').trim(),
        subtopic: subtopic,
        track: track,
        note: note,
        examType: examType,
        examYear: examYear,
        caseId: String(data.caseId || data.caseGroupId || '').trim()
      };

      const rowData = buildRowArrayForSheet_(colMap, addData);
      targetSheet.appendRow(rowData);
      const actualRow = targetSheet.getLastRow();
      const newQId = `${sheetName}::${actualRow}`;

      if (qImg && qImg.startsWith('http')) {
        try { targetSheet.getRange(actualRow, 3).setNote(qImg); } catch(e) {}
      }
      if (aImg && aImg.startsWith('http')) {
        try { targetSheet.getRange(actualRow, 11).setNote(aImg); } catch(e) {}
      }

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
        itemNo: nextItemNo,
        questionImage: qImg,
        answerImage: aImg
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

      const sourceColMap = resolveSheetColumnMap_(sourceSheet);
      const destColMap = resolveSheetColumnMap_(destSheet);

      const oldVals = sourceSheet.getRange(sourceRowNum, 1, 1, Math.max(19, sourceSheet.getLastColumn())).getValues()[0];

      const destNextRow = destSheet.getLastRow() + 1;
      let destItemNo = 1;
      if (destNextRow > 3) {
        const lastItemVal = destSheet.getRange(destNextRow - 1, 1).getValue();
        const parsed = parseInt(lastItemVal, 10);
        destItemNo = isNaN(parsed) ? (destNextRow - 2) : (parsed + 1);
      }

      const choices = Array.isArray(data.choices) ? data.choices : [
        String(oldVals[sourceColMap.c1 - 1] || ''),
        String(oldVals[sourceColMap.c2 - 1] || ''),
        String(oldVals[sourceColMap.c3 - 1] || ''),
        String(oldVals[sourceColMap.c4 - 1] || ''),
        String(oldVals[sourceColMap.c5 - 1] || '')
      ];

      const moveData = {
        itemNo: destItemNo,
        caseContext: data.caseContext != null ? String(data.caseContext) : (sourceColMap.caseContext ? String(oldVals[sourceColMap.caseContext - 1] || '') : ''),
        question: data.question ? String(data.question).replace(/\*\*/g, '').trim() : String(oldVals[sourceColMap.question - 1] || ''),
        imgQ: data.questionImage != null ? String(data.questionImage).trim() : (sourceColMap.imgQ ? String(oldVals[sourceColMap.imgQ - 1] || '') : ''),
        choices: choices.map(c => String(c || '').replace(/\*\*/g, '').trim()),
        answer: (data.correctAnswer != null || data.answer != null) ? parseInt(data.correctAnswer != null ? data.correctAnswer : data.answer, 10) : oldVals[sourceColMap.answer - 1],
        explanation: data.explanation ? String(data.explanation).replace(/\*\*/g, '').replace(/<br\s*\/?>/gi, '\n').trim() : String(oldVals[sourceColMap.explanation - 1] || ''),
        imgA: data.answerImage != null ? String(data.answerImage).trim() : (sourceColMap.imgA ? String(oldVals[sourceColMap.imgA - 1] || '') : ''),
        topic: data.topic != null ? String(data.topic).trim() : (sourceColMap.topic ? String(oldVals[sourceColMap.topic - 1] || '') : ''),
        subtopic: data.subtopic != null ? String(data.subtopic).replace(/\*\*/g, '').trim() : (sourceColMap.subtopic ? String(oldVals[sourceColMap.subtopic - 1] || '') : ''),
        track: data.track != null ? String(data.track).trim() : (sourceColMap.track ? String(oldVals[sourceColMap.track - 1] || '') : ''),
        note: (data.note != null ? String(data.note).replace(/\*\*/g, '').trim() : (sourceColMap.note ? String(oldVals[sourceColMap.note - 1] || '') : '')) + ` [ย้ายจาก ${sourceSheetName}::${sourceRowNum}]`,
        examType: data.examType != null ? String(data.examType).trim() : (sourceColMap.examType ? String(oldVals[sourceColMap.examType - 1] || '') : ''),
        examYear: data.examYear != null ? String(data.examYear).trim() : (sourceColMap.examYear ? String(oldVals[sourceColMap.examYear - 1] || '') : ''),
        caseId: data.caseId != null ? String(data.caseId).trim() : (sourceColMap.caseId ? String(oldVals[sourceColMap.caseId - 1] || '') : '')
      };

      const newRowVals = buildRowArrayForSheet_(destColMap, moveData);
      destSheet.appendRow(newRowVals);
      const newRowNum = destSheet.getLastRow();
      const newQId = `${targetSheetName}::${newRowNum}`;

      try {
        sourceSheet.deleteRow(sourceRowNum);
      } catch (delErr) {
        try {
          sourceSheet.getRange(sourceRowNum, sourceColMap.question).setValue(`[ย้ายไป ${newQId}] ${moveData.question}`);
        } catch (e) {}
      }

      let logSheet = ss.getSheetByName('Log_Question_Edits');
      if (logSheet) {
        const thaiTimestamp = Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
        logSheet.appendRow([
          thaiTimestamp,
          String(data.editorName || 'Admin'),
          qId + ' -> ' + newQId,
          targetSheetName,
          newRowNum,
          String(oldVals[sourceColMap.question - 1] || '').substring(0, 150),
          moveData.question.substring(0, 150),
          String(oldVals[sourceColMap.answer - 1] || ''),
          String(moveData.answer),
          String(oldVals[sourceColMap.explanation - 1] || '').substring(0, 150),
          moveData.explanation.substring(0, 150),
          'Moved to ' + targetSheetName
        ]);
      }

      return jsonResponse_({
        success: true,
        message: `ย้ายข้อสอบไปยังหมวด ${targetSheetName} (แถวที่ ${newRowNum}) สำเร็จแล้ว`,
        oldQuestionId: qId,
        newQuestionId: newQId,
        newRow: newRowNum,
        targetSheet: targetSheetName
      });
    }

    if (action === 'reportIssue') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      let sheet = ss.getSheetByName('Report_Quiz_Issues');
      if (!sheet) {
        sheet = setupReportIssuesSheet();
      }

      const thaiTimestamp = data.timestamp || Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
      const user = String(data.user || 'Anonymous');
      const cat = String(data.category || '').trim();
      const qId = String(data.questionId || '').trim();
      const issueType = String(data.issueType || 'ทั่วไป').trim();
      const detail = String(data.detail || '').trim();

      // ดึงข้อมูลข้อสอบเดิมจากชีตวิชาหรือจาก payload
      let originalQ = {
        caseContext: String(data.caseContext || data.caseStem || ''),
        question: String(data.question || ''),
        choices: Array.isArray(data.choices) ? data.choices : [],
        answer: data.answer || '',
        explanation: String(data.explanation || ''),
        topic: String(data.topic || ''),
        subtopic: String(data.subtopic || ''),
        track: String(data.track || ''),
        caseId: String(data.caseId || '')
      };

      let targetSheetName = cat;
      let targetRowNum = 0;

      if (qId.includes('::')) {
        const parts = qId.split('::');
        targetSheetName = parts[0].trim();
        targetRowNum = parseInt(parts[1], 10);
      }

      if (targetSheetName && targetRowNum >= 3) {
        const targetSheet = findSheetSafely_(ss, targetSheetName);
        if (targetSheet && targetRowNum <= targetSheet.getLastRow()) {
          const colMap = resolveSheetColumnMap_(targetSheet);
          const rowVals = targetSheet.getRange(targetRowNum, 1, 1, Math.max(19, targetSheet.getLastColumn())).getValues()[0];
          
          if (!originalQ.caseContext && colMap.caseContext) originalQ.caseContext = String(rowVals[colMap.caseContext - 1] || '');
          if (!originalQ.question) originalQ.question = String(rowVals[colMap.question - 1] || '');
          if (!originalQ.choices.length) {
            originalQ.choices = [
              String(rowVals[colMap.c1 - 1] || ''),
              String(rowVals[colMap.c2 - 1] || ''),
              String(rowVals[colMap.c3 - 1] || ''),
              String(rowVals[colMap.c4 - 1] || ''),
              String(rowVals[colMap.c5 - 1] || '')
            ].filter(Boolean);
          }
          if (!originalQ.answer) originalQ.answer = rowVals[colMap.answer - 1];
          if (!originalQ.explanation) originalQ.explanation = String(rowVals[colMap.explanation - 1] || '');
          if (!originalQ.topic && colMap.topic) originalQ.topic = String(rowVals[colMap.topic - 1] || '');
          if (!originalQ.subtopic && colMap.subtopic) originalQ.subtopic = String(rowVals[colMap.subtopic - 1] || '');
          if (!originalQ.track && colMap.track) originalQ.track = String(rowVals[colMap.track - 1] || '');
          if (!originalQ.caseId && colMap.caseId) originalQ.caseId = String(rowVals[colMap.caseId - 1] || '');
        }
      }

      // สรุปข้อสอบและเฉลยเดิม
      const currentExamSnippet = 
        (originalQ.caseContext ? 'เคส: ' + originalQ.caseContext.substring(0, 70) + '...\n' : '') +
        'โจทย์: ' + originalQ.question.substring(0, 100) + '\n' +
        'ตัวเลือก: 1.' + (originalQ.choices[0] || '-') + ' | 2.' + (originalQ.choices[1] || '-') + ' | 3.' + (originalQ.choices[2] || '-') + '\n' +
        'เฉลยเดิม: ข้อ ' + (originalQ.answer || '-');

      // เรียก Gemini AI วินิจฉัยข้อสอบครบทุกฟิลด์
      let aiResult = null;
      try {
        aiResult = callGeminiQuizResolver(targetSheetName, qId, originalQ, {
          issueType: issueType,
          detail: detail
        });
      } catch (aiErr) {
        Logger.log('AI resolver call error: ' + aiErr.toString());
      }

      const aiDiagnosis = aiResult ? ('[' + aiResult.verdict + '] ' + aiResult.diagnosis) : 'AI อยู่ระหว่างเตรียมประมวลผล หรือกรุณากดเมนูเพื่อรันย้อนหลัง';
      const aiProposedCase = aiResult ? (aiResult.proposedCaseContext || '') : '';
      const aiProposedQ = aiResult ? (aiResult.proposedQuestion || '') : '';
      const aiProposedChoices = (aiResult && Array.isArray(aiResult.proposedChoices)) ? aiResult.proposedChoices.map((c, i) => `${i+1}. ${c}`).join('\n') : '';
      const aiProposedAns = aiResult ? (aiResult.proposedAnswer || '') : '';
      const aiProposedExp = aiResult ? (aiResult.proposedExplanation || '') : '';
      const aiProposedTargetSheet = aiResult ? (aiResult.proposedTargetSheet || targetSheetName) : targetSheetName;
      const aiProposedTopicSubtopic = aiResult ? ((aiResult.proposedTopic || '') + (aiResult.proposedSubtopic ? ' / ' + aiResult.proposedSubtopic : '')) : '';
      const aiProposedTrack = aiResult ? (aiResult.proposedTrack || '') : '';

      const newRow = [
        thaiTimestamp,           // Col 1
        user,                    // Col 2
        targetSheetName,         // Col 3
        qId,                     // Col 4
        issueType,               // Col 5
        detail,                  // Col 6
        currentExamSnippet,      // Col 7
        aiDiagnosis,             // Col 8
        aiProposedCase,          // Col 9 -> AI Proposed Case Context
        aiProposedQ,             // Col 10 -> AI Proposed Question
        aiProposedChoices,       // Col 11 -> AI Proposed Choices
        aiProposedAns,           // Col 12 -> AI Proposed Answer (1-5)
        aiProposedExp,           // Col 13 -> AI Proposed Explanation
        aiProposedTargetSheet,   // Col 14 -> AI Proposed Target Sheet
        aiProposedTopicSubtopic, // Col 15 -> AI Proposed Topic & Subtopic
        aiProposedTrack,         // Col 16 -> AI Proposed Track
        '⏳ รอประธานอนุมัติ (Pending)', // Col 17 -> Status
        'AI วิเคราะห์ครบทุกฟิลด์สำเร็จ พร้อมให้ประธานตรวจสอบ', // Col 18 -> Log
        JSON.stringify(aiResult || {}) // Col 19 -> Full AI JSON
      ];

      sheet.appendRow(newRow);
      const lastRow = sheet.getLastRow();

      applyStatusValidationToRow_(sheet, lastRow);

      return jsonResponse_({
        success: true,
        message: 'บันทึกรายงานปัญหาและ AI วิเคราะห์ครบทุกฟิลด์เรียบร้อย',
        aiResult: aiResult
      });
    }

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


/**
 * ════════════════════════════════════════════════════════════════════════
 * 🧭 Dynamic Sheet Column Resolver (รองรับทั้ง 19-Column Schema และ Legacy 12/16-Column)
 * ════════════════════════════════════════════════════════════════════════
 */
function resolveSheetColumnMap_(sheet) {
  const map = {
    caseContext: 2,
    question: 3,
    imgQ: 4,
    c1: 5, c2: 6, c3: 7, c4: 8, c5: 9,
    answer: 10,
    explanation: 11,
    imgA: 12,
    topic: 13,
    subtopic: 14,
    track: 15,
    note: 16,
    examType: 17,
    examYear: 18,
    caseId: 19,
    hasSeparateCase: true
  };
  if (!sheet) return map;
  const lastCol = Math.max(20, sheet.getLastColumn());
  const headerVals = sheet.getRange(2, 1, 1, lastCol).getValues()[0];

  let hasSeparateCase = false;
  for (let c = 0; c < headerVals.length; c++) {
    const v = String(headerVals[c] || '').trim();
    if (!v) continue;
    const colNum = c + 1;
    if (v.includes('สถานการณ์') || v.includes('Scenario') || v.includes('ข้อมูลผู้ป่วย')) {
      map.caseContext = colNum;
      hasSeparateCase = true;
    } else if (v.includes('คำถาม') || v.includes('Question')) {
      map.question = colNum;
    } else if (v.includes('รูปถาม') || v.includes('Question Image')) {
      map.imgQ = colNum;
    } else if (v.includes('ตัวเลือก 1') || v.includes('Choice 1')) {
      map.c1 = colNum;
    } else if (v.includes('ตัวเลือก 2') || v.includes('Choice 2')) {
      map.c2 = colNum;
    } else if (v.includes('ตัวเลือก 3') || v.includes('Choice 3')) {
      map.c3 = colNum;
    } else if (v.includes('ตัวเลือก 4') || v.includes('Choice 4')) {
      map.c4 = colNum;
    } else if (v.includes('ตัวเลือก 5') || v.includes('Choice 5')) {
      map.c5 = colNum;
    } else if (v.includes('เฉลย') && (v.includes('ตัวเลข') || v.includes('Answer') || v.includes('Key'))) {
      map.answer = colNum;
    } else if (v.includes('คำอธิบาย') || v.includes('Rationale')) {
      map.explanation = colNum;
    } else if (v.includes('รูปเฉลย') || v.includes('Answer Image')) {
      map.imgA = colNum;
    } else if (v.includes('หัวข้อโรคสภาฯ') || v.includes('Topic')) {
      map.topic = colNum;
    } else if (v.includes('หัวข้อย่อย') || v.includes('Subtopic')) {
      map.subtopic = colNum;
    } else if (v.includes('Track') || v.includes('สายวิชา') || v.includes('Product')) {
      map.track = colNum;
    } else if (v.includes('หมายเหตุ') || v.includes('Note')) {
      map.note = colNum;
    } else if (v.includes('ประเภท') || v.includes('Type')) {
      map.examType = colNum;
    } else if (v.includes('ปี') || v.includes('Year')) {
      map.examYear = colNum;
    } else if (v.includes('Case') || v.includes('รหัสเคส')) {
      map.caseId = colNum;
    }
  }
  map.hasSeparateCase = hasSeparateCase;
  // Fallback สำหรับชีตแบบเก่าที่ไม่มีคอลัมน์สถานการณ์เคสแยก
  if (!hasSeparateCase && headerVals[1] && String(headerVals[1]).includes('คำถาม')) {
    map.caseContext = 0;
    map.question = 2;
    map.imgQ = 3;
    map.c1 = 4; map.c2 = 5; map.c3 = 6; map.c4 = 7; map.c5 = 8;
    map.answer = 9; map.explanation = 10; map.imgA = 11;
    map.topic = 12; map.subtopic = 13; map.track = 14; map.note = 15;
    map.examType = 16; map.examYear = 17; map.caseId = 18;
  }
  return map;
}

function buildRowArrayForSheet_(colMap, data) {
  const maxCol = Math.max(19, colMap.caseId || 19);
  const row = new Array(maxCol).fill('');

  if (data.itemNo != null) row[0] = data.itemNo;
  if (colMap.caseContext && colMap.caseContext > 0) {
    row[colMap.caseContext - 1] = data.caseContext || data.caseStem || '';
  }
  if (colMap.question && colMap.question > 0) {
    row[colMap.question - 1] = data.question || '';
  }
  if (colMap.imgQ && colMap.imgQ > 0) {
    row[colMap.imgQ - 1] = data.imgQ || '';
  }
  const choices = Array.isArray(data.choices) ? data.choices : [];
  if (colMap.c1 && colMap.c1 > 0) row[colMap.c1 - 1] = choices[0] || '';
  if (colMap.c2 && colMap.c2 > 0) row[colMap.c2 - 1] = choices[1] || '';
  if (colMap.c3 && colMap.c3 > 0) row[colMap.c3 - 1] = choices[2] || '';
  if (colMap.c4 && colMap.c4 > 0) row[colMap.c4 - 1] = choices[3] || '';
  if (colMap.c5 && colMap.c5 > 0) row[colMap.c5 - 1] = choices[4] || '';
  if (colMap.answer && colMap.answer > 0) row[colMap.answer - 1] = data.answer || 1;
  if (colMap.explanation && colMap.explanation > 0) row[colMap.explanation - 1] = data.explanation || '';
  if (colMap.imgA && colMap.imgA > 0) row[colMap.imgA - 1] = data.imgA || '';
  if (colMap.topic && colMap.topic > 0) row[colMap.topic - 1] = data.topic || '';
  if (colMap.subtopic && colMap.subtopic > 0) row[colMap.subtopic - 1] = data.subtopic || '';
  if (colMap.track && colMap.track > 0) row[colMap.track - 1] = data.track || '';
  if (colMap.note && colMap.note > 0) row[colMap.note - 1] = data.note || '';
  if (colMap.examType && colMap.examType > 0) row[colMap.examType - 1] = data.examType || '';
  if (colMap.examYear && colMap.examYear > 0) row[colMap.examYear - 1] = data.examYear || '';
  if (colMap.caseId && colMap.caseId > 0) row[colMap.caseId - 1] = data.caseId || '';

  return row;
}

function applyUpdatesToRowValues_(targetSheet, rowNum, colMap, updates) {
  const lastCol = Math.max(19, targetSheet.getLastColumn());
  const existingRow = targetSheet.getRange(rowNum, 1, 1, lastCol).getValues()[0];

  if (updates.itemNo != null && updates.itemNo !== '') existingRow[0] = updates.itemNo;
  if (colMap.caseContext && colMap.caseContext > 0 && updates.caseContext !== undefined) {
    existingRow[colMap.caseContext - 1] = updates.caseContext;
  }
  if (colMap.question && colMap.question > 0 && updates.question !== undefined) {
    existingRow[colMap.question - 1] = updates.question;
  }
  if (colMap.imgQ && colMap.imgQ > 0 && updates.imgQ !== undefined) {
    existingRow[colMap.imgQ - 1] = updates.imgQ;
  }
  if (Array.isArray(updates.choices)) {
    if (colMap.c1 && colMap.c1 > 0 && updates.choices[0] !== undefined) existingRow[colMap.c1 - 1] = updates.choices[0];
    if (colMap.c2 && colMap.c2 > 0 && updates.choices[1] !== undefined) existingRow[colMap.c2 - 1] = updates.choices[1];
    if (colMap.c3 && colMap.c3 > 0 && updates.choices[2] !== undefined) existingRow[colMap.c3 - 1] = updates.choices[2];
    if (colMap.c4 && colMap.c4 > 0 && updates.choices[3] !== undefined) existingRow[colMap.c4 - 1] = updates.choices[3];
    if (colMap.c5 && colMap.c5 > 0 && updates.choices[4] !== undefined) existingRow[colMap.c5 - 1] = updates.choices[4];
  }
  if (colMap.answer && colMap.answer > 0 && updates.answer !== undefined) existingRow[colMap.answer - 1] = updates.answer;
  if (colMap.explanation && colMap.explanation > 0 && updates.explanation !== undefined) existingRow[colMap.explanation - 1] = updates.explanation;
  if (colMap.imgA && colMap.imgA > 0 && updates.imgA !== undefined) existingRow[colMap.imgA - 1] = updates.imgA;
  if (colMap.topic && colMap.topic > 0 && updates.topic !== undefined) existingRow[colMap.topic - 1] = updates.topic;
  if (colMap.subtopic && colMap.subtopic > 0 && updates.subtopic !== undefined) existingRow[colMap.subtopic - 1] = updates.subtopic;
  if (colMap.track && colMap.track > 0 && updates.track !== undefined) existingRow[colMap.track - 1] = updates.track;
  if (colMap.note && colMap.note > 0 && updates.note !== undefined) existingRow[colMap.note - 1] = updates.note;
  if (colMap.examType && colMap.examType > 0 && updates.examType !== undefined) existingRow[colMap.examType - 1] = updates.examType;
  if (colMap.examYear && colMap.examYear > 0 && updates.examYear !== undefined) existingRow[colMap.examYear - 1] = updates.examYear;
  if (colMap.caseId && colMap.caseId > 0 && updates.caseId !== undefined) existingRow[colMap.caseId - 1] = updates.caseId;

  targetSheet.getRange(rowNum, 1, 1, existingRow.length).setValues([existingRow]);
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
 * บันทึกรูปภาพ Base64 ลงใน Google Drive โฟลเดอร์ PLE_Quiz_Images พร้อมตั้งสิทธิ์ Public View
 * คืนค่าเป็น Direct Image URL: https://lh3.googleusercontent.com/d/{fileId}
 */
function saveBase64ImageToDrive_(base64Data, sheetName, rowNum, prefix) {
  if (!base64Data) return '';
  const s = String(base64Data).trim();
  if (!s.startsWith('data:image/')) {
    return s;
  }

  try {
    const parts = s.split(',');
    if (parts.length < 2) return '';
    const header = parts[0];
    const rawBase64 = parts[1];
    const mimeMatch = header.match(/:(.*?);/);
    const mimeType = mimeMatch ? mimeMatch[1] : 'image/jpeg';
    const ext = (mimeType.split('/')[1] || 'jpg').replace('jpeg', 'jpg');
    const bytes = Utilities.base64Decode(rawBase64);
    const fileName = `PLE_${prefix}_${sheetName.replace(/[^\w]/g, '_')}_R${rowNum}_${Date.now()}.${ext}`;
    const blob = Utilities.newBlob(bytes, mimeType, fileName);

    let folder = null;
    const folderName = 'PLE_Quiz_Images';
    const iter = DriveApp.getFoldersByName(folderName);
    if (iter.hasNext()) {
      folder = iter.next();
    } else {
      folder = DriveApp.createFolder(folderName);
      try {
        folder.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
      } catch(e) {}
    }

    const file = folder.createFile(blob);
    try {
      file.setSharing(DriveApp.Access.ANYONE_WITH_LINK, DriveApp.Permission.VIEW);
    } catch(e) {}

    const fileId = file.getId();
    return `https://lh3.googleusercontent.com/d/${fileId}`;
  } catch(err) {
    console.error('Error saving image to Drive:', err);
    return '';
  }
}

/**
 * ดึง Image URL อย่างฉลาด (รองรับทั้ง Object CellImage, สูตร IMAGE, URL ตรง, และ In-Cell Image Map จาก XLSX)
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

  // 1.5 ถ้าเป็นสูตร =IMAGE("...") หรือ IMAGE("...")
  if (sVal.toUpperCase().indexOf('IMAGE(') !== -1) {
    const m = sVal.match(/IMAGE\(\s*["']([^"']+)["']/i);
    if (m && m[1]) return m[1];
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



// ────────────────────────────────────────────────────────────────────────────
// AI QUIZ REPORT AUTO-RESOLVER & ONE-CLICK APPROVAL SYSTEM
// ────────────────────────────────────────────────────────────────────────────

function getGeminiApiKey_() {
  try {
    const propKey = PropertiesService.getScriptProperties().getProperty('GEMINI_API_KEY');
    if (propKey && propKey.trim()) return propKey.trim();
  } catch (e) {}
  return '';
}

function callGeminiQuizResolver(category, questionId, originalQ, studentReport) {
  const apiKey = getGeminiApiKey_();
  if (!apiKey) {
    Logger.log('callGeminiQuizResolver: GEMINI_API_KEY is not set');
    return null;
  }

  const candidateModels = [
    'gemini-2.0-flash',
    'gemini-1.5-flash',
    'gemini-2.5-flash',
    'gemini-1.5-pro'
  ];

  const systemInstruction = `คุณเป็นประธานและเภสัชกรผู้เชี่ยวชาญ คณะกรรมการเตรียมสอบใบประกอบวิชาชีพเภสัชกรรม (PLE-CC)
หน้าที่ของคุณคือ ตรวจสอบและแก้ไขรายงานปัญหาข้อสอบที่นิสิตส่งเข้ามาแบบครบวงจร (Full-Scope Diagnostic & Revision) ทั้งสถานการณ์เคส, ประโยคคำถาม, ตัวเลือกทั้ง 5 ข้อ, เฉลย, คำอธิบายเฉลย, หมวดวิชา/ชีตที่ถูกต้อง, หัวข้อโรคสภาฯ, หัวข้อย่อย และสายวิชา

กฎเหล็กมาตรฐานสภาเภสัชกรรม (Mandatory Blueprint Rules):
1. การแยกสถานการณ์เคสและประโยคคำถาม (Case Scenario & Question Prompt Separation):
   - หากโจทย์มีประวัติคนไข้/ผลแล็บ/ข้อมูลตำรับ/บริบทเคสผู้ป่วย ให้แยกข้อมูลเคสทั้งหมดใส่ใน proposedCaseContext
   - ใน proposedQuestion ให้ใส่เฉพาะ 'ประโยคคำถามเฉพาะข้อ' ที่ชัดเจน สละสลวย ตรงประเด็น (ห้ามนำเคสคนไข้มาปนซ้ำใน question)
   - หากเป็นข้อสอบเดี่ยวทั่วไปที่ไม่มีเคสคนไข้ ให้ proposedCaseContext เป็นค่าว่าง ("")
2. ตรวจสอบและเกลาตัวเลือกทั้ง 5 ข้อ (Choices 1-5):
   - ส่งคืน Array proposedChoices ครบทั้ง 5 ข้อเสมอ โดยแก้ไขคำสะกดผิด ชื่อยาผิด หน่วยผิด หรือปรับตัวลวงให้สอดคล้องกับหลักวิชาการ
3. ตรวจสอบความถูกต้องของเฉลยและคำอธิบาย 3 ส่วน:
   - proposedAnswer เป็นตัวเลข 1 ถึง 5 (1=ก, 2=ข, 3=ค, 4=ง, 5=จ) สอดคล้องกับแนวทางเวชปฏิบัติปัจจุบัน (CPG ล่าสุด)
   - proposedExplanation ต้องมีโครงสร้าง 3 ส่วนอย่างเคร่งครัด:
     ✅ คำตอบที่ถูกต้อง: ข้อ [ก-จ]. [ข้อความตัวเลือก]
     🎯 ทำไมข้อนี้ถึงถูก:
     [เหตุผลตรงประเด็นภาษาไทย อ้างอิง Guideline/หลักการทางเภสัช 1-3 บรรทัด]
     🔍 ข้ออื่นผิดเพราะอะไร:
     • ข้อ [ก-จ].: [เหตุผลที่ผิด แยกทีละข้อ ห้ามรวมย่อหน้า]
4. ตรวจสอบการจัดหมวดวิชาและชีต (Target Sheet Reclassification):
   - หากข้อสอบอยู่ผิดหมวดวิชา เช่น คำถามเป็นการคำนวณไทเทรต/เคมีวิเคราะห์ แต่อยู่ในหมวดคลินิก หรือคำถามเป็นกฎหมายยา แต่อยู่ในหมวดโรค ให้ระบุชื่อชีตที่ถูกต้องใน proposedTargetSheet (เช่น 1. Titrations, 13. Medicinal Chemistry, 1. Pharmacy Laws & Ethics, 2. Cardiovascular, 5. Research & Biostats)
   - หากข้อสอบอยู่ถูกหมวดแล้ว ให้ proposedTargetSheet เท่ากับหมวดเดิม
5. หัวข้อโรคสภาฯ (Topic), หัวข้อย่อย (Subtopic) และสายวิชา (Track):
   - proposedTopic: ระบุกลุ่มโรค/หัวข้อหลักตามหลักสูตรสภาเภสัชกรรม เช่น 2. Cardiovascular, 4. Endocrine, 8. Infectious diseases, Product Group 6: Solid Dosage Forms, 1. Law & Regulations
   - proposedSubtopic: ระบุรหัสและชื่อหัวข้อย่อยมาตรฐาน เช่น 2.1 Hypertension, 4.1 Diabetes mellitus, 8.7 Pneumonia, 6.1 Tablet Manufacturing, 5.2 สถิติวิเคราะห์ (RR, OR)
   - proposedTrack: Clinic หรือ Product หรือ SAP
   - proposedCaseId: ระบุรหัสเคสร่วม เช่น CASE-CVD-01 (ถ้าเป็นข้อสอบเคสต่อเนื่อง)
6. ภาษาและสมการ KaTeX:
   - ภาษาไทยสละสลวย คงคำศัพท์ทางการแพทย์และชื่อยาเป็นภาษาอังกฤษตรงตัว (hydrolyze, prodrug, active metabolite)
   - ห้ามมีดอกจัน (*) หรือ (**) เด็ดขาด
   - สูตรคำนวณ สแควร์รูท และเศษส่วน ต้องครอบด้วย $...$ ในรูปแบบ KaTeX เสมอ เช่น $BSA = \\sqrt{\\frac{Height \\times Weight}{3600}}$, $t_{1/2} = \\frac{0.693}{k_e}$, eGFR < 30 (ห้ามใช้ /sqrt หรือ $it; หรือ &lt; เด็ดขาด)
7. ตอบกลับเป็น JSON เท่านั้น`;

  const userPrompt = `หมวดวิชาปัจจุบัน: ` + (category || 'ไม่ระบุ') + `\n` +
    `รหัสข้อสอบ: ` + (questionId || 'ไม่ระบุ') + `\n` +
    `ข้อมูลข้อสอบเดิม:\n` +
    JSON.stringify(originalQ, null, 2) + `\n\n` +
    `สิ่งที่นิสิตรายงานปัญหา:\n` +
    `- ประเภทปัญหา: ` + (studentReport.issueType || 'ทั่วไป') + `\n` +
    `- รายละเอียด: ` + (studentReport.detail || 'ไม่มี') + `\n\n` +
    `กรุณาวินิจฉัยและส่งออก JSON ในรูปแบบนี้เท่านั้น:\n` +
    `{\n` +
    `  "verdict": "AGREE / DISAGREE / PARTIAL",\n` +
    `  "diagnosis": "สรุปผลการวินิจฉัยและ CPG/หลักวิชาอ้างอิง สั้นกระชับ 1-3 บรรทัด",\n` +
    `  "proposedCaseContext": "สถานการณ์เคส/ข้อมูลผู้ป่วย (หรือเว้นว่างถ้าเป็นข้อเดี่ยว)",\n` +
    `  "proposedQuestion": "ประโยคคำถามเฉพาะข้อที่ปรับปรุงแล้ว",\n` +
    `  "proposedChoices": ["ตัวเลือก 1", "ตัวเลือก 2", "ตัวเลือก 3", "ตัวเลือก 4", "ตัวเลือก 5"],\n` +
    `  "proposedAnswer": 1,\n` +
    `  "proposedExplanation": "เฉลย 3 ส่วนมาตรฐาน (✅ / 🎯 / 🔍) ไม่มีดอกจัน",\n` +
    `  "proposedTargetSheet": "ชื่อชีตปลายทางที่ถูกต้อง",\n` +
    `  "proposedTopic": "หัวข้อโรคสภาฯ",\n` +
    `  "proposedSubtopic": "รหัสและชื่อหัวข้อย่อย",\n` +
    `  "proposedTrack": "Clinic / Product / SAP",\n` +
    `  "proposedCaseId": "รหัสเคส (ถ้ามี)"\n` +
    `}`;

  for (let m = 0; m < candidateModels.length; m++) {
    const model = candidateModels[m];
    const url = 'https://generativelanguage.googleapis.com/v1beta/models/' + model + ':generateContent?key=' + apiKey;

    const payload = {
      contents: [{
        role: 'user',
        parts: [{ text: userPrompt }]
      }],
      systemInstruction: {
        parts: [{ text: systemInstruction }]
      },
      generationConfig: {
        temperature: 0.1,
        responseMimeType: 'application/json'
      }
    };

    try {
      const resp = UrlFetchApp.fetch(url, {
        method: 'post',
        contentType: 'application/json',
        payload: JSON.stringify(payload),
        muteHttpExceptions: true
      });

      const status = resp.getResponseCode();
      if (status === 200) {
        const json = JSON.parse(resp.getContentText());
        const candidate = json.candidates && json.candidates[0];
        const text = candidate && candidate.content && candidate.content.parts && candidate.content.parts[0] && candidate.content.parts[0].text;
        if (text) {
          const parsed = JSON.parse(text);
          return parsed;
        }
      } else {
        Logger.log('Model ' + model + ' failed with status ' + status + ': ' + resp.getContentText());
      }
    } catch (err) {
      Logger.log('Model ' + model + ' fetch error: ' + err.toString());
    }
  }

  return null;
}

function applyReportIssueApproved(rowNum) {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const reportSheet = ss.getSheetByName('Report_Quiz_Issues');
  if (!reportSheet) return { success: false, error: 'ไม่พบชีต Report_Quiz_Issues' };

  const lastCol = Math.max(19, reportSheet.getLastColumn());
  const rowVals = reportSheet.getRange(rowNum, 1, 1, lastCol).getValues()[0];
  const cat = String(rowVals[2] || '').trim();
  const qId = String(rowVals[3] || '').trim();
  const aiDiag = String(rowVals[7] || '').trim();

  // 1. ตรวจสอบว่ามี JSON ก้อนเต็มใน Col 19 หรือไม่
  let ai = null;
  if (rowVals.length >= 19 && rowVals[18]) {
    try {
      ai = JSON.parse(String(rowVals[18]));
    } catch (e) {}
  }

  // 2. ดึงข้อมูลที่เสนอแก้ไข โดยให้ความสำคัญกับค่าในเซลล์จริงก่อน (Cell-First Architecture)
  // Col 9 = Proposed Case Context
  const cellCase = rowVals.length >= 9 ? String(rowVals[8] || '').trim() : '';
  const proposedCase = cellCase || (ai ? (ai.proposedCaseContext || '') : '');

  // Col 10 = Proposed Question
  const cellQ = rowVals.length >= 10 ? String(rowVals[9] || '').trim() : '';
  const proposedQ = cellQ || (ai ? (ai.proposedQuestion || '') : '');

  // Col 11 = Proposed Choices
  const cellChoicesStr = rowVals.length >= 11 ? String(rowVals[10] || '').trim() : '';
  let proposedChoices = null;
  if (cellChoicesStr) {
    const lines = cellChoicesStr.split('\n').map(l => l.trim()).filter(Boolean);
    if (lines.length === 5) {
      proposedChoices = lines.map(l => l.replace(/^(\d+[\.\)]|[ก-จ][\.\)])\s*/, '').trim());
    }
  }
  if (!proposedChoices && ai && Array.isArray(ai.proposedChoices) && ai.proposedChoices.length === 5) {
    proposedChoices = ai.proposedChoices;
  }

  // Col 12 = Proposed Answer
  const cellAnsRaw = rowVals.length >= 12 ? rowVals[11] : '';
  let proposedAns = NaN;
  if (cellAnsRaw !== '' && cellAnsRaw !== null && cellAnsRaw !== undefined) {
    const parsedAns = parseInt(cellAnsRaw, 10);
    if (!isNaN(parsedAns) && parsedAns >= 1 && parsedAns <= 5) {
      proposedAns = parsedAns;
    }
  }
  if (isNaN(proposedAns) && ai && ai.proposedAnswer) {
    const parsedAiAns = parseInt(ai.proposedAnswer, 10);
    if (!isNaN(parsedAiAns) && parsedAiAns >= 1 && parsedAiAns <= 5) {
      proposedAns = parsedAiAns;
    }
  }

  // Col 13 = Proposed Explanation
  const cellExp = rowVals.length >= 13 ? String(rowVals[12] || '').trim() : '';
  const proposedExp = cellExp || (ai ? (ai.proposedExplanation || '') : '');

  // Col 14 = Proposed Target Sheet
  const cellTargetSheet = rowVals.length >= 14 ? String(rowVals[13] || '').trim() : '';
  const proposedTargetSheet = cellTargetSheet || (ai ? (ai.proposedTargetSheet || '').trim() : '');

  // Col 15 = Proposed Topic & Subtopic
  const cellTopicSubtopic = rowVals.length >= 15 ? String(rowVals[14] || '').trim() : '';
  let proposedTopic = '';
  let proposedSubtopic = '';
  if (cellTopicSubtopic) {
    if (cellTopicSubtopic.includes('/')) {
      const parts = cellTopicSubtopic.split('/');
      proposedTopic = parts[0].trim();
      proposedSubtopic = parts.slice(1).join('/').trim();
    } else {
      proposedTopic = cellTopicSubtopic;
    }
  }
  if (!proposedTopic && ai && ai.proposedTopic) proposedTopic = (ai.proposedTopic || '').trim();
  if (!proposedSubtopic && ai && ai.proposedSubtopic) proposedSubtopic = (ai.proposedSubtopic || '').trim();

  // Col 16 = Proposed Track
  const cellTrack = rowVals.length >= 16 ? String(rowVals[15] || '').trim() : '';
  const proposedTrack = cellTrack || (ai ? (ai.proposedTrack || '').trim() : '');

  // Case ID from AI JSON
  const proposedCaseId = ai ? (ai.proposedCaseId || '').trim() : '';

  const statusCol = 17;
  const logCol = 18;

  const hasValidFix = (proposedQ && proposedQ !== '-') || (!isNaN(proposedAns) && proposedAns >= 1 && proposedAns <= 5) || (proposedExp && proposedExp !== '-');
  if (!hasValidFix) {
    reportSheet.getRange(rowNum, statusCol).setValue('⏳ รอประธานอนุมัติ (Pending)');
    reportSheet.getRange(rowNum, logCol).setValue('⚠️ ยังไม่มีข้อมูลที่เสนอแก้ กรุณากรอกข้อมูลในคอลัมน์ 9-13 หรือกดเมนู ⚡ ประมวลผล AI ก่อน');
    return { success: false, error: 'ยังไม่มีข้อมูลข้อสอบที่เสนอแก้' };
  }

  let sourceSheetName = cat;
  let sourceRowNum = 0;
  if (qId.includes('::')) {
    const parts = qId.split('::');
    sourceSheetName = parts[0].trim();
    sourceRowNum = parseInt(parts[1], 10);
  }

  if (!sourceSheetName || sourceRowNum < 3) {
    reportSheet.getRange(rowNum, logCol).setValue('ข้อผิดพลาด: ไม่พบตำแหน่งแถวในชีตต้นทาง (qId: ' + qId + ')');
    return { success: false, error: 'ตำแหน่งแถวไม่ถูกต้อง' };
  }

  const sourceSheet = findSheetSafely_(ss, sourceSheetName);
  if (!sourceSheet) {
    reportSheet.getRange(rowNum, logCol).setValue('ข้อผิดพลาด: ไม่พบชีต ' + sourceSheetName);
    return { success: false, error: 'ไม่พบชีตต้นทาง' };
  }

  const sourceColMap = resolveSheetColumnMap_(sourceSheet);
  const oldVals = sourceSheet.getRange(sourceRowNum, 1, 1, Math.max(19, sourceSheet.getLastColumn())).getValues()[0];
  const oldQuestion = String(oldVals[sourceColMap.question - 1] || '').trim();
  const oldAns = oldVals[sourceColMap.answer - 1];
  const oldExp = String(oldVals[sourceColMap.explanation - 1] || '').trim();

  let changesList = [];

  // ══════════════════════════════════════════════════════════════════════
  // กรณีที่ 1: AI วินิจฉัยให้ย้ายหมวดวิชา/ชีต (Reclassify & Move to New Sheet)
  // ══════════════════════════════════════════════════════════════════════
  const isMoveSheet = proposedTargetSheet && proposedTargetSheet !== sourceSheetName;
  if (isMoveSheet) {
    const destSheet = findSheetSafely_(ss, proposedTargetSheet);
    if (destSheet) {
      const destColMap = resolveSheetColumnMap_(destSheet);
      const destNextRow = destSheet.getLastRow() + 1;
      let destItemNo = 1;
      if (destNextRow > 3) {
        const lastItemVal = destSheet.getRange(destNextRow - 1, 1).getValue();
        const parsed = parseInt(lastItemVal, 10);
        destItemNo = isNaN(parsed) ? (destNextRow - 2) : (parsed + 1);
      }

      // รวบรวม choices
      let finalChoices = [];
      if (proposedChoices && proposedChoices.length === 5) {
        finalChoices = proposedChoices;
      } else {
        finalChoices = [
          String(oldVals[sourceColMap.c1 - 1] || ''),
          String(oldVals[sourceColMap.c2 - 1] || ''),
          String(oldVals[sourceColMap.c3 - 1] || ''),
          String(oldVals[sourceColMap.c4 - 1] || ''),
          String(oldVals[sourceColMap.c5 - 1] || '')
        ];
      }

      const moveData = {
        itemNo: destItemNo,
        caseContext: proposedCase || (sourceColMap.caseContext ? String(oldVals[sourceColMap.caseContext - 1] || '') : ''),
        question: proposedQ || oldQuestion,
        imgQ: sourceColMap.imgQ ? String(oldVals[sourceColMap.imgQ - 1] || '') : '',
        choices: finalChoices,
        answer: (!isNaN(proposedAns) && proposedAns >= 1 && proposedAns <= 5) ? proposedAns : oldAns,
        explanation: proposedExp || oldExp,
        imgA: sourceColMap.imgA ? String(oldVals[sourceColMap.imgA - 1] || '') : '',
        topic: proposedTopic || (sourceColMap.topic ? String(oldVals[sourceColMap.topic - 1] || '') : ''),
        subtopic: proposedSubtopic || (sourceColMap.subtopic ? String(oldVals[sourceColMap.subtopic - 1] || '') : ''),
        track: proposedTrack || (sourceColMap.track ? String(oldVals[sourceColMap.track - 1] || '') : ''),
        note: (sourceColMap.note ? String(oldVals[sourceColMap.note - 1] || '') : '') + ` [ย้ายจาก ${sourceSheetName}::${sourceRowNum}]`,
        examType: sourceColMap.examType ? String(oldVals[sourceColMap.examType - 1] || '') : '',
        examYear: sourceColMap.examYear ? String(oldVals[sourceColMap.examYear - 1] || '') : '',
        caseId: proposedCaseId || (sourceColMap.caseId ? String(oldVals[sourceColMap.caseId - 1] || '') : '')
      };

      const newRowVals = buildRowArrayForSheet_(destColMap, moveData);
      destSheet.appendRow(newRowVals);
      const actualNewRow = destSheet.getLastRow();
      const newQId = `${destSheet.getName()}::${actualNewRow}`;

      // ทำเครื่องหมายย้ายในแถวเดิม หรือลบแถว
      try {
        sourceSheet.getRange(sourceRowNum, sourceColMap.question).setValue(`[ย้ายไป ${newQId}] ${oldQuestion}`);
      } catch (e) {}

      changesList.push(`ย้ายหมวดจาก ${sourceSheetName} ไปยัง ${destSheet.getName()} (แถวใหม่ ${actualNewRow})`);

      // บันทึกลง Log_Question_Edits
      let logSheet = ss.getSheetByName('Log_Question_Edits');
      if (logSheet) {
        const thaiTimestamp = Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
        logSheet.appendRow([
          thaiTimestamp,
          'AI Auto-Resolver (Reclassified & Moved)',
          qId + ' -> ' + newQId,
          destSheet.getName(),
          actualNewRow,
          oldQuestion.substring(0, 150),
          (moveData.question).substring(0, 150),
          String(oldAns || ''),
          String(moveData.answer),
          oldExp.substring(0, 150),
          (moveData.explanation).substring(0, 150),
          'Reclassified to ' + destSheet.getName()
        ]);
      }

      const thaiTime = Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
      reportSheet.getRange(rowNum, 4).setValue(newQId);
      reportSheet.getRange(rowNum, statusCol).setValue('🚀 นำไปใช้ในชีตข้อสอบแล้ว (Applied)');
      reportSheet.getRange(rowNum, logCol).setValue(`ย้ายไป ${destSheet.getName()} แถว ${actualNewRow} สำเร็จ เมื่อ ${thaiTime}`);
      return { success: true, moved: true, newQId: newQId };
    }
  }

  // ══════════════════════════════════════════════════════════════════════
  // กรณีที่ 2: แก้ไขในชีตเดิม (In-Place Full Attribute Revision)
  // ══════════════════════════════════════════════════════════════════════
  const updates = {};

  if (proposedCase !== undefined && proposedCase !== null && sourceColMap.caseContext) {
    updates.caseContext = proposedCase;
    if (proposedCase) changesList.push('สถานการณ์เคส');
  }

  if (proposedQ && proposedQ !== '-') {
    updates.question = proposedQ;
    if (proposedQ !== oldQuestion) changesList.push('ประโยคคำถาม');
  }

  if (proposedChoices && proposedChoices.length === 5) {
    updates.choices = proposedChoices;
    changesList.push('ตัวเลือก 1-5');
  }

  if (!isNaN(proposedAns) && proposedAns >= 1 && proposedAns <= 5) {
    updates.answer = proposedAns;
    if (proposedAns !== oldAns) changesList.push('เฉลยเป็นข้อ ' + proposedAns);
  }

  if (proposedExp && proposedExp !== '-') {
    updates.explanation = proposedExp;
    if (proposedExp !== oldExp) changesList.push('คำอธิบาย 3 ส่วน');
  }

  if (proposedTopic) {
    updates.topic = proposedTopic;
    changesList.push('หัวข้อโรค (' + proposedTopic + ')');
  }

  if (proposedSubtopic) {
    updates.subtopic = proposedSubtopic;
    changesList.push('หัวข้อย่อย (' + proposedSubtopic + ')');
  }

  if (proposedTrack) {
    updates.track = proposedTrack;
    changesList.push('สายวิชา (' + proposedTrack + ')');
  }

  if (proposedCaseId) {
    updates.caseId = proposedCaseId;
    changesList.push('รหัสเคส (' + proposedCaseId + ')');
  }

  applyUpdatesToRowValues_(sourceSheet, sourceRowNum, sourceColMap, updates);

  // บันทึกลง Log_Question_Edits
  let logSheet = ss.getSheetByName('Log_Question_Edits');
  if (logSheet) {
    const thaiTimestamp = Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
    logSheet.appendRow([
      thaiTimestamp,
      'AI Auto-Resolver (Approved Full Update)',
      qId,
      sourceSheetName,
      sourceRowNum,
      oldQuestion.substring(0, 150),
      (updates.question || oldQuestion).substring(0, 150),
      String(oldAns || ''),
      String(updates.answer !== undefined ? updates.answer : oldAns),
      oldExp.substring(0, 150),
      (updates.explanation || oldExp).substring(0, 150),
      'Approved from Report (' + (changesList.length ? changesList.join(', ') : 'ไม่มีการเปลี่ยนแปลง') + ')'
    ]);
  }

  const thaiTime = Utilities.formatDate(new Date(), "Asia/Bangkok", "dd/MM/yyyy HH:mm:ss");
  reportSheet.getRange(rowNum, statusCol).setValue('🚀 นำไปใช้ในชีตข้อสอบแล้ว (Applied)');
  reportSheet.getRange(rowNum, logCol).setValue(`อัปเดตชีต ${sourceSheetName} แถว ${sourceRowNum} (${changesList.length ? changesList.join(', ') : 'ไม่มีส่วนที่แก้'}) สำเร็จ เมื่อ ${thaiTime}`);

  return { success: true };
}

function setupReportIssuesSheet() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  let sheet = ss.getSheetByName('Report_Quiz_Issues');
  if (!sheet) {
    sheet = ss.insertSheet('Report_Quiz_Issues');
  }

  const headers = [
    "Timestamp (เวลาไทย)",
    "User (ผู้แจ้ง)",
    "Category (หมวดวิชาปัจจุบัน)",
    "Question ID (รหัสข้อ)",
    "Issue Type (ประเภทปัญหา)",
    "Student Detail (สิ่งที่นิสิตแจ้ง)",
    "Current Exam & Key (โจทย์และเฉลยเดิม)",
    "AI Diagnosis & Reason (AI วินิจฉัย & CPG อ้างอิง)",
    "AI Proposed Case Context (สถานการณ์เคสใหม่)",
    "AI Proposed Question (โจทย์คำถามใหม่)",
    "AI Proposed Choices (ตัวเลือกใหม่ 1-5)",
    "AI Proposed Answer (เฉลยใหม่ 1-5)",
    "AI Proposed Explanation (เฉลย 3 ส่วนใหม่)",
    "AI Proposed Target Sheet (ชีตเป้าหมาย)",
    "AI Proposed Topic & Subtopic (หัวข้อโรค & หัวข้อย่อย)",
    "AI Proposed Track (สายวิชา)",
    "Status (สถานะการอนุมัติ)",
    "Applied Log (บันทึกการนำไปใช้)",
    "AI Full Payload JSON (JSON ก้อนเต็ม)"
  ];

  sheet.getRange(1, 1, 1, headers.length).setValues([headers]);
  sheet.getRange(1, 1, 1, headers.length)
    .setFontWeight("bold")
    .setBackground("#831843")
    .setFontColor("#ffffff")
    .setFontFamily("Bai Jamjuree");

  sheet.setFrozenRows(1);

  sheet.setColumnWidth(1, 140); // Timestamp
  sheet.setColumnWidth(2, 100); // User
  sheet.setColumnWidth(3, 140); // Category
  sheet.setColumnWidth(4, 130); // Question ID
  sheet.setColumnWidth(5, 130); // Issue Type
  sheet.setColumnWidth(6, 220); // Student Detail
  sheet.setColumnWidth(7, 220); // Current Exam
  sheet.setColumnWidth(8, 260); // AI Diagnosis
  sheet.setColumnWidth(9, 220); // AI Proposed Case Context
  sheet.setColumnWidth(10, 220); // AI Proposed Question
  sheet.setColumnWidth(11, 200); // AI Proposed Choices
  sheet.setColumnWidth(12, 90);  // AI Proposed Ans
  sheet.setColumnWidth(13, 280); // AI Proposed Exp
  sheet.setColumnWidth(14, 140); // AI Proposed Target Sheet
  sheet.setColumnWidth(15, 180); // AI Proposed Topic & Subtopic
  sheet.setColumnWidth(16, 90);  // AI Proposed Track
  sheet.setColumnWidth(17, 200); // Status Dropdown
  sheet.setColumnWidth(18, 250); // Applied Log
  sheet.setColumnWidth(19, 150); // AI Full Payload JSON

  const rule = SpreadsheetApp.newDataValidation()
    .requireValueInList([
      '⏳ รอประธานอนุมัติ (Pending)',
      '✅ อนุมัติ (Approved)',
      '❌ ปฏิเสธ (Rejected)',
      '✏️ แก้ไขเองแล้ว (Manual Fixed)',
      '🚀 นำไปใช้ในชีตข้อสอบแล้ว (Applied)'
    ], true)
    .setAllowInvalid(false)
    .build();

  sheet.getRange(2, 17, 500, 1).setDataValidation(rule);

  return sheet;
}

function applyStatusValidationToRow_(sheet, rowNum) {
  try {
    const rule = SpreadsheetApp.newDataValidation()
      .requireValueInList([
        '⏳ รอประธานอนุมัติ (Pending)',
        '✅ อนุมัติ (Approved)',
        '❌ ปฏิเสธ (Rejected)',
        '✏️ แก้ไขเองแล้ว (Manual Fixed)',
        '🚀 นำไปใช้ในชีตข้อสอบแล้ว (Applied)'
      ], true)
      .setAllowInvalid(false)
      .build();
    sheet.getRange(rowNum, 17).setDataValidation(rule);
  } catch (e) {}
}

function processPendingReportsInternal_() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName('Report_Quiz_Issues');
  if (!sheet) return 0;

  const lastRow = sheet.getLastRow();
  if (lastRow < 2) return 0;

  const lastCol = Math.max(19, sheet.getLastColumn());
  const data = sheet.getRange(2, 1, lastRow - 1, lastCol).getValues();
  let count = 0;

  for (let i = 0; i < data.length; i++) {
    const rowNum = i + 2;
    const cat = String(data[i][2] || '').trim();
    const qId = String(data[i][3] || '').trim();
    const issueType = String(data[i][4] || '').trim();
    const detail = String(data[i][5] || '').trim();
    const currentDiag = String(data[i][7] || '').trim();

    const needProcess = (!currentDiag || currentDiag.includes('อยู่ระหว่างเตรียม') || currentDiag === 'null');

    if (needProcess) {
      let originalQ = { question: '', choices: [], answer: '', explanation: '', caseContext: '', topic: '', subtopic: '', track: '', caseId: '' };
      let targetSheetName = cat;
      let targetRowNum = 0;
      if (qId.includes('::')) {
        const parts = qId.split('::');
        targetSheetName = parts[0].trim();
        targetRowNum = parseInt(parts[1], 10);
      }
      if (targetSheetName && targetRowNum >= 3) {
        const targetSheet = findSheetSafely_(ss, targetSheetName);
        if (targetSheet && targetRowNum <= targetSheet.getLastRow()) {
          const colMap = resolveSheetColumnMap_(targetSheet);
          const rowVals = targetSheet.getRange(targetRowNum, 1, 1, Math.max(19, targetSheet.getLastColumn())).getValues()[0];
          originalQ = {
            caseContext: colMap.caseContext ? String(rowVals[colMap.caseContext - 1] || '') : '',
            question: String(rowVals[colMap.question - 1] || ''),
            choices: [
              String(rowVals[colMap.c1 - 1] || ''),
              String(rowVals[colMap.c2 - 1] || ''),
              String(rowVals[colMap.c3 - 1] || ''),
              String(rowVals[colMap.c4 - 1] || ''),
              String(rowVals[colMap.c5 - 1] || '')
            ].filter(Boolean),
            answer: rowVals[colMap.answer - 1],
            explanation: String(rowVals[colMap.explanation - 1] || ''),
            topic: colMap.topic ? String(rowVals[colMap.topic - 1] || '') : '',
            subtopic: colMap.subtopic ? String(rowVals[colMap.subtopic - 1] || '') : '',
            track: colMap.track ? String(rowVals[colMap.track - 1] || '') : '',
            caseId: colMap.caseId ? String(rowVals[colMap.caseId - 1] || '') : ''
          };
        }
      }

      const ai = callGeminiQuizResolver(targetSheetName, qId, originalQ, { issueType, detail });
      if (ai) {
        sheet.getRange(rowNum, 8).setValue('[' + ai.verdict + '] ' + ai.diagnosis);
        sheet.getRange(rowNum, 9).setValue(ai.proposedCaseContext || '');
        sheet.getRange(rowNum, 10).setValue(ai.proposedQuestion || '');
        sheet.getRange(rowNum, 11).setValue(Array.isArray(ai.proposedChoices) ? ai.proposedChoices.map((c, idx) => `${idx+1}. ${c}`).join('\n') : '');
        sheet.getRange(rowNum, 12).setValue(ai.proposedAnswer || '');
        sheet.getRange(rowNum, 13).setValue(ai.proposedExplanation || '');
        sheet.getRange(rowNum, 14).setValue(ai.proposedTargetSheet || targetSheetName);
        sheet.getRange(rowNum, 15).setValue((ai.proposedTopic || '') + (ai.proposedSubtopic ? ' / ' + ai.proposedSubtopic : ''));
        sheet.getRange(rowNum, 16).setValue(ai.proposedTrack || '');
        sheet.getRange(rowNum, 17).setValue('⏳ รอประธานอนุมัติ (Pending)');
        sheet.getRange(rowNum, 18).setValue('AI วิเคราะห์ครบทุกฟิลด์สำเร็จ พร้อมให้ประธานกดอนุมัติ');
        sheet.getRange(rowNum, 19).setValue(JSON.stringify(ai));
        applyStatusValidationToRow_(sheet, rowNum);
        count++;
      }
    }
  }

  return count;
}

function processPendingReports() {
  const count = processPendingReportsInternal_();
  try {
    SpreadsheetApp.getUi().alert('⚡ ประมวลผล AI ข้อที่ค้างอยู่สำเร็จทั้งหมด ' + count + ' ข้อ');
  } catch (e) {}
}

function applyAllApprovedReports() {
  const ss = SpreadsheetApp.getActiveSpreadsheet();
  const sheet = ss.getSheetByName('Report_Quiz_Issues');
  if (!sheet) {
    try { SpreadsheetApp.getUi().alert('ไม่พบชีต Report_Quiz_Issues'); } catch (e) {}
    return;
  }

  const lastRow = sheet.getLastRow();
  if (lastRow < 2) {
    try { SpreadsheetApp.getUi().alert('ไม่มีข้อมูลรายงานในชีต'); } catch (e) {}
    return;
  }

  const lastCol = Math.max(19, sheet.getLastColumn());
  const data = sheet.getRange(2, 1, lastRow - 1, lastCol).getValues();
  let count = 0;
  let errorMsgs = [];

  for (let i = 0; i < data.length; i++) {
    const rowNum = i + 2;
    const status = String(data[i][16] || '').trim(); // Column 17 is Index 16
    if (status.includes('อนุมัติ') || status.includes('Approved')) {
      const res = applyReportIssueApproved(rowNum);
      if (res && res.success) {
        count++;
      } else if (res && res.error) {
        errorMsgs.push('แถว ' + rowNum + ': ' + res.error);
      }
    }
  }

  try {
    let alertText = '✅ อัปเดตข้อสอบลงชีตหลักสำเร็จทั้งหมด ' + count + ' ข้อ';
    if (errorMsgs.length > 0) {
      alertText += '\n⚠️ มีข้อผิดพลาดบางแถว:\n' + errorMsgs.slice(0, 5).join('\n');
    }
    SpreadsheetApp.getUi().alert(alertText);
  } catch (e) {}
}

function testGeminiConnectionManual() {
  console.log('=== เริ่มทดสอบการเชื่อมต่อ Gemini API ===');
  const apiKey = getGeminiApiKey_();
  console.log('API Key length: ' + (apiKey ? apiKey.length : 0));
  
  if (!apiKey) {
    console.error('❌ ไม่พบ GEMINI_API_KEY ใน Script Properties');
    return 'ไม่พบคีย์ GEMINI_API_KEY';
  }

  const url = 'https://generativelanguage.googleapis.com/v1beta/models/gemini-flash-lite-latest:generateContent?key=' + apiKey;
  const response = UrlFetchApp.fetch(url, {
    method: 'post',
    contentType: 'application/json',
    payload: JSON.stringify({
      contents: [{ parts: [{ text: 'Hello, reply OK' }] }]
    }),
    muteHttpExceptions: true
  });
  
  const status = response.getResponseCode();
  const text = response.getContentText();
  console.log('HTTP Status: ' + status);
  console.log('Response: ' + text);
  
  if (status === 200) {
    console.log('🟢 การเชื่อมต่อ Gemini API สำเร็จ 100% พร้อมใช้งาน!');
  } else {
    console.error('⚠️ การเชื่อมต่อไม่สำเร็จ: ' + text);
  }
  
  return 'HTTP ' + status;
}
