import json
from pprint import pprint

with open("sample_candidates.json","r",encoding="utf-8") as f:
    candidates = json.load(f)

candidate = candidates[0]

print("\nPROFILE")
pprint(candidate["profile"])

print("\nCAREER HISTORY")
pprint(candidate["career_history"][0])

print("\nSKILLS")
pprint(candidate["skills"][:3])

print("\nREDROB SIGNALS")
pprint(candidate["redrob_signals"])