from random import randint

lista = []
sorteios = []

jogos = int(input("Quantos jogos deseja sortear?"))
total = 1

while total <= jogos:
    contador = 0
    while True:
        
        num = randint(1, 60)
        if num not in lista:
            lista.append(num)
            contador += 1
        if contador >= 6:
            break
    
    lista.sort()
    sorteios.append(lista[:])
    lista.clear()
    total += 1
    
for i, l in enumerate(sorteios):
    print(f'jogo {i+ 1}: {l}')
    
        