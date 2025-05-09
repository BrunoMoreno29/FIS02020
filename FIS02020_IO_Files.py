dir_dados = "/home/bmorales/FIS02020/prog/Dados/"

#%% 1. Escrevendo em um arquivo (modo texto)

file1 = dir_dados + "exemplo.txt"
with open(file1, "w") as arquivo:
    arquivo.write("Primeira linha\n")
    arquivo.write("Segunda linha\n")
    arquivo.write("Terceira linha\n")

#%% 2. Lendo arquivo linha por linha

with open(file1, "r") as arquivo:
        for linha in arquivo:
#            print(linha, end='')
            print(linha.strip())
print()
#%% 3. Lendo todo o conteúdo de uma vez

with open(file1, "r") as arquivo:
    conteudo = arquivo.read()
print(conteudo)
print()

#%% 4. Acrescentando dados no final do aqruivo

with open(file1, "a") as arquivo:
    arquivo.write("Mais uma linha.\n")


#%% 5. Lendo e escrevendo dados tabulares com CSV

import csv

file2 = dir_dados + "stars.csv"
with open(file2, "w", newline = "") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerow(["Id", "DEC", "RA"])
    escritor.writerow(["star1", -30.001, 3.415])
    escritor.writerow(["star2", -29.232, 12.789])
    escritor.writerow(["star3", 40.123, 23.123])

#%%

with open(file2, "r") as aqruivo:
    leitor = csv.reader(aqruivo)
    for linha in leitor:
        print(linha)
print()
#%% 6. Lendo dados tabulares...

file3 = dir_dados + "dados2.csv"

with open(file3, "r") as fid:
    leitor = csv.reader(fid)
    matriz =[]
    for linha in leitor:
        t = int(linha[0])
        x = float(linha[1])
        y = float(linha[2])
        matriz.append([t,x,y])
print(matriz)
print() 
#%%

file3 = dir_dados + "dados2.csv"

with open(file3, "r") as fid:
    leitor = csv.reader(fid)
    matriz =[]
    for linha in leitor:
        row = [float(e) for e in linha]
        matriz.append(row)
print(matriz)