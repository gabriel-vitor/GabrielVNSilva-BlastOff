import pandas as pd
import numpy as np

data = {'Sede':['SP','SP','MG','MG','RJ','RJ','ES','ES'],
       'Vendedor':['Jorge','Ana','Tiago','Pedro','Raphaela','Guto','Maria','Carolina'],
       'Vendas':[2000,2500,3100,1200,1500,3900,2900,3900]}

df = pd.DataFrame(data)

#print(df)

#print(df.groupby('Sede'))

by_sede = df.groupby('Sede')

print(by_sede)

vendeu_mais = by_sede.max()                           #quem vendeu mais

media_sede = by_sede.mean()                           #média de vendas de cada sede

estatisticas = by_sede.describe()                     #mostra várias estatisticas

mod_colunaLinha = by_sede.describe().transpose()      #coluna pra linha, linha pra coluna

mod_colunaLinha_SP = by_sede.describe().transpose()['SP']  


print('vendeu mais:\n\n', vendeu_mais)

print('media:\n\n', media_sede)

print('estatisticas:\n\n', estatisticas)

print('mudança de linha e coluna:\n\n', mod_colunaLinha)

print('mudança de linha e coluna SP :\n\n', mod_colunaLinha_SP)


#############################################################################################

arrays = [['São Paulo', 'São Paulo', 'Rio de Janeiro', 'Rio de Janeiro','Minas Gerais','Minas Gerais'],
['Garrafas','Copos','Garrafas','Copos','Garrafas','Copos' ]]
index = pd.MultiIndex.from_arrays(arrays, names=('Estado', 'Produto'))

df1 = pd.DataFrame({'Total Vendido R$': [10000, 35000, 22400, 12890,10880,13900]},index=index)

multi_bysede = df1.groupby('Estado', level = 0)

media2 = multi_bysede.mean()

vendeu_mais2 = multi_bysede.max()

print('multiIndex:\n\n', multi_bysede)
print('média:\n\n',media2)
print('vendeu mais:\n\n', vendeu_mais2)

multi_byproduto = df1.groupby('Produto', level = 1)

media3 = multi_byproduto.mean()
print('-----------produtos-----------')
print('média:\n\n', media3)





