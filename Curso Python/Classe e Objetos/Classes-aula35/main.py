from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
'''
p1.comer('maça')
p1.falar('POO')
p1.parar_comer()
p1.falar('POO')
p1.comer('alimento')
p1.parar_falar()
p1.falar('assunto')
'''
p2 = Pessoa('João', 32)

p1.falar('POO')
p2.falar('Filmes')

print(p1.ano_atual)
print(p2.ano_atual)
print(Pessoa.ano_atual)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())