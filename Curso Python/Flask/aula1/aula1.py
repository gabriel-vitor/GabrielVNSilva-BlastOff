# aula 1 - instalando flask

from flask import Flask

app = Flask(__name__)

# decorator
@app.route("/")
def index():
    return "Index"


@app.route("/teste")
def teste():
    return "Teste"


if __name__ == '__main__':
    app.run()