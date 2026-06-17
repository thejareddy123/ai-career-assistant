
"""
PDF 
 ↓
Text

Read PDF
Extract Text
Return Text

"""


from pypdf import PdfReader

#used to extract text from PDF documents. 
#This function takes the file path of a PDF document as input and returns the extracted text as a string. 
#It utilizes the PdfReader class from the pypdf library to read the PDF file and extract text from each page.


# rag/document_loader.py

from pypdf import PdfReader


class DocumentLoader:

    @staticmethod
    def load_pdf(file_path: str) -> str:

        reader = PdfReader(file_path)

        text = ""

        for page in reader.pages:

            page_text = page.extract_text()

            if page_text:
                text += page_text + "\n"

        return text