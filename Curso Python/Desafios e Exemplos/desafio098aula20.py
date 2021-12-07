def contador(inicio, fim, passo):
    for i in range(inicio, fim+1, passo):
        print(i)
        
        
#Main
contador(0, 10, 1)
contador(10, -1, -1)

escolha = int(input('Qual contagem deseja fazer? [1] crescente [2]decrescente'))

if escolha == 1:
    inicio = int(input('informe o ínicio da contagem:'))
    fim = int(input('informe o fim da contagem:'))
    passo = int(input('informe o passo da contagem:'))
    contador (inicio, fim, passo)
else:
    inicio = int(input('informe o inicio da contagem:'))
    contador (inicio, -1, -1)    

