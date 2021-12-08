def fatorial(num, show = False):
    f = 1
    for contador in range(num, 0, -1):
        if show:
            print(contador, end = '')
            if contador > 1:
                print('x', end = '')
            else:
                print(' = ', end = '')
        f *= contador
    return f


resp = fatorial(5, show = True)
print(resp)