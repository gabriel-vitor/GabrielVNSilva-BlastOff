lista = []

contador = 0
while True:
    nome = input("Nome:")
    nota1 = float(input('Nota1: '))
    nota2 = float(input('Nota2: '))

    media = (nota1 + nota2) / 2

    lista.append([nome, [nota1, nota2], media])
    contador += 1
    escolha = input("Deseja continuar? S/N").strip().upper()
    if escolha == 'N':
        break
    
print(f'{"N: ":<4}{"NOME ":<10}{"MEDIA ":>8}')

for i, a in enumerate(lista):
    print(f'{i:<4}{a[0]:<10}{a[2]:>8.1f}')
    
print('-'*30)
while True:
    opcao = int(input('Mostrar notas de qual aluno? (999 interrompe):'))
    if opcao == 999:
        break
    if opcao <= len(lista) - 1:
        print(f'notas de {lista[opcao][0]} são {lista[opcao][1]}')
        
    

