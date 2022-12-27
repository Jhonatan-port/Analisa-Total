from analisaTotal import app
from flask_wtf import FlaskForm
from flask import flash
import os
from wtforms import StringField, validators, SubmitField, PasswordField, BooleanField,TextAreaField

class FormularioValidaUser(FlaskForm):
    nickname = StringField('Nickname', [validators.data_required(), validators.length(min=1, max=50)], render_kw={'placeholder': 'Usuario'})
    senha = PasswordField('Senha', [validators.data_required(), validators.length(min=1, max=100)], render_kw={'placeholder': 'Senha'})
    login = SubmitField('Login')

class FormularioCadastraUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.data_required(), validators.length(min=1, max=50)], render_kw={'placeholder': 'Usuario'})
    senha = PasswordField('Senha', [validators.data_required(), validators.length(min=1, max=100)], render_kw={'placeholder': 'Senha'})
    nome = StringField('Nome', [validators.data_required(), validators.length(min=1, max=20)], render_kw={'placeholder': 'Nome Completo'})
    admin = BooleanField('admin')
    cadastrar = SubmitField('Cadastrar')

class FormularioAlteraUsuario(FlaskForm):
    nickname = StringField('Nickname', [validators.data_required(), validators.length(min=1, max=50)], render_kw={'placeholder': 'Usuario'})
    nome = StringField('Nome', [validators.data_required(), validators.length(min=1, max=20)], render_kw={'placeholder': 'Nome Completo'})
    admin = BooleanField('admin')
    cadastrar = SubmitField('Cadastrar')

class FormularioCadastraReview(FlaskForm):
    nome = StringField('Nome do Jogo', [validators.data_required(), validators.Length(min=1, max=50)], render_kw={'placeholder': 'Nome do Game'})
    categoria = StringField('Categoria', [validators.data_required(), validators.Length(min=1, max=40)], render_kw={'placeholder': 'Categoria do Game'})
    review = TextAreaField('review', [validators.data_required(), validators.Length(min=1, max=255)], render_kw={'placeholder': 'Review'})
    salvar = SubmitField('Salvar')

def recupera_imagem(id, nome_review):
    for nome_arquivo in os.listdir(app.config['UPLOAD_PATH']):
        if f'capa_{id}' and nome_review in nome_arquivo:
            return nome_arquivo
    
    return 'Capa_padrao.jpg'


def deleta_arquivo(id, nome_review):
    arquivo = recupera_imagem(id, nome_review)
    if arquivo != 'Capa_padrao.jpg':
        os.remove(os.path.join(app.config['UPLOAD_PATH'], arquivo))

