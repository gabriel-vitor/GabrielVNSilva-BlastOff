from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# adaptação da aula 16 para a tarefa2

class Employee(db.Model):
    #table name para informar o nome da tabela no banco de dados
    __tablename__ = 'employee'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    address = db.Column(db.String(150))

    def __init__(self, name, address):
        self.name = name
        self.address = address

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "name": self.name, "address": self.address}
        else:
            return {col: getattr(self, col) for col in columns}


class Dependent(db.Model):
    __tablename__ = 'dependent'
    id = db.Column('id', db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(150))
    address = db.Column(db.String(150))
    Employee_id = db.Column(db.Integer, db.ForeignKey('employee.id'))
    # chave estrangeira para que o dependente só tenha relação com um funcionário

    def __init__(self, name, address, Employee_id):
        self.name = name
        self.address = address
        self.Employee_id = Employee_id

    def to_dict(self, columns=[]):
        if not columns:
            return {"id": self.id, "name": self.name}
        else:
            return {col: getattr(self, col) for col in columns}