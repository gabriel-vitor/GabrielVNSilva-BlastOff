from classes import Escritor, Caneta, MaquinaDeEscrever

escritor = Escritor('joãozinho')
print(escritor.nome)

caneta = Caneta('Bic')
print(caneta.marca)

maquina = MaquinaDeEscrever()
print(maquina)

print(escritor.nome)

print(caneta.marca)

maquina.escrever()

escritor.ferramenta = caneta

escritor.ferramenta.escrever()

