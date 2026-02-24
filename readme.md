# Resume vs Job Description Matcher

A web-based NLP application that compares a resume with a job description and calculates a match percentage using TF-IDF and cosine similarity.

---

## Project Objective

The goal of this project is to analyze a candidate’s resume and compare it with a job description to:

- Extract relevant skills
- Calculate similarity score
- Identify missing skills
- Provide a match percentage

---

## Tech Stack

- **Frontend:** Streamlit  
- **Backend:** Python  
- **NLP Libraries:** NLTK, spaCy  
- **Machine Learning:** Scikit-learn (TF-IDF, Cosine Similarity)  
- **File Handling:** pdfplumber, python-docx  
- **Database:** SQLite (User Authentication)

---

## Project Structure

resume_jd_parser/
│
├── app.py             # Main Streamlit application
├── auth.py            # Authentication system
├── file_reader.py     # Resume & JD file extraction
├── nlp_pipeline.py    # NLP preprocessing & matching logic
├── requirements.txt   # Project dependencies
└── users.db           # SQLite database 


---

## 🔍 Features

- User Authentication (Login / Register)
- Upload Resume (PDF, DOCX, TXT)
- Upload Job Description
- Text Preprocessing Pipeline
- Skill Extraction
- TF-IDF Vectorization
- Cosine Similarity Matching
- Match Percentage Calculation
- Missing Skill Identification
- Debug Panel (Processed Text View)

---

## 🧠 How It Works

1. Extract text from Resume and Job Description
2. Clean and preprocess text
3. Extract relevant skills
4. Convert text to TF-IDF vectors
5. Compute cosine similarity
6. Display match score and missing skills

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

streamlit run app.py

The app will open in your browser.