from random import randint

tupla = [0,0,0,0,0]

for i in range(0, 5):
    tupla[i] = randint(1,10)

print(tupla)

ordenado = sorted(tupla)

print('menor valor:', ordenado[0])
print('maior valor:',ordenado[-1])    