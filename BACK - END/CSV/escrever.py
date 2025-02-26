import csv

dados = [["nome", "idade"], ["ana", "25"], ["carlos", "30"]]

with open("dados.csv", "w", newline="", encoding="utf-8") as arquivo:
    escritor = csv.writer(arquivo)
    escritor.writerows(dados)