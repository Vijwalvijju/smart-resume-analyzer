# Smart Resume Analyzer & Job Matcher

A Python + Streamlit app to analyze resumes using NLP and match them against job descriptions with a match score and skill suggestions.

## Features

- Resume (PDF) parser using `pdfplumber`
- Skill extraction using `spaCy`
- Job matching using TF-IDF and cosine similarity
- Missing skill suggestions
- Easy-to-use Streamlit UI

## Tech Stack

- Python
- Streamlit
- spaCy (NLP)
- pdfplumber
- scikit-learn

## How to Run

git clone https://github.com/YOUR_USERNAME/smart-resume-analyzer.git
cd smart-resume-analyzer
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
streamlit run app.py
