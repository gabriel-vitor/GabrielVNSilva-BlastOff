frase = '     Curso em video python'
print(frase[::2]) #salto de duas em duas letras

print(frase.count('o')) #conta quantas vezes o 'o' aparece

print(frase.upper().count('o')) #converte pra maiusculo e depois conta.

print(len(frase)) #tamanho da frase

print(len(frase.strip())) #remove os espaços antes e depois

print(frase.replace('python', 'Android')) #sobrepoe mas nao altera string original

frase = frase.replace('python', 'Android')

print(frase)

print("oi")

print('Curso' in frase) #verifica se a palavra existe

print(frase.find('curso')) #posicao onde se encontra. Se não existe, retorna -1

print(frase.lower().find('curso')) #converte pra minusculo

print(frase.split())
dividido = frase.split()
print(dividido)
print(dividido[0])
print(dividido[2][3])


print("""Welcome! are you completely new to programing?
about why and how to get started with Python. Fortunately
an experienced programmer in any programing language
(whatever it may be) can pick up Python very quickly.
Its also easy for beginners to use and learn, so jump in!""")

