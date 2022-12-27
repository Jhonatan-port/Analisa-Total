from models import Usuarios
from analisaTotal import app, db
from helpers import FormularioValidaUser, FormularioCadastraUsuario, FormularioAlteraUsuario
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




@app.route('/listaUsuario')
def listaUsuario():
    if session['usuario_admin'] == True:
        listaUsuarios = Usuarios.query.order_by(Usuarios.nickname)
        return render_template('listaUsuario.html', titulo="Usuarios cadastrados", lista=listaUsuarios)
    else:
        return render_template('erro.html')

@app.route('/cadastroUsuario')
def cadastroUsuario():
   
    if session['usuario_admin'] == True:
        form = FormularioCadastraUsuario()

        return render_template('cadastroUsuario.html', form = form, titulo="Cadastro")
    else:
        return render_template('erro.html')

@app.route('/validaCadastro', methods=['POST',])
def validaCadastro():
    form = FormularioCadastraUsuario(request.form)

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


@app.route('/editarUsuario/<string:nickname>')
def editarUsuario(nickname):
    if session['usuario_admin'] == True:
        usuario =  Usuarios.query.filter_by(nickname=nickname).first()
        form = FormularioAlteraUsuario()

        form.nickname.data = usuario.nickname
        form.nome.data = usuario.nome
        form.admin.data = usuario.admin


        return render_template('editarUsuario.html', titulo='Editando Usuario', usuario = usuario, form=form)

@app.route('/atualizarUsuario', methods=['POST',])
def atualizarUsuario():
    form = FormularioAlteraUsuario(request.form)

    if form.validate_on_submit():
        usuario = Usuarios.query.filter_by(nickname=request.form['nickname']).first()
        usuario.nome = form.nome.data
        usuario.nickname = form.nickname.data
        usuario.admin = form.admin.data

        db.session.add(usuario)
        db.session.commit()

    return redirect(url_for('listaUsuario'))

@app.route("/removeUsuario/<nickname>")
def removeUsuario(nickname):
    if session['usuario_admin'] == True:
        Usuarios.query.filter_by(nickname=nickname).delete()
        db.session.commit()
        return redirect(url_for('listaUsuario'))
    else:
        return redirect(url_for('index'))