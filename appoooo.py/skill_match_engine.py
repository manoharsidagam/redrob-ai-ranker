import json

# Load candidates
with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

# JD skills
jd_skills = ["Python", "NLP"]

candidate = candidates[0]

candidate_skills = [s["name"] for s in candidate["skills"]]

matched = []

for skill in jd_skills:
    if skill in candidate_skills:
        matched.append(skill)

score = len(matched) / len(jd_skills)

print("Candidate:", candidate["candidate_id"])
print("Matched Skills:", matched)
print("Skill Score:", round(score * 100, 2))