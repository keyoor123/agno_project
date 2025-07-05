import fitz  

def write_pdf(summary, corrected_text):
    filename = "final_report.pdf"
    doc = fitz.open()
    page = doc.new_page()
    y = 50  # Starting y-position

    def write_lines(title, text):
        nonlocal y, page
        # Add title
        page.insert_text((50, y), title, fontsize=14)
        y += 20
        # Split long lines and add text
        for line in text.splitlines():
            chunks = [line[i:i+100] for i in range(0, len(line), 100)]
            for chunk in chunks:
                page.insert_text((50, y), chunk, fontsize=10)
                y += 15
                if y > 800:
                    page = doc.new_page()
                    y = 50

    write_lines("Summary:", summary)
    write_lines("Corrected Text:", corrected_text)

    doc.save(filename)
    return filename
