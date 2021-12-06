temperatura = []
meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto',
         'Setembro', 'Outubro', 'Novembro', 'Dezembro']

soma_temp = 0
contador = 0
while contador < 12:
    try:
        temp = int(input("Informe a temperatura do mês de {}: ".format(meses[contador])))
        contador += 1
        temperatura.append(temp)
        soma_temp += temp
    except ValueError:
        print("Digito inválido. Tente novamente")
        
media_temp = soma_temp / 12

print('-'*30)
print("Média anual das temperaturas: {:.2f} °C".format(media_temp))
print('-'*30)

for i in range(0,12):
    if temperatura[i] > media_temp:
        print("O mês de \033[33m{}\033[m está acima da média: {}°C.".format(meses[i], temperatura[i]))

