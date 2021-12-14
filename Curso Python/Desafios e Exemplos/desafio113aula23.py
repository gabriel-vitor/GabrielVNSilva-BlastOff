def leiaInt(msg):
    while True:
        try:
            n = int(input(msg))
        except (ValueError, TypeError):
            print('digite um número inteiro válido:')
            continue
        except (KeyboardInterrupt):
            print('entrada de dados interrompida pelo usuario')
            return 0
        else:
            return n
           
def leiaFloat(msg):
    while True:
        try:
            n = float(input(msg))
        except (ValueError, TypeError):
            print('digite um número float válido')
        except (KeyboardInterrupt):
            print('usuario decidiu não digitar esse numero')
            return 0
        else:
            return n
    
    
#Main
n = leiaFloat('digite um número real: ')

num = leiaInt('digite um número inteiro:')
print(n)
print(num)


    