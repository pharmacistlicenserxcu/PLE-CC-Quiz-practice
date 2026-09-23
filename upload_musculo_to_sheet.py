# -*- coding: utf-8 -*-
import os, sys, json
sys.stdout.reconfigure(encoding='utf-8')

from google.oauth2 import service_account
from googleapiclient.discovery import build
import parse_musculo

CREDS_FILE = 'C:/Users/thana/Desktop/PLE-CC/gemini-sheets-editor-497118-060a7f15daf9.json'
SPREADSHEET_ID = '1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w'
SHEET_NAME = '1. Musculoskeleton'

print(f"🚀 Preparing to upload {len(parse_musculo.parsed_questions)} questions to '{SHEET_NAME}'...")

creds = service_account.Credentials.from_service_account_file(
    CREDS_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets']
)
service = build('sheets', 'v4', credentials=creds)

# Build rows: A to O (15 columns)
rows = []
for idx, q in enumerate(parse_musculo.parsed_questions):
    c = q['choices']
    row = [
        idx + 1, # A: ข้อที่
        q['question'], # B: คำถาม
        "", # C: รูปถาม
        c[0] if len(c) > 0 else "", # D: ตัวเลือก 1
        c[1] if len(c) > 1 else "", # E: ตัวเลือก 2
        c[2] if len(c) > 2 else "", # F: ตัวเลือก 3
        c[3] if len(c) > 3 else "", # G: ตัวเลือก 4
        c[4] if len(c) > 4 else "", # H: ตัวเลือก 5
        int(q['answer']), # I: เฉลย (ตัวเลข 1-5)
        q['explanation'], # J: คำอธิบายเฉลย
        "", # K: รูปเฉลย
        q['subtopic'], # L: Filter หมวด/Subtopic
        "Clinic", # M: Product / Clinic
        q['note'], # N: หมายเหตุ (Clinical Guideline / Key Takeaway)
        q['exam_type'] # O: ประเภทข้อสอบ / ปีข้อสอบ
    ]
    rows.append(row)

# Clear existing rows from row 3 downwards
print(f"🧹 Clearing existing data rows in '{SHEET_NAME}' from row 3 downwards...")
service.spreadsheets().values().clear(
    spreadsheetId=SPREADSHEET_ID,
    range=f"'{SHEET_NAME}'!A3:O500"
).execute()

# Upload rows starting at A3
print(f"📤 Uploading {len(rows)} rows to '{SHEET_NAME}'!A3...")
body = {
    'values': rows
}
res = service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID,
    range=f"'{SHEET_NAME}'!A3:O{len(rows)+2}",
    valueInputOption='RAW',
    body=body
).execute()

print(f"✅ Successfully updated {res.get('updatedRows')} rows in Google Sheet!")

# Format cells: wrap text, font Bai Jamjuree
print("🎨 Setting wrap text and clean formatting...")
meta = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
sheet_id = None
for s in meta.get('sheets', []):
    if s['properties']['title'] == SHEET_NAME:
        sheet_id = s['properties']['sheetId']
        break

if sheet_id is not None:
    reqs = [
        {
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": 2,
                    "endRowIndex": len(rows) + 2,
                    "startColumnIndex": 0,
                    "endColumnIndex": 15
                },
                "cell": {
                    "userEnteredFormat": {
                        "wrapStrategy": "WRAP",
                        "verticalAlignment": "MIDDLE",
                        "textFormat": {
                            "fontFamily": "Bai Jamjuree",
                            "fontSize": 10
                        }
                    }
                },
                "fields": "userEnteredFormat(wrapStrategy,verticalAlignment,textFormat)"
            }
        },
        # Center align item number (Col A) and answer key (Col I)
        {
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": 2,
                    "endRowIndex": len(rows) + 2,
                    "startColumnIndex": 0,
                    "endColumnIndex": 1
                },
                "cell": {
                    "userEnteredFormat": {
                        "horizontalAlignment": "CENTER",
                        "textFormat": {
                            "bold": True,
                            "fontSize": 10
                        }
                    }
                },
                "fields": "userEnteredFormat(horizontalAlignment,textFormat)"
            }
        },
        {
            "repeatCell": {
                "range": {
                    "sheetId": sheet_id,
                    "startRowIndex": 2,
                    "endRowIndex": len(rows) + 2,
                    "startColumnIndex": 8,
                    "endColumnIndex": 9
                },
                "cell": {
                    "userEnteredFormat": {
                        "horizontalAlignment": "CENTER",
                        "textFormat": {
                            "bold": True,
                            "fontSize": 11,
                            "foregroundColor": { "red": 0.08, "green": 0.5, "blue": 0.24 }
                        }
                    }
                },
                "fields": "userEnteredFormat(horizontalAlignment,textFormat)"
            }
        }
    ]
    service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body={"requests": reqs}
    ).execute()
    print("✅ Sheet styling applied successfully!")
