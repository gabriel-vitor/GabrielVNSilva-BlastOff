"""
public, protected, private
_ protected/ privado (public _)
__ private  (_NomeClasse__nomeatributo)
"""

class BaseDeDados:
    def __init__(self):                #se comporta como construtor
        self.__dados = {}              #coração da classe

    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)


    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]




bd = BaseDeDados()
bd.inserir_cliente(1, 'otavio')
bd.inserir_cliente(2, 'rose')
bd.__dados = 'outra coisa'                    #não vai quebrar a classe
print(bd.__dados)
print(bd._BaseDeDados__dados)                 #vai printar o atributo privado
bd.lista_clientes()

print(bd.dados)                               #consegue printar o valor devido o property
bd.dados = 'outro valor'                      #vai dar erro, falta criar o set