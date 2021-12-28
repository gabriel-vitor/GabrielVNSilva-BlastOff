import numpy as np

qtd = [2, 5, 10, 20, 35]

custo = [100, 150, 450, 320, 195]

arr1 = np.array(qtd)

arr2 = np.array(custo)

# estoque = qtd * custo                    da erro

estoque = arr1 * arr2

print(estoque)

custo2 = [100, 200, 300, 400]

venda = [125, 235, 355, 490]

arr3 = np.array(custo2)

arr4 = np.array(venda)

lucro = arr4 - arr3
print(lucro)

#arrays a partir do numpy

arr5 = np.arange(10, 20) 

print(arr5)

arr6 = np.arange(10, 21, 2)

print(arr6)

arr7 = np.arange(10, 101, 2, dtype = float)

print(arr7)

arr8 = np.linspace(1, 10, 10) #inicio / fim/ quantidade de espaços

print(arr8)
