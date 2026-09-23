# -*- coding: utf-8 -*-
import sys, json
sys.stdout.reconfigure(encoding='utf-8')

from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDS_FILE = 'C:/Users/thana/Desktop/PLE-CC/gemini-sheets-editor-497118-060a7f15daf9.json'
SPREADSHEET_ID = '1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w'

creds = service_account.Credentials.from_service_account_file(
    CREDS_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets']
)
service = build('sheets', 'v4', credentials=creds)

meta = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
sheets = meta['sheets']

NEW_HEADERS = [
    "ข้อที่", "คำถาม", "รูปถาม",
    "ตัวเลือก 1", "ตัวเลือก 2", "ตัวเลือก 3", "ตัวเลือก 4", "ตัวเลือก 5",
    "เฉลย (ตัวเลข 1-5)", "คำอธิบายเฉลย", "รูปเฉลย",
    "Filter หมวด/Subtopic", "Product / Clinic", "หมายเหตุ", "ประเภทข้อสอบ / ปีข้อสอบ"
]

print(f"📊 Updating columns for {len(sheets)} sheets...")

for s in sheets:
    title = s['properties']['title']
    sheet_id = s['properties']['sheetId']
    if title == 'สารบัญ' or title.startswith('Log_') or title.startswith('Report_'):
        continue

    print(f"  -> Processing '{title}'...")
    
    # Read existing rows A2:N
    res = service.spreadsheets().values().get(
        spreadsheetId=SPREADSHEET_ID,
        range=f"'{title}'!A2:N500"
    ).execute()
    vals = res.get('values', [])
    
    if not vals:
        # Just write header
        service.spreadsheets().values().update(
            spreadsheetId=SPREADSHEET_ID,
            range=f"'{title}'!A2:O2",
            valueInputOption='RAW',
            body={'values': [NEW_HEADERS]}
        ).execute()
        continue

    header = vals[0]
    data_rows = vals[1:]
    
    # Check if column A is already 'ข้อที่'
    if header and header[0] == 'ข้อที่':
        print(f"     Already has 'ข้อที่' column.")
        continue

    new_rows = [NEW_HEADERS]
    for idx, r in enumerate(data_rows, start=1):
        if not any(r):
            continue
        # Prepend item number as string or int
        item_no = idx
        # Ensure row has up to 14 elements from old structure
        padded = r + [""] * (14 - len(r))
        new_row = [item_no] + padded
        new_rows.append(new_row)

    # Clear old range
    service.spreadsheets().values().clear(
        spreadsheetId=SPREADSHEET_ID,
        range=f"'{title}'!A2:O500"
    ).execute()

    # Write new range
    service.spreadsheets().values().update(
        spreadsheetId=SPREADSHEET_ID,
        range=f"'{title}'!A2:O{len(new_rows)+1}",
        valueInputOption='RAW',
        body={'values': new_rows}
    ).execute()

    # Style column A (Center align, bold)
    service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body={
            "requests": [
                {
                    "repeatCell": {
                        "range": {
                            "sheetId": sheet_id,
                            "startRowIndex": 2,
                            "endRowIndex": len(new_rows) + 1,
                            "startColumnIndex": 0,
                            "endColumnIndex": 1
                        },
                        "cell": {
                            "userEnteredFormat": {
                                "horizontalAlignment": "CENTER",
                                "verticalAlignment": "MIDDLE",
                                "textFormat": {
                                    "fontFamily": "Bai Jamjuree",
                                    "fontSize": 10,
                                    "bold": True,
                                    "foregroundColor": { "red": 0.08, "green": 0.35, "blue": 0.65 }
                                }
                            }
                        },
                        "fields": "userEnteredFormat(horizontalAlignment,verticalAlignment,textFormat)"
                    }
                }
            ]
        }
    ).execute()

print("\n🎉 Completed updating all sheets with 'ข้อที่' column!")
