import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

print("Total Candidates:", len(candidates))

print("\nFirst Candidate ID:")
print(candidates[0]["candidate_id"])

print("\nCurrent Title:")
print(candidates[0]["profile"]["current_title"])

print("\nYears of Experience:")
print(candidates[0]["profile"]["years_of_experience"])

print("\nSkills:")
for skill in candidates[0]["skills"][:5]:
    print("-", skill["name"])