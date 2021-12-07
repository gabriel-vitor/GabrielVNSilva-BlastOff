def padrao(numero):
    for linha in range(0, numero):
        num = 1        
        for coluna in range(0, linha + 1):
            print(num, end =' ')
            num = num + 1
        print('\r')
             

#Main
escolha = int(input('Digite um número para imprimir a sequencia padronizada:'))
padrao(escolha)


#outro modo encontrado em:
#https://ichi.pro/pt/como-fazer-programas-de-padroes-python-com-exemplos-129613110223919

'''
def pattern(n):
     for i in range(1, n):
         for j in range(1, i + 1):
             print(j, end= " ")
         print("\r")
pattern(5)
'''