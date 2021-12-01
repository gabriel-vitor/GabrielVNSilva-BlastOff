maior = 0
menor = 1000
for c in range(1,6):
    peso = float(input("{} - informe seu peso:".format(c)))
    if peso == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso 
print("o maior peso é:", maior)
print("o menor peso é:", menor) 
    
    