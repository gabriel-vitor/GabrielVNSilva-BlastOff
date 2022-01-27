import requests

headers = {'Authorization': 'Token 5e499c9e00ef0af62be5f5596e941771d9d94719'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

curso_atualizado = {
    "titulo": "Novo curso de Scrum 3",
    "url": "http://www.geekuniversity.com.br/ncs3"
}

# Buscando o curso com ID 8
curso = requests.get(f'{url_base_cursos}8/', headers=headers)
print(curso.json())

# resultado = requests.put(url=f'{url_base_cursos}8/', headers=headers, data=curso_atualizado)

# Testando o código de status HTTP
# assert resultado.status_code == 200

# Testando o titulo
# assert resultado.json()['titulo'] == curso_atualizado['titulo']



