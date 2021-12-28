import pandas as pd
import numpy as np

#series a partir de uma lista

lista = [10, 20, 30, 40, 50]

visualizacao = pd.Series(lista)

print(visualizacao)

print(visualizacao[1])

#series a partir de um dicionário

dict = {'telefone': '9999999', 'telefone2':'2398749832', 'telefone3':'93287439'}

visualizacao2 = pd.Series(dict)

print(visualizacao2)

print(visualizacao2[2])
print(visualizacao2['telefone3'])

#series a partir de um array

arr = np.array([10, 20, 30, 40 ,50])

visualizacao3 = pd.Series(arr)

print(visualizacao3)

visualizacao4 = pd.Series([10, 20, 30, 40, 50])

visualizacao5 = pd.Series([1, 2, 3, 4], index=['brasil', 'usa', 'argentina','chile'])

print(visualizacao5)

lista = [1, 2, 3, 4]

labels = ['brasil','usa', 'argentina', 'chile']

visualizacao6 = pd.Series(data = lista, index=labels)

print(visualizacao6)

visualizacao7 = pd.Series(data=[2, 4, 6, 8], index = ['brasil', 'usa', 'chile', 'uruguai'])

print(visualizacao7)

print(visualizacao6 + visualizacao7)