import fitz  

def extract_text_from_pdf(pdf_path):
    doc = fitz.open(pdf_path)
    text = ""
    for page in doc:
        text += page.get_text()
    return text

textbook_paths = ["textbook1.pdf", "textbook2.pdf", "textbook3.pdf"]
texts = [extract_text_from_pdf(path) for path in textbook_paths]

with open("extracted_texts.txt", "w") as f:
    for text in texts:
        f.write(text + "\n\n")
