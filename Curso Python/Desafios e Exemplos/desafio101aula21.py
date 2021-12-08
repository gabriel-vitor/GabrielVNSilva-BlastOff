def voto(nascimento):
    from datetime import date
    ano_atual = date.today().year
    idade = ano_atual - nascimento
    if idade < 16:
        return f'{idade}: Não pode votar'
    elif 16 <= idade < 18 or idade > 65:
        return f'{idade}: voto opcional'
    else:
        return f'{idade}: obrigatório'
    

#Main
nasc = int(input('Em que ano você nasceu?:'))
print(voto(nasc))
