from files.reader import extract_text
from agents.grammar_agent import correct_text
from agents.summarizer_agent import summarize_text
from files.pdfwriter import write_pdf

def process_file_pipeline(file_path):
    original_text = extract_text(file_path)
    corrected = correct_text(original_text)
    summary = summarize_text(corrected)
    output_pdf = write_pdf(summary, corrected)
    return output_pdf
