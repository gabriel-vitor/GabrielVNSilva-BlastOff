try:
    a = int(input('numerador:'))
    b = int(input('denominador:'))
    r = a/b
    
except (ValueError, TypeError):
    print('Temos problema com os tipos de dados que voce digitou')

except ZeroDivisionError:
    print('não é possível dividir um número por zero')
    
except Exception as erro:
    print(f'infelizmente tivemos um problema:{erro.__class__}')

else:
    print('o resultado é', r)
    
finally:
    print('Volte sempre')