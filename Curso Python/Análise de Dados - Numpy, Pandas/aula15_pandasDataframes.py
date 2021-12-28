import pandas as pd
import numpy as np

#criação de dataframe a partir de um array

arr = np.random.randint(10,55, size=(4,4))

print(arr)

df1 = pd.DataFrame(data=arr, index=['A','B','C','D'], columns = ['W', 'X', 'Y', 'Z'])

print(df1)

#criação de dataFrames a partir de listas

lista = [[10, 20, 30, 40, 50],[60, 70, 80, 90, 100], [110, 120, 130, 140, 150]]

df2 = pd.DataFrame(data=lista, index=['a','b','c'], columns=['v','w','x', 'y', 'z'])
print()
print(df2)

#criação de dataframes através de um dicionário

dados = {'produtos':['video game','pc' ,'teclado', 'mouse', 'microfone'], 'preço':[2600, 2450, 99.90, 75, 129]}

df3 = pd.DataFrame(data=dados)
print(df3)

#criando uma nova coluna

df3['custo'] = [1900, 2000, 40, 56, 95]
print()
print(df3)

df3['lucro'] = df3['preço'] - df3['custo']

print(df3)