from pymongo import MongoClient

def verifica(resultado):
    if resultado.acknowledged:
        print('Operação feita com sucesso!')

    else:
        print('Falha na operação!')

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017')
    db = client['educacao']

    escolas = db.escolas
    professores = db.professores

    #Buscas
    results = escolas.find({'$and':[{'numero': {'$lt':400}}, {"nome": {'$regex': '.*r.*'}}]})
    for aux in results:
        print(aux['nome'], '/' , aux['endereco'], '/', aux['numero'])
        

    results = professores.find({'$or':[{'ano_nasc': {'$lte':1990}}, {"natural.estado": "Sao Paulo"}]})
    for aux in results:
        print(aux['nome'], '/' , aux['natural']['estado'], '/', aux['natural']['cidade'])
    