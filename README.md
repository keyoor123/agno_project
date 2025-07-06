# Multi Agent System using Agno and Mistral

This project is a Python-based multi-agent system built using Agno and Mistral AI to perform grammar correction and summarization on textual content extracted from PDF, DOCX, or CSV files. The final result is exported as a clean, formatted PDF report.

---
## Problem Statement

The objective of this project is to develop a multi-agent AI system using the Agno that automates the task of grammar correction and summarization for unstructured text data.

The system must fulfill the following core requirements:

1. Multi-Agent Architecture: Use Agno to define and manage separate agents for grammar correction and text summarization.
2. Multi-format Input Support: Accept input files in one of three formats — PDF, DOCX, or CSV.
3. PDF Report Output: Generate a final, structured PDF report containing the corrected and summarized content.

---

##  Features

- Multi-Agent Architecture using Agno 
  - Grammar Correction Agent (Mistral)
  - Summarization Agent (Mistral)
- Accepts files in `.pdf`, `.docx`, or `.csv` format
- Outputs a corrected and summarized PDF report
- Powered by LLMs via Mistral API

---

## Technologies Used

- Python 3.8+
- Agno 
- Mistral AI (mistralai)
- PyMuPDF (fitz)
- python-docx
- pandas
- dotenv

---

## Approach

This system uses a multi-agent pipeline approach to process input documents and generate human-like, corrected summaries:

1. Input Handler:
   - Reads text from PDF, DOCX, or CSV using format-specific parsers (`PyMuPDF`, `python-docx`, `pandas`).

2. Agent 1: Grammar Correction Agent:
   - Uses `MistralChat` model via Agno to correct grammar, spelling, and style issues.
   - Takes raw extracted text and returns a polished version.

3. Agent 2: Summarizer Agent:
   - Summarizes the corrected text into a 5–6 sentence summary.
   - Helps users quickly understand the document’s key ideas.

4. Report Generator:
   - Combines both the corrected text and its summary into a final PDF report using `PyMuPDF`.

5. **Pipeline Logic**:  
   - The `pipeline.py` script **manages** the flow between reading the input, processing it through multiple AI agents, and generating the final PDF report.  
   - It ensures modularity and makes it easy to extend the system with new features.

The system applies task-specific prompting for each agent, ensuring high-quality outputs while keeping each LLM focused on a narrow domain.
