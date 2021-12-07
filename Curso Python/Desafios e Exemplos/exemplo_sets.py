s = {1, 3.14, 'Tooddo', 1, 3.14}

print(type(s))
print(s)
print(f'tipo: {type(s)}, Valores: {s}')

x = {1, 2, 3, 4.15}
y = {3, 2, 1, 25}

#operações
print('-'*50)
print('união:', x | y)
print('diferença X - Y:', x - y) #o que tem em X que não tem em Y?
print('diferença Y - X:', y - x) #o que tem em Y que não tem em X?
print('interseção:', x&y)




