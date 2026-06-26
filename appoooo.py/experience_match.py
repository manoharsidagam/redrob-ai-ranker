import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

candidate = candidates[0]

candidate_exp = candidate["profile"]["years_of_experience"]

required_exp = 5

if candidate_exp >= required_exp:
    score = 100
else:
    score = (candidate_exp / required_exp) * 100

print("Candidate Experience:", candidate_exp)
print("Required Experience:", required_exp)
print("Experience Score:", round(score,2))
