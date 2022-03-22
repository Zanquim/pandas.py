import pandas as pd
import numpy as np
from matplotlib import pyplot as plt

rmsp = pd.read_excel('populacao_rmsp.xlsx')

rmsp = pd.DataFrame(rmsp)

#print(rmsp)

print(rmsp.loc[rmsp['REGIAO METROPOLITANA'] == 'Região Metropolitana de São Paulo'])

list_demografia = []

list_anos = []

for ano in range(2009, 2020):
    ano += 1
    list_anos.append(ano)


populacao2010 = rmsp.loc[55, 'Pop_2010']

list_demografia.append(f'{(populacao2010/10**6):.1f}')

populacao2011 = rmsp.loc[55, 'Pop_2011']

list_demografia.append(f'{(populacao2011/10**6):.1f}')

populacao2012 = rmsp.loc[55, 'Pop_2012']

list_demografia.append(f'{(populacao2012/10**6):.1f}')

populacao2013 = rmsp.loc[55, 'Pop_2013']

list_demografia.append(f'{(populacao2013/10**6):.1f}')

populacao2014 = rmsp.loc[55, 'Pop_2014']

list_demografia.append(f'{(populacao2014/10**6):.1f}')

populacao2015 = rmsp.loc[55, 'Pop_2015']

list_demografia.append(f'{(populacao2015/10**6):.1f}')

populacao2016 = rmsp.loc[55, 'Pop_2016']

list_demografia.append(f'{(populacao2016/10**6):.1f}')

populacao2017 = rmsp.loc[55, 'Pop_2017']

list_demografia.append(f'{(populacao2017/10**6):.1f}')

populacao2018 = rmsp.loc[55, 'Pop_2018']

list_demografia.append(f'{(populacao2018/10**6):.1f}')

populacao2019 = rmsp.loc[55, 'Pop_2019']

list_demografia.append(f'{(populacao2019/10**6):.1f}')

populacao2020 = rmsp.loc[55, 'Pop_2020']

list_demografia.append(f'{(populacao2020/10**6):.1f}')

delta_crescimento = populacao2020 - populacao2010

porcentagem = delta_crescimento*100/populacao2020

#plt.plot(list_anos, list_demografia, color= 'green', marker='o', linestyle='solid')

plt.bar(list_anos, list_demografia)

#plt.plot(vendedores_positivos, p_a_positivo, color= 'blue', marker='o', linestyle='solid')

plt.title('POPULAÇÃO REGIÃO METROPOLITANA DE SÃO PAULO')

plt.ylabel('POPULAÇÃO EM MILHÕES')

plt.xlabel(f'ANOS: A população da região metropolitana de São Paulo cresceu {porcentagem:.2f}% em 10 anos')

plt.show()

