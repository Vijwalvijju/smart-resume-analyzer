import pdfplumber
import spacy

nlp = spacy.load("en_core_web_sm")

SKILL_KEYWORDS = [
    "Python", "Machine Learning", "Deep Learning", "Data Analysis", "NLP", "Pandas",
    "NumPy", "SQL", "Power BI", "Tableau", "Java", "Git", "Docker", "AWS", "FastAPI",
    "Flask", "Streamlit", "TensorFlow", "PyTorch"
]

def extract_text_from_pdf(file):
    text = ""
    with pdfplumber.open(file) as pdf:
        for page in pdf.pages:
            text += page.extract_text() or ""
    return text

def extract_skills(text):
    doc = nlp(text)
    tokens = [token.text for token in doc if not token.is_stop and not token.is_punct]
    found_skills = [skill for skill in SKILL_KEYWORDS if skill in tokens]
    return found_skills

