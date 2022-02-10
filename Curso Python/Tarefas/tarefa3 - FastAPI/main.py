import requests
import json

while True:
    select = int(input('1 - Cadastro \n2 - Login \n Listar produtos \n Buscar produto(id) \n Buscar produto(nome'))

    if select ==1:
        print("CADASTRO")
        username = input("Digite o nome do usuário:")
        password = input("Digite sua senha:")
        address = input("Informe seu endereço:")
        account = input("Número da conta")

        new_user = {
            "user": username,
            "password": password,
            "address": address,
            "account": account
        }

        url = "http://localhost:8000/sign_up/"
        request = requests.post(url, data=json.dumps(new_user))

    elif select==2:
        print("LOGIN")
        username = input("Usuario: ")
        password = input('Senha: ')

        data_user = {
            "username": username,
            "password": password
        }

        url = "http://localhost:8000/token"
        request = requests.post(url, data=json.dumps(data_user))
        # or use data={"username":username, "password": password}
        print(request.text)

    elif select==3:
        print("PRODUTOS")
        url = "http://localhost:8000/get_all_products"
        request = requests.get(url)
        list_products = request.json()
        # é necessario percorrer a lista e printar cada produto
        for product in list_products['products']:
            print(product['name'])
            print(product['price'])
            print(product['description'])

    elif select==4:
        print("PRODUTO(ID)")
        prod_id = int(input("Digite o ID:"))
        # formatação para inserir valor dentro da string
        url = f"http://localhost:8000/get_product/{prod_id}"
        request = requests.get(url)
        product = request.json()
        print(product['name'])
        print(product['price'])
        print(product['description'])

    elif select==5:
        print("PRODUTO(NOME)")
        name = input("Digite o nome do produto: ")
        url = f"http://localhost:8000/search_product?name={name}"
        request = requests.get(url)
        product_name = request.get(url)
        for product in product_name['products']:
            print(product['name'])
            print(product['price'])
            print(product['description'])
    else:
        print('Digito inválido, tente novamente')