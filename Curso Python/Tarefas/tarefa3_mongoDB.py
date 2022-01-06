from pymongo import MongoClient

def verifica(resultado):
    if resultado.acknowledged:
        print('Operação feita com sucesso!')

    else:
        print('Falha na operação!')

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017')
    db = client['educacao']

    professor1 = {
        "nome": "Pamela",
        "ano_nasc": 1950,
        "cpf": "789.012.345-67",
        "natural": {
            "cidade": "Serra da Saudade",
            "estado": "Minas Gerais",
            "pais": "Brasil"
        }
    }
    professor2 = {
        "nome": "Elza",
        "ano_nasc": 1997,
        "cpf": "901.234.567-89",
        "natural": {
            "cidade": "São Tomé das Letras",
            "estado": "Minas Gerais",
            "pais": "Brasil"
        }
    }

    
    '''results = db.professores.insert_many([professor1, professor2])
    verifica(results)'''

    #escola

    escola1 = {
        "nome": "Sinhá Moreira",
        "endereco": "Av. Dr. Delfim Moreira",
        "numero": 509,
        "cpf_prof": "789.012.345-67"
    }

    escola2 = {
        "nome": "Zenaide",
        "endereco": "Conj. Hab. Gilberto Rossetti",
        "numero": 332,
        "cpf_prof": "901.234.567-89"
    }

    results = db.escolas.insert_many([escola1, escola2])
    verifica(results)

    #Buscas

    