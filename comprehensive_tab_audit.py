#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys, openpyxl

sys.stdout.reconfigure(encoding='utf-8')

wb = openpyxl.load_workbook("PLE CC QUIZ.xlsx")
num_to_let = {1: 'ก', 2: 'ข', 3: 'ค', 4: 'ง', 5: 'จ'}

audit_results = []
for name in wb.sheetnames:
    ws = wb[name]
    if name in ['สารบัญ', 'Log_Quiz_Results', '🔍 รวมข้อสอบ & กรองข้อมูล', 'User_Profiles', 'Community_Chat', 'Report_Quiz_Issues']:
        continue
        
    total_rows = ws.max_row
    q_count = 0
    mismatch = 0
    asterisks = 0
    templates = 0
    banner_ok = False
    
    a1_val = str(ws['A1'].value or '')
    if 'HYPERLINK' in a1_val and 'หน้าแรก' in a1_val:
        banner_ok = True
    elif 'กลับสู่หน้าแรก' in a1_val:
        banner_ok = True
        
    for r in range(3, total_rows + 1):
        q = ws.cell(r, 2).value
        if not q or str(q).strip() == '':
            continue
        q_count += 1
        
        ans_val = ws.cell(r, 9).value
        exp_val = str(ws.cell(r, 10).value or '')
        
        if '*' in exp_val:
            asterisks += 1
        if any(tpl in exp_val for tpl in [
            'ไม่ใช่คำตอบที่ถูกต้องสำหรับภาวะ',
            'ไม่ตรงกับบริบท',
            'ไม่ใช่ข้อที่ถูกต้องตามบริบท',
            'ไม่เกี่ยวข้องกับบริบท',
            'ไม่ใช่คำตอบที่ถูกต้อง'
        ]):
            templates += 1
            
        try:
            ans_int = int(ans_val)
            let = num_to_let.get(ans_int, '?')
            first_line = exp_val.split('\n')[0]
            if f'ข้อ {let}.' not in first_line:
                mismatch += 1
        except:
            mismatch += 1
            
    audit_results.append({
        'name': name,
        'q_count': q_count,
        'mismatch': mismatch,
        'asterisks': asterisks,
        'templates': templates,
        'banner_ok': banner_ok
    })

print(f"{'Sheet Name':32} | {'Q Count':7} | {'Mismatch':8} | {'Asterisks':9} | {'Templates':9} | {'Banner':6}")
print("-" * 85)
for res in audit_results:
    b_str = 'OK' if res['banner_ok'] else 'FAIL'
    print(f"{res['name']:32} | {res['q_count']:7d} | {res['mismatch']:8d} | {res['asterisks']:9d} | {res['templates']:9d} | {b_str:6}")
