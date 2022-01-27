import requests

headers = {'Authorization': 'Token 5e499c9e00ef0af62be5f5596e941771d9d94719'}

url_base_cursos = 'http://localhost:8000/api/v2/cursos/'
url_base_avaliacoes = 'http://localhost:8000/api/v2/avaliacoes/'

novo_curso = {
    "titulo": "Gerencia Agil Scrum",
    "url": "http://www.geekuniversity.com.br/scrum2"
}

resultado = requests.post(url=url_base_cursos, headers=headers, data=novo_curso)


# Testando o código de status HTTP 201
assert resultado.status_code == 201

# Testando se o titulo do curso retornado é o mesmo informado
assert resultado.json()['titulo'] == novo_curso['titulo']


