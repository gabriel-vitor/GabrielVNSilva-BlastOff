nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2


if media < 4.0:
    print("REPROVADO - E")
elif media < 6.0:
    print("REPROVADO - D")
elif media < 7.5:
    print("APROVADO - C")
elif media < 9.0:
    print("APROVADO - B")
else:
    print("APROVADO - A")


#as estruturas de decisão tembém pode ser escritas dessa forma:
'''
if media >= 0 and media < 4.0:
    print("REPROVADO - E")
elif media >= 4.0 and media < 6.0:
    print("REPROVADO - D")
elif media >= 6.0 and media < 7.5:
    print("APROVADO - C")
elif media >= 7.5 and media < 9.0:
    print("APROVADO - B")
else:
    print("APROVADO - A")
'''    