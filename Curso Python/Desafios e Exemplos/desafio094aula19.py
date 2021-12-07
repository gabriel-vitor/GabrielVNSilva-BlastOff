pessoa = {}
grupo = []
somaidade = 0
contador = 0
lista_mulher = []
while True:
    pessoa['nome'] = input('informe o nome: ')
    pessoa['sexo'] = input('informe o sexo [M/F]: ').strip().upper()
    pessoa['idade'] = int(input('informe a idade: '))
    
    grupo.append(pessoa.copy())
    somaidade = somaidade + pessoa['idade']
    contador += 1
    
    if pessoa['sexo'] == 'F':
        lista_mulher.append(pessoa['nome'])
        
    escolha = input('Deseja continuar? S/N: ').strip().upper()
    if escolha == 'N':
        break
    
media = somaidade / contador
print(f'O grupo tem {len(grupo)} pessoas')
print(f'A média de idade é de {media:.2f} anos')
print(f'As mulheres cadastradas foram:')
print('-'*30)

for m in lista_mulher:
    print(m)
    
for p in grupo:
    if p['idade'] > media:
        print(f'Acima da média: {p["nome"]} com {p["idade"]} anos')


    
    

