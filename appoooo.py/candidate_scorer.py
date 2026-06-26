import json

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    first_candidate = json.loads(next(f))

profile = first_candidate["profile"]
skills = first_candidate["skills"]
redrob = first_candidate["redrob_signals"]

skill_score = len(skills) * 5

experience_score = min(
    profile["years_of_experience"] * 10,
    100
)

behavior_score = (
    redrob["profile_completeness_score"] * 0.5 +
    redrob["offer_acceptance_rate"] * 100 * 0.25 +
    redrob["interview_completion_rate"] * 100 * 0.25
)

final_score = (
    skill_score * 0.4 +
    experience_score * 0.3 +
    behavior_score * 0.3
)

print("Candidate ID:", first_candidate["candidate_id"])
print("Skill Score:", round(skill_score,2))
print("Experience Score:", round(experience_score,2))
print("Behavior Score:", round(behavior_score,2))
print("Final Score:", round(final_score,2))