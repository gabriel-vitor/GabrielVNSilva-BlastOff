
num = int(input("Informe um número:"))
fatorial = 1
i = 2
while i <= num:
    fatorial = fatorial*i
    i = i + 1
    
print("fatorial: ", fat)

#ou
'''
from math import factorial

n = int(input("digite um número para calcular o fatorial"))
f = factorial(n)
print("fatorial: ", n)

'''
#ou

'''
n = int(input("digite um número para calcular o fatorial: "))
c = n
f = 1
#fator de multiplicação limpa começa com 1, soma começa com 0

while c > 0:
    print('{} '.format(c), end = '')
    print('x ' if c > 1 else ' = ', end = '')
    f = f * c
    c -= 1
print(f)
'''   



