import json

count = 0
first_candidate = None

with open("candidates.jsonl", "r", encoding="utf-8") as f:
    for line in f:
        if line.strip():
            count += 1

            if first_candidate is None:
                first_candidate = json.loads(line)

print("Total Candidates:", count)

print("\nFirst Candidate ID:")
print(first_candidate["candidate_id"])

print("\nCurrent Title:")
print(first_candidate["profile"]["current_title"])

print("\nYears of Experience:")
print(first_candidate["profile"]["years_of_experience"])