'''
pessoas = {'nome':'Gustavo', 'sexo':'M', 'idade':22}
print(pessoas)
#print(pessoas[0]) #error
print(pessoas['idade'])

print("-"*30)

print(f'o {pessoas["nome"]} tem {pessoas["idade"]} anos') #as aspas precisam ser diferentes
print(pessoas.keys())
print(pessoas.values())
print(pessoas.items())

print("-"*30)

for key in pessoas.keys():
    print(key)

print("-"*30)

for value in pessoas.values():
    print(value)
    
print("-"*30)

for key, value in pessoas.items():  #ao invés de usar enumerate, usa-se items()
    print(f'{key} = {value}')
    
print("-"*30)

del pessoas['sexo']
pessoas['nome'] = 'leandro'

for key, value in pessoas.items():  #ao invés de usar enumerate, usa-se items()
    print(f'{key} = {value}')
    
print("-"*30)

pessoas['peso'] = 98.5

for key, value in pessoas.items():  #ao invés de usar enumerate, usa-se items()
    print(f'{key} = {value}')
'''
'''
brasil = []
estado1 = {'UF':'Rio de Janeiro', 'sigla':'RJ'}
estado2 = {'UF':'São Paulo', 'sigla':'SP'}

brasil.append(estado1)
brasil.append(estado2)

print(estado1)
print("-"*30)
print(estado2)
print("-"*30)
print(brasil)
print(brasil[0])
print(brasil[1])
print(brasil[0]['UF'])
print(brasil[1]['sigla'])
'''
'''
estado = dict()
brasil = list()

for contador in range (0,3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('sigla:'))
    brasil.append(estado)
print(brasil)

#todos os dados ficarão iguais ao ultimo adicionado, e não é possivel fazer
#fatiamento com [:] como nas listas
'''

estado = dict()
brasil = list()

for contador in range (0,3):
    estado['uf'] = str(input('Unidade Federativa:'))
    estado['sigla'] = str(input('sigla:'))
    brasil.append(estado.copy())  #agora irá funcionar sem igualar todos os dados
print(brasil)

print("-"*30)

for estados in brasil:
    print(estados)

print("-"*30)

for estados in brasil:
    for key, value in estados.items():
        print(f'o campo {key} tem valor {value}')

print("-"*30)
        
for estados in brasil:
    for value in estados.values():
        print(value) 
        


