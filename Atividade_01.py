import csv

with open("csv_aula.csv", newline='', encoding='utf-8') as arquivo:
    leitor = csv.reader(arquivo, delimiter=';')
    for linha in leitor:
        print(linha)