import streamlit as st
import fitz  # PyMuPDF
import re

# Extract text from uploaded PDF
def extract_text_from_pdf(uploaded_file):
    doc = fitz.open(stream=uploaded_file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text

# Score resume based on keyword match
def score_resume(resume_text, job_description):
    resume_text = resume_text.lower()
    job_description = job_description.lower()
    keywords = re.findall(r'\b\w+\b', job_description)
    matched_keywords = [word for word in keywords if word in resume_text]
    score = (len(matched_keywords) / len(set(keywords))) * 100 if keywords else 0
    return score

# Streamlit UI
st.set_page_config(page_title="Resume Ranker", layout="centered")

st.title("📄 Resume Ranker (ATS-Compatible)")
st.write("Upload multiple resumes and paste a job description to rank them against each other!")

# Upload multiple resumes
uploaded_files = st.file_uploader("Upload Resumes (PDF only)", type=["pdf"], accept_multiple_files=True)

# Enter job description
job_description = st.text_area("Paste the Job Description Here")

# Add a submit button to process the uploaded files and description
if st.button("Submit"):
    if uploaded_files and job_description:
        try:
            st.write("### Ranking Results:")
            # Loop through all uploaded files and rank them
            for uploaded_file in uploaded_files:
                resume_text = extract_text_from_pdf(uploaded_file)
                score = score_resume(resume_text, job_description)
                
                st.write(f"#### Resume: {uploaded_file.name}")
                st.progress(score / 100)  # Score should be between 0.0 and 1.0
                st.success(f"Resume matches job description by: {score:.2f}%\n")
        
        except Exception as e:
            st.error(f"⚠️ Error processing files: {e}")
    else:
        st.warning("Please upload multiple resumes and enter a job description to submit.")
else:
    st.info("Please upload multiple resumes and enter a job description to get started.")
