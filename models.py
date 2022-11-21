from analisaTotal import db

class Jogos(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nome = db.Column(db.String(50), nullable=False)
    categoria = db.Column(db.String(40), nullable=False)
    review = db.Column(db.String(255), nullable=False)

    def __repr__(self):#__repr__ tem como objetivo mostrar uma versão em string
        # para a pessoa programadora quando a classe é acessada em modo interativo.
        return '<Name %r>' % self.name

class Usuarios(db.Model):
    nickname = db.Column(db.String(8), primary_key=True)
    nome = db.Column(db.String(20), nullable=False)
    senha = db.Column(db.String(100), nullable=False)
    admin = db.Column(db.Boolean)

    def __repr__(self): #boa pratica utilizar
        return '<Name %r>' % self.name