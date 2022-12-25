import os
import PyPDF2
import aspose.words as aw

class PDFClass:
    def __init__(self, folder):
        self.folder = folder
        self.convert_to = '.md'
    
    def __make_dir(self):
        try:
            print("aaa:", self.folder)
            os.makedirs(self.folder)
        except OSError as error: 
            print(error)
    
    def merge(self, pdfs, output):
        self.__make_dir()
        pdfMerger = PyPDF2.PdfMerger()
        try:
            for pdf in pdfs:
                pdfMerger.append(pdf)

            with open(output, 'wb') as f:
                pdfMerger.write(f)
        except FileNotFoundError as ex:
            raise
    
    def pdf_to_md(self, pdf_filename, md_filename):
        doc = aw.Document(pdf_filename)
        doc.save(md_filename)
        print(f"{pdf_filename} converted to markdown, filename:{md_filename}")
