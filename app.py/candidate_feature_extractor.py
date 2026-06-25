import json
from pprint import pprint

with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

candidate = candidates[0]

features = {
    "candidate_id": candidate["candidate_id"],
    "experience": candidate["profile"]["years_of_experience"],

    "skills_count": len(candidate["skills"]),

    "github_score":
        candidate["redrob_signals"].get(
            "github_activity_score", 0
        ),

    "profile_completeness":
        candidate["redrob_signals"].get(
            "profile_completeness_score", 0
        ),

    "recruiter_response_rate":
        candidate["redrob_signals"].get(
            "recruiter_response_rate", 0
        ),

    "offer_acceptance_rate":
        candidate["redrob_signals"].get(
            "offer_acceptance_rate", 0
        ),

    "interview_completion_rate":
        candidate["redrob_signals"].get(
            "interview_completion_rate", 0
        )
}

pprint(features)