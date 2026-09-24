import json

with open('C:/Users/thana/Desktop/PLE-CC/PLE CC Quiz/derm_part3.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('C:/Users/thana/Desktop/PLE-CC/PLE CC Quiz/inspect_exps.txt', 'w', encoding='utf-8') as out:
    for k, v in data.items():
        out.write(f"Key {k} (ans: {v.get('ans')}, note: {v.get('note')}):\n")
        out.write(f"  Q: {v.get('q_text')}\n")
        out.write(f"  c1: {v.get('c1')}\n")
        out.write(f"  c2: {v.get('c2')}\n")
        out.write(f"  c3: {v.get('c3')}\n")
        out.write(f"  c4: {v.get('c4')}\n")
        out.write(f"  c5: {v.get('c5')}\n")
        exp = v.get('exp', '')
        lines = exp.split('\n')
        out.write(f"  exp line 1: {lines[0] if len(lines) > 0 else ''}\n")
        out.write(f"  exp line 2: {lines[1] if len(lines) > 1 else ''}\n")
        out.write(f"  exp line 3: {lines[2] if len(lines) > 2 else ''}\n")
        out.write(f"  exp line 4: {lines[3] if len(lines) > 3 else ''}\n")
        out.write(f"  exp line 5: {lines[4] if len(lines) > 4 else ''}\n")
        out.write(f"  exp line 6: {lines[5] if len(lines) > 5 else ''}\n")
        out.write("\n")

print("Wrote inspect_exps.txt")
