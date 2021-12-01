preco = float(input("informe o preço do produto: "))

controlador = 0
while (controlador == 0):
    print("[1] A VISTA EM DINHEIRO/CHEQUE")
    print("[2] A VISTA CARTÃO")
    print("[3] 2X CARTÃO")
    print("[4] 3X OU MAIS NO CARTÃO\n")
    escolha = int(input())

    if escolha == 1:
        preco = preco - (preco * 0.10)
        print("Preço com desconto R$:", preco)
        controlador = 1
        
    elif escolha == 2:
        preco = preco - (preco *0.05)
        print("Preço com desconto R$: ", preco)
        controlador = 1
        
    elif escolha == 3:
        print("o mesmo preço R$: ", preco)
        controlador = 1
        
    elif escolha == 4:
        preco = preco + (preco * 0.20)
        print("Preço com Juros R$: ", preco)
        controlador = 1

    else:
        print("opção inválida, tente novamente")
        print(" ")
        