import json

data = json.load(open('neuro_part3.json', encoding='utf-8'))
with open('temp_all_30.txt', 'w', encoding='utf-8') as f:
    for k in sorted(data.keys(), key=lambda x: int(x)):
        v = data[k]
        f.write('=== ' + str(k) + ' ===\n')
        f.write('Q: ' + str(v.get('q_text')) + '\n')
        f.write('ans: ' + str(v.get('ans')) + '\n')
        for i in range(1, 6):
            f.write('  c' + str(i) + ': ' + str(v.get('c' + str(i))) + '\n')
        f.write('\n')
print('Successfully exported temp_all_30.txt')
