# -*- coding: utf-8 -*-
import os, sys, re, json

sys.stdout.reconfigure(encoding='utf-8')

FILE = r'C:\Users\thana\Desktop\PLE-CC\Contents\CC1 Clinic\1. Musculoskeletal\Exam Extract Muscle ข้อสอบเก่า.md'

with open(FILE, 'r', encoding='utf-8') as f:
    raw_content = f.read()

parts = raw_content.split('## 📌 เฉลยละเอียดข้อสอบเก่า')
q_section = parts[0]
a_section = parts[1] if len(parts) > 1 else ''

# 1. Parse Answers
# Handle ### เฉลยข้อที่ X or ### เฉลยข้อ = X
ans_map = {}
a_blocks = re.split(r'###\s*เฉลยข้อ(?:ที่|\s*=)\s*', a_section)
for ab in a_blocks[1:]:
    lines = ab.strip().split('\n')
    m_num = re.match(r'(\d+)', lines[0])
    if not m_num:
        continue
    q_num = int(m_num.group(1))
    
    # Extract Answer Key
    ans_key = 1
    m_ans = re.search(r'คำตอบ[*:\s]+([ก-จa-eA-E1-5])', ab)
    if m_ans:
        letter = m_ans.group(1).lower()
        mapping = {'ก': 1, 'ข': 2, 'ค': 3, 'ง': 4, 'จ': 5, 'a': 1, 'b': 2, 'c': 3, 'd': 4, 'e': 5, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5}
        ans_key = mapping.get(letter, 1)
    
    # Extract Explanation & References
    exp_text = ab.strip()
    ans_map[q_num] = {
        'key': ans_key,
        'full_explanation': exp_text
    }

print(f"Total parsed answers: {len(ans_map)}")

# 2. Parse Case Scenarios
# Find all cases and their question ranges
# Format: กรณีศึกษาที่ X (ข้อ Y - Z) \n Text...
case_scenarios = {}
case_matches = re.finditer(r'(\*{0,2}กรณีศึกษาที่\s*([A-Za-zก-ฮ0-9]+)[^\n]*\((?:ข้อ\s*)?(\d+)\s*[-–—]\s*(\d+)\)\*{0,2}[\s\S]*?)(?=###\s*ข้อที่|\Z)', q_section)
for cm in case_matches:
    full_block = cm.group(1).strip()
    case_name = cm.group(2)
    start_q = int(cm.group(3))
    end_q = int(cm.group(4))
    
    # Clean scenario text (remove header markdown)
    scenario_lines = full_block.split('\n')
    # Filter out empty or header lines
    scenario_text = '\n'.join([l.strip() for l in scenario_lines if l.strip()])
    
    for q_idx in range(start_q, end_q + 1):
        case_scenarios[q_idx] = scenario_text

print(f"Total questions mapped to case scenarios: {len(case_scenarios)}")

# 3. Parse Questions
# Header format: ### ข้อที่ X [ปี YYYY] [เรื่อง: ZZZ]
q_blocks = re.split(r'###\s*ข้อที่\s*', q_section)
parsed_questions = []

for qb in q_blocks[1:]:
    lines = [l.strip() for l in qb.strip().split('\n') if l.strip()]
    if not lines:
        continue
    
    header_line = lines[0]
    m_header = re.match(r'(\d+)\s*(?:\[ปี\s*(\d+)\])?(?:\s*\[เรื่อง:\s*([^\]]+)\])?', header_line)
    if not m_header:
        continue
    
    q_num = int(m_header.group(1))
    year = m_header.group(2) or ''
    subtopic = m_header.group(3) or 'ระบบกล้ามเนื้อ กระดูก และข้อ'
    
    # Exam type tag
    exam_type = f"ข้อสอบจริงปี {year}" if year else "ข้อสอบจริง"
    
    # Body and choices
    body_lines = []
    choices = {}
    current_choice = None
    
    for line in lines[1:]:
        m_c = re.match(r'^([ก-จa-eA-E])\.\s*(.+)', line)
        if m_c:
            current_choice = m_c.group(1).lower()
            choices[current_choice] = m_c.group(2).strip()
        elif current_choice:
            choices[current_choice] += ' ' + line.strip()
        else:
            if not line.startswith('<br>') and not line.startswith('---'):
                body_lines.append(line)
    
    q_prompt = ' '.join(body_lines).strip()
    
    # If question belongs to a scenario, prepend it nicely
    if q_num in case_scenarios:
        scenario = case_scenarios[q_num]
        full_q_text = f"▶ [{scenario}]\n\n📌 ข้อที่ {q_num}: {q_prompt}"
    else:
        full_q_text = f"📌 ข้อที่ {q_num}: {q_prompt}"
    
    c_list = [
        choices.get('ก', choices.get('a', '')),
        choices.get('ข', choices.get('b', '')),
        choices.get('ค', choices.get('c', '')),
        choices.get('ง', choices.get('d', '')),
        choices.get('จ', choices.get('e', ''))
    ]
    
    ans_data = ans_map.get(q_num, {'key': 1, 'full_explanation': ''})
    
    parsed_questions.append({
        'q_num': q_num,
        'year': year,
        'subtopic': subtopic,
        'exam_type': exam_type,
        'question': full_q_text,
        'choices': c_list,
        'answer': ans_data['key'],
        'explanation': ans_data['full_explanation']
    })

print(f"Successfully parsed {len(parsed_questions)} questions!")
for sample in parsed_questions[:3]:
    print(f"\n[Q{sample['q_num']}] {sample['subtopic']} ({sample['exam_type']})")
    print(f"  Q: {sample['question'][:120]}...")
    print(f"  Choices count: {len([c for c in sample['choices'] if c])}")
    print(f"  Answer: {sample['answer']}")
    print(f"  Explanation preview: {sample['explanation'][:100]}...")
