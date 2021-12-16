from combustivel import *
opcao_inicial = 1
bomba = BombaCombustivel(opcao_inicial, precoCombG, precoCombD, quantCombBG, quantCombBD)
while True:
    escolha = leiaInt('[1]ABASTECER\n[2]ALTERAR VALOR\n[3]ALTERAR BOMBA')
    print('-'*50)
    
    if escolha != 1 and escolha != 2 and escolha !=3:
        print('opção não disponível, tente novamente:')
        print('-'*50)
    
    while True:
        if escolha == 1:
            escolha2 = leiaInt('[1]POR VALOR\n[2]POR LITRO\n')
            print('-'*50)
            if escolha2 != 1 and escolha2 != 2:
                print('opção não disponível, tente novamente')
                
                
            while True:
                if escolha == 1:
                    escolha3 = leiaInt('[1]GASOLINA\n[2]DIESEL\n')
                    print('-'*50)
                    #bomba = BombaCombustivel(escolha3, precoCombG, precoCombD, quantCombBG, quantCombBD)
                    valor = leiaFloat('Quantidade em reais')
                    bomba.abastecerPorValor(valor,  quantCombBG, quantCombBD, escolha3)
                    break
                elif escolha == 2:
                    escolha3 = leiaInt('[1]GASOLINA\n[2]DIESEL\n')
                    print('-'*50)
                    litro = leiaInt('Quantidade em litros:')
                    bomba.abastecerPorLitro(litro, quantCombBG, quantCombBD, escolha3)
                    break
                else:
                    print('opcao inválida, tente novamente')
            
            break
        elif escolha == 2:
            tipo = leiaInt('[1]GASOLINA\n[2]DIESEL\n')
            print('-'*50)
            valor = leiaFloat('digite o novo valor')
            #bomba.BombaCombustivel(escolha3, precoCombG, precoCombD, quantCombBG, quantCombBD)
            bomba.alterarValor(tipo, valor)
            break
            
        elif escolha == 3:
            tipo = leiaInt('[1]GASOLINA\n[2]DIESEL\n')
            print('-'*50)
            quantidade = leiaInt('informe quanto quer encher a bomba')
            #bomba = BombaCombustivel(escolha3, precoCombG, precoCombD, quantCombBG, quantCombBD)
            bomba.alterarCombustivel(tipo, quantidade)
            break
        else:
            print('digito inválido, tente novamente')
            print('-'*50)
        
        
        
        