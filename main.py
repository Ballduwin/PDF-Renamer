#from tika import parser   
#parsed_pdf = parser.from_file(r"C:\testes\16.09.22 NFS-E 44606 - COPASTUR VIAGENS E TURISMO LTDA.pdf") 
#data = parsed_pdf['content']
from asyncore import read
import os

path = "C:/Testes/"
dirs = os.listdir(path)

for index in range(len(dirs)):
    arquivo = open(dirs[index], "r", encoding="utf-8")
    arq = arquivo.read()
    data_nota = arq[15 : 35]
    n_nota = arq[35 : 55]
    nome_nota = arq[85 : 105]
    dadoscompletos = data_nota + " " + n_nota + " " + nome_nota
    a = open("listanomes.txt", "w")
    a = open("listanomes.txt", "a")
    a.write(dadoscompletos)
    a.close

#data_nota = data[47 : 57]
#n_nota = data[87 : 93]
#nome_nota = data[698 : 730]


# ok abrir varios arquivos pdf
# ok pegar as 3 informaçãoes data, nº da nota, nome em que está a nota
# ok salva as informações em um arquivos txt
# renomeia todos os arquivos na pasta usando o arquivo txt