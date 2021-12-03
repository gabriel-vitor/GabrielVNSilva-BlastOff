tupla = ('caderno', 3.50,
         'pulseira', 1.00,
         'régua', 2.50,
         'caneta', 2.00)

for i in range(0, len(tupla)):
    if i % 2 == 0:
        print(f'{tupla[i]:.<30}', end='')
    else:
        print(f'R$ {tupla[i]:.>4.2f}')