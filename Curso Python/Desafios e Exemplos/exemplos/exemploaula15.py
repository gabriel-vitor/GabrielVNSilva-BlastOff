n = s = 0
while True:
    n = int(input("digite um número:"))
    if n == 999:
        break
    s += n
print(f'a soma vale {s}')

nome = 'josé'
idade = 33
salario = 987.3
print(f' o {nome} tem {idade} anos') #python 3.6+
print('o {} tem {} anos'.format(nome, idade))#python 3
print('o %s tem %d anos' % (nome, idade)) #python 2
print(f'o {nome} tem {idade} anos e ganha R${salario:.2f}')
