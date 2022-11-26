from models import Usuarios
from analisaTotal import app, db
from helpers import FormularioValidaUser, FormularioCadastraUser
from flask import render_template, request,session, redirect, url_for
from flask_bcrypt import check_password_hash, generate_password_hash

@app.route('/login')
def login():
    form = FormularioValidaUser()
    return render_template('login.html', titulo="Login", form=form)

@app.route('/autenticar', methods=['POST',])
def autenticar():
    form = FormularioValidaUser(request.form)#esta solicitando os dados do form de login de usuario
    usuario = Usuarios.query.filter_by(nickname = form.nickname.data).first()#esta solicitando os dados do primeiro usuario com nome semelhante
    senha = check_password_hash(usuario.senha, form.senha.data)
    if usuario and senha:
        session['usuario_logado'] = usuario.nickname
        session['usuario_admin'] = usuario.admin
        return redirect(url_for('index'))
    else:
        return redirect(url_for('login'))


@app.route('/logoff')
def logoff():
    session['usuario_logado'] = None
    session['usuario_admin'] = None
    return redirect(url_for('index'))






@app.route('/cadastroUser')
def cadastroUser():
   
    
    form = FormularioCadastraUser()

    return render_template('cadastroUser.html', form = form)

@app.route('/validaCadastro', methods=['POST',])
def validaCadastro():
    form = FormularioCadastraUser(request.form)

    #validando se o form foi preenchido corretamente
    if(not form.validate_on_submit()):
        return redirect(url_for('index'))
    
    #pegando os dados do usuario do forms
    nome = form.nome.data
    senha = form.senha.data
    nickname = form.nickname.data
    admin = form.admin.data

    #verificação se usuario ja existe
    user = Usuarios.query.filter_by(nickname = nickname).first()
    #caso o usuario exista por enquanto ele esta redirecionando a pagina principal
    if user:
        return redirect(url_for('index'))

    #esta fazendo o commit no BD
    novo_usuario = Usuarios(nome = nome, nickname = nickname, admin = admin, senha = generate_password_hash(senha))
    db.session.add(novo_usuario)
    db.session.commit()


    return redirect(url_for('index'))
    