matriz = [[0, 0, 0], [0 ,0, 0], [0, 0, 0]]

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'digite um valor na posição [{linha}, {coluna}]: '))
        
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]}]', end = '')
    print()
        