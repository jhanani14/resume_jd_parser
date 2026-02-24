import streamlit as st
import nltk
import auth
from file_reader import read_pdf, read_docx, read_txt
from nlp_pipeline import preprocess, extract_skills, match_score


if not auth.login():
    st.stop()



try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')


st.set_page_config(page_title="Resume vs JD Matcher", layout="wide")


st.markdown("""
<style>
.stApp {
    background-color: #0e1117;
    color: white;
}
.stTextInput>div>div>input {
    background-color: #262730;
    color: white;
}
.stTextArea textarea {
    background-color: #262730;
    color: white;
}
.stButton>button {
    background-color: #4CAF50;
    color: white;
}
</style>
""", unsafe_allow_html=True)

st.title("Resume vs Job Description Matcher")
st.markdown("### Core NLP – Text Preprocessing & Skill Extraction")



st.header("Resume")

resume_option = st.radio("Choose Resume Input", ["Upload File", "Paste Text"])
resume_text = ""

if resume_option == "Upload File":
    resume_file = st.file_uploader("Upload Resume", type=["pdf", "docx", "txt"])
    if resume_file:
        if resume_file.type == "application/pdf":
            resume_text = read_pdf(resume_file)
        elif resume_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            resume_text = read_docx(resume_file)
        else:
            resume_text = read_txt(resume_file)
else:
    resume_text = st.text_area("Paste Resume Text", height=200)



st.header("Job Description")

jd_option = st.radio("Choose JD Input", ["Upload File", "Paste Text"])
jd_text = ""

if jd_option == "Upload File":
    jd_file = st.file_uploader("Upload Job Description", type=["pdf", "docx", "txt"])
    if jd_file:
        if jd_file.type == "application/pdf":
            jd_text = read_pdf(jd_file)
        elif jd_file.type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
            jd_text = read_docx(jd_file)
        else:
            jd_text = read_txt(jd_file)
else:
    jd_text = st.text_area("Paste Job Description Text", height=200)



if st.button("Analyze Match"):

    try:
        if not resume_text.strip():
            st.error("Resume is empty")
        elif not jd_text.strip():
            st.error("Job Description is empty")
        else:
            
            cleaned_resume = preprocess(resume_text)
            cleaned_jd = preprocess(jd_text)

            
            resume_skills = extract_skills(cleaned_resume)
            jd_skills = extract_skills(cleaned_jd)

            missing_skills = list(set(jd_skills) - set(resume_skills))

            
            score = match_score(cleaned_resume, cleaned_jd)

            st.markdown("---")


            st.subheader("Match Score")
            st.progress(int(score))
            st.success(f"{score}% Match")

            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Resume Skills")
                st.write(resume_skills)

            with col2:
                st.subheader("JD Skills")
                st.write(jd_skills)

            st.subheader("Missing Skills")
            if missing_skills:
                st.write(missing_skills)
                st.info("Add these skills to improve your match score.")
            else:
                st.success("No missing skills! Great match")

            
            with st.expander("View Extracted & Processed Text"):
                st.subheader("Raw Resume Text")
                st.text_area("Resume Raw", resume_text, height=150)

                st.subheader("Raw JD Text")
                st.text_area("JD Raw", jd_text, height=150)

                st.subheader("Cleaned Resume Text")
                st.text_area("Clean Resume", cleaned_resume, height=150)

                st.subheader("Cleaned JD Text")
                st.text_area("Clean JD", cleaned_jd, height=150)

    except Exception as e:
        st.error(f"Error occurred: {e}")