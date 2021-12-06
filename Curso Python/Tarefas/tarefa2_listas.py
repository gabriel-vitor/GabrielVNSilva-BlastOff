from random import randint

vetor = []
contador = 0


for i in range(0, 100):
    lancamento = randint(1, 6)
    vetor.append(lancamento)

print('Lançamentos:')
print(vetor)

print('-' * 30)
print('Ocorrências:')
print('Número 1: ',vetor.count(1))
print('Número 2: ',vetor.count(2))
print('Número 3: ',vetor.count(3))
print('Número 4: ',vetor.count(4))
print('Número 5: ',vetor.count(5))
print('Número 6: ',vetor.count(6))


        