from analisaTotal import app, db
from flask import render_template, request, send_from_directory, session, redirect, url_for
from helpers import FormularioCadastraUsuario, FormularioCadastraReview, recupera_imagem, deleta_arquivo
import os




from models import Jogos
@app.route('/')
def index():
    listaRev = Jogos.query.order_by(Jogos.id)
    return render_template('index.html', titulo="Analisa Total", lista=listaRev)

@app.route('/cadastroReview')
def cadastroReview():
    if session['usuario_admin'] == True:
        form = FormularioCadastraReview()
        return render_template('novaReview.html', titulo='Nova Review', form=form)
    else:
        return redirect(url_for('erro.html'))

#funcionalidade dedicada ao upload de arquivos de imagens
@app.route('/uploads/' + '<nome_arquivo>')
def imagem(nome_arquivo):
    return send_from_directory('uploads', nome_arquivo)
    

@app.route('/criarReview', methods=['POST',])
def criarReview():
    form = FormularioCadastraReview(request.form)
    if(not form.validate_on_submit()):
        return redirect(url_for('cadastroReview'))
    nome = form.nome.data
    categoria = form.categoria.data
    review = form.review.data

    checa_review = Jogos.query.filter_by(nome = nome).first()

    if checa_review:
        print('Review ja existente')
        return redirect(url_for('index'))

    nova_review = Jogos(nome = nome, categoria = categoria, review = review)
    db.session.add(nova_review)
    db.session.commit()

    imagem = request.files['arquivo']
    _, extensao = os.path.splitext(imagem.filename)
    upload_path = app.config['UPLOAD_PATH']
    imagem.save(f'{upload_path}/capa_{nova_review.id}_{nova_review.nome}{extensao}')

    return redirect(url_for('index'))



@app.route('/editarReview/<int:id>')
def editarReview(id):
    if session['usuario_admin'] == True:
        review = Jogos.query.filter_by(id=id).first()
        capa_review = recupera_imagem(id)
        form = FormularioCadastraReview()

        form.nome.data = review.nome
        form.categoria.data = review.categoria
        form.review.data = review.review
        return render_template('editarReview.html', titulo='Editando jogo', capa_review = capa_review, id=id, form=form)

        

@app.route('/atualizarReview', methods=['POST',])
def atualizarReview():
    form = FormularioCadastraReview(request.form)

    if form.validate_on_submit():
        jogo = Jogos.query.filter_by(id=request.form['id']).first()
        jogo.nome = form.nome.data
        jogo.categoria = form.categoria.data
        jogo.review = form.review.data

        db.session.add(jogo)
        db.session.commit()
        
        imagem = request.files['arquivo']
        _, extensao = os.path.splitext(imagem.filename)
        upload_path = app.config['UPLOAD_PATH']
        imagem.save(f'{upload_path}/capa_{jogo.id}_{jogo.nome}{extensao}')

    return redirect(url_for('index'))

@app.route('/removerReview/<int:id>')
def removerReview(id):
    if session['usuario_admin'] == True:
        Jogos.query.filter_by(id=id).delete() 
        db.session.commit()
        return redirect(url_for('index'))
        
    else:
        return redirect(url_for('erro.html'))