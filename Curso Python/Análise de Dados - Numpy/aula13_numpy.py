import numpy as np

a = 40
b = 70

cadastro = np.random.randint(15, 51, size = (50,10))

print(cadastro)  

cadastro_maior18 = cadastro > 18
print(cadastro_maior18)           #mostra matriz com True e False

print(cadastro[cadastro_maior18]) #mostra apenas o número dos maiores de 18

print(cadastro[cadastro>18])

print(len(cadastro[cadastro_maior18]))

print(cadastro_maior18.sum())   #soma todos os valores 0 e 1, como True é 1, a soma fica igual o len

print(cadastro[2])

arr4 = cadastro[cadastro>35]
print(len(arr4))

condicao = (cadastro>20)

extraido = np.extract(condicao, cadastro)

print(extraido)



