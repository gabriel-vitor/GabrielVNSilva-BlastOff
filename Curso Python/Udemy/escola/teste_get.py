import requests
headers = {'Authorization': 'Token 5e499c9e00ef0af62be5f5596e941771d9d94719'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'

url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

resultado = requests.get(url=url_base_cursos, headers=headers)

# print(resultado.json())

# print(resultado.status_code)

# Testando se o endpoint está correto
assert resultado.status_code == 200

# Testando a quantidade de registros
assert resultado.json()['count'] == 3

# Testando se o titulo do primeiro curso está correto
assert resultado.json()['results'][0]['titulo'] == 'Programação para web com django framework'



