import sys
from datetime import datetime
from PDFClass import PDFClass

if __name__ == "__main__":
    try:
        pdf_output=sys.argv[1]
        pdfs = sys.argv[2:]

        folder="output"

        combined_file_name = f"{folder}/{pdf_output}"
        relative_path = f'{combined_file_name}/{pdf_output}'
        
        pc = PDFClass(folder=combined_file_name)

        pc.merge(pdfs = pdfs, output = relative_path + '.pdf')
        pc.pdf_to_md(relative_path + '.pdf', relative_path + '.md')
    except FileNotFoundError as ex:
        print(ex)
