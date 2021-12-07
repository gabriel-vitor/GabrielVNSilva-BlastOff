aluno = dict()

nome = input('digite seu nome:')
media = float(input('informe sua média'))
aluno['nome'] = nome
aluno['media'] = media

print('Nome:', aluno['nome'])
print('Media:', aluno['media'])

if aluno['media'] > 7.0:
    print('Situação: Aprovado')
else:
    print('Situação: Reprovado')
    
    