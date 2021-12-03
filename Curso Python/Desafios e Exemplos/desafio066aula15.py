cont = 0
num = 0
soma = 0
while num != 999:
    num = int(input("digite um número"))
    if num != 999:
        cont = cont + 1
        soma = soma + num
    else:
        print("Saindo")
        
print("Soma: ", soma)
print("Quantidade: ", cont)