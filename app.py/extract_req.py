with open("job_description.txt", "r", encoding="utf-8") as f:
    jd = f.read()

skills = [
    "Python",
    "SQL",
    "Machine Learning",
    "NLP",
    "Deep Learning",
    "Data Science",
    "Java",
    "AWS"
]

found_skills = []

for skill in skills:
    if skill.lower() in jd.lower():
        found_skills.append(skill)

print("Skills Found:")
print(found_skills)