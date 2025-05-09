import streamlit as st
from resume_parser import extract_text_from_pdf, extract_skills
from job_matcher import match_resume_with_job

st.set_page_config(page_title="Smart Resume Analyzer", layout="centered")

st.title("🧠 Smart Resume Analyzer & Job Matcher")

# Upload resume
uploaded_file = st.file_uploader("Upload your Resume (PDF format)", type=["pdf"])

# Enter job description
job_description = st.text_area("Paste the Job Description here", height=200)

if uploaded_file and job_description:
    with st.spinner("Analyzing..."):
        resume_text = extract_text_from_pdf(uploaded_file)
        extracted_skills = extract_skills(resume_text)
        score, missing_skills = match_resume_with_job(resume_text, job_description)

    st.subheader("📊 Match Score")
    st.success(f"✅ Your resume matches {score:.2f}% with the job description.")

    st.subheader("💡 Skills Found in Resume")
    st.write(", ".join(extracted_skills) if extracted_skills else "No skills extracted.")

    st.subheader("❗Missing Skills")
    if missing_skills:
        st.warning(", ".join(missing_skills))
    else:
        st.success("Great! All key skills are present.")
