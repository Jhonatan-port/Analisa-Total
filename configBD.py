import os
SECRET_KEY = 'raspadotacho'
#a barra invertida é usada para continuar escrevendo o mesmo comando em outra linha
#parte referente a conexão com BD
SQLALCHEMY_DATABASE_URI = \
    '{SGBD}://{usuario}:{senha}@{servidor}/{database}'.format(
        SGBD = 'mysql+mysqlconnector',
        usuario = 'root',
        senha = 'admin',
        servidor = 'localhost',
        database = 'jogoteca'
    )


# UPLOAD_PATH = os.path.dirname(os.path.abspath(__file__)) + '/uploads'