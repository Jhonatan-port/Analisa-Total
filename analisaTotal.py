from flask import Flask
from flask import render_template


class review:
    def __init__(self, id, titulo, categoria, texto):
        self.id = id
        self.titulo = titulo
        self.categoria = categoria
        self.texto = texto

review1 = review(1, 'God of War', 'Porrada', 'Lorem ipsum dolor sit amet. Et consectetur consequuntur id delectus distinctio id cumque dolorum eum eligendi')
review2 = review(2, 'skyrim', 'RPG', 'Lorem ipsum dolor sit amet. Et consectetur consequuntur id delectus distinctio id cumque dolorum eum eligendi')

listaRev = [review1, review2]

app = Flask(__name__)

from views import *

if __name__ == '__main__':
    app.run(debug=True)

