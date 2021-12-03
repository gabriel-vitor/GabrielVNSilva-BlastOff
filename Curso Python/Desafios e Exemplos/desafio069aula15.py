contador_sexoF = 0
contador_sexoM = 0
contador_idade18 = 0
decisao = True
while decisao == True:
    idade = int(input("informe sua idade:"))
    sexo = input('informe o sexo [M/F]:')
    
    if idade > 18:
        contador_idade18 += 1
    if sexo in 'Mm':
        contador_sexoM = contador_sexoM + 1
    if sexo in 'Ff' and idade < 20:
        contador_sexoF = contador_sexoF + 1
    
    decisao = input("Deseja continuar? [S/N]")
    if decisao in 'Ss':
        decisao = True
    else:
        decisao = False



print("quantidade de pessoas que tem mais de 18:", contador_idade18)
print("quantidade de homens cadastrados:", contador_sexoM)
print("quantidade de mulheres que tem menos de 20: ", contador_sexoF)
    
    
        
    