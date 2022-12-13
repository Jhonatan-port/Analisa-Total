from analisaTotal import app, db
from flask import render_template, request, send_from_directory, session, redirect, url_for
from helpers import FormularioCadastraUsuario, FormularioCadastraReview, recupera_imagem, deleta_arquivo


from models import Jogos
@app.route('/')
def index():
    listaRev = Jogos.query.order_by(Jogos.id)
    return render_template('index.html', titulo="Analisa Total", lista=listaRev)

@app.route('/cadastroReview')
def cadastroReview():
    form = FormularioCadastraReview()
    return render_template('novaReview.html', titulo='Nova Review', form=form)
    

@app.route('/criarReview', methods=['POST',])
def criar():
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


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
        return send_from_directory('uploads', nome_arquivo)