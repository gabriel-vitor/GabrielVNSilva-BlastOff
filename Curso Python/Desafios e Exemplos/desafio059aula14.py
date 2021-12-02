condicao = True

num1 = int(input("Num1: "))
num2 = int(input("Num2: "))

while condicao == True:
    
    print('[1] - Somar \n[2] - Multiplicar \n[3] - Maior \n[4] - novos números \n[5] - sair do programa')
    escolha = int(input())
    if escolha == 1:
        print("soma: ", num1+num2)
        condicao = False
        
    elif escolha == 2:
        print("multiplicação: ", num1 * num2)
        condicao = False
        
    elif escolha == 3:
        if num1 > num2:
            print("Maior: {} -> {}".format('num1',num1))
        elif num1 < num2:
            print("Maior: {} -> {}".format('num2',num2))
        else:
            print("números iguais")
        condicao = False
        
    elif escolha == 4:
        num1 = int(input("Num1: "))
        num2 = int(input("Num2: "))
        condicao = True
        
    elif escolha == 5:
        break
    else:
        print("Digito inválido, tente novamente")
        condicao = True