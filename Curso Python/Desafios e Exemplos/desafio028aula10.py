import random

escolha = random.randint(0,5)

usuario = int(input("tente adivinhar o número que o computador pensou:"))

if usuario == escolha:
    print("Parabéns, você acertou!")
else:
    print("você errou")