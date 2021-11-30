frase = input('diga uma frase:')
frase = frase.upper().strip()
print("Quantidade de aparições: {}".format(frase.count('A')))

print('A primeira vez que aparece é na posição {}'.format(frase.find('A')))
print('A primeira vez que aparece é na posição {}'.format(frase.rfind('A')))

#para que a contagem comece por 1 ao invés de 0, basta
#inserir '+1' após a função 'find'
      
