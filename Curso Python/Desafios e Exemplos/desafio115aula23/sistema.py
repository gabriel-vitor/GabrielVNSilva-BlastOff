from utilidades import interface 
from utilidades import arquivo

arq = 'cadastrados.txt'

if not arquivo.arquivoExiste(arq):
    arquivo.criarArquivo(arq)

while True:
    resposta = interface.menu(['Listar', 'Cadastrar', 'Sair'])
    if resposta == 1:
        arquivo.lerArquivo(arq)
    elif resposta == 2:
        interface.cabecalho('novo cadastro:')
        nome = str(input('Nome:'))
        idade = interface.leiaInt('Idade:')
        arquivo.cadastrar(arq, nome, idade)
    elif resposta == 3:
        print('saindo do sistema')
        break
    else:
        print('ERRO! OPÇÃO INVÁLIDA')
