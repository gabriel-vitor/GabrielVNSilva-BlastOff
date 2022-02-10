import requests
import json

while True:
    select = int(input('1 - Cadastro \n2 - Login \n Listar produtos \n Buscar produto(id) \n Buscar produto(nome'))

    if select ==1:
        print("")
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
        print("")
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
        print("")
        url = "http://localhost:8000/get_all_products"
        request = requests.get(url)
        list_products = request.json()

