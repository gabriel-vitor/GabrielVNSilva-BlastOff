import random
usuario = 6
escolha = 7
while usuario != escolha:
    escolha = random.randint(0,5)
    usuario = int(input("tente adivinhar o número que o computador pensou:"))

    if usuario == escolha:
        print("Parabéns, você acertou!")
    else:
        print("você errou, tente novamente:")
