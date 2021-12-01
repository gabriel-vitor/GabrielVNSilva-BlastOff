from random import randint

jokempo = ('pedra', 'papel', 'tesoura')
computador = randint(0, 2)

print("Escolha uma opção: \n[0]pedra \n[1]papel \n[2]tesoura\n")
escolha = int(input())

print("Computador jogou {} e o usuário jogou {} ".format(jokempo[computador], jokempo[escolha])) 

if computador == 0 and escolha == 0:
    print("EMPATE")
elif computador == 1 and escolha == 1:
    print("EMPATE")
elif computador == 2 and escolha == 2:
    print("EMPATE")

elif computador == 0 and escolha == 1:
    print("USUARIO VENCEU")
elif computador == 0 and escolha == 2:
    print("COMPUTADOR VENCEU")
    
elif computador == 1 and escolha == 0:
    print("COMPUTADOR VENCEU")
elif computador == 1 and escolha == 2:
    print("USUARIO VENCEU")
elif computador == 2 and escolha == 0:
    print("USUARIO VENCEU")
elif computador == 2 and escolha == 1:
    print("COMPUTADOR VENCEU")




