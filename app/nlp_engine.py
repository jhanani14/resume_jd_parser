# app/nlp_engine.py

import json
import os
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Load Skill Taxonomy
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
SKILL_FILE = os.path.join(BASE_DIR, "skill_taxonomy.json")

with open(SKILL_FILE, "r", encoding="utf-8") as f:
    skill_data = json.load(f)


# ----------------------------
# TEXT CLEANING FUNCTION
# ----------------------------
def clean_text(text):
    text = text.lower()
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)
    text = re.sub(r"\s+", " ", text)
    return text.strip()


# ----------------------------
# SKILL EXTRACTION
# ----------------------------
def extract_skills(text):
    text_lower = text.lower()
    extracted = []

    for skill in skill_data.keys():
        if skill.lower() in text_lower:
            extracted.append(skill)

    return list(set(extracted))


# ----------------------------
# SIMILARITY CALCULATION
# ----------------------------
def calculate_similarity(resume_text, jd_text):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume_text, jd_text])
    score = cosine_similarity(vectors[0:1], vectors[1:2])[0][0]
    return round(score * 100, 2)


# ----------------------------
# MAIN ANALYSIS FUNCTION
# ----------------------------
def analyze_resume(resume_text, jd_text):

    # Clean texts
    cleaned_resume = clean_text(resume_text)
    cleaned_jd = clean_text(jd_text)

    # Extract skills
    resume_skills = extract_skills(cleaned_resume)
    jd_skills = extract_skills(cleaned_jd)

    matched_skills = list(set(resume_skills) & set(jd_skills))
    missing_skills = list(set(jd_skills) - set(resume_skills))

    # Calculate similarity
    score = calculate_similarity(cleaned_resume, cleaned_jd)

    # Learning Recommendations
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
        "cleaned_jd": cleaned_jd
    }