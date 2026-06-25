import json
import csv

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

results = []

for candidate in candidates:

    skills = [s["name"] for s in candidate.get("skills", [])]

    skill_score = 0

    if "Python" in skills:
        skill_score += 50

    if "NLP" in skills:
        skill_score += 50

    years = candidate["profile"].get("years_of_experience", 0)

    redrob = candidate["redrob_signals"]

    behavior_score = (
        redrob.get("profile_completeness_score", 0) * 0.4 +
        redrob.get("interview_completion_rate", 0) * 100 * 0.3 +
        redrob.get("offer_acceptance_rate", 0) * 100 * 0.3
    )

    final_score = (
        0.5 * skill_score +
        0.3 * behavior_score +
        0.2 * min(years * 10, 100)
    )

    reasoning = (
        f"{years} years experience, "
        f"skills: {', '.join(skills[:3])}, "
        f"good behavioral profile"
    )

    results.append({
        "candidate_id": candidate["candidate_id"],
        "score": round(final_score, 2),
        "reasoning": reasoning
    })

results.sort(key=lambda x: x["score"], reverse=True)

with open("submission.csv", "w", newline="", encoding="utf-8") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ])

    for rank, candidate in enumerate(results, start=1):

        writer.writerow([
            candidate["candidate_id"],
            rank,
            candidate["score"],
            candidate["reasoning"]
        ])

print("submission.csv generated successfully!")
print("Total Candidates:", len(results))
