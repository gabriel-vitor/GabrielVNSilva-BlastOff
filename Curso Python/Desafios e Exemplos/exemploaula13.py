for c in range(0, 7):
    print(c)
print("FIM")

for c in range(0, 7, 2):
    print(c)
print("FIM")

n = int(input("digite um número: "))
for c in range(0, n):
    print(c)
    
n = int(input("digite um número: "))
for c in range(0, n + 1):
    print(c)

i = int(input("inicio: "))
f = int(input("fim: "))
p = int(input("passo: "))

for c in range(i, f + 1, p):
    print(c)

s=0
for c in range(0, 4):
    n = int(input("num: "))
    s += n
print("somatorio:", s)