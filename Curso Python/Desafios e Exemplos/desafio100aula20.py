from random import randint

def sorteia(lista):
    for contador in range(0,5):
        num = randint(1, 10)
        lista.append(num)
    
def somaPar(lista):
    soma = 0;
    for valor in lista:
        if valor % 2 == 0:
            soma = soma + valor
    print('Soma:', soma)            
                
    
#Main
numeros = []
sorteia(numeros)
print(numeros)
somaPar(numeros)