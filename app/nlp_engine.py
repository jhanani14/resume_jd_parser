# app/nlp_engine.py

import json
import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_FILE = os.path.join(BASE_DIR, "skill_taxonomy.json")

with open(SKILL_FILE, "r", encoding="utf-8") as f:
    skill_data = json.load(f)


def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


def extract_skills(text):
    text_lower = text.lower()
    extracted = []

    for skill in skill_data.keys():
        if skill.lower() in text_lower:
            extracted.append(skill)

    return list(set(extracted))



def calculate_cleaning_percentage(original_text, cleaned_text):
    """Calculate the percentage of text cleaned/removed"""
    original_len = len(original_text)
    cleaned_len = len(cleaned_text)
    if original_len == 0:
        return 0
    cleaning_pct = round(((original_len - cleaned_len) / original_len) * 100, 2)
    return cleaning_pct



def calculate_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)



def calculate_accuracy(matched_skills, jd_skills):
    """Calculate accuracy as percentage of matched skills from total JD skills"""
    if len(jd_skills) == 0:
        return 0
    accuracy = round((len(matched_skills) / len(jd_skills)) * 100, 2)
    return accuracy


def analyze_resume(resume_text, jd_text):

    
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(jd_text)

    resume_cleaning_pct = calculate_cleaning_percentage(resume_text, cleaned_resume)
    jd_cleaning_pct = calculate_cleaning_percentage(jd_text, cleaned_jd)

    
    resume_skills = extract_skills(cleaned_resume)
    jd_skills = extract_skills(cleaned_jd)

    matched_skills = list(set(resume_skills) & set(jd_skills))
    missing_skills = list(set(jd_skills) - set(resume_skills))

    
    score = calculate_similarity(cleaned_resume, cleaned_jd)

    
    accuracy = calculate_accuracy(matched_skills, jd_skills)

    recommendations = {}
    for skill in missing_skills:
        if skill in skill_data:
            recommendations[skill] = skill_data[skill].get("resources", [])

    return {
        "score": score,
        "matched_skills": matched_skills,
        "missing_skills": missing_skills,
        "recommendations": recommendations,
        "cleaned_resume": cleaned_resume,
        "cleaned_jd": cleaned_jd,
        "resume_skills_count": len(resume_skills),
        "jd_skills_count": len(jd_skills),
        "matched_skills_count": len(matched_skills),
        "missing_skills_count": len(missing_skills),
        "resume_cleaning_pct": resume_cleaning_pct,
        "jd_cleaning_pct": jd_cleaning_pct,
        "accuracy": accuracy
    }