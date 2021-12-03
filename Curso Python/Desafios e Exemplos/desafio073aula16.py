tabela = ('Atletico MG', 'Flamengo', 'Palmeiras', 'Corinthians', 'Bragantino', 'Fortaleza',
          'Fluminense', 'America MG', 'Ceará', 'Internacional', 'Santos', 'São Paulo',
          'Atlético GO', 'Juventude', 'Cuiabá', 'Athletico PR', 'Bahia', 'Gremio',
          'Sport', 'Chapecoense')

print("Os cinco primeiros colocados são:", tabela[0:5])
print()
print("Os 4 últimos são:", tabela[16:20]) #ou tabela[-4:0]
print()
print("Ordem alfabética", sorted(tabela))
print()
print('Chapecoense está na posição:', tabela.index('Chapecoense')+1 )
