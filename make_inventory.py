import json

with open('hemato_part2.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

with open('distractor_inventory.txt', 'w', encoding='utf-8') as out:
    for k, v in data.items():
        ans_digit = str(v.get('ans'))
        mapping = {'1':'ก', '2':'ข', '3':'ค', '4':'ง', '5':'จ'}
        c_letter = mapping[ans_digit]
        wrong_letters = [l for l in ['ก', 'ข', 'ค', 'ง', 'จ'] if l != c_letter]
        correct_text = v.get('c' + ans_digit)
        out.write(f"KEY: {k} (ans: {ans_digit} -> {c_letter})\n")
        out.write(f"Q: {v.get('q_text')}\n")
        out.write(f"Correct choice [{c_letter}]: {correct_text}\n")
        out.write("Wrong choices to explain:\n")
        for l in wrong_letters:
            d = {'ก':'1', 'ข':'2', 'ค':'3', 'ง':'4', 'จ':'5'}[l]
            out.write(f"  [{l}]: {v.get('c' + d)}\n")
        out.write(f"Note: {v.get('note')}\n")
        out.write("="*60 + "\n")

print("Inventory written to distractor_inventory.txt")
