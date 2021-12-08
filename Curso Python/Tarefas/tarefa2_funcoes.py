import datetime

meses = [0, 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto','Setembro', 'Outubro', 'Novembro', 'Dezembro']

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
        #strptime não verifica se o digito é decimal
        print('Formatação correta.')
        return True
        
    except ValueError:
        print('Formato de data inválido!')
        #raise ValueError("Incorrect data format, should be DD-MM-AAAA")
        return False


data = input('informe a data no formato DD/MM/AAAA:')

if validate(data) == True:
    dia = int(data[0:2])
    mes = int(data[3:5])
    ano = int(data[6:10])
    print(f'{dia} de {meses[mes]} de {ano}')
else:
    print('Tente novamente')


