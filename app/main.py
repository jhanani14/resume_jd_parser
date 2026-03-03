# app/main.py

from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
import os
import pdfplumber
import docx
from .models import MatchHistory
from . import db
from app.nlp_engine import analyze_resume

main = Blueprint("main", __name__)

# ----------------------------
# FILE TEXT EXTRACTOR
# ----------------------------
def extract_text_from_file(file):

    filename = file.filename.lower()
    text = ""

    if filename.endswith(".pdf"):
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                text += page.extract_text() or ""

    elif filename.endswith(".docx"):
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"

    elif filename.endswith(".txt"):
        text = file.read().decode("utf-8")

    return text


# ----------------------------
# ROOT
# ----------------------------
@main.route("/")
def home():
    return redirect(url_for("auth.login"))


# ----------------------------
# DASHBOARD
# ----------------------------
@main.route("/dashboard")
@login_required
def dashboard():
    return render_template(
        "dashboard.html",
        username=current_user.username
    )


# ----------------------------
# ANALYZE
# ----------------------------
@main.route("/analyze", methods=["POST"])
@login_required
def analyze():

    resume_text = request.form.get("resume_text")
    jd_text = request.form.get("jd_text")

    resume_file = request.files.get("resume_file")
    jd_file = request.files.get("jd_file")

    # -------- Resume Handling --------
    if resume_file and resume_file.filename != "":
        resume_content = extract_text_from_file(resume_file)
    else:
        resume_content = resume_text or ""

    # -------- JD Handling --------
    if jd_file and jd_file.filename != "":
        jd_content = extract_text_from_file(jd_file)
    else:
        jd_content = jd_text or ""

    # Validation
    if not resume_content.strip() or not jd_content.strip():
        flash("Resume and Job Description cannot be empty.", "danger")
        return redirect(url_for("main.dashboard"))

    # NLP Analysis
    results = analyze_resume(resume_content, jd_content)

    # Save to DB
    history = MatchHistory(
        user_id=current_user.id,
        score=results["score"]
    )
    db.session.add(history)
    db.session.commit()

    return render_template(
        "results.html",
        username=current_user.username,
        score=results["score"],
        matched=results["matched_skills"],
        missing=results["missing_skills"],
        recommendations=results["recommendations"],
        cleaned_resume=results["cleaned_resume"],
        cleaned_jd=results["cleaned_jd"]
    )