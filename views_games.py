from analisaTotal import app
from flask import render_template, send_from_directory

from models import Jogos
@app.route('/')
def index():
    listaRev = Jogos.query.order_by(Jogos.id)
    return render_template('index.html', titulo="Analisa Total", lista=listaRev)

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
        return send_from_directory('uploads', nome_arquivo)


