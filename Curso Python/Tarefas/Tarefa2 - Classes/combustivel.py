quantCombBG = 1000
quantCombBD = 1000
precoCombG = 10
precoCombD = 5

class BombaCombustivel:
    
    
    def __init__(self, tipoCombustivel, valorLitroBG, valorLitroBD, quantidadeCombustivelG, QuantidadeCombustivelD):
        
        self.tipoCombustivel = tipoCombustivel
        self.valorLitroG = valorLitroBG
        self.valorLitroD = valorLitroBD
        self.quantidadeCombustivelG = quantidadeCombustivelG
        self.quantidadeCombustivelD = QuantidadeCombustivelD
        
    def abastecerPorValor(self, valor, quantidadeCombustivelG, quantidadeCombustivelD, tipoCombustivel):
        
        global quantCombBG 
        global quantCombBD 
        global precoCombG 
        global precoCombD 

        if self.tipoCombustivel == 1:
            litro = (valor / precoCombG)
            quantCombBG -= litro
            print('Quantidade na bomba de Gasolina:', quantCombBG)
            print('A quantidade de litros de Gasolina é:', litro)
            
            
        elif self.tipoCombustivel == 2:
            litro = (valor / precoCombD)
            quantCombBD -= litro
            print('Quantidade na bomba de Diesel:', quantCombBD)
            print('A quantidade de litros de Diesel é:', litro )   
        
            
    def abastecerPorLitro(self, litro, quantidadeCombustivelG, quantidadeCombustivelD, tipoCombustivel,):
        global quantCombBG 
        global quantCombBD 
        global precoCombG 
        global precoCombD 
        
        if self.tipoCombustivel == 1:
            valor = (litro * precoCombG)
            quantCombBG -= litro
            print('a quantidade em reais de gasolina é R$:', valor)
            
        elif self.tipoCombustivel == 2:
            valor = (litro *precoCombD)
            quantCombBD -= litro
            print('a quantidade em reais de diesel é R$:', valor)
    
    def alterarValor(self, tipoCombustivel, novoValor):
        global precoCombG
        global precoCombD
        
        if tipoCombustivel == 1:
            precoCombG = novoValor
        elif tipoCombustivel == 2:
            precoCombD = novoValor
    
    def alterarCombustivel(self, tipoCombustivel, novoValor):
        global quantCombBG 
        global quantCombBD 
        
        if self.tipoCombustivel == 1:
            quantCombBG += novoValor
            print('Quantidade na bomba de Gasolina:', quantCombBG)
        elif self.tipoCombustivel == 2:
            quantCombBD += novoValor
            print('Quantidade na bomba de Diesel:', quantCombBD)
        
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