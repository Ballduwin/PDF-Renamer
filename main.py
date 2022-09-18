from tika import parser   
parsed_pdf = parser.from_file(r"C:\Users\User\Downloads\16.09.22 NFS-E 44606 - COPASTUR VIAGENS E TURISMO LTDA.pdf") 
data = parsed_pdf['content']  

#print(data)
#day = data.find("16/09/2022")
#nome = data.find("COPASTUR")
#print(day)
#print(nome)


data_nota = data[47 : 57]
n_nota = data[87 : 93]
nome = data[698 : 730]
print(data_nota + n_nota + nome)
