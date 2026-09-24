import json

with open(r'C:/Users/thana/Desktop/PLE-CC/PLE CC Quiz/derm_part3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open(r'C:/Users/thana/Desktop/PLE-CC/PLE CC Quiz/derm_part3_dump.txt', 'w', encoding='utf-8') as out:
    for k, v in data.items():
        ans = v.get('ans')
        q = v.get('q_text')
        c1, c2, c3, c4, c5 = v.get('c1'), v.get('c2'), v.get('c3'), v.get('c4'), v.get('c5')
        note = v.get('note')
        sub = v.get('subtopic')
        out.write(f"[{k}] ans={ans} | sub={sub} | note={note} | Q: {q}\n")
        out.write(f"  c1: {c1}\n")
        out.write(f"  c2: {c2}\n")
        out.write(f"  c3: {c3}\n")
        out.write(f"  c4: {c4}\n")
        out.write(f"  c5: {c5}\n\n")

print("Dumped successfully, count:", len(data))
