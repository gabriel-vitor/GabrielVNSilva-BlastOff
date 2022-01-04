import pymysql.cursors

def insert_empregado(conexao, id, nome, endereco):
    with conexao.cursor() as db:
        sql = "INSERT INTO Empregado()VALUES(%s, %s, %s)"
        db.execute(sql, (id, nome, endereco))
        conexao.commit()


def insert_dependentes(conexao, nome, endereco, fk):
    with conexao.cursor() as db:
        sql = f"INSERT INTO Dependentes(nome, endereco, idEmpregado)VALUES(%s, %s, %s)"
        db.execute(sql, (nome, endereco, fk))
        conexao.commit()


def select_empregado(conexao):
    with conexao.cursor() as db:
        
        #sql = "SELECT nome FROM Empregado"    #seleciona apenas o nome (em dicionario)
        #sql = "SELECT nome FROM Empregado WHERE idEmpregado <= 2" 
        #sql = "SELECT nome FROM Empregado WHERE endereco = %s" 
        #db.execute(sql, 'Rua 2')  #irá concatenar em %s

        sql = "SELECT * FROM Empregado"
        db.execute(sql)
        resultado = db.fetchall()

        for registro in resultado:
            print(registro)
            #print(registro['nome'])


def select_dependentes(conexao):
    with conexao.cursor() as db:
        sql = "SELECT * FROM Dependentes"
        db.execute(sql)
        resultado = db.fetchall()

        for registro in resultado:
            print(registro)


def update_empregado(conexao, id, endereco):
    with conexao.cursor() as db:
        sql = "UPDATE Empregado SET endereco = %s WHERE idEmpregado = %s"
        db.execute(sql, (endereco, id))
        conexao.commit()  


def update_Dependentes(conexao, id, nome):
    with conexao.cursor() as db:
        sql = "UPDATE Dependentes SET nome = %s WHERE idDependente = %s"
        db.execute(sql, (nome, id))
        conexao.commit()


def delete_empregado(conexao, id):
    with conexao.cursor() as db:
        sql = "DELETE FROM Empregado WHERE idEmpregado = %s"
        db.execute(sql, id)
        conexao.commit()


def delete_dependentes(conexao, id):
    with conexao.cursor() as db:
        sql = "DELETE FROM Dependentes WHERE idDependente = %s"
        db.execute(sql, id)
        conexao.commit()


def consulta(conexao):
    with conexao.cursor() as db:
        sql = "SELECT E.nome, D.nome FROM Empregado E JOIN Dependentes D on D.idEmpregado = E.idEmpregado"    
        db.execute(sql)
        resultado = db.fetchall()
        

        for registro in resultado:
            print(registro)
        
            #print(f'{registro["Dependente"]} é dependente de {registro["Empregado"]}')


if __name__ == "__main__":
    conexao = pymysql.connect(
        host ='127.0.0.1',
        user = 'root',
        password='insira sua senha aqui',
        db='Empresa',
        charset='utf8mb4',
        cursorclass=pymysql.cursors.DictCursor
    )


''' 
    insert_empregado(conexao, 1, 'Flavio', 'Rua 1')
    insert_empregado(conexao, 2, 'Rafaela', 'Rua 2')
    insert_empregado(conexao, 3, 'Pamela', 'Rua 2')
    insert_dependentes(conexao,'Fernando', 'Rua 10', 1)
    insert_dependentes(conexao, 'Vania', 'Rua 10', 1)
    update_empregado(conexao, 3, 'Rua 13')
    select_empregado(conexao)
    select_dependentes(conexao)
    select_dependentes(conexao)
    print('-'*50)
    update_Dependentes(conexao, 1, 'Fernando Ferreira')
    select_dependentes(conexao)
    insert_dependentes(conexao, 'Aline', 'Rua 9', 3)
    select_dependentes(conexao)
    print('-'*60)
    delete_dependentes(conexao, 3)
    select_dependentes(conexao)
    consulta(conexao)
    insert_empregado(conexao, 4,'Eduardo','Rua 3')
'''
