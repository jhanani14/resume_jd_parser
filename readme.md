# Resume JD Matcher - AI-Powered Career Analysis

An intelligent web application that matches your resume against job descriptions using advanced NLP and machine learning. Get instant insights into skill gaps, match percentages, and personalized learning recommendations.

---

## Project Objectives

This project demonstrates a modern AI-driven recruitment automation system that:

- **Extract Skills** - Identify technical and professional capabilities from documents
- **Calculate Similarity** - Use TF-IDF and Cosine Similarity for semantic matching
- **Gap Analysis** - Pinpoint missing skills and competencies
- **Learning Path** - Generate personalized development recommendations
- **Track History** - Store and manage analysis results per user

---

## Technology Stack

### Backend
- **Framework:** Flask with App Factory Architecture
- **Authentication:** Flask-Login with password hashing
- **Database:** SQLite with SQLAlchemy ORM
- **NLP:** NLTK, spaCy
- **ML:** Scikit-learn (TF-IDF, Cosine Similarity)
- **File Processing:** pdfplumber, python-docx

### Frontend
- **HTML5/CSS3** - Modern responsive design
- **Bootstrap 5** - Professional UI components
- **Chart.js** - Interactive data visualization
- **Font Awesome** - Icon library

---

## Project Structure

```
resume_jd_parser/
│
├── run.py                          # Application entry point
│
├── requirements.txt                # Project dependencies
│
├── skill_data.py                   # Skill taxonomy data
│
└── app/
    ├── __init__.py                 # Flask App Factory initialization
    ├── models.py                   # SQLAlchemy database models
    ├── auth.py                     # Authentication routes
    ├── main.py                     # Analysis routes
    ├── nlp_engine.py               # NLP processing & ML logic
    ├── utils.py                    # Utility functions
    │
    ├── templates/                  # Jinja2 HTML templates
    │   ├── base.html              # Base template with navbar
    │   ├── login.html             # Login page
    │   ├── register.html          # Registration page
    │   ├── dashboard.html         # Analysis input form
    │   ├── results.html           # Results display
    │   └── suggestions.html       # Learning suggestions
    │
    ├── static/
    │   ├── css/
    │   │   └── style.css          # Professional styling
    │   └── js/
    │       └── charts.js          # Chart configurations
    │
    ├── skill_taxonomy.json        # Skill database
    │
    └── instance/
        └── database.db            # SQLite database

```

## Features

### **User Authentication**
- Secure user registration with password hashing
- Session-based login system
- Protected routes with Flask-Login
- Logout functionality with session management

### **Resume & Job Description Handling**
- Upload files: PDF, DOCX, TXT
- Paste text directly into text areas
- File validation and error handling
- Support for large documents

### **Advanced NLP Processing**
- Text normalization and cleaning
- Stopword removal (NLTK)
- Named entity recognition (spaCy)
- Skill extraction from custom taxonomy
- TF-IDF vectorization
- Cosine similarity computation (0-100%)

### **Comprehensive Analysis**
- Overall match percentage score
- Skills breakdown (matched/missing)
- Accuracy rate calculation
- Text preprocessing metrics
- Skills gap visualization
- Interactive charts and graphs

### **Learning Recommendations**
- Personalized skill development paths
- Recommended learning timeline (2-4 weeks per skill)
- Learning resources and platforms
- Practice suggestions
- Pro tips for effective learning

### **Data Management**
- Store analysis results per user
- Match history tracking
- Timestamped records
- Preprocessed text debugging view

---

## How It Works

### Algorithm Flow

```
1. User Input
   ├── Upload/Paste Resume
   └── Upload/Paste Job Description

2. Text Preprocessing
   ├── Lowercase normalization
   ├── Special character removal
   ├── Stopword removal
   └── Tokenization

3. Skill Extraction
   ├── Match against skill taxonomy
   ├── Extract from resume
   └── Extract from job description

4. Vector Generation
   ├── Create TF-IDF vectors
   ├── Compute feature importance
   └── Normalize values

5. Similarity Calculation
   ├── Calculate cosine similarity
   ├── Generate match score (%)
   └── Identify matched skills

6. Gap Analysis
   ├── Find missing skills
   ├── Calculate accuracy rate
   └── Determine learning needs

7. Recommendations
   ├── Generate learning path
   ├── Suggest resources
   └── Provide timeline

8. Data Storage
   ├── Save results to database
   ├── Store timestamp
   └── Link to user account

---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)
- Virtual environment (recommended)

### Installation

**1. Clone the Repository**
```bash
git clone https://github.com/jhanani14/resume_jd_parser.git
cd resume_jd_parser
```

**2. Create Virtual Environment**
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

**3. Install Dependencies**
```bash
pip install -r requirements.txt
```

**4. Download NLP Models**
```bash
# Download spaCy model for entity recognition
python -m spacy download en_core_web_sm
```

**5. Run Application**
```bash
python run.py
```

The application will start on `http://localhost:5000`

---

## Usage Guide

### Step 1: Register/Login
- Create a new account with username and password
- Login with your credentials
- Your password is securely hashed and stored

### Step 2: Upload Documents
- Navigate to the Dashboard
- Upload or paste your resume (PDF, DOCX, or TXT)
- Upload or paste the job description
- Click **Analyze & Compare**

### Step 3: Review Results
- View your overall match percentage
- Check matched and missing skills
- Review accuracy metrics
- Examine preprocessing details

### Step 4: Learning Path
- Review personalized skill recommendations
- Follow the suggested learning timeline
- Explore learning resources
- Implement practice suggestions

---

## Testing

To test the application:

1. Create a test account
2. Use sample resume and job description
3. Verify skill extraction accuracy
4. Check match score calculation
5. Review learning recommendations
6. Validate database storage

---

## Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=your-secret-key-here
DATABASE_URL=sqlite:///instance/database.db
```

### Database Setup
The SQLite database is created automatically on first run.

---

## Sample Output

### Match Results Show:
- **55% Overall Match** - Your resume aligns with ~55% of job requirements
- **18 Matched Skills** - Python, Flask, Docker, etc.
- **8 Missing Skills** - Kubernetes, AWS, Machine Learning
- **Text Cleaned: 92%** - Preprocessing effectiveness

---

## Troubleshooting

| Issue | Solution |
|-------|----------|
| Database locked error | Delete `instance/database.db` and restart |
| Static files not loading | Clear browser cache, restart Flask server |
| PDF upload fails | Ensure PDF is text-based (not scanned image) |
| No skills extracted | Check skill taxonomy, verify text content |
| Port 5000 in use | Change port in `run.py` or kill process using port |

---

## Future Enhancements

- Support for multiple languages
- LinkedIn profile integration
- Resume builder tool
- Job recommendation engine
- Advanced analytics dashboard
- Career roadmap visualization
- Interview preparation resources
- Real-time collaboration features

---



