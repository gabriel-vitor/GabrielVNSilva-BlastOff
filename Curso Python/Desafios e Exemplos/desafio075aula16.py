tupla = [0,0,0,0]
contador = 0
contador_pares = 0

for i in range(0,4):
    tupla[i] = int(input("informe um valor: "))
    if tupla[i] == 9:
        contador = contador + 1
    if tupla[i] % 2 == 0:
        contador_pares = contador_pares + 1
        



print("o número 9 apareceu {} vezes".format(contador))

if 3 in tupla:
    indice_tres = tupla.index(3)
    print("o número 3 aparece na posição: ", indice_tres)
else:
    print("número 3 não foi digitado")

print("quantidade de números pares:", contador_pares)
print(tupla)