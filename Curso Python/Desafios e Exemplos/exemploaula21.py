'''

def par(n=0):
    if n % 2 ==0:
        return True
    else:
        return False
    
#Main
num = int(input())
print(par(num))
'''


'''
def fatorial(num = 1):
    f = 1
    for contador in range(num, 0, -1):
        f *= contador
    return f


#Main
n = int(input('digite um número'))
print('fatorial:', fatorial(n))
'''

'''
def somar (a = 0, b = 0, c = 0): #parametros opcionais
     
    s = a+b+c
    print(s)
    

somar(3, 2, 0)    #funciona
somar(3, 2)       #funciona
#somar(3, 3, 5, 8) #não funciona

somar(b=4, c =2)
somar(a=3, b=2)
'''

'''
def teste():
    x = 8 #variavel local
    print('N vale:', n)
    print('x vale:', x)
    
#Main
n = 2 #variavel global
print('n vale:', n)
teste()
# print(' no Main, x vale:', x) não funciona
'''

'''
def teste(b):
    global a  #mesmo criando outra variavel a, ele utilizará o global A
    a=8
    b+= 4
    c=2
    print(a)
    print(b)
    print(c)
    
    

#Main
    
a = 5
teste(a)
'''

'''
def somar (a = 0, b = 0, c = 0): #parametros opcionais
     
    s = a+b+c
    #print(s)
    return s
    


resp = somar(3,2,5)
somar(3, 2, 5)    
somar(2, 2)
somar(4)
print(resp)
'''



