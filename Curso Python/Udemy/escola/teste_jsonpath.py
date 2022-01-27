import requests
import jsonpath

avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# resultados = jsonpath.jsonpath(avaliacoes.json(), 'results')

# print(resultados)

# primeiro elemento
# primeira = jsonpath.jsonpath(avaliacoes.json(), 'results[0]')

# print(primeira)

# apenas o nome
# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')
# print(nome)

# apenas o nome sem lista
# nome = jsonpath.jsonpath(avaliacoes.json(), 'results[0].nome')[0]
# print(nome)

# usando o email
# email = jsonpath.jsonpath(avaliacoes.json(), 'results[0].email')
# print(email)

# nota
# nota_data = jsonpath.jsonpath(avaliacoes.json(), 'results[0].avaliacao')
# print(nota_data)

# id do curso
# curso_id = jsonpath.jsonpath(avaliacoes.json(), 'results[0].curso')
# print(curso_id)

# todos os nomes das pessoas que avaliaram o curso
# nomes = jsonpath.jsonpath(avaliacoes.json(), 'results[*].nome')
# print(nomes)

# todos as avaliacoes das pessoas que avaliaram o curso
# notas = jsonpath.jsonpath(avaliacoes.json(), 'results[*].avaliacao')
# print(notas)

