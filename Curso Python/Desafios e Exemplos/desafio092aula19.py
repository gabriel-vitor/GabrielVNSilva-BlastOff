from datetime import datetime

dados = dict()
dados['nome'] = input('nome:')
nasc = int(input('ano de nascimento:' ))
dados['idade'] = datetime.now().year - nasc
dados['ctps'] = int(input('carteira de trabalho:(0 não tem):'))
if dados['ctps'] != 0:
    dados['contratação'] = int(input('ano de contratação: '))
    dados['salario'] = float(input('Salário? : R$')) 
    dados['aposentadoria'] = dados['idade'] + ((dados['contratação'] + 35) - datetime.now().year)

print(dados)

print('-'*30)

for key, value in dados.items():
    print(f'{key} : {value}')