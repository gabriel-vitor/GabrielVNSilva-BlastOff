

from flask import Flask
from tarefa2.models.models import db
from tarefa2.controllers.dependent import app as employee_controller
from tarefa2.controllers.employee import app as dependent_controller

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///corporation.sqlite3'

app.register_blueprint(employee_controller, url_prefix="/employee/")
app.register_blueprint(dependent_controller, url_prefix="/dependent/")

if __name__ == '__main__':
    db.init_app(app=app)
    with app.test_request_context():
        db.create_all()
    app.run(debug=True)

