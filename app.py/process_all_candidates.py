import json

results = []

with open("candidates.jsonl", "r", encoding="utf-8") as f:

    for line in f:

        candidate = json.loads(line)

        profile = candidate["profile"]
        skills = candidate["skills"]
        redrob = candidate["redrob_signals"]

        # Skill Score
        skill_score = min(len(skills) * 5, 100)

        # Experience Score
        experience_score = min(
            profile["years_of_experience"] * 10,
            100
        )

        # Behavior Score
        behavior_score = (
            redrob.get("profile_completeness_score", 0) * 0.5 +
            redrob.get("offer_acceptance_rate", 0) * 100 * 0.25 +
            redrob.get("interview_completion_rate", 0) * 100 * 0.25
        )

        # Final Score
        final_score = (
            skill_score * 0.4 +
            experience_score * 0.3 +
            behavior_score * 0.3
        )

        results.append({
            "candidate_id": candidate["candidate_id"],
            "score": round(final_score, 2)
        })

# Sort descending
results.sort(
    key=lambda x: x["score"],
    reverse=True
)

print("\nTOP 10 CANDIDATES\n")

for r in results[:10]:
    print(r)

print("\nTOTAL SCORED:", len(results))