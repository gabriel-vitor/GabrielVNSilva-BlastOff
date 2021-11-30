a = int(input("Digite o número A: "))
b = int(input("Digite o número B: "))
c = int(input("Digite o número C: "))

if a > b and a > c:
    print("A é maior:", a)
elif b > a and b > c:
    print("B é maior:", b)
else:
    print("C é maior:", c)
    