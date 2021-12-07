from random import randint
from operator import itemgetter

jogo = {'jogador1':randint(1,6),'jogador2':randint(1,6), 'jogador3':randint(1,6),'jogador4':randint(1,6)}

ordem = list()

for key, value in jogo.items():
    print(f'{key} tirou {value}')

print('-'*30)
    
ordem = sorted(jogo.items(), key=itemgetter(1), reverse=True) #ou seja, do indice 1 que é o value
print(ordem)

print('-'*30)

for indice, value in enumerate(ordem):
    print(f'{indice + 1} lugar: {value[0]} com {value[1]}.')


