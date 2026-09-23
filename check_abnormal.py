# -*- coding: utf-8 -*-
import sys
sys.stdout.reconfigure(encoding='utf-8')
from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDS_FILE = 'C:/Users/thana/Desktop/PLE-CC/gemini-sheets-editor-497118-060a7f15daf9.json'
SPREADSHEET_ID = '1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w'
creds = service_account.Credentials.from_service_account_file(CREDS_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])
service = build('sheets', 'v4', credentials=creds)

res = service.spreadsheets().values().get(spreadsheetId=SPREADSHEET_ID, range='1. Musculoskeleton!A3:O100').execute()
rows = res.get('values', [])
print(f"Total rows fetched: {len(rows)}")

for idx, r in enumerate(rows):
    item_no = r[0] if len(r) > 0 else idx+1
    q_text = r[1][:40] if len(r) > 1 else ''
    c1 = r[3] if len(r) > 3 else ''
    c2 = r[4] if len(r) > 4 else ''
    c3 = r[5] if len(r) > 5 else ''
    c4 = r[6] if len(r) > 6 else ''
    c5 = r[7] if len(r) > 7 else ''
    ans = r[8] if len(r) > 8 else ''
    exp = r[9][:40] if len(r) > 9 else ''

    # Check if choice 5 looks abnormal or like an answer
    for c_idx, c_val in enumerate([c1, c2, c3, c4, c5], 1):
        if any(kw in c_val for kw in ['คำตอบ', 'เฉลย', '💡', 'exp', 'ข้อสอบ']):
            print(f"⚠️ [Q{item_no}] Choice {c_idx} abnormal: '{c_val}' | Q: {q_text}")
    if not c5:
        print(f"ℹ️ [Q{item_no}] Choice 5 is empty! Q: {q_text}")
