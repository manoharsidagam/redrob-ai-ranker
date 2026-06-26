import json

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

candidate = candidates[0]

signals = candidate["redrob_signals"]

profile_score = signals.get("profile_completeness_score", 0)
github_score = signals.get("github_activity_score", 0)

response_rate = signals.get("recruiter_response_rate", 0) * 100
offer_rate = signals.get("offer_acceptance_rate", 0) * 100

final_redrob_score = (
    profile_score * 0.30 +
    github_score * 5 +
    response_rate * 0.20 +
    offer_rate * 0.20
)

print("Redrob Score:", round(final_redrob_score,2))