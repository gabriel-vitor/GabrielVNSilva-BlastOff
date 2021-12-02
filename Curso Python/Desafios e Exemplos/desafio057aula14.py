contador = 0
while contador == 0:
    sexo = input("Digite seu sexo [F/M]:")
    
    if sexo in 'Mm' or sexo in 'Ff':
        print("Ok!")
        contador = 1
    else:
        print("Digito inválido, tente novamente:")

