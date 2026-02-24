import pdfplumber
import docx


def read_pdf(file):
    text = ""
    try:
        with pdfplumber.open(file) as pdf:
            for page in pdf.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text + "\n"
    except Exception as e:
        return ""
    return text


def read_docx(file):
    text = ""
    try:
        doc = docx.Document(file)
        for para in doc.paragraphs:
            text += para.text + "\n"
    except:
        return ""
    return text


def read_txt(file):
    try:
        return file.read().decode("utf-8")
    except:
        return ""
