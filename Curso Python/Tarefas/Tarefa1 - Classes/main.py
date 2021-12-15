from retangulo import Retangulo

while True:
    try:
        
        comprimento = float(input('informe o comprimento do local:'))
        largura = float(input('informe a largura do local:'))
        r1 = Retangulo(comprimento, largura)
        
    except ValueError:
        print('Dados inválidos, tente novamente')
    else:
        r1 = Retangulo(comprimento, largura)
        r1.retornaLados(r1.comprimento, r1.largura)
        
        while True:
            try:
                escolha = input('Deseja altera o valor dos lados? [S/N]').strip().upper()
                
            except ValueError:
                print('Digito inválido, tente novamente:')
            else:
                if escolha == 'S':
                    comprimento = float(input('informe o comprimento do local:'))
                    largura = float(input('informe a largura do local:'))
                    r1.mudaLados(comprimento, largura)
                    break
                elif escolha == 'N':
                    break
                
        
        r1.retornaLados(r1.comprimento, r1.largura)
                    
                
        valor_area = r1.area(r1.comprimento, r1.largura)
        print('Área:', valor_area)
                    
        valor_perimetro = r1.perimetro(r1.comprimento, r1.largura)
        print('Perimetro:', valor_perimetro)
                    
        piso = 0.5
        rodape = 0.5
        
        numpiso = valor_area / 0.5
        numrodape = valor_perimetro / 0.5
        
        print(f'É necessário {valor_area} metros de piso: {numpiso} pisos')
        print(f'É necessário {valor_perimetro} metros de rodapé: {numrodape} rodapés')
        break        
        
    
        
        
        
        

        
            
        