'''
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste)
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste)
print(galera)
'''


'''
teste = list()
teste.append('Gustavo')
teste.append(40)
galera = list()
galera.append(teste[:])
teste[0] = 'Maria'
teste[1] = 22
galera.append(teste[:])
print(galera)
'''

'''
galera = [['Joao', 19], ['Ana', 33], ['Joaquim', 13], ['Maria', 45]]
print(galera[0][0])
print(galera[2][1])

for p in galera:
    print(p)
    print(p[0])
    print(p[1])

'''


galera = list()

dado = list()

for c in range(0, 3):
    dado.append(str(input('nome:')))
    dado.append(int(input('idade:')))
    galera.append(dado[:])
    dado.clear()
print(galera)


totmai = totmen = 0

'''
for c in range(0, 3):
    dado.append(str(input('nome:')))
    dado.append(int(input('idade:')))
    galera.append(dado)
    dado.clear()
'''   

for p in galera:
    if p[1] >= 21:
        print(f'{p[0]} é maior de idade')
        totmai += 1
    else:
        print(f'{p[0]} é menor de idade.')
        totmen += 1
        
print(f'temos {totmai} maiores e {totmen} menores de idade')
    

