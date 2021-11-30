import random

alunos = []

for i in range(0,4):
        aluno = input("informe o nome do aluno: ")
        alunos.append(aluno)

random.shuffle(alunos)
print("a ordem de apresentação é: ", alunos)

