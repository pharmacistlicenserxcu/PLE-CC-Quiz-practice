import json

with open('id_part6.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

keys = ['200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '239', '240', '242', '243', '248', '249', '250', '251', '252', '253', '255', '256', '257', '258', '305']

with open('all_35_clean.txt', 'w', encoding='utf-8') as out:
    for k in keys:
        v = data[k]
        ans = v.get('ans')
        out.write(f"=== KEY: {k} (ans: {ans}) ===\n")
        out.write(f"Q: {v.get('q_text')}\n")
        out.write(f"c1: {v.get('c1')}\n")
        out.write(f"c2: {v.get('c2')}\n")
        out.write(f"c3: {v.get('c3')}\n")
        out.write(f"c4: {v.get('c4')}\n")
        out.write(f"c5: {v.get('c5')}\n")
        out.write("\n")
print("Exported all 35 clean successfully.")
