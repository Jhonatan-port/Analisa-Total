from analisaTotal import app
from flask_wtf import FlaskForm
from wtforms import StringField, validators, SubmitField, PasswordField

class FormularioUser(FlaskForm):
    nickname = StringField('Nickname', [validators.data_required(), validators.length(min=1, max=50)], render_kw={'placeholder': 'Usuario'})
    senha = PasswordField('Senha', [validators.data_required(), validators.length(min=1, max=100)], render_kw={'placeholder': 'Senha'})
    login = SubmitField('Login')