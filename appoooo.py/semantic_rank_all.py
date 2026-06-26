import json
from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# Load JD
with open("job_description.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

# JD embedding
jd_embedding = model.encode(
    jd_text,
    convert_to_tensor=True
)

# Load candidates
with open("sample_candidates.json", "r", encoding="utf-8") as f:
    candidates = json.load(f)

results = []

for candidate in candidates:

    # Candidate summary
    summary = candidate["profile"].get(
        "summary", ""
    )

    # Candidate skills
    skills = " ".join(
        [skill["name"]
         for skill in candidate["skills"]]
    )

    # Career history descriptions
    career_text = ""

    for job in candidate["career_history"]:
        career_text += (
            job.get("description", "")
            + " "
        )

    # Full candidate text
    candidate_text = (
        summary
        + " "
        + skills
        + " "
        + career_text
    )

    # Candidate embedding
    candidate_embedding = model.encode(
        candidate_text,
        convert_to_tensor=True
    )

    # Similarity
    similarity = util.cos_sim(
        jd_embedding,
        candidate_embedding
    )

    semantic_score = (
        float(similarity[0][0]) * 100
    )

    results.append({
        "candidate_id":
            candidate["candidate_id"],
        "semantic_score":
            round(semantic_score, 2)
    })

# Sort
results.sort(
    key=lambda x: x["semantic_score"],
    reverse=True
)

print("\nTOP 10 SEMANTIC MATCHES\n")

for r in results[:10]:
    print(r)