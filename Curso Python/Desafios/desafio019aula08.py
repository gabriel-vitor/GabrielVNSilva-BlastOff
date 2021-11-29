import random

alunos = []

for i in range(0,4):
        aluno = input("informe o nome do aluno: ")
        alunos.append(aluno)

escolhido = random.choice(alunos)
print("o aluno que irá apagar o quadro é: ", escolhido)

