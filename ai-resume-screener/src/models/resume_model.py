def parse_resume(uploaded_file):
    # Dummy implementation: read text from file
    if uploaded_file.type == "application/pdf":
        return "Extracted text from PDF resume."
    elif uploaded_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return "Extracted text from DOCX resume."
    else:
        return uploaded_file.read().decode("utf-8")

def match_skills(resume_text, job_description):
    # Dummy implementation: compare overlap of words
    resume_words = set(resume_text.lower().split())
    job_words = set(job_description.lower().split())
    if not job_words:
        return 0.0
    match = len(resume_words & job_words) / len(job_words)
    return match * 100