lista = []
lista_par = []
lista_impar = []

while True:
    num = int(input("digite um número: "))
    lista.append(num)
    
    escolha = input("Deseja continuar? S/N: ").strip().upper()
    if escolha == 'N':
        break

for i, v in enumerate(lista):
    if v % 2 == 0:
        lista_par.append(v)
    else:
        lista_impar.append(v)
        
print("lista: ", lista)
print("lista de pares: ",lista_par)
print("lista de impares :",lista_impar)