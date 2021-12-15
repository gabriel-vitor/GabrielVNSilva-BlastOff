
print("\033[1;31;43m ola mundo\033[m")

print("\033[4;30;45m ola mundo\033[m")

print("\033[0;33;44m ola mundo\033[m")



a = 3
b = 5

print("ps valores são \033[32m{}\033[m e \033[31m{}\033[m".format(a, b))
     
nome = 'gabriel'

print("Olá, {}{}{}".format('\033[34m', nome, '\033[m'))

cores = {'limpa': '\033[m',
         'azul' : '\033[34m',
         'amarelo' : '\033[33m',
         'pretoebranco' : '\033[7;30m'}

print("Olá, {}{}{}".format(cores['pretoebranco'], nome, cores['limpa']))