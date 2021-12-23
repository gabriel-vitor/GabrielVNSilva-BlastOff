import pandas as pd
import numpy as np

lista = [['BRASIL', 'BRASIL', 'BRASIL','ARGENTINA', 'ARGENTINA', 'ARGENTINA'], [2017, 2018, 2019, 2017, 2018, 2019]]

tuplas = zip(*lista)

tuplas = list(tuplas)

print(tuplas)

multi = pd.MultiIndex.from_tuples(tuplas)

print(multi)

df1 = pd.DataFrame(data = np.random.randn(6,2), index = multi, columns = ['EXP TRIGO', 'EXP ARROZ'])

print(df1)

df1.index.names = ['PAÍS', 'ANO']

print(df1)

#encontrando valores
print(df1['EXP ARROZ'])

print(df1.loc['BRASIL'])


#print(df1.loc[2017])             #da erro
print(df1.xs(2017, level=1))      #correto, tem que especificar o level do indice

print(df1[:2])

print(df1[0:5])

print(df1[['EXP TRIGO', 'EXP ARROZ']])

#Vendo o DF de outra maneira

print(df1.unstack())

df2 = df1.unstack()

print(df2)

print(df2['EXP TRIGO'])

print(df2.xs(2017, axis = 1, level = 1))

