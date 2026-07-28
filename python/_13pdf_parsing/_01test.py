import fitz
import os
from pprint import pprint

folder="_13pdf_parsing/documents"

documents_list=[os.path.join(folder,file)
                for file in os.listdir(folder)
                if file.endswith(".pdf")]
print(documents_list)
    
pdf=fitz.open(documents_list[1])

text=[]
page=[]

for page_no,page in enumerate(pdf):
    print(f"Page no : {page_no + 1}")
    print(page.get_text())
    print("-"*50)