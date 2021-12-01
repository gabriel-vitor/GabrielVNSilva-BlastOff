peso = float(input("informe seu peso: "))
altura = float(input("informe sua altura:"))

imc = peso / (altura * altura)

if imc < 18.5:
    print("abaixo do peso")
elif imc < 25:
    print("peso ideal")
elif imc < 30:
    print("sobrepeso")
elif imc < 40:
    print("obesidade")
else:
    print("obesidade mórbida")