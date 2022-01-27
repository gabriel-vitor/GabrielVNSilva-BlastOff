# Aula11 - Cookies

from flask import Flask, render_template, request, make_response, redirect, url_for
from json import dumps

app = Flask(__name__, template_folder='templates')


@app.route('/')
def index():
    return render_template('login.html')


@app.route('/successornot', methods=['GET', 'POST'])
def successornot():

    login = 'teste'
    senha = '123456'

    if request.method == 'POST':
        if request.form['username'] == login and request.form['pass'] == '123456':
            dados = dumps(request.form)
            resp = make_response(render_template('sucesso-login.html'))
            resp.set_cookie('testeCookie', dados)
        else:
            resp = make_response(render_template('erro-login.html'))

    return resp


@app.route('/getcookie')
def getcookie():
    usuarioName = request.cookies.get('testeCookie')
    return '<h1>Usuário é: {}</h1>'.format(usuarioName)


if __name__ == '__main__':
    app.run(debug=True)
