lista = []
while True:
    num = int(input("digite um número"))
    if num in lista:
        print("esse número já está na lista")
    else:
        lista.append(num)
    escolha = input("deseja continuar? S/N").upper()
    if escolha == 'N':
        break

print(lista)
lista = sorted(lista)
print(lista)
        