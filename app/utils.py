import PyPDF2
import docx

def extract_text_from_file(file):
    filename = file.filename.lower()

    if filename.endswith(".pdf"):
        reader = PyPDF2.PdfReader(file)
        return " ".join(page.extract_text() for page in reader.pages)

    elif filename.endswith(".docx"):
        doc = docx.Document(file)
        return " ".join([para.text for para in doc.paragraphs])

    elif filename.endswith(".txt"):
        return file.read().decode("utf-8")

    return ""