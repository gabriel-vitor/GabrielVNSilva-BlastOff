import datetime

meses = [0, 'Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho',
         'Agosto','Setembro', 'Outubro', 'Novembro', 'Dezembro']

def validate(date_text):
    try:
        datetime.datetime.strptime(date_text, '%d/%m/%Y')
    except ValueError:
        print('Formato de data inválido!')
        #raise ValueError("Incorrect data format, should be DD-MM-AAAA")


validate('23/12/2003')

data = input('informe a data no formato DD/MM/AAAA:')
dia = int(data[0:2])
mes = int(data[3:5])
ano = int(data[6:10])

print(f'{dia} de {meses[mes]} de {ano}')
