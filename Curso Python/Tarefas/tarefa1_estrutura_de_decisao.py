num1 = float(input("informe o primeiro número: "))
num2 = float(input("informe o segundo número: "))

print("qual operação deseja realizar?")
escolha = input("A) Par ou Impar \nB)Positivo ou Negativo \nC)Inteiro ou Decimal\n").upper()

if escolha == 'A':
    ip_num1 = num1 % 2
    ip_num2 = num2 % 2
    if ip_num1 == 0 and ip_num2 == 0:
        print("os dois números são pares")
    elif ip_num1 == 0 and ip_num2 != 0:
        print("o primeiro número é par e o segundo é ímpar")
    elif ip_num1 != 0 and ip_num2 == 0:
        print("o primeiro número é ímpar e o segundo é par")
    else:
        print("os dois são ímpares")
        
elif escolha == 'B':
    if num1 > 0 and num2 > 0:
        print("os dois números são positivos")
    elif num1 > 0 and num2 <0:
        print("o primeiro número é positivo e o segundo é negativo")
    elif num1 < 0 and num2 >0:
        print("o primeiro número é negativo e o segundo é positivo")
    else:
        print("os dois números são negativos")
        
elif escolha == 'C':
    intdec_num1 = float.is_integer(num1)
    intdec_num2 = float.is_integer(num2)
    if intdec_num1 == True and intdec_num2 == True:
        print("os dois números são inteiros")
    elif intdec_num1 == False and intdec_num2 == False:
        print("os dois são decimais")
    elif intdec_num1 == True and intdec_num2 == False:
        print("o primeiro é inteiro e o segundo é decimal")
    else:
        print("o primeiro é decimal e o segundo é inteiro")

else:
    print("Dado inválido")