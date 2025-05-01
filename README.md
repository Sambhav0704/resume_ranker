Resume Ranker (ATS-Compatible)

A Streamlit-based web application that allows users to upload resumes and get ranked based on job descriptions using NLP techniques. It mimics an Applicant Tracking System (ATS) to help recruiters or candidates evaluate resume relevance.

 Features

- Upload PDF resumes
- Extract and analyze resume content
- Compare resumes with a job description using NLP
- Rank resumes based on match score
- Simple web interface with Streamlit
- Keyword extraction from job description
- ATS-like scoring logic

 Technologies Used
- Python
- Streamlit
- spaCy
- PyMuPDF (`fitz`)
- Scikit-learn (for TF-IDF & cosine similarity)

 Installation
1. **Clone the repository**
   ```bash

 How it Works
Extracts text from uploaded resumes (PDFs)
Extracts keywords from the job description
Uses TF-IDF vectorization and cosine similarity to calculate match scores
Displays scores and ranks resumes accordingly

Issues
If you face any problems or bugs, feel free to create an issue.

License
This project is licensed under the MIT License.

Contributing
Pull requests are welcome! Feel free to open an issue or submit a PR to improve functionality.

