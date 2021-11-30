#forma 1
frase1 = input("Digite uma frase:").strip()
frase2 = input("Digite uma nova frase:").strip()

tam_frase1 = len(frase1)
tam_frase2 = len(frase2)

print("tamanho de {}: {}".format(frase1, tam_frase1))
print("tamanho de {}: {}".format(frase2, tam_frase2))

if tam_frase1 == tam_frase2 and frase1 == frase2:
    print("as strings possuem tamanhos iguais")
    print("as strings possuem o mesmo conteudo")
    
elif tam_frase1 == tam_frase2 and frase1 != frase2:
    print("as strings possuem tamanhos iguais")
    print("as strings possuem conteudo diferente")
    
else: 
    print("as strings possuem tamanhos diferentes")  
    print("as strings possuem conteúdos diferentes")

#tam_frase1 != tam_frase2:
#se o tamanho é diferente, obrigatoriamente o conteúdo será diferente.


###################################################

#forma 2
'''
frase1 = input("Digite uma frase:").strip()
frase2 = input("Digite uma nova frase:").strip()

tam_frase1 = len(frase1)
tam_frase2 = len(frase2)

print("tamanho de {} é: {}".format(frase1, tam_frase1))
print("tamanho de {} é: {}".format(frase2, tam_frase2))

if tam_frase1 == tam_frase2:
    print("as strings possuem tamanhos iguais")
else:
    print("as strings possuem tamanhos diferentes")

if frase1 != frase2:
    print("as duas strings possuem conteúdo diferentes")
else:
    print("as strings possuem conteúdos iguais")
'''
    

