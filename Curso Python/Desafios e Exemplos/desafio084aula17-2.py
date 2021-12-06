grupo = []
pessoa = []

while True:
    pessoa.append(input('digite o nome:'))
    pessoa.append(int(input('informe seu peso')))
    grupo.append(pessoa[:])
    pessoa.clear()
    escolha = input("deseja continuar? S/N").strip().upper()
    if escolha == 'N':
        break
    

print(grupo)

print("Quantidade de pessoas cadastradas:", len(grupo))
print('-' *30)

print("listagem de pesados:")
for peso in grupo:
    if peso[1] > 70:
        print(peso[0])
print('-'*30)

print("listagem de leves:")
for peso in grupo:
    if peso[1] < 70:
        print(peso[0])
        



    
    