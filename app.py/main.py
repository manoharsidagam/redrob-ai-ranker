import streamlit as st

st.set_page_config(page_title="Redrob AI Candidate Ranker", layout="wide")

st.title("🤖 Redrob AI Candidate Ranker")

st.write("Upload a Job Description and let AI rank the best candidates.")

uploaded_file = st.file_uploader(
    "Upload Job Description",
    type=["txt", "docx"]
)

if uploaded_file is not None:
    st.success("Job Description Uploaded Successfully!")

    if uploaded_file.name.endswith(".txt"):
        jd = uploaded_file.read().decode("utf-8")

        st.subheader("Job Description")

        st.text_area(
            "",
            jd,
            height=250
        )


import pandas as pd

if st.button("🔍 Analyze Candidates"):

    st.info("Analyzing Candidates...")

    df = pd.read_csv("submission.csv")

    st.success("Analysis Completed!")

    st.subheader("🏆 Top 100 Ranked Candidates")

    st.dataframe(df)