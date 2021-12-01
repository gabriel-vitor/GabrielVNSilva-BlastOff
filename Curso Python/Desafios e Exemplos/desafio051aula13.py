prim = int(input("informe o primeiro termo: "))
razao = int(input("informe a razao da P.A: "))
decimo = prim + (10 - 1) * razao #forma do enesimo termo de uma PA

for c in range(prim, decimo, razao):
    print(c, end = '  ')
print("Fim")
    
        

    