# Resume vs Job Description Matcher

An AI-powered web application that compares a candidate’s resume with a job description and calculates a match percentage using TF-IDF and Cosine Similarity, along with skill gap analysis and learning recommendations.

---

## Project Objective

The goal of this project is to analyze a resume against a job description and:

1. Extract relevant technical skills
2. Calculate semantic similarity score
3. Identify missing skills
4. Provide learning recommendations
5. Store match history per user

This system simulates how modern AI-driven recruitment automation systems perform resume screening.

---

## Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python,Flask (App Factory Architecture),Flask-Login (Authentication),Flask-SQLAlchemy (Database ORM)  
- **NLP Libraries:** NLTK, spaCy
- **Machine Learning:** Scikit-learn (TF-IDF, Cosine Similarity)  
- **File Handling:** pdfplumber, python-docx  
- **Database:** SQLite (User Authentication)

---

## Project Structure

resume_jd_parser/
│
├── run.py                 # Application entry point
│
└── app/
    ├── __init__.py        # Flask App Factory
    ├── models.py          # Database models
    ├── auth.py            # Login / Register system
    ├── main.py            # Resume matching routes
    ├── nlp_engine.py      # NLP processing & similarity logic
    │
    ├── templates/         # HTML templates
    │     ├── login.html
    │     ├── register.html
    │     ├── dashboard.html
    │     └── results.html
    │
    └── static/            # CSS / JS files
│
├── requirements.txt
└── instance/
      └── database.db

---

## 🔍 Features

### Authentication System

User Registration
Secure Login (Password Hashing)
Session-based access control
Logout functionality

### Resume & JD Handling

Upload Resume (PDF, DOCX, TXT)
Upload Job Description
Manual text input option
File validation and preprocessing

### NLP Processing

Text cleaning & normalization
Stopword removal
Skill extraction
TF-IDF vectorization
Cosine similarity computation

### Match Analysis

Match Percentage Score
Matched Skills
Missing Skills
Learning Recommendations
Preprocessed Text Debug View

### Database Integration

Stores match score
Tracks analysis history per user
Timestamped records

---

## 🧠 How It Works

1. Extract text from resume and job description
2. Preprocess text (lowercasing, cleaning, stopword removal)
3. Extract relevant skills from both texts
4. Convert texts into TF-IDF vectors
5. Compute cosine similarity
6. Generate match percentage
7. Identify missing skills
8. Provide learning suggestions
9. Store match results in database

---

## 📦 Installation

### 1. Clone the repository

```bash
git clone https://github.com/jhanani14/resume_jd_parser.git
cd resume-jd-matcher

### 2. Create virtual environment
python -m venv venv

### 3. Activate it:

Windows

venv\Scripts\activate

Mac/Linux

source venv/bin/activate

### 4. Install dependencies

pip install -r requirements.txt

### 5. Run the Application

streamlit run.py

The app will open in your browser.