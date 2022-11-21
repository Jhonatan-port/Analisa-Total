from analisaTotal import app, listaRev
from flask import render_template, send_from_directory

@app.route('/')
def index():
    return render_template('index.html', titulo="Analisa Total", lista=listaRev)

@app.route('/uploads/<nome_arquivo>')
def imagem(nome_arquivo):
        return send_from_directory('uploads', nome_arquivo)

