from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_wtf.csrf import CSRFProtect



app = Flask(__name__)
app.config.from_pyfile('./setups/configBD.py')

db = SQLAlchemy(app)
bcrypt = Bcrypt(app)
csrf = CSRFProtect(app)

from views_games import *
from views_user import * 

if __name__ == '__main__':
    app.run(debug=True)

