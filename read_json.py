import json

def process():
    try:
        with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\cardio_part4.json', encoding='utf-8') as f:
            data = json.load(f)
        
        with open(r'C:\Users\thana\Desktop\PLE-CC\PLE CC Quiz\q_text.txt', 'w', encoding='utf-8') as f_out:
            for d in data:
                f_out.write(f"ID: {d['cardio_idx']}\n")
                f_out.write(f"Q: {d['q_text']}\n")
                for i in range(1, 6):
                    f_out.write(f"C{i}: {d.get(f'c{i}', '')}\n")
                f_out.write(f"Ans: {d['ans']}\n\n")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == '__main__':
    process()
