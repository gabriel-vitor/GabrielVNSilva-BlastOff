num = int(input("informe um número:"))

controlador = 0
while (controlador == 0):
    escolha = int(input("[1] Binário \n[2]Octal \n[3]Hexadecimal"))
    if escolha == 1:
        binario = str(bin(num))
        print(binario)
        controlador = 1
        
    elif escolha == 2:
        octal = str(oct(num))
        print(octal)
        controlador = 1
        
    elif escolha == 3:
        hexa = str(hex(num))
        print(hexa)
        controlador = 1
        
    else:
        print("digito inválido, tente novamente")
        controlador = 0
        
        
