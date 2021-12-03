lista = []
for i in range(0,5):
    num = int(input("informe um número:"))
    lista.append(num)

print(lista)

lista = sorted(lista)

print(lista)

print("Menor:", lista[0])
print("Maior:", lista[-1])