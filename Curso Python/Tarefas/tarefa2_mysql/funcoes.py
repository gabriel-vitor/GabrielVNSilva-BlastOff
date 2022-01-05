import pymysql.cursors

#insert
def insert_agente(conexao, idAgente, nome, endereco, nascimento, habilidade, sexo, email):
    with conexao.cursor() as db:
        sql = "INSERT INTO Agente() VALUES (%s, %s, %s, %s, %s, %s, %s)"
        db.execute(sql, (idAgente, nome, endereco, nascimento, habilidade, sexo, email))
        conexao.commit()

def insert_missao(conexao, idmissao, data, nome, localizacao, duracao, vilao_idvilao):
    with conexao.cursor() as db:
        sql = "INSERT INTO missao() VALUES (%s, %s, %s, %s, %s, %s)"
        db.execute(sql, (idmissao, data, nome,localizacao, duracao, vilao_idvilao))
        conexao.commit()
        
def insert_agente_has_missao(conexao, Agente_idAgente, missao_idmissao):
    with conexao.cursor() as db:
        sql = "INSERT INTO agente_has_missao() VALUES (%s, %s)"
        db.execute(sql, (Agente_idAgente, missao_idmissao))
        conexao.commit()

def insert_vilao(conexao, idvilao, nome, num_crimes):
    with conexao.cursor() as db:
        sql = 'INSERT INTO vilao() VALUES (%s, %s, %s)'
        db.execute(sql, (idvilao, nome, num_crimes))
        conexao.commit()

#busca

def select_agente_missao(conexao):
    with conexao.cursor() as db:
        sql = 'SELECT nome, email FROM Agente'
        db.execute(sql)
        resultado = db.fetchall()

        for agenteM in resultado:
            print(agenteM)

def select_missao_vilao(conexao):
    with conexao.cursor() as db:
        sql = 'SELECT missao.nome, missao.data, missao.duracao, vilao.nome FROM missao, vilao WHERE missao.idmissao = vilao.idVilao'
        db.execute(sql)
        resultado = db.fetchall()

        for vilaoM in resultado:
            print(vilaoM)

def select_agente_missao_vilao(conexao):
    with conexao.cursor() as db:
        sql = 'SELECT Agente.nome, missao.nome, vilao.nome FROM Agente, missao, vilao WHERE Agente.idAgente = missao.idmissao = vilao.idVilao'
        db.execute(sql)
        resultado = db.fetchall()

        for agemisvil in resultado:
            print(agemisvil)

#UPDATE

def update_data_missao(conexao, idmissao, data):
    with conexao.cursor() as db:
        sql = 'UPDATE missao SET data = %s WHERE idmissao = %s'
        db.execute(sql, (data, idmissao))
        conexao.commit()

#DELETE

def delete_agente(conexao, idAgente):
    with conexao.cursor() as db:
        sql = 'DELETE FROM Agente WHERE idAgente = %s'
        db.execute(sql, idAgente)
        conexao.commit()

if __name__ == "__main__":
    conexao = pymysql.connect(
        host ='127.0.0.1',
        user = 'root',
        password='insira-sua-senha-aqui',
        db='TopSecret',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )

    #Inserção
    
    #Agente
    
    insert_agente(conexao, 1, 'Gabriel', 'RUA A', '2000-01-01','ARMAS PESADAS', 'M','gabriel@hotmail.com')
    insert_agente(conexao, 2, 'Lucas', 'RUA B', '2000-02-02','ARMAS BRANCAS', 'M','lucas@hotmail.com')
    insert_agente(conexao, 3, 'Angelo', 'RUA C', '2000-03-03','ARMAS LEVES', 'M','angelo@hotmail.com')
    insert_agente(conexao, 4, 'Kayo', 'RUA D', '2000-04-04','NAVES', 'M','kayo@hotmail.com')
    insert_agente(conexao, 5, 'Sertralina', 'RUA E', '2000-05-05','CAMUFLAGEM', 'M','sertralina@hotmail.com')
    

    #vilao
    
    insert_vilao(conexao, 1, 'Ramiel', 10)
    insert_vilao(conexao, 2, 'Azazel', 20)
    insert_vilao(conexao, 3, 'Lilith', 10)
    insert_vilao(conexao, 4, 'Sachiel', 12)
    insert_vilao(conexao, 5, 'Tabris', 10)
    

    #missao
    
    insert_missao(conexao,1, '2015-03-02','Missão 1', 'Local 1', 10, 1)
    insert_missao(conexao,2, '2016-03-02','Missão 2', 'Local 1', 10, 2)
    insert_missao(conexao,3, '2017-03-02','Missão 3', 'Local 1', 10, 3)
    insert_missao(conexao,4, '2018-03-02','Missão 4', 'Local 1', 10, 4)
    insert_missao(conexao,5, '2019-03-02','Missão 5', 'Local 1', 10, 5)
    

    #agente_has_missao
    
    insert_agente_has_missao(conexao, 1, 1)
    insert_agente_has_missao(conexao, 2, 2)
    insert_agente_has_missao(conexao, 3, 3)
    insert_agente_has_missao(conexao, 4, 4)
    insert_agente_has_missao(conexao, 5, 5)
    

    #BUSCA
    select_agente_missao(conexao)
    select_missao_vilao(conexao)
    select_agente_missao_vilao(conexao)

    #UPDATE
    update_data_missao(conexao, 1, '2005-05-05')

    #DELETE
    delete_agente(conexao, 3)







   



    



