r1 = int(input("informe o tamanho da reta 1:"))
r2 = int(input("informe o tamanho da reta 2:"))
r3 = int(input("informe o tamanho da reta 3:"))

if r1 + r2 > r3 and r1 + r3 > r2 and r3 + r2 > r1:
    print("pode formar um triângulo")
    if r1 == r2 == r3:
        print("Equilátero")
    elif r1 != r2 != r3 != r1:
        print("ESCALENO")
    else:
        print("ISÓSCELES")
    
else:
    print("não pode formar um triângulo")
