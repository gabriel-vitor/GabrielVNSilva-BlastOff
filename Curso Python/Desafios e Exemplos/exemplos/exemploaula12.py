nome = str(input("qual é seu nome?"))
if nome == 'Gustavo':
    print("Que nome bonito!")
elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é bem popular no brasil')
elif nome in 'Ana Claudia Jessica Juliana':
    print("belo nome feminino")
else:
    print("seu nome é bem normal")
print("tenha um bom dia, {}".format(nome))