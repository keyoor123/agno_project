import os
import fitz  
import pandas as pd
from docx import Document

def extract_text(file_path):
    ext = os.path.splitext(file_path)[1].lower()

    if ext == '.pdf':
        return extract_from_pdf(file_path)
    elif ext == '.csv':
        return extract_from_csv(file_path)
    elif ext == '.docx':
        return extract_from_docx(file_path)
    else:
        raise ValueError("Unsupported file type")

def extract_from_pdf(file_path):
    doc = fitz.open(file_path)
    return "\n".join([page.get_text() for page in doc])

def extract_from_csv(file_path):
    df = pd.read_csv(file_path)
    return df.to_string(index=False)

def extract_from_docx(file_path):
    doc = Document(file_path)
    return "\n".join([p.text for p in doc.paragraphs if p.text.strip()])
