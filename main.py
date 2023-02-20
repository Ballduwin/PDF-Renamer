import os
import PyPDF2
import re

# Defina o caminho da pasta que contém os arquivos PDF
pasta = r'C:\Users\Recepcao II\Documents\ALEX\PY\001'

# Iterar sobre cada arquivo na pasta com a extensão .pdf
for filename in os.listdir(pasta):
    if filename.endswith('.pdf'):
        # Abre o arquivo PDF
        with open(os.path.join(pasta, filename), 'rb') as pdf_file:
            # Criar um objeto PDF Reader
            pdf_reader = PyPDF2.PdfReader(pdf_file)

            # Obter o número de páginas
            num_pages = len(pdf_reader.pages)

            # Iterar através de cada página
            for page in range(num_pages):
                # Obter o conteúdo de texto da página
                page_text = pdf_reader.pages[page].extract_text()

            a = page_text[16:26]
                        
            pdf_file.close()         
            
            x = a.split("/")
            
            print(x)
        
            #new_filename = re.sub("NFSe-\d{5}", "NFS-E ", filename)
            #new_filename = re.sub("IM-13005057", ""+x[0]+"."+x[1]+"."+"23", filename)
            new_filename = re.sub("NFSe-\d{5}|IM-13005057", lambda match: "NFS-E " if match.group().startswith("NFSe") else x[0]+"."+x[1]+"."+"23", filename)
            os.rename(os.path.join(pasta, filename), os.path.join(pasta, new_filename))

exit()
