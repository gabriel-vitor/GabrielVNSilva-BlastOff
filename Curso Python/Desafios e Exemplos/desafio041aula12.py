ano_atleta = int(input("informe o ano de nascimento do atleta:"))
ano_atual = 2021
idade = ano_atual - ano_atleta

if idade <= 9:
    print("MIRIM")

elif idade < 14:
    print("INFANTIL")

elif idade < 19:
    print("JUNIOR")

elif idade == 20:
    print("SENIOR")
else:
    print("MASTER")