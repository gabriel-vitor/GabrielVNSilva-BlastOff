soma_num = 0 #quantidade de números digitados
contador = 0
soma = 0 #soma dos valores
while contador ==0:
    num = int(input("digite um número"))
    if num != 999:
        soma_num += 1
        soma = soma + num
    else:
        contador = 1
    
print("a soma dos números é :", soma)
print("quantidade de números digitados é:", soma_num)
