lanche = ('hamburguer', 'suco', 'pizza', 'pudim')

#sao imutaveis

print(lanche[-2])
print(lanche[1:3])

print(len(lanche))

for comida in lanche:
    print(f'eu vou comer {comida}')
print("comi pra caramba")

'''
for cont in range(0, len(lanche)):
    print(cont)
    print(lanche[cont])
'''
'''
for cont in range(0, len(lanche)):
    print(cont)
    print(f'eu vou comer {lanche[cont]}')
    
print(sorted(lanche))
print(lanche)
'''

a = (2, 5, 4)
b = (5, 8, 1, 2)
c = b + a
print(c.count(5))
print(c.count(9))
print(c.index(8)) 

    