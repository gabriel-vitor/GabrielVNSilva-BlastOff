salario = float(input("informe seu salário: "))

if salario > 1250.00:
    novo_salario = (salario * 0.10) + salario
    print("Seu novo salário é:", novo_salario)
else:
    novo_salario = (salario * 0.15) + salario
    print("Seu novo salário é:", novo_salario)    
