import json
import csv

results = []

with open("candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        profile = candidate["profile"]
        skills = candidate["skills"]
        redrob = candidate["redrob_signals"]

        skill_score = min(len(skills) * 5, 100)

        experience_score = min(
            profile["years_of_experience"] * 10,
            100
        )

        behavior_score = (
            redrob.get("profile_completeness_score", 0) * 0.5 +
            redrob.get("offer_acceptance_rate", 0) * 100 * 0.25 +
            redrob.get("interview_completion_rate", 0) * 100 * 0.25
        )

        final_score = (
            skill_score * 0.4 +
            experience_score * 0.3 +
            behavior_score * 0.3
        )

        reasoning = (
            f"{profile['years_of_experience']} years experience, "
            f"{len(skills)} skills, "
            f"profile completeness "
            f"{redrob.get('profile_completeness_score',0)}"
        )

        results.append({
            "candidate_id": candidate["candidate_id"],
            "score": round(final_score, 2),
            "reasoning": reasoning
        })

results.sort(
    key=lambda x: x["score"],
    reverse=True
)

top100 = results[:100]

with open("submission.csv", "w", newline="", encoding="utf-8") as csvfile:

    writer = csv.writer(csvfile)

    writer.writerow([
        "candidate_id",
        "rank",
        "score",
        "reasoning"
    ])

    for rank, candidate in enumerate(top100, start=1):

        writer.writerow([
            candidate["candidate_id"],
            rank,
            candidate["score"],
            candidate["reasoning"]
        ])

print("submission.csv generated")
print("Top 100 candidates saved")