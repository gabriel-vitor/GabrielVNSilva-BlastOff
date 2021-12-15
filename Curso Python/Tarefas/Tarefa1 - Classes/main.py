from retangulo import Retangulo

comprimento = float(input('informe o comprimento do local:'))
largura = float(input('informe a largura do local:'))

r1 = Retangulo(comprimento, largura)

while True:
    print()
    print('Informe o que deseja fazer:')
    print()
    escolha = int(input('[1] Mudar valor dos lados\n[2] Retornar valor dos lados\n[3] Calcular área\n[4] Calcular Perímetro'))
    
    if escolha == 1:
        
            
        