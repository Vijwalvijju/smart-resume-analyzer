from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from resume_parser import SKILL_KEYWORDS

def match_resume_with_job(resume_text, job_description):
    vectorizer = TfidfVectorizer()
    tfidf = vectorizer.fit_transform([resume_text, job_description])
    score = cosine_similarity(tfidf[0:1], tfidf[1:2])[0][0] * 100  # Convert to %
    
    missing_skills = []
    for skill in SKILL_KEYWORDS:
        if skill.lower() in job_description.lower() and skill.lower() not in resume_text.lower():
            missing_skills.append(skill)

    return score, missing_skills
