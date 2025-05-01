import fitz  # PyMuPDF for reading PDF files


def extract_text_from_pdf(file):
    # Reset file pointer to the beginning
    file.seek(0)
    doc = fitz.open(stream=file.read(), filetype="pdf")
    text = ""
    for page in doc:
        text += page.get_text()
    return text



def calculate_ats_score(resume_text, job_description):
    resume_keywords = resume_text.split()  # Convert text to a list of words
    job_keywords = job_description.split()
    matching_keywords = set(resume_keywords) & set(job_keywords)
    
    ats_score = len(matching_keywords)  # Simple score: number of matching keywords
    return ats_score
