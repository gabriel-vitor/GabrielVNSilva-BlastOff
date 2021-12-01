
import math

n1 = int(input("\033[33m informe um número: \033[m"))

dobro = n1 * 2
triplo = n1 *3
raiz = math.sqrt(n1)
#ou
raiz2 = n1 ** 0.5

print("o dobro é {}, o triplo é {}, e a raiz é {:3f}".format(dobro, triplo, raiz))