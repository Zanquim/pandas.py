import pandas as pd
from matplotlib import pyplot as plt
import tabula
import re
import fitz
import PyPDF2

#lista_passageiros2010 = tabula.read_pdf('balanco2010.pdf', pages=5)

lista_passageiros2015 = tabula.read_pdf('relatorio-diretoria.pdf', pages=1)

lista_passageiros2020 = tabula.read_pdf('RelatorioADM.pdf', pages=12)

lista_de_lista2020 = []

for tabela_de_passageiro in lista_passageiros2020:

    lista_de_lista2020.append(tabela_de_passageiro)

lista_de_lista2020.pop(1)

lista_de_paginas = []

conteudo = ""

with fitz.open('balanco2010.pdf') as pdf:

    for pagina in pdf:
        
        conteudo += pagina.getText()
        
        lista_de_paginas.append(conteudo)

print(lista_de_paginas[5:6])

print(lista_passageiros2015)

print(lista_passageiros2020)

tamanho_analise_passageiros = int(input(f'\nQuantos anos serão analisados ?\t'))

anos_quantidade = []

passageiros_na_lista = []

for anos_analise in range(0, tamanho_analise_passageiros):
    
    quais_anos = str(input(f'\nQual ano será analisado:\t'))
    anos_quantidade.append(quais_anos)
    milhoes = int(input(f'\nQual é a quantidade de passageiros transportados em {anos_quantidade:} ?\t'))
    passageiros_na_lista.append(milhoes)


porcentagem_de_passageiros = (100-(passageiros_na_lista[2])*100/passageiros_na_lista[0])

plt.plot(anos_quantidade, passageiros_na_lista, color= 'red', marker='o', linestyle='solid')
plt.xlabel(f'ANOS: houve uma diminuição de {porcentagem_de_passageiros:.2f}% passageiros transportados em 10 anos')
plt.ylabel('QUANTIDADE DE PASSAGEIROS EM MILHÕES')
plt.show()
