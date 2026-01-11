# This script will fetch the dataset from OpenNeuro
import requests
import os

BASE_URL = "https://raw.githubusercontent.com/OpenNeuroDatasets/ds006067/main"
SUBS = [f"sub-{i:03d}" for i in range(1, 128)]  # sub-001 to sub-127
OUTPUT_DIR = "data/transcripts"
os.makedirs(OUTPUT_DIR, exist_ok=True)

for sub in SUBS:
    transcript_path = f"{sub}/func/{sub}_task-thinkaloud_transcript.txt"
    url = f"{BASE_URL}/{transcript_path}"
    r = requests.get(url)
    if r.status_code == 200:
        out_file = os.path.join(OUTPUT_DIR, f"{sub}_task-thinkaloud_transcript.txt")
        with open(out_file, "w", encoding="utf-8") as f:
            f.write(r.text)
        print(f"Downloaded {out_file}")
    else:
        print(f"Skipping {sub}, file not found.")
print("All available transcripts downloaded.")
