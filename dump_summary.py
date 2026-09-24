import json

with open('pulmo_p3_dump.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

lines = []
for it in items:
    lines.append(f"KEY: {it['key']} (idx: {it['idx']}) | ans: {it['ans']}")
    lines.append(f"  Q: {it['q']}")
    for i in range(1, 6):
        c_val = it.get(f'c{i}')
        if c_val:
            lines.append(f"  c{i}: {c_val}")
    lines.append("-" * 60)

with open('summary.txt', 'w', encoding='utf-8') as f:
    f.write("\n".join(lines))

print("Done writing summary.txt")
