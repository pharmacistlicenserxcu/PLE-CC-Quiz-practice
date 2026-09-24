import json

with open('id_base_items.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

indices = {'200', '201', '202', '203', '204', '205', '206', '207', '208', '209', '210', '211', '212', '213', '214', '215', '216', '217', '218', '219', '239', '240', '242', '243', '248', '249', '250', '251', '252', '253', '255', '256', '257', '258', '305'}

with open('base_items_dump.txt', 'w', encoding='utf-8') as out:
    for item in data:
        idx_str = str(item.get('idx'))
        if idx_str in indices:
            ans = item.get('ans')
            out.write(f"*** IDX: {idx_str} (ans: {ans}) ***\n")
            out.write(f"q_text: {item.get('q_text')}\n")
            out.write(f"exp: {item.get('exp')}\n")
            out.write('-'*40 + '\n')
print('Base items dump finished.')
