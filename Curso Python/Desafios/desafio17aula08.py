import math

cat_op = float(input("informe o comprimento do cateto oposto: "))
cat_ad = float(input("informe o comprimento do cateto adjacente:"))

hipotenusa = math.hypot(cat_op, cat_ad)
print("a hipotenusa é:", hipotenusa)