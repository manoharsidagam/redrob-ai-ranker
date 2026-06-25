import json

with open("sample_candidates.json","r",encoding="utf-8") as f:
    candidates = json.load(f)

candidate = candidates[0]

parsed = {
    "candidate_id": candidate["candidate_id"],
    "title": candidate["profile"]["current_title"],
    "experience": candidate["profile"]["years_of_experience"],
    "skills":[s["name"] for s in candidate["skills"]],
    "github_score": candidate["redrob_signals"]["github_activity_score"],
    "interview_rate": candidate["redrob_signals"]["interview_completion_rate"],
    "response_rate": candidate["redrob_signals"]["recruiter_response_rate"],
    "open_to_work": candidate["redrob_signals"]["open_to_work_flag"]
}

print(parsed)