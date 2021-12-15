class Retangulo:
    
    def __init__(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        
        
    def retornaLados(self, comprimento, largura):
        print(f'Comprimento: {self.comprimento}\nLargura: {self.largura}')
        
        
    def mudaLados(self, comprimento, largura):
        self.comprimento = comprimento
        self.largura = largura
        
        
    def area(self, comprimento, largura):
        valor_area = comprimento * largura
        return valor_area
    
    def perimetro(self, comprimento, largura):
        p = 2 * (comprimento + largura)
        return p
        
        
