import glob, re, sys

sys.stdout.reconfigure(encoding='utf-8')

def search_text(pattern, max_results=3):
    results = 0
    for f in glob.glob('../scripts/extracted_txt/*.txt'):
        try:
            content = open(f, 'r', encoding='utf-8', errors='ignore').read()
            matches = list(re.finditer(pattern, content, re.IGNORECASE))
            if matches:
                print(f"=== Found in {f} ===")
                for m in matches[:max_results]:
                    start = max(0, m.start() - 100)
                    end = min(len(content), m.end() + 300)
                    print(content[start:end])
                    print("-" * 40)
                results += 1
        except Exception as e:
            pass

print("Searching for LAMA in asthma (ID 54)...")
search_text(r"LAMA.*asthma|asthma.*LAMA")

print("\nSearching for ID 55...")
search_text(r"Salmetarol.*Fluticasone.*คุมอาการดี|Fluticasone.*Salmeterol.*คุมอาการ")

print("\nSearching for ID 57...")
search_text(r"FEV.*35.*FEV/FVC.*65")

print("\nSearching for ID 58...")
search_text(r"เกณฑ์.*โรคปอดอุดกั้นเรื้อรัง.*2560.*antibiotic|antibiotic.*ปอดอุดกั้นเรื้อรัง")

print("\nSearching for ID 61...")
search_text(r"rechallenge.*องุ่นไมเกรน|rechallenge.*Maculopapular")

print("\nSearching for ID 63...")
search_text(r"chiral molecule.*salbutamol|50:50.*salbutamol")

print("\nSearching for ID 64...")
search_text(r"ครั้งที่12/2564.*COPD.*ไม่ใช่สาเหตุ|ไม่ใช่สาเหตุ.*COPD")

print("\nSearching for ID 65...")
search_text(r"ปัจจัยเสี่ยงกำเริบของ COPD")

print("\nSearching for ID 66...")
search_text(r"ผลข้างเคียงของ salbutamol")

print("\nSearching for ID 68...")
search_text(r"aerosol evohaler ดูดซึมเข้าปอดได้ดีที่สุด")

print("\nSearching for ID 71...")
search_text(r"Gold Standard ในการวินิจฉัยโรคนี้.*ปอดอุดกั้นเรื้อรัง")
