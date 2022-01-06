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

    agrega1 = {
        '$lookup':{
            'from':'escolas',
            'localField':'cpf',
            'foreignField':'cpf_prof',   
            'as':'cpf'
        }
    }

    agrega2 = {
        '$project':{
            '_id':0,
            'Nome': '$nome',
            'Cidade':'$natural.cidade',
            'Ano':'$ano_nasc',
            'info': {'$arrayElemAt':['$cpf',0]}
        }
    }

    agrega3 = {
        '$project':{
            'Nome':'$Nome',
            'Cidade': '$Cidade',
            'Ano': '$Ano',
            'Escola': '$info.nome',
        }
    }

    results = professores.aggregate([agrega1, agrega2, agrega3])
    for aux in results:
        print(f"Nome:{aux['Nome']}")
        print(f"Cidade:{aux['Cidade']}")
        print(f"Nascimento:{aux['Ano']}")
        print(f"Escola:{aux['Escola']}")
        