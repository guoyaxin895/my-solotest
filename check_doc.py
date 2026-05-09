from docx import Document

doc = Document('2026-05-08.doc')
print("=== Document Content ===")
for para in doc.paragraphs:
    print(f"{para.style.name}: {para.text}")
