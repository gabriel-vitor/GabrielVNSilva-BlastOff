from flask import Blueprint, Response, request
import json
from ..models.models import db, Dependent

app = Blueprint("Dependent", __name__)


@app.route('/')
def index():
    # disciplinas = Dependent.query.all() #sem necessidade de pegar todos os dependentes
    rows = db.session.execute("select * from dependent").fetchall()
    result = [dict(e) for e in rows]
    return Response(response=json.dumps(result), status=200, content_type="application/json")


@app.route('/view/<int:id>', methods=['GET'])
def view(id):
    row = db.session.execute("select * from dependent where id = %s" % id).fetchone()
    return Response(response=json.dumps(dict(row)), status=200, content_type="application/json")


@app.route('/add', methods=['POST'])
def add():
    dependent = Dependent(request.form['name'])
    db.session.add(dependent)
    db.session.commit()
    return Response(response=json.dumps({'status': 'success', 'data': dependent.to_dict()}), status=200,
                    content_type="application/json")


@app.route('/edit/<int:id>', methods=['PUT', 'POST'])
def edit(id):
    dependent = Dependent.query.get(id)
    dependent.name = request.form['name']
    dependent.address = request.form['address']
    dependent.Employee_id = request.form['Employee_id']
    db.session.commit()
    return Response(response=json.dumps(dependent.to_dict()), status=200, content_type="application/json")


@app.route('/delete/<int:id>', methods=['GET', 'DELETE'])
def delete(id):
    dependent = Dependent.query.get(id)
    db.session.delete(dependent)
    db.session.commit()
    return Response(response=json.dumps(dependent.to_dict()), status=200, content_type="application/json")


