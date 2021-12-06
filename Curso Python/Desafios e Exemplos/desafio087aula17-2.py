matriz = [[0, 0, 0], [0 ,0, 0], [0, 0, 0]]
somapares = maior = somacoluna = 0

for linha in range(0, 3):
    for coluna in range(0, 3):
        matriz[linha][coluna] = int(input(f'digite um valor na posição [{linha}, {coluna}]: '))
        
for linha in range(0, 3):
    for coluna in range(0,3):
        print(f'[{matriz[linha][coluna]}]', end = '')
        if matriz[linha][coluna] % 2 ==0:
            somapares += matriz[linha][coluna]
    print()
    
for linha in range(0, 3):
    somacoluna += matriz[linha][2]
    
for coluna in range(0, 3):
    if coluna == 0:
        maior = matriz[1][coluna]
    elif matriz[1][coluna] > maior:
        maior = matriz[1][coluna]

print('Maior número da segunda linha:', maior)
print('Soma da terceira coluna', somacoluna)
print('Soma de todos os pares:', somapares)
        
