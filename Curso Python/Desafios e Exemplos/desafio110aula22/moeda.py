def aumentar(preco = 0, taxa = 0, formato = False):
	res = preco + (preco *taxa/100)
	return res if formato is False else moeda(res)


def diminuir(preco = 0, taxa = 0, formato = False):
	res = preco - (preco * taxa/100)
	return res if formato is False else moeda(res)


def dobro(preco = 0, formato = False):
	res = preco * 2
	return res if not formato else moeda(res)


def metade(preco = 0, formato = False):
	res = preco / 2
	return res if not formato else moeda(res)


def moeda(preco = 0, moeda = ' R$'):
    return f'{moeda}{preco:>8.2f}'.replace('.', ',')

def resumo(preco = 0, taxaau = 10, taxared = 5):
    print('-'*30)
    print('RESUMO DO VALOR'.center(30))
    print('-'*30)
    print(f'preço analisado:{moeda(preco)}')
    print('-'*30)
    print(f'Dobro:{dobro(preco, True)}')
    print(f'Metade:{metade(preco, True)}')
    print(f'Com{taxaau}% de aumento: {aumentar(preco, taxaau, True)}')
    print(f'Com{taxared}% de redução: {diminuir(preco, taxared, True)}')
    
    