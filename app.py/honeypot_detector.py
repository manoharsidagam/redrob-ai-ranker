import json

def honeypot_score(candidate):
    suspicious = 0

    profile = candidate.get("profile", {})
    skills = candidate.get("skills", [])
    redrob = candidate.get("redrob_signals", {})

    years_exp = profile.get("years_of_experience", 0)

    # Rule 1
    if years_exp < 2 and len(skills) > 10:
        suspicious += 1

    # Rule 2
    expert_skills = 0
    for skill in skills:
        if skill.get("proficiency", "").lower() == "expert":
            expert_skills += 1

    if expert_skills > 8:
        suspicious += 1

    # Rule 3
    github_score = redrob.get("github_activity_score", 0)

    if github_score < 2 and expert_skills > 5:
        suspicious += 1

    # Rule 4
    endorsements = 0

    for skill in skills:
        endorsements += skill.get("endorsements", 0)

    if len(skills) > 0:
        avg_endorsements = endorsements / len(skills)

        if avg_endorsements < 2 and expert_skills > 5:
            suspicious += 1

    penalty = suspicious * 10

    return penalty


# TESTING

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

candidate = candidates[0]

penalty = honeypot_score(candidate)

print("Candidate:", candidate["candidate_id"])
print("Honeypot Penalty:", penalty)