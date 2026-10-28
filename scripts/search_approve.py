import sys
sys.stdout.reconfigure(encoding='utf-8')

with open('c:/Users/thana/Desktop/PLE-CC/PLE CC Quiz/google_apps_script/Code.gs', 'r', encoding='utf-8') as f:
    lines = f.readlines()

for i, l in enumerate(lines):
    low = l.lower()
    if 'approve' in low or 'onedit' in low or 'processpending' in low:
        print(f"{i+1}: {l.strip()[:100]}")
