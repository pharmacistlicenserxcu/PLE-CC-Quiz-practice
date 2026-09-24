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
      const inCellImages = getCachedInCellImages_();

      targetSheets.forEach(sheet => {
        const sName = sheet.getName();
        const lastRow = sheet.getLastRow();
        if (lastRow < 3) return; // แถว 1=Banner, แถว 2=Header

        // อ่าน A3:P(lastRow) -> 16 คอลัมน์ (รองรับคอลัมน์ A เป็น "ข้อที่")
        const values = sheet.getRange(3, 1, lastRow - 2, 16).getValues();

        values.forEach((row, idx) => {
          const rowNum = idx + 3;
          const firstVal = String(row[0] || '').trim();
          
          let offset = 0;
          let itemNo = allQuestions.length + 1;
          if (/^\d+$/.test(firstVal) || (row.length >= 16 && firstVal.length <= 4)) {
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
          const subtopic     = String(row[offset + 10] || '').trim() || sName;
          const track        = String(row[offset + 11] || 'Clinic').trim();
          const note         = String(row[offset + 12] || '').trim();
          const examType     = String(row[offset + 13] || '').trim();
          const examYear     = String(row[offset + 14] || '').trim();

          if (!questionText && !c1) return;

          // ดึง Image URL สำหรับคำถาม (Col B หรือ C ตาม offset) และเฉลย (Col J หรือ K ตาม offset)
          const qImgColIdx = offset + 1; // 0-indexed column
          const aImgColIdx = offset + 9;
          const questionImg = resolveImageUrl_(rawQImg, sName, rowNum, qImgColIdx, inCellImages);
          const answerImg   = resolveImageUrl_(rawAImg, sName, rowNum, aImgColIdx, inCellImages);

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
            examYear: examYear,
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

