#minha versão

palavra = input("Digite uma palavra: ").strip().upper()
palavra = palavra.split()
palavra = ''.join(palavra)
if palavra == ''.join(reversed(palavra)):
    print("É palindromo")
else:
    print("Não é palindromo")

'''
versão do Guanabara
    
frase = input("digite uma frase: ").strip().upper()
palavras = frase.split()
junto = ''.join(palavras)
inverso = ''

#ao inves do for, pode usar iverso = junto[::-1]

for letra in range(len(junto) - 1, - 1, - 1):
    inverso += junto[letra]
if inverso == junto:
    print("É Palíndromo")
else:
    print("Não é Palíndromo")
'''