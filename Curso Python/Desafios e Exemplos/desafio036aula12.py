casa = float(input("informe o valor da casa: "))
salario = float(input("informe seu salário: "))
tempo = int(input("tempo de pagamento em anos:"))

limite = salario * 0.30
prestacao_mensal = casa / tempo
print("o limite é de R$: ", limite)
print("prestação", prestacao_mensal)

if prestacao_mensal > limite:
    print("Empréstimo negado")
elif prestacao_mensal < 0:
    print("dados inválidos")
else:
    print("empréstimo aprovado")
    


