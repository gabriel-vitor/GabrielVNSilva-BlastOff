def maior(*num):
    contador = maior = 0
    for valor in num:
        
        if contador ==0:
            maior = valor
        else:
            if valor > maior:
                maior = valor
        contador += 1
        
    print(f'foram informados {contador} ao todo.')
    print('Maior valor:', maior)


#Main
maior(2, 9, 4)