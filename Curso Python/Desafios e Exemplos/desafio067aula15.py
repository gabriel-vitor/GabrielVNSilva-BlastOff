
while True:
    n = int(input("Tabuada - digite um número: "))
    if n < 0:
        break
    for c in range(1,11):
        print(f'{n} x {c} = {n*c}')
        