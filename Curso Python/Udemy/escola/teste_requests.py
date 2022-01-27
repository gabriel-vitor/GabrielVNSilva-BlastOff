import requests

# GET Avaliacoes

# avaliacoes = requests.get('http://localhost:8000/api/v2/avaliacoes/')

# acessando código de status http
# print(avaliacoes.status_code)

# acessando os dados da resposta
# print(avaliacoes.json())
# obs: json tem aspas duplas
# print(type(avaliacoes.json())) #dicionario

# acessando a quantidade de registros
# print(avaliacoes.json()['count'])

# acessando a próxima página de resultado
# print(avaliacoes.json()['next'])

# acessando os resultados desta página
# print(avaliacoes.json()['results'])
# print(type(avaliacoes.json()['results']))

# acessando o primeiro elemento da lista de resultados
# print(avaliacoes.json()['results'][0])

# acessando o último elemento da lista de resultados
# print(avaliacoes.json()['results'][-1])

# acessando somente o nome da pessoa que fez a última avaliação
# print(avaliacoes.json()['results'][-1]['nome'])

# GET Avaliacao

# avaliacao = requests.get('http://localhost:8000/api/v2/avaliacoes/6/')
# print(avaliacao.json())

# GET Cursos

headers = {'Authorization': 'Token 5e499c9e00ef0af62be5f5596e941771d9d94719'}

cursos = requests.get(url='http://localhost:8000/api/v2/cursos/', headers=headers)

print(cursos.status_code)
print(cursos.json())
