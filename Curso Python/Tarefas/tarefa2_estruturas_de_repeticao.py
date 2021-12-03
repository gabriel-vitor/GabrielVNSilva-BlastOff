mais_alto = mais_baixo = mais_gordo = mais_magro = 0
contador = media = somapeso = soma_altura = 0
codigo_maisbaixo = codigo_maisalto = 0
codigo_maisgordo = codigo_maismagro = 0

codigo = int(input("informe seu código:"))
altura = float(input("informe sua altura:"))
peso = float(input("informe seu peso"))

while True:
    
    contador += 1
    
    somapeso = somapeso + peso
    soma_altura = soma_altura + altura
    
    if contador == 1:
        mais_baixo = mais_alto = altura
        mais_magro = mais_gordo = peso
        codigo_maisbaixo = codigo_maisalto = codigo
        codigo_maisgordo = codigo_maismagro = codigo
    else:
        if altura > mais_alto:
            mais_alto = altura
            codigo_maisalto = codigo
            
        elif altura < mais_baixo:
            mais_baixo = altura
            codigo_maisbaixo = codigo
            
        if peso > mais_gordo:
            mais_gordo = peso
            codigo_maisgordo = codigo
        
        elif peso < mais_magro:
            mais_magro = peso
            codigo_maismagro = codigo
        codigo = int(input("informe seu código:"))
        if codigo == 0:
            break
        altura = float(input("informe sua altura:"))
        peso = float(input("informe seu peso"))
            

media_altura = soma_altura / contador
media_peso = somapeso / contador

print("Cliente Nº {} mais alto: {}".format(codigo_maisalto, mais_alto))
print("Cliente Nº {} mais baixo: {}".format(codigo_maisbaixo, mais_baixo))
print("Cliente Nº {} mais gordo: {}".format(codigo_maisgordo, mais_gordo))
print("Cliente Nº {} mais magro: {}".format(codigo_maismagro, mais_magro))



        
    
    