from models import Usuarios
from analisaTotal import app
from helpers import FormularioUser
from flask import render_template, request,session, redirect, url_for
from flask_bcrypt import check_password_hash

@app.route('/login')
def login():
    form = FormularioUser()
    return render_template('login.html', titulo="Login", form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioUser(request.form)#esta solicitando os dados do form de login de usuario
    usuario = Usuarios.query.filter_by(nickname = form.nickname.data).first()#esta solicitando os dados do primeiro usuario com nome semelhante
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        session['usuario_admin'] = usuario.admin
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


@app.route('/logoff' )
def logoff():
    session['usuario_logado'] = None
    session['usuario_admin'] = None
    return redirect(url_for('index'))