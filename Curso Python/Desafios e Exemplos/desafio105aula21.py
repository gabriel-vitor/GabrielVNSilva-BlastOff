def notas(*nota, sit=False):
    
    """
    ->função para analisar notas de vários alunos.
    :param n: uma ou mais notas dos alunos.
    :param sit: valor opcional para situação.
    :param return dicionario com as informações.
    """
    dicionario = {}
    dicionario['total'] = len(nota)
    dicionario['maior'] = max(nota)
    dicionario['menor'] = min(nota)
    dicionario['media'] = sum(nota) / len(nota)
    if sit:
        if dicionario['media'] > 7:
            dicionario['situação'] = 'aprovado'
        else:
            dicionario['situação'] = 'reprovado'
    return dicionario
    
#main
resp = notas(5.5, 2.5, 9, 8.5, sit = True)
print(resp)
