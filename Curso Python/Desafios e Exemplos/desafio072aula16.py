contagem = ('zero', 'um', 'dois', 'tres','quatro', 'cinco', 'seis', 'sete',
            'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'catorze',
            'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito',
            'dezenove', 'vinte')


while True:
    num = int(input('digite um número:'))

    if num >= 0 and num <= 20:
        print(contagem[num])
    else:
        break