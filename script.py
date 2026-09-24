import json
data = json.load(open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\cardio_part2.json', encoding='utf-8'))
for item in data:
    c1 = str(item.get('c1', ''))
    c2 = str(item.get('c2', ''))
    c3 = str(item.get('c3', ''))
    c4 = str(item.get('c4', ''))
    c5 = str(item.get('c5', ''))
    print(f"{item['cardio_idx']}: {c1} | {c2} | {c3} | {c4} | {c5}")
