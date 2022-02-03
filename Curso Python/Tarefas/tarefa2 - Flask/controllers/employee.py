from flask import Blueprint, Response, request
import json
from ..models.models import db, Employee

app = Blueprint("employee", __name__)


@app.route('/')
def index():

    rows = db.session.execute("select * from employee").fetchall()
    result = [dict(r) for r in rows]
    return Response(response=json.dumps(result), status=200, content_type="application/json")


# é necessário uma rota para dependentes do funcionário
@app.route('/<int:id>/dependents')
def dependents(id):
    rows = db.session.execute("select F.name, D.name from employee E JOIN dependent D ON D.Employee_id = E.id where E.id = %s" % id)
    result = [dict(r) for r in rows]
    return Response(response=json.dumps(result), status=200, content_type="application/json")


@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    row = db.session.execute("select * from employee where id = %s" % id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")


@app.route('/add', methods=['POST'])
def add():
    employee = Employee(request.form['name'], request.form['address'])
    db.session.add(employee)
    db.session.commit()
    return Response(response=json.dumps({'status': 'sucesso', 'data': employee.to_dict()}), status=200,
                    content_type="application/json")


@app.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    employee = Employee.query.get(id)
    employee.name = request.form['name']
    employee.address = request.form['address']
    db.session.commit()
    return Response(response=json.dumps(employee.to_dict()), status=200, content_type="application/json")


@app.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    employee = Employee.query.get(id)
    db.session.delete(employee)
    db.session.commit()
    return Response(response=json.dumps(employee.to_dict()), status=200, content_type="application/json")


