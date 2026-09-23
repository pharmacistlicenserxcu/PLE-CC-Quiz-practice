# -*- coding: utf-8 -*-
import os, sys
from google.oauth2 import service_account
from googleapiclient.discovery import build

CREDS_FILE = 'C:/Users/thana/Desktop/PLE-CC/gemini-sheets-editor-497118-060a7f15daf9.json'
SPREADSHEET_ID = '1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w'
creds = service_account.Credentials.from_service_account_file(CREDS_FILE, scopes=['https://www.googleapis.com/auth/spreadsheets'])
service = build('sheets', 'v4', credentials=creds)

meta = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
existing = [s['properties']['title'] for s in meta['sheets']]

sheet_id = None
for s in meta['sheets']:
    if s['properties']['title'] == 'Report_Quiz_Issues':
        sheet_id = s['properties']['sheetId']
        break

if sheet_id is None:
    req = {'addSheet': {'properties': {'title': 'Report_Quiz_Issues'}}}
    res = service.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body={'requests': [req]}).execute()
    sheet_id = res['replies'][0]['addSheet']['properties']['sheetId']
    print('Created Report_Quiz_Issues with id:', sheet_id)

format_reqs = [
    {'mergeCells': {'range': {'sheetId': sheet_id, 'startRowIndex': 0, 'endRowIndex': 1, 'startColumnIndex': 0, 'endColumnIndex': 8}, 'mergeType': 'MERGE_ALL'}},
    {'updateDimensionProperties': {'range': {'sheetId': sheet_id, 'dimension': 'ROWS', 'startIndex': 0, 'endIndex': 1}, 'properties': {'pixelSize': 35}, 'fields': 'pixelSize'}},
    {'repeatCell': {
        'range': {'sheetId': sheet_id, 'startRowIndex': 0, 'endRowIndex': 1, 'startColumnIndex': 0, 'endColumnIndex': 8},
        'cell': {
            'userEnteredFormat': {
                'backgroundColor': {'red': 0.89, 'green': 0.95, 'blue': 0.99},
                'horizontalAlignment': 'CENTER',
                'verticalAlignment': 'MIDDLE',
                'textFormat': {'fontFamily': 'Bai Jamjuree', 'fontSize': 11, 'bold': True, 'foregroundColor': {'red': 0.05, 'green': 0.28, 'blue': 0.63}}
            }
        },
        'fields': 'userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)'
    }},
    {'repeatCell': {
        'range': {'sheetId': sheet_id, 'startRowIndex': 1, 'endRowIndex': 2, 'startColumnIndex': 0, 'endColumnIndex': 8},
        'cell': {
            'userEnteredFormat': {
                'backgroundColor': {'red': 0.85, 'green': 0.15, 'blue': 0.15},
                'horizontalAlignment': 'CENTER',
                'verticalAlignment': 'MIDDLE',
                'textFormat': {'fontFamily': 'Bai Jamjuree', 'fontSize': 11, 'bold': True, 'foregroundColor': {'red': 1.0, 'green': 1.0, 'blue': 1.0}}
            }
        },
        'fields': 'userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)'
    }}
]
service.spreadsheets().batchUpdate(spreadsheetId=SPREADSHEET_ID, body={'requests': format_reqs}).execute()

values = [
    ['=HYPERLINK("#gid=0", "🏠 กลับสู่หน้าแรก (Go to Home Page)")', '', '', '', '', '', '', ''],
    ['Timestamp', 'User', 'Category', 'Question ID', 'Question Text', 'Issue Type', 'Detail', 'Status'],
    ['2026-09-23 17:00:00', 'Doctor Max', '1. Musculoskeleton', 'Musculo_01', 'ข้อใดถูกต้องเกี่ยวกับการรักษาโรคเกาต์เฉียบพลัน', 'คำอธิบายเฉลยไม่ชัดเจน', 'ระบบพร้อมรับรายงานปัญหาข้อสอบจากนิสิต', 'กำลังตรวจสอบ']
]
service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID,
    range='Report_Quiz_Issues!A1:H3',
    valueInputOption='USER_ENTERED',
    body={'values': values}
).execute()
print('Populated Report_Quiz_Issues successfully!')
