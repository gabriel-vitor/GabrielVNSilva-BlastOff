
num = int(input("informe o numero de 0 a 9999: " ))

u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10

#dm = num // 10000 % 10
#cm = num // 100000 % 10
#mi = num // 1000000 % 10

print('analisando o numero {}'.format(num))
print("unidade: {}".format(u))
print("dezena: {}".format(d))
print("centena: {}".format(c))
print("milhar: {}".format(m))

#print("dezena de milhar: {}".format(dm))
#print("centena de milhar: {}".format(cm))
#print("milhão: {}".format(mi))

