from sentence_transformers import SentenceTransformer, util

# Load model
model = SentenceTransformer("all-MiniLM-L6-v2")

# JD Text
with open("job_description.txt", "r", encoding="utf-8") as f:
    jd_text = f.read()

# Candidate Profile Text
candidate_text = """
Backend Engineer
SQL Spark Cloud
Python NLP Machine Learning
Implemented streaming data pipelines on Kafka and Spark.
Built backend systems and analytics infrastructure.
"""

# Convert to embeddings
jd_embedding = model.encode(jd_text, convert_to_tensor=True)
candidate_embedding = model.encode(candidate_text, convert_to_tensor=True)

# Similarity
score = util.cos_sim(jd_embedding, candidate_embedding)

print("Semantic Match Score:", round(float(score[0][0]) * 100, 2))
