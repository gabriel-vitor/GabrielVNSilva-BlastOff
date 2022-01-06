from pymongo import MongoClient

def verifica(resultado):
    if resultado.acknowledged:
        print('Operação feita com sucesso!')

    else:
        print('Falha na operação!')

if __name__ == '__main__':
    client = MongoClient('mongodb://localhost:27017')
    db = client['hospital']

    paciente1 = {
        'nome': 'Gabriel',
        'ano_nasc': 1998,
        'cpf': '222.222.333-35',
        'enfermidade': 'tumor cerebral',
        'leito': 32,
        'alergico': 'amoxicilina',
        'familiares': {
            'pai': 'José',
            'mae': 'Dora',
            'conjuge': 'Julia'
        }
    }
    paciente2 = {
        'nome': 'Livio',
        'ano_nasc': 2002,
        'cpf': '444.111.333-66',
        'enfermidade': 'diabetes',
        'leito': 50,
        'familiares': {
            'pai': 'Marcos',
            'mae': 'Joana',
        }
    }
    paciente3 = {
        'nome': 'Rasta',
        'ano_nasc': 1997,
        'cpf': '555.666.555-66',
        'enfermidade': 'braço cortado',
        'leito': 35,
        'alergico': 'fenitoína',
        'familiares': {
            'pai': 'Neto',
            'mae': 'Lucia',
        }
    }




    #results = db.pacientes.insert_one(paciente1)
    #verifica(results)

    #results = db.pacientes.insert_many([paciente2, paciente3])
    #verifica(results)

    leito1 = {
        'numero': 32,
        'sala': 10,
        'alergico': 'amoxicilina',
        'medicamento': {
            'antibiotico': 'penicilina',
            'analgesico': 'dipirona'
        }
    }
    leito2 = {
        'numero': 50,
        'sala': 30,
        'medicamento': {
            'analgesico': 'buscopan',
            'procedimento': 'soro fisiologico'
        }
    }
    leito3 = {
        'numero': 35,
        'sala': 15,
        'alergico': 'fenitoina',
        'medicamento': {
            'antibiotico': 'penicilina',
            'analgesico': 'dipirona'
        }
    }

    #results = db.leitos.insert_many([leito1, leito2, leito3])
    #verifica(results)

    #Buscas
    
    leitos = db.leitos
    pacientes = db.pacientes

    '''
    results = pacientes.find({'leito':{'$gte':35}}) #igual ou mais #MQL
    for aux in results:
        print(aux)

    print('-'*100)

    results = leitos.find()
    for aux in results:
        print(aux)
    '''

    #atualizando documentos
    '''
    results = pacientes.find()
    for aux in results:
        print(aux['nome'])

    results = pacientes.update_one(
        {'cpf':'222.222.333-35'},
        {'$set':{'nome':'Aroldo'}}
    )
    verifica(results)

    print('-'*100)

    results = pacientes.find()
    for aux in results:
        print(aux['nome'])
    '''

    #deletando
    '''
    results = pacientes.find()
    for aux in results:
        print(aux['nome'])

    results = pacientes.delete_one({'leito': 32})
    verifica(results)

    print('-'*100)

    results = pacientes.find()
    for aux in results:
        print(aux['nome'])
    '''

    '''
    results = leitos.find()
    for aux in results:
        print(aux['numero'])

    results = leitos.delete_one({'numero':32})
    verifica(results)

    print('-'*100)

    results = leitos.find()
    for aux in results:
        print(aux['numero'])
    '''

    #agregações

    ag1 = {
        '$lookup':{
            'from':'leitos',
            'localField':'leito',
            'foreignField':'numero',
            'as':'LEITO'
        }
    }

    ag2 = {
        '$project':{
            '_id':0,
            'Nome':'$nome',  #'portal' onde a gnt acessa o campo da nossa coleção
            'Ano':'$ano_nasc',
            'Dor':'$enfermidade',
            'Leito':'$leito',
            'info':{'$arrayElemAt':['$LEITO', 0]}

        }
    }

    ag3 = {
        '$project': {
            'Nome':'$Nome',
            'Ano':'$Ano',
            'Dor':'$Dor',
            'Leito':'$Leito',
            'Sala':'$info.sala',
            'Analgesico':'$info.medicamento.analgesico'
        }
    }

    results = pacientes.aggregate([ag1, ag2, ag3])
    for aux in results:
        print('Nome:', aux['Nome'])
        print('Ano de Nascimento:', aux['Ano'])
        print('Enfermidade:', aux['Dor'])
        print('Leito:', aux['Leito'])
        print('Sala:', aux['Sala'])
        print('Analgesico', aux['Analgesico'])
        print('-'*100)