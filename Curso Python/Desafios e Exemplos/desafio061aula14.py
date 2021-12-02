prim = int(input("informe o primeiro termo: "))
razao = int(input("informe a razao da P.A: "))
termo = prim
cont = 1

while cont <= 10:
    print(" {} ->".format(termo), end = '')
    termo += razao
    cont += 1
print("fim")



