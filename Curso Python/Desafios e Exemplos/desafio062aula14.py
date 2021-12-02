controle = 1
prim = int(input("informe o primeiro termo: "))
razao = int(input("informe a razao da P.A: "))
quant_termo = int(input("informe a quantidade de termos que quer mostrar:"))
while controle == 1:

    termo = prim
    cont = 1

    while cont <= quant_termo:
        print(" {} ->".format(termo), end = '')
        termo += razao
        cont += 1
    print("fim")
    
    print("deseja mostrar mais termos?[0] não [1] sim")
    escolha = int(input())
    if escolha == 1:
        quant_termo = int(input("informe a quantidade de termos que quer mostrar:"))
        controle = 1
    else:
        controle = 0