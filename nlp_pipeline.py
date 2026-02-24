import re
import nltk
import spacy
from nltk.corpus import stopwords
from sklearn.feature_extraction.text import TfidfVectorizer


nlp = spacy.load("en_core_web_sm")

stop_words = set(stopwords.words("english"))


def preprocess(text):
    text = text.lower()
    text = re.sub(r'[^a-zA-Z\s]', '', text)
    tokens = text.split()
    tokens = [word for word in tokens if word not in stop_words]
    return " ".join(tokens)


SKILL_LIST = [
    "python", "java", "sql", "machine learning",
    "deep learning", "nlp", "data analysis",
    "html", "css", "javascript", "react",
    "django", "flask", "streamlit"
]



def extract_skills(text):
    found = []
    text = text.lower()
    for skill in SKILL_LIST:
        if skill in text:
            found.append(skill)
    return found



def match_score(resume, jd):
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform([resume, jd])
    score = (vectors * vectors.T).toarray()[0][1]
    return round(score * 100, 2)
