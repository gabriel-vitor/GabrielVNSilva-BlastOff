lista = []
contador = 0
contador_5 = 0
while True:
    num = int(input("Digite um número:"))
    lista.append(num)
    contador += 1
    
    if num == 5:
        contador_5 += 1
    
    escolha = input("Deseja continuar? S/N: ").strip().upper()
    if escolha == 'N':
        break
    
lista.sort(reverse = True)


print("Números digitados: ", contador)
print("Lista decrescente: ", lista)
print("o número 5 foi digitado {} vezes".format(contador_5))

