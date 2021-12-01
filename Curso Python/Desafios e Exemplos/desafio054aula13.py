soma_maior = 0
soma_menor = 0
ano_atual = 2021

for c in range(1, 8):
    ano_nasc = int(input("{} - informe seu ano de nascimento:".format(c)))
    idade = ano_atual - ano_nasc
    if idade < 18:
        soma_menor += 1
    else:
        soma_maior += 1
print("maiores:", soma_maior)
print("menores:", soma_menor)
        
