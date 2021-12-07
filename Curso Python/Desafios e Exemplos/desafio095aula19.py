time = []
jogador = {}
lista_partidas = []

while True:
    jogador.clear()
    jogador['nome'] = input('Nome do jogador: ')

    total_partidas = int(input('Quantidade de partidas jogou? '))

    for contador in range(0, total_partidas):
        lista_partidas.append(int(input(f'Quantidade de gols na partida {contador}: ')))
        
    jogador['gols'] = lista_partidas[:]
    jogador['total'] = sum(lista_partidas) #soma dos itens da lista
    time.append(jogador.copy())
    while True:
        escolha = input('Deseja continuar? S/N').strip().upper()
        if escolha == 'S' or escolha =='N':
            break
        print('erro, tente novamente')
    if escolha == 'N':
        break
    
print('-'*30)
print(time)

    
    
    





