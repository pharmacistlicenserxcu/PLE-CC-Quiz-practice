with open(r'C:\Users\thana\Desktop\PLE-CC\scripts\extracted_txt\PLE_CC1_Key_2553_2560.txt', 'r', encoding='utf-8') as f:
    t = f.read()

with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\snippets_2553_2560.txt', 'w', encoding='utf-8') as out:
    for term in ['Malassezia', 'fluocinolone', 'paclitaxel', 'clotrimazole', 'supp']:
        pos = 0
        while True:
            pos = t.lower().find(term.lower(), pos)
            if pos == -1:
                break
            out.write(f"=== Found '{term}' at {pos} ===\n")
            out.write(t[max(0, pos-200):min(len(t), pos+800)] + "\n\n")
            pos += len(term) + 500

print("Wrote snippets_2553_2560.txt")
