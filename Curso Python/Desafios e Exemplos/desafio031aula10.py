distancia = float(input("informe a distancia da viagem em Km:"))

passagem = 0.50

if distancia > 200:
    passagem = 0.45
    valor_passagem = distancia * passagem
    print("valor da passagem é R$: {}".format(valor_passagem))
else:
    valor_passagem = distancia * passagem
    print("valor da passagem é R$: {}".format(valor_passagem))

