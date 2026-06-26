import json

# Load candidates
with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

results = []

for candidate in candidates:

    # Skill Score
    skill_score = len(candidate["skills"]) * 5
    if skill_score > 100:
        skill_score = 100

    # Experience Score
    exp_score = min(
        candidate["profile"]["years_of_experience"] * 10,
        100
    )

    # Behavior Score
    signals = candidate["redrob_signals"]

    behavior_score = (
        signals.get("recruiter_response_rate", 0) * 40 +
        signals.get("interview_completion_rate", 0) * 30 +
        signals.get("offer_acceptance_rate", 0) * 30
    )

    # Redrob Score
    redrob_score = (
        signals.get("profile_completeness_score", 0) * 0.5 +
        signals.get("github_activity_score", 0) * 5
    )

    # Temporary Semantic Score
    semantic_score = 50

    final_score = (
        0.20 * skill_score +
        0.15 * exp_score +
        0.15 * behavior_score +
        0.20 * redrob_score +
        0.30 * semantic_score
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