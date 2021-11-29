limite = 50
peso = float(input("informe o peso de peixes: "))
excesso = peso - limite

if excesso < 1:
    print("Está tudo certo")
else:
    
    multa = excesso * 4.00
    print("o excesso é {} kg:".format(excesso))
    print("a multa é de R$: ", multa)    
