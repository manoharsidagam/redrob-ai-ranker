import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

results = []

for candidate in candidates:

    # Skill Score
    skill_score = 0

    skills = candidate.get("skills", [])

    for skill in skills:
        if skill["name"] in ["Python", "NLP"]:
            skill_score += 25

    skill_score = min(skill_score, 100)

    # Experience Score
    years = candidate["profile"].get("years_of_experience", 0)
    experience_score = min(years * 10, 100)

    # Behavior Score
    redrob = candidate["redrob_signals"]

    behavior_score = (
        redrob.get("profile_completeness_score", 0) * 0.4 +
        redrob.get("interview_completion_rate", 0) * 100 * 0.3 +
        redrob.get("offer_acceptance_rate", 0) * 100 * 0.3
    )

    # Semantic Score
    semantic_score = skill_score

    # Honeypot Penalty
    penalty = 0

    if years < 2 and len(skills) > 10:
        penalty += 10

    final_score = (
        0.35 * semantic_score +
        0.25 * skill_score +
        0.20 * behavior_score +
        0.20 * experience_score
    ) - penalty

    results.append({
        "candidate_id": candidate["candidate_id"],
        "score": round(final_score, 2)
    })

results.sort(key=lambda x: x["score"], reverse=True)

print("\nTOP 10 CANDIDATES\n")

for r in results[:10]:
    print(r)