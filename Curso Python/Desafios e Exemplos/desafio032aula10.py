from calendar import isleap

ano = int(input("Informe o ano: "))

if isleap(ano):
    print("É bissexto")
else:
    print("Não é bissexto")