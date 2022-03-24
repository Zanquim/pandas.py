import pyodbc
import tabula
import pandas as pd
from tabulate import tabulate
from matplotlib import pyplot as plt
 
#dados_conexao = (
    
    #"Driver={SQL Server};"
    #"Server=LAPTOP-SG53A25P\SQLEXPRESS;"
    #"DataBase=emtu;"

#)

#conexao = pyodbc.connect(dados_conexao)

#print('Conexão bem sucedida')

#cursor = conexao.cursor()

lista_tabelas2010 = tabula.read_pdf('audienciapublica_rev5.pdf', pages=5)

lista_tabelas2015 = tabula.read_pdf('relatorio-diretoria.pdf', pages=2)

lista_tabelas2020 = tabula.read_pdf('RelatorioADM.pdf', pages=12)


tabelas_na_lista_2010 = []

tabelas_na_lista_2015 = []

tabelas_na_lista_2020 = []


for tabela1 in lista_tabelas2010:
    
    tabelas_na_lista_2010.append(tabela1)


for tabela2 in lista_tabelas2015:

    tabelas_na_lista_2015.append(tabela2)


for tabela3 in lista_tabelas2020:

    tabelas_na_lista_2020.append(tabela3)


tabelas_na_lista_2020.pop(0)


print(tabelas_na_lista_2010)

print(lista_tabelas2015)

print(tabulate(tabelas_na_lista_2020))

tamanho_analise = int(input(f'\nQuantos anos serão analisados ?\t'))

anos = []

frota_na_lista = []

for anos_analise in range(0, tamanho_analise):
    
    quais_anos = str(input(f'\nQual ano será analisado:\t'))
    anos.append(quais_anos)
    frota = int(input(f'\nQual é o tamanho da frota da EMTU em {anos} ?\t'))
    frota_na_lista.append(frota)


porcentagem = 100 - ((frota_na_lista[2])*100/frota_na_lista[0])

plt.plot(anos, frota_na_lista, color= 'red', marker='o', linestyle='solid')
plt.xlabel(f'ANOS: a frota da EMTU na região metropolitana de São Paulo diminuiu {porcentagem:.2f}% em 10 anos')
plt.ylabel('QUANTIDADE DE ÔNIBUS')
plt.show()


#comando = """ INSERT INTO Vendas(id_venda, cliente, produto, data_venda, preco, qunatidade)
#Values
    #(2, 'João', 'Teclado', '16/03/22', 7000, 2)"""

#cursor.execute(comando)
#cursor.commit()




