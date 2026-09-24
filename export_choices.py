import json

with open('C:/Users/thana/Desktop/PLE-CC/PLE CC Quiz/derm_part3.json', 'r', encoding='utf-8') as f:
    d = json.load(f)

with open('C:/Users/thana/Desktop/PLE-CC/PLE CC Quiz/all_choices_utf8.txt', 'w', encoding='utf-8') as out:
    for k in d:
        choices = []
        for c, l in [('c1', 'ก'), ('c2', 'ข'), ('c3', 'ค'), ('c4', 'ง'), ('c5', 'จ')]:
            val = d[k].get(c)
            if val is not None and str(val).strip():
                choices.append(f"{l}: {str(val).strip()}")
        ans_val = d[k].get('ans')
        q_val = d[k].get('q_text')
        note_val = d[k].get('note')
        out.write(f"[{k}] ans={ans_val} | note={note_val}\n")
        out.write(f"  Q: {q_val}\n")
        for ch in choices:
            out.write(f"  {ch}\n")
        out.write("\n")

print("Wrote all_choices_utf8.txt successfully")
