def leiaInt(msg):
    ok = False
    valor = 0
    while True:
        n = input(msg)
        if n.isnumeric():
            valor = int(n)
            ok = True
        else:
            print('Inválido, digite novamente')
        if ok:
            break
    return valor
    

#Main
resp = leiaInt('digite um número:')

print(resp)


    
    