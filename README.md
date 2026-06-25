# 🚀 Redrob AI Candidate Ranker

An AI-powered candidate ranking system built for the **Redrob AI Hiring Challenge**.

The system analyzes candidate profiles against a given Job Description using semantic understanding, skill matching, experience evaluation, behavioral signals, and profile quality to identify the best-fit candidates. It generates a ranked list of the **Top 100 candidates** along with concise reasoning for each recommendation.

---

# 📌 Problem Statement

Traditional Applicant Tracking Systems (ATS) rely heavily on keyword matching, often missing highly qualified candidates who use different wording or demonstrate relevant experience in non-standard ways.

This project aims to simulate how an experienced recruiter evaluates candidates by combining multiple signals instead of relying solely on keyword overlap.

---

# ✨ Features

- 📄 Upload Job Description (.txt)
- 🤖 AI-based Candidate Ranking
- 🧠 Semantic Similarity using Sentence Transformers
- 🛠 Skill Matching Engine
- 💼 Experience Matching
- 📊 Behavioral Signal Scoring
- 🛡 Honeypot Candidate Detection
- 🏆 Top 100 Candidate Ranking
- 💬 Candidate Reason Generation
- 🌐 Streamlit Web Dashboard

---

# 🏗 System Architecture

```
                Job Description
                       │
                       ▼
                 JD Parsing Engine
                       │
                       ▼
          Candidate Feature Extraction
                       │
       ┌───────────────┼───────────────┐
       ▼               ▼               ▼
Semantic Match    Skill Match   Experience Match
       │               │               │
       └───────────────┼───────────────┘
                       ▼
              Behavioral Scoring
                       │
                       ▼
            Honeypot Detection Engine
                       │
                       ▼
              Final Candidate Ranking
                       │
                       ▼
          Top 100 Ranked Candidates
```

---

# ⚙ Technologies Used

## Programming

- Python 3.11

## Machine Learning

- Sentence Transformers (SBERT)
- Scikit-learn

## Data Processing

- Pandas
- NumPy

## Web Framework

- Streamlit

## Version Control

- Git
- GitHub

---

# 📂 Project Structure

```
app.py
candidate_parser.py
candidate_feature_extractor.py
candidate_scorer.py
semantic_match.py
skill_match_engine.py
experience_match.py
behavior_score.py
honeypot_detector.py
final_ranker.py
generate_submission.py
submission.csv
requirements.txt
README.md
```

---

# 🔄 Workflow

1. Upload Job Description
2. Parse JD Requirements
3. Extract Candidate Features
4. Compute Semantic Similarity
5. Evaluate Skills
6. Match Experience
7. Calculate Behavioral Score
8. Detect Honeypot Profiles
9. Compute Final Score
10. Rank Candidates
11. Generate Top 100 Submission

---

# 🚀 Installation

```bash
git clone https://github.com/manoharsidagam/redrob-ai-ranker.git

cd redrob-ai-ranker

pip install -r requirements.txt
```

---

# ▶ Run

```bash
streamlit run app.py
```

---

# 📊 Output

The system produces:

- Ranked Top 100 Candidates
- Candidate Score
- Rank
- AI-generated Reasoning
- Submission CSV

---

# 🤖 AI Tools Used

The following AI tools were used to assist during development:

- ChatGPT (OpenAI)
  - Architecture planning
  - Code optimization
  - Debugging assistance
  - Documentation writing
  - Streamlit UI guidance

- GitHub Copilot
  - Code completion
  - Boilerplate generation

- Sentence Transformers (SBERT)
  - Semantic similarity computation

**Note:** All system design decisions, implementation, testing, integration, debugging, and final validation were completed manually by the author.

---

# 🔮 Future Improvements

- Resume Upload (PDF/DOCX)
- Resume Parsing
- OCR Support
- Explainable AI Ranking
- Recruiter Dashboard
- Candidate Profile Visualization
- Interview Recommendation System
- API Deployment

---

# 👨‍💻 Author

**Sidagam Sai Manohar**

Machine Learning Engineer | AI Enthusiast

GitHub:
https://github.com/manoharsidagam

Email:
manoharsidagam3@gmail.com

---

# 📜 License

This project was developed for the **Redrob AI Hiring Challenge** for educational and evaluation purposes.
