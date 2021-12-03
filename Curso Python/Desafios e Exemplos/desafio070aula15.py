total_gasto = 0
maisdemil = 0
condicao = True
barato = ''
contador = 0
menor = 0

while True:
    
    nome = input("diga o nome do produto:")
    preco = float(input("informe o preço do produto:"))
    
    contador += 1
    
    total_gasto = total_gasto + preco
    
    if preco > 1000:
        maisdemil += 1
    
    if contador == 1 or preco < menor:
        menor = preco
        barato = nome
    resp = ' '
    while resp not in 'SN':
        resp = input("quer continuar? S/N:").strip().upper()
    if resp =='N':
        break
    

print("Total gasto:", total_gasto)
print("Produtos acima de R$ 1000: ", maisdemil)
print("Produto mais barato: {}  preço:{}".format(barato, menor))    
        
        
    