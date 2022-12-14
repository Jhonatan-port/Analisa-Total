from analisaTotal import app, db
from flask import render_template, request, send_from_directory, session, redirect, url_for
from helpers import FormularioCadastraUsuario, FormularioCadastraReview, recupera_imagem, deleta_arquivo


@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
        return send_from_directory('uploads', nome_arquivo)


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

    return redirect(url_for('index'))



@app.route('/editarReview/<int:id>')
def editarReview(id):
    if session['usuario_admin'] == True:
        review = Jogos.query.filter_by(id=id).first()
        form = FormularioCadastraReview()

        form.nome.data = review.nome
        form.categoria.data = review.categoria
        form.review.data = review.review
        capa_jogo = recupera_imagem(id)
        return render_template('editar.html', titulo='Editando jogo', id=id, capa_jogo = capa_jogo, form=form)