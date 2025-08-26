import streamlit as st
from models.resume_model import parse_resume, match_skills
# ...existing code...
def main():
    st.title("AI-Powered Resume Screener")
    st.write("Upload your resume to see how well it matches the job description.")

    uploaded_file = st.file_uploader("Choose a resume file", type=["pdf", "docx", "txt"])
    job_description = st.text_area("Job Description")

    if st.button("Analyze"):
        if uploaded_file is not None and job_description:
            resume_text = parse_resume(uploaded_file)
            match_score = match_skills(resume_text, job_description)
            st.success(f"Match Score: {match_score:.2f}")
        else:
            st.error("Please upload a resume and enter a job description.")

if __name__ == "__main__":
    main()