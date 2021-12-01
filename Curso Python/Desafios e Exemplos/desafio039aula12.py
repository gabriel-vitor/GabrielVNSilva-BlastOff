ano = int(input("informe seu ano de nascimento"))

ano_atual = 2021
idade = ano_atual - ano

if idade < 18:
    print("ainda vai se alistar ao serviço militar")
    falta = 18 - idade
    print("ainda falta {} anos".format(falta))
    
elif idade == 18:
    print("é a hora de se alistar")

else:
    print("já passou o tempo do alistamento")
    passou = idade - 18
    print("passou-se {} anos".format(passou))
    
    