#from tika import parser   
#parsed_pdf = parser.from_file(r"C:\testes\16.09.22 NFS-E 44606 - COPASTUR VIAGENS E TURISMO LTDA.pdf") 
#data = parsed_pdf['content']

arq = open(r"C:\Testes\teste.txt")
print(arq.read())
data = str(arq)

print(type(data))
 
data_nota = data[15 : 35]
n_nota = data[35 : 55]
nome_nota = data[85 : 145]

dadoscompletos = data_nota + "" + n_nota + "" + nome_nota

print(data_nota)
print(n_nota)
print(nome_nota)

print(dadoscompletos)



a = open("C:\Testes\listanomes.txt", "w")
a = open("C:\Testes\listanomes.txt", "a")
a.write(dadoscompletos)
a.close 

#print(data)



#print(data)
#day = data.find("16/09/2022")
#nome = data.find("COPASTUR")
#print(day)
#print(nome)

#data_nota = data[47 : 57]
#n_nota = data[87 : 93]
#nome_nota = data[698 : 730]









# ok abrir o arquivo
# ok pegar as 3 informaçãoes data, nº da nota, nome em que está a nota
# salva as informações em um arquivos txt
# fecha o arquivo e abre o proximo
# repete o processo para cada arquivo na pasta
# renomeia todos os arquivos na pasta usando o arquivo txt



