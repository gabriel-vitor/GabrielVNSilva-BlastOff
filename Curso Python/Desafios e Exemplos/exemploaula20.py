'''
def soma(a, b):
    print(f'A = {a} e B = {b}')
    s = a + b
    print(s)
    print(f'a soma de A+B = {s}')


#Main
soma(4, 5)
soma(8, 9)
soma(2, 1)
soma(b=2,a=1) # é possível trocar a ordem
'''

def contador(*num):
    #print(num)
    for valor in num:
        print(valor, end='')

def dobra(lst):
    pos = 0
    while pos < len(lst):
        lst[pos] = lst[pos] * 2
        pos += 1
        
def soma(*valores):
    s=0
    for num in valores:
        s += num
        
    print(f'somando os valores {valores} temos {s}')

#Main
        
valores = [6, 3 ,9, 0, 1 ,2]
dobra(valores)
print(valores)
contador(2, 1, 7)

soma(5,2)
soma(2, 9, 4)





