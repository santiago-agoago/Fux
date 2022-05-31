import statistics

dados = open("dados.txt", "r")

lista = []

for i in range(22):
    linha = dados.readline()
    lista.append(int(linha[37:43]))

print(statistics.mean(lista))