nota1 = float(input("informe a nota1: "))
nota2 = float(input("informe a nota2: "))

media = (nota1 + nota2) / 2

if media < 5:
    print("Reprovado")
    
elif media >= 5 and media < 7:
    print("Recuperação")
    
else:
    print("Aprovado")