h = float(input("informe sua altura: "))

peso_h = (72.7 * h) - 58 #homem
peso_m = (62.1 * h) - 44.7 #mulher

print("peso ideal para homens: {:.2f}".format(peso_h))
print("peso ideal para mulheres: {:.2f}".format(peso_m))

#também é possível fazer com if e else.
