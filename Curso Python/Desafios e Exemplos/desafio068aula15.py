import random

controle = True

while controle == True:
    jogador = input("Escolha IMPAR ou PAR:").strip().upper()
    escolha_jogador = int(input("escolha um número:"))
    
    if jogador == 'PAR':
        computador = 'IMPAR'
        escolha_computador = random.randint(0,10)
        soma = escolha_jogador + escolha_computador
        
        if soma % 2 == 0:
            print('Jogador VENCEU')
        else:
            print('Computador VENCEU')
            break
        
    if jogador =='IMPAR':
        computador = 'PAR'
        escolha_computador = random.randint(0,10)
        soma = escolha_jogador + escolha_computador
        
        if soma % 2 == 0:
            print("Computador VENCEU")
            break
        else:
            print("Jogador VENCEU")
    

        
    
        
        
    
    

