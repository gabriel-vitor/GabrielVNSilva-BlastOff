cores = ['\033[m', '\033[0;30;41m']

def ajuda(com):
    help(com)
    
def titulo(msg, cor = 0):
    tam = len(msg) + 4
    print(cores[cor], end='')
    print('-'*tam)
    print(' ',msg)
    print('-'*tam)
    print(cores[0], end ='')

comando = ''
while True:
    titulo('Sistema de ajuda', 1)
    comando = input('função ou biblioteca: ')
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)
        
titulo('ATÉ LOGO', 1)