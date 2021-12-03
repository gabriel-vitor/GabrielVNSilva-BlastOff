tupla = ('arroz', 'feijao', 'frango')

for p in tupla:
    print(f'\nPalavra {p.upper()} - vogais: ', end='')
    for letra in p:
        if letra.lower() in 'aeiou':
            print(letra, end=' ')

