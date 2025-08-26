import streamlit as st
from src.models.resume_model import parse_resume, match_skills
from src.utils.helpers import load_sample_resumes

def main():
    st.title("AI-Powered Resume Screener")
    st.write("Upload your resume to see how well it matches the job description.")

    uploaded_file = st.file_uploader("Choose a file", type=["pdf", "docx", "txt"])
    
    if uploaded_file is not None:
        resume_text = parse_resume(uploaded_file)
        st.subheader("Parsed Resume Text")
        st.write(resume_text)

        job_description = st.text_area("Enter Job Description")
        
        if st.button("Match Skills"):
            if job_description:
                skills_match = match_skills(resume_text, job_description)
                st.subheader("Skills Match Results")
                st.write(skills_match)
            else:
                st.warning("Please enter a job description to match against.")

    st.sidebar.header("Sample Resumes")
    sample_resumes = load_sample_resumes()
    for resume in sample_resumes:
        st.sidebar.write(resume)

if __name__ == "__main__":
    main()