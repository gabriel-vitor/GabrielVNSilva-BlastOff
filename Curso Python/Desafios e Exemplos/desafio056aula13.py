soma_idade = 0
media = 0
maior_h = 0
nome_maior = ''
total_m20 = 0

for p in range(1, 5):
    print("Pessoa {}: ".format(p))
    nome = input("Nome:").strip()
    idade = int(input("Idade: "))
    sexo = input("Sexo [M/F]: ").strip()
    soma_idade += idade
    
    if p == 1 and sexo in 'Mm':
        maior_h = idade
        nome_maior = nome
    if sexo in 'Mm' and idade > maior_h:
        maior_h = idade
        nome_maior = nome
    if sexo in 'Ff' and idade < 20:
        total_m20 += 1

media = soma_idade / 4
print("Média de idade", media)
print("Homem mais velho tem {} e seu nome é {}".format(maior_h, nome_maior))
print("Mulheres com menos de 20:", total_m20)
        