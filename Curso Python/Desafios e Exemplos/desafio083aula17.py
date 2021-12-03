expres = input('digite uma expressão: ')
pilha = []

for simb in expres:
    if simb == '(':
        pilha.append('(')
    elif simb == ')':
        if len(pilha) > 0:
            pilha.pop()
        else:
            pilha.append(')')
            
            break

if len(pilha) == 0:
    print("sua expressão está válida")
else:
    print("incorreto")
    
    