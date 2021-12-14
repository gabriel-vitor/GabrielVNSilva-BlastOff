from utilidades import interface

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('Erro na criação do arquivo')
    else:
        print(f'arquivo {nome} criado')

def lerArquivo(nome):
    try:
        a = open(nome, 'rt')
    except:
        print('erro ao ler o arquivo')
    else:
        interface.cabecalho('PESSOAS CADASTRADAS:')
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('n', '')
            print(f'{dado[0]:<25} {dado[1]:>3}')
            
        
    finally:
        a.close()
        
        
def cadastrar(arq, nome ='desconhecido', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('erro na abertura do arquivo')
    else:
        try:
            a.write(f'{nome}; {idade}\n')
        except:
            print('erro na hora de escrever dados')
        else:
            print('novo registro de {nome} adicionado')
            a.close()
        