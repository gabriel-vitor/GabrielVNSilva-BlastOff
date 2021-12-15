num = [2, 5, 9, 1]

num[2] = 3

num.append(7)

#num.sort()

#num.sort(reverse = True)

num.insert(2, 0) #na posicao dois inserir o número 0

num.pop() #remove o último

num.pop(3) #remove no indice a partir do inicio da lista, no caso, a primeira ocorrencia
if 5 in num:
    num.remove(5) #remove a primeira ocorrencia
else:
    print("não achei")

print(num)

print(f'essa lista tem {len(num)} elementos')