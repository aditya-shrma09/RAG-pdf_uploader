from services.pdf_uploader import extract_text

path = "sample.pdf"

text = extract_text(path)

print(text)