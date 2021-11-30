velocidade = float(input("Velocidade do carro: "))

limite = 80.00
excedente = velocidade - limite
multa = excedente * 7

if velocidade > limite:
    print("você foi multado. Multa: R$: {:.2f}".format(multa))
else:
    print("você está de acordo com as normas de trânsito")
    
