somaidade = 0

n = int(input("informe a quantidade de pessoas da turma"))

for c in range(1, n + 1):
    idade = int(input("aluno {} - informe sua idade: ".format(c)))
    somaidade = somaidade + idade

media = somaidade / n
if media < 25:
    print("Turma jovem")
elif media < 60:
    print("turma adulta")
else:
    print("turma idosa")