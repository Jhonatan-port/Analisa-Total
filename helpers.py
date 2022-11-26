from analisaTotal import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField, BooleanField

class FormularioValidaUser(FlaskForm):
    nickname = StringField('Nickname', [validators.data_required(), validators.length(min=1, max=50)], render_kw={'placeholder': 'Usuario'})
    senha = PasswordField('Senha', [validators.data_required(), validators.length(min=1, max=100)], render_kw={'placeholder': 'Senha'})
    login = SubmitField('Login')

class FormularioCadastraUser(FlaskForm):
    nickname = StringField('Nickname', [validators.data_required(), validators.length(min=1, max=50)], render_kw={'placeholder': 'Usuario'})
    senha = PasswordField('Senha', [validators.data_required(), validators.length(min=1, max=100)], render_kw={'placeholder': 'Senha'})
    nome = StringField('Nome', [validators.data_required(), validators.length(min=1, max=20)], render_kw={'placeholder': 'Nome Completo'})
    admin = BooleanField('admin')
    cadastrar = SubmitField('Cadastrar')