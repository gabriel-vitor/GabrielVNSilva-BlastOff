def ficha(nome = 'não informado', gols = 0):
    if nome =='':
        return f'Nome do jogador:Desconhecido. Gols:{gols}'
    else:
        return f'Nome do jogador:{nome}. Gols:{gols}'

#Main
nome = input('nome do jogador:')
gols = int(input('quantos gols?'))

resp = ficha(nome, gols)
print(resp)
    
    