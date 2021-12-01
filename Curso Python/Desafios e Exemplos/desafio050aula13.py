soma = 0 
for c in range(0,7):
    num = int(input("informe um número: "))
    if num % 2 == 0:
        soma = soma + num
print(soma)