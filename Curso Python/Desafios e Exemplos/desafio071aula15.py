print('------------------------')
valor = int(input("Valor do saque:"))
total = valor
ced = 50
totalced = 0
while True:
    if total >= ced:
        total = total - ced
        totalced = totalced + 1
    else:
        if totalced > 0:
            print(f"total de {totalced} cédulas de R$ {ced}")
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        elif ced == 10:
            ced = 1
        totalced = 0
        if total == 0:
            break