# -*- coding: utf-8 -*-
"""
Setup Community & Leaderboard Tabs in Google Sheets
Follows Rule 3.5:
- Row 1: Banner =HYPERLINK("#gid=0", "🏠 กลับสู่หน้าแรก (Go to Home Page)")
- Merged A1:G1
- Height 35px, background #E3F2FD, font Bai Jamjuree 11pt bold, center, color #0D47A1
"""

import sys
from google.oauth2 import service_account
from googleapiclient.discovery import build

sys.stdout.reconfigure(encoding='utf-8')

CREDS = 'C:/Users/thana/Desktop/PLE-CC/gemini-sheets-editor-497118-060a7f15daf9.json'
SPREADSHEET_ID = '1CaIHXpiiAi8tFFX2IGXwXp2rXUv6JaOMiKBAiVpAV0w'

creds = service_account.Credentials.from_service_account_file(
    CREDS, scopes=['https://www.googleapis.com/auth/spreadsheets']
)
service = build('sheets', 'v4', credentials=creds)

meta = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
existing_sheets = {s['properties']['title']: s['properties']['sheetId'] for s in meta['sheets']}

print(f"Current sheets: {len(existing_sheets)}")

# 1. Add sheets if they don't exist
requests = []
if 'User_Profiles' not in existing_sheets:
    requests.append({
        'addSheet': {
            'properties': {
                'title': 'User_Profiles',
                'gridProperties': {'rowCount': 100, 'columnCount': 8, 'frozenRowCount': 2}
            }
        }
    })

if 'Community_Chat' not in existing_sheets:
    requests.append({
        'addSheet': {
            'properties': {
                'title': 'Community_Chat',
                'gridProperties': {'rowCount': 200, 'columnCount': 8, 'frozenRowCount': 2}
            }
        }
    })

if requests:
    res = service.spreadsheets().batchUpdate(
        spreadsheetId=SPREADSHEET_ID,
        body={'requests': requests}
    ).execute()
    print("Created new sheets successfully.")
    # refresh meta
    meta = service.spreadsheets().get(spreadsheetId=SPREADSHEET_ID).execute()
    existing_sheets = {s['properties']['title']: s['properties']['sheetId'] for s in meta['sheets']}

profiles_id = existing_sheets['User_Profiles']
chat_id = existing_sheets['Community_Chat']

# 2. Write content for User_Profiles
profiles_values = [
    ['=HYPERLINK("#gid=0", "🏠 กลับสู่หน้าแรก (Go to Home Page)")', '', '', '', '', '', ''],
    ['Username', 'Display Name', 'Total Answered', 'Total Correct', 'Accuracy (%)', 'Current Streak (Days)', 'Last Active'],
    ['max', 'Doctor Max (ประธานรุ่น)', 140, 126, '90%', 12, '2026-09-23T16:30:00Z'],
    ['thanadol', 'Thanadol (RxCU84)', 95, 82, '86%', 7, '2026-09-23T15:20:00Z'],
    ['admin', 'PLE Academic Admin', 210, 195, '93%', 25, '2026-09-23T16:45:00Z'],
    ['rx_lin', 'Lin (วิชาการ Clinic)', 160, 142, '89%', 14, '2026-09-23T14:10:00Z'],
    ['rx_fon', 'Fon (วิชาการ Product)', 110, 94, '85%', 9, '2026-09-23T13:40:00Z'],
    ['rx_irene', 'Irene (Head OSPE)', 130, 115, '88%', 11, '2026-09-23T12:00:00Z'],
    ['rx_kratae', 'Kratae (Clinic OSPE)', 85, 71, '84%', 5, '2026-09-23T11:30:00Z'],
    ['rx_min', 'Min (Product OSPE)', 90, 78, '87%', 6, '2026-09-23T10:15:00Z'],
    ['rx_poy', 'Poy (เลขาโครงการ)', 75, 62, '83%', 4, '2026-09-23T09:20:00Z'],
    ['rx_title', 'Title (เหรัญญิก)', 60, 49, '82%', 3, '2026-09-23T08:50:00Z']
]

chat_values = [
    ['=HYPERLINK("#gid=0", "🏠 กลับสู่หน้าแรก (Go to Home Page)")', '', '', '', '', '', ''],
    ['MessageId', 'Timestamp', 'Username', 'Display Name', 'Message Text', 'ReplyToId', 'Topic Tag'],
    ['msg_1', '2026-09-23T10:00:00Z', 'max', 'Doctor Max (ประธานรุ่น)', 'ยินดีต้อนรับเพื่อนๆ นิสิต RxCU สู่ระบบเตรียมสอบใบประกอบวิชาชีพ 2569 ครับ! หากมีข้อสงสัยเกี่ยวกับโจทย์หรือต้องการแลกเปลี่ยนแนวคิด สามารถพิมพ์คุยกันในนี้ได้เลยครับ 🎉', '', 'ประกาศ'],
    ['msg_2', '2026-09-23T10:15:00Z', 'rx_lin', 'Lin (วิชาการ Clinic)', 'หมวด Musculoskeletal ตอนนี้คัดเฉพาะ Clinic แท้ 70 ข้อพร้อม Clinical Pearls แล้วนะครับ เน้นข้อห้ามใช้ Allopurinol ใน HLA-B*58:01 ให้แม่นๆ นะครับ 💊', '', 'Clinic'],
    ['msg_3', '2026-09-23T10:20:00Z', 'thanadol', 'Thanadol (RxCU84)', 'ขอบคุณครับ! ข้อสอบ OA เรื่อง Paracetamol กับ Selective COX-2 ออกตรงแนวสอบสภาบ่อยมาก', 'msg_2', 'Clinic']
]

service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID,
    range='User_Profiles!A1:G12',
    valueInputOption='USER_ENTERED',
    body={'values': profiles_values}
).execute()

service.spreadsheets().values().update(
    spreadsheetId=SPREADSHEET_ID,
    range='Community_Chat!A1:G5',
    valueInputOption='USER_ENTERED',
    body={'values': chat_values}
).execute()

print("Populated values for User_Profiles and Community_Chat.")

# 3. Format sheets according to Rule 3.5
format_reqs = []

# User_Profiles formatting
format_reqs.extend([
    # Merge A1:G1
    {
        'mergeCells': {
            'range': {'sheetId': profiles_id, 'startRowIndex': 0, 'endRowIndex': 1, 'startColumnIndex': 0, 'endColumnIndex': 7},
            'mergeType': 'MERGE_ALL'
        }
    },
    # Set Row 1 Height = 35px
    {
        'updateDimensionProperties': {
            'range': {'sheetId': profiles_id, 'dimension': 'ROWS', 'startIndex': 0, 'endIndex': 1},
            'properties': {'pixelSize': 35},
            'fields': 'pixelSize'
        }
    },
    # Format Row 1 Banner: Background #E3F2FD, Font Bai Jamjuree 11pt Bold, Center & Middle, Color #0D47A1
    {
        'repeatCell': {
            'range': {'sheetId': profiles_id, 'startRowIndex': 0, 'endRowIndex': 1, 'startColumnIndex': 0, 'endColumnIndex': 7},
            'cell': {
                'userEnteredFormat': {
                    'backgroundColor': {'red': 0.89, 'green': 0.95, 'blue': 0.99}, # #E3F2FD
                    'horizontalAlignment': 'CENTER',
                    'verticalAlignment': 'MIDDLE',
                    'textFormat': {
                        'fontFamily': 'Bai Jamjuree',
                        'fontSize': 11,
                        'bold': True,
                        'foregroundColor': {'red': 0.05, 'green': 0.28, 'blue': 0.63} # #0D47A1
                    }
                }
            },
            'fields': 'userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)'
        }
    },
    # Format Row 2 Header: Background #0E7490, Font Bai Jamjuree 10pt Bold, Center & Middle, White Text
    {
        'repeatCell': {
            'range': {'sheetId': profiles_id, 'startRowIndex': 1, 'endRowIndex': 2, 'startColumnIndex': 0, 'endColumnIndex': 7},
            'cell': {
                'userEnteredFormat': {
                    'backgroundColor': {'red': 0.055, 'green': 0.455, 'blue': 0.565}, # #0E7490
                    'horizontalAlignment': 'CENTER',
                    'verticalAlignment': 'MIDDLE',
                    'textFormat': {
                        'fontFamily': 'Bai Jamjuree',
                        'fontSize': 10,
                        'bold': True,
                        'foregroundColor': {'red': 1.0, 'green': 1.0, 'blue': 1.0}
                    }
                }
            },
            'fields': 'userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)'
        }
    }
])

# Community_Chat formatting
format_reqs.extend([
    # Merge A1:G1
    {
        'mergeCells': {
            'range': {'sheetId': chat_id, 'startRowIndex': 0, 'endRowIndex': 1, 'startColumnIndex': 0, 'endColumnIndex': 7},
            'mergeType': 'MERGE_ALL'
        }
    },
    # Set Row 1 Height = 35px
    {
        'updateDimensionProperties': {
            'range': {'sheetId': chat_id, 'dimension': 'ROWS', 'startIndex': 0, 'endIndex': 1},
            'properties': {'pixelSize': 35},
            'fields': 'pixelSize'
        }
    },
    # Format Row 1 Banner: Background #EEF2FF, Font Bai Jamjuree 11pt Bold, Center & Middle, Color #3730A3
    {
        'repeatCell': {
            'range': {'sheetId': chat_id, 'startRowIndex': 0, 'endRowIndex': 1, 'startColumnIndex': 0, 'endColumnIndex': 7},
            'cell': {
                'userEnteredFormat': {
                    'backgroundColor': {'red': 0.93, 'green': 0.95, 'blue': 1.0}, # #EEF2FF
                    'horizontalAlignment': 'CENTER',
                    'verticalAlignment': 'MIDDLE',
                    'textFormat': {
                        'fontFamily': 'Bai Jamjuree',
                        'fontSize': 11,
                        'bold': True,
                        'foregroundColor': {'red': 0.21, 'green': 0.19, 'blue': 0.64} # #3730A3
                    }
                }
            },
            'fields': 'userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)'
        }
    },
    # Format Row 2 Header: Background #4338CA, Font Bai Jamjuree 10pt Bold, Center & Middle, White Text
    {
        'repeatCell': {
            'range': {'sheetId': chat_id, 'startRowIndex': 1, 'endRowIndex': 2, 'startColumnIndex': 0, 'endColumnIndex': 7},
            'cell': {
                'userEnteredFormat': {
                    'backgroundColor': {'red': 0.26, 'green': 0.22, 'blue': 0.79}, # #4338CA
                    'horizontalAlignment': 'CENTER',
                    'verticalAlignment': 'MIDDLE',
                    'textFormat': {
                        'fontFamily': 'Bai Jamjuree',
                        'fontSize': 10,
                        'bold': True,
                        'foregroundColor': {'red': 1.0, 'green': 1.0, 'blue': 1.0}
                    }
                }
            },
            'fields': 'userEnteredFormat(backgroundColor,horizontalAlignment,verticalAlignment,textFormat)'
        }
    }
])

service.spreadsheets().batchUpdate(
    spreadsheetId=SPREADSHEET_ID,
    body={'requests': format_reqs}
).execute()

print("✅ Successfully configured User_Profiles and Community_Chat with Rule 3.5 compliance!")
