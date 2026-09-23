/**
 * =========================================================================
 * 📝 PLE-CC Quiz Practice — Web App API (Code.gs)
 * =========================================================================
 * Script ID: 1LB8brFu49jQwb5xR3WeeyW2Su_M8e1X2XX3mxD6sxlO7yVwWpDPwG-tS
 * Sheet ID: 1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w
 * 
 * Column Layout (A - M):
 *  A: คำถาม (Question)
 *  B: รูปถาม (Question Image URL)
 *  C: ตัวเลือก 1 (Choice 1)
 *  D: ตัวเลือก 2 (Choice 2)
 *  E: ตัวเลือก 3 (Choice 3)
 *  F: ตัวเลือก 4 (Choice 4)
 *  G: ตัวเลือก 5 (Choice 5)
 *  H: เฉลย (Answer Key - 1-5)
 *  I: คำอธิบายเฉลย (Explanation)
 *  J: รูปเฉลย (Answer Image URL)
 *  K: Filter หมวด/Subtopic
 *  L: Product / Clinic (Track)
 *  M: หมายเหตุ (Note)
 * =========================================================================
 */

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

    // 2. ดึงรายชื่อหมวดหมู่ / Tabs ทั้งหมด
    if (action === 'getCategories' || action === 'getSheetList') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      const sheets = ss.getSheets();
      const categories = [];

      sheets.forEach(sheet => {
        const title = sheet.getName();
        // ข้าม sheet บันทึกผลหรือ log หรือ สารบัญ
        if (title.startsWith('Log_') || title.startsWith('Report_') || title.startsWith('Eval_') || title === 'สารบัญ') return;

        const lastRow = sheet.getLastRow();
        let count = 0;
        let track = 'Clinic';
        if (lastRow >= 3) {
          count = lastRow - 2; // ลบ banner row 1 และ header row 2
          try {
            const sampleTrack = sheet.getRange(3, 12).getValue();
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
        targetSheets = ss.getSheets().filter(s => {
          const n = s.getName();
          return !n.startsWith('Log_') && !n.startsWith('Report_') && !n.startsWith('Eval_') && n !== 'สารบัญ';
        });
      }

      const allQuestions = [];

      targetSheets.forEach(sheet => {
        const sName = sheet.getName();
        const lastRow = sheet.getLastRow();
        if (lastRow < 3) return; // แถว 1=Banner, แถว 2=Header

        // อ่าน A3:O(lastRow) -> 15 คอลัมน์ (รองรับคอลัมน์ A เป็น "ข้อที่")
        const values = sheet.getRange(3, 1, lastRow - 2, 15).getValues();

        values.forEach((row, idx) => {
          const rowNum = idx + 3;
          const firstVal = String(row[0] || '').trim();
          
          let offset = 0;
          let itemNo = allQuestions.length + 1;
          if (/^\d+$/.test(firstVal) || (row.length >= 15 && firstVal.length <= 4)) {
            offset = 1;
            itemNo = parseInt(firstVal, 10) || (allQuestions.length + 1);
          }

          const questionText = String(row[offset + 0] || '').trim();
          const questionImg  = String(row[offset + 1] || '').trim();
          const c1           = String(row[offset + 2] || '').trim();
          const c2           = String(row[offset + 3] || '').trim();
          const c3           = String(row[offset + 4] || '').trim();
          const c4           = String(row[offset + 5] || '').trim();
          const c5           = String(row[offset + 6] || '').trim();
          const answerKey    = parseInt(row[offset + 7], 10) || 1;
          const explanation  = String(row[offset + 8] || '').trim();
          const answerImg    = String(row[offset + 9] || '').trim();
          const subtopic     = String(row[offset + 10] || '').trim() || sName;
          const track        = String(row[offset + 11] || 'Clinic').trim();
          const note         = String(row[offset + 12] || '').trim();
          const examType     = String(row[offset + 13] || 'ข้อสอบจำลอง (Mock)').trim();

          if (!questionText && !c1) return;

          // รวม choices ที่ไม่ว่าง
          const choices = [c1, c2, c3, c4];
          if (c5) choices.push(c5);

          allQuestions.push({
            id: sName + '::' + rowNum,
            itemNo: itemNo,
            category: sName,
            subtopic: subtopic,
            track: track,
            examType: examType,
            question: questionText,
            questionImage: questionImg,
            choices: choices,
            answer: answerKey,
            explanation: explanation,
            answerImage: answerImg,
            note: note
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

    // บันทึกรายงานข้อสอบผิดพลาด
    if (action === 'reportIssue') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      let sheet = ss.getSheetByName('Report_Quiz_Issues');
      if (!sheet) {
        sheet = ss.insertSheet('Report_Quiz_Issues');
        sheet.appendRow([
          "Timestamp", "User", "Category", "Question ID", "Question Text",
          "Issue Type", "Detail", "Status"
        ]);
        sheet.getRange(1, 1, 1, 8).setFontWeight("bold").setBackground("#991b1b").setFontColor("#ffffff");
        sheet.setFrozenRows(1);
      }

      sheet.appendRow([
        new Date().toISOString(),
        String(data.user || 'Anonymous'),
        String(data.category || ''),
        String(data.questionId || ''),
        String(data.question || '').substring(0, 150),
        String(data.issueType || 'ทั่วไป'),
        String(data.detail || ''),
        "Pending"
      ]);

      return jsonResponse_({ success: true, message: 'บันทึกรายงานปัญหาเรียบร้อย' });
    }

    // บันทึกสถิติการทำข้อสอบ (Exam Log)
    if (action === 'submitQuizResult') {
      const ss = SpreadsheetApp.getActiveSpreadsheet();
      let sheet = ss.getSheetByName('Log_Quiz_Results');
      if (!sheet) {
        sheet = ss.insertSheet('Log_Quiz_Results');
        sheet.appendRow([
          "Timestamp", "User", "Category/Mode", "Score", "Total",
          "Percentage", "TimeSpentSeconds"
        ]);
        sheet.getRange(1, 1, 1, 7).setFontWeight("bold").setBackground("#0E7490").setFontColor("#ffffff");
        sheet.setFrozenRows(1);
      }

      sheet.appendRow([
        new Date().toISOString(),
        String(data.user || 'Anonymous'),
        String(data.category || 'All'),
        Number(data.score || 0),
        Number(data.total || 0),
        Number(data.percentage || 0) + '%',
        Number(data.timeSpent || 0)
      ]);

      return jsonResponse_({ success: true, message: 'บันทึกผลการทำข้อสอบเรียบร้อย' });
    }

    return jsonResponse_({ success: false, error: 'Unknown action: ' + action });
  } catch (err) {
    return jsonResponse_({ success: false, error: err.toString() });
  }
}

function jsonResponse_(obj) {
  return ContentService.createTextOutput(JSON.stringify(obj)).setMimeType(ContentService.MimeType.JSON);
}
