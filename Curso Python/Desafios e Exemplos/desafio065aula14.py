soma = digitos = contador = media = menor = maior = 0
while contador == 0:
    num = int(input("digite um número"))
    soma = soma + num
    digitos = digitos + 1
    if digitos == 1:
        maior = menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    contador = int(input("deseja continuar? [0]Sim - [1]Não"))
    
media = soma / digitos
print("números digitados:", digitos)
print("media:", media)
print("menor: {} maior {}".format(menor, maior))
    