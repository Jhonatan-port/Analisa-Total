import mysql.connector#para instalar o mysql connector utilizar o comando: pip install mysql-connector-python==8.0.28, logo apos o script pode ser rodado
from mysql.connector import errorcode
from flask_bcrypt import generate_password_hash

print("Conectando...")
try:
      conn = mysql.connector.connect(
            host='127.0.0.1',
            user='root',
            password='admin'
      )
except mysql.connector.Error as err:
      if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print('Existe algo errado no nome de usuário ou senha')
      else:
            print(err)

cursor = conn.cursor()

cursor.execute("DROP DATABASE IF EXISTS `jogoteca`;")

cursor.execute("CREATE DATABASE `jogoteca`;")

cursor.execute("USE `jogoteca`;")

# criando tabelas
TABLES = {}
TABLES['Jogos'] = ('''
      CREATE TABLE `jogos` (
      `id` int(11) NOT NULL AUTO_INCREMENT,
      `nome` varchar(50) NOT NULL,
      `categoria` varchar(40) NOT NULL,
      `review` varchar(255) NOT NULL,
      PRIMARY KEY (`id`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

TABLES['Usuarios'] = ('''
      CREATE TABLE `usuarios` (
      `nome` varchar(20) NOT NULL,
      `nickname` varchar(8) NOT NULL,
      `senha` varchar(100) NOT NULL,
      `admin` boolean NOT NULL,
      PRIMARY KEY (`nickname`)
      ) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;''')

for tabela_nome in TABLES:
      tabela_sql = TABLES[tabela_nome]
      try:
            print('Criando tabela {}:'.format(tabela_nome), end=' ')
            cursor.execute(tabela_sql)
      except mysql.connector.Error as err:
            if err.errno == errorcode.ER_TABLE_EXISTS_ERROR:
                  print('Já existe')
            else:
                  print(err.msg)
      else:
            print('OK')

# inserindo usuarios
usuario_sql = 'INSERT INTO usuarios (nome, nickname, senha, ADMIN) VALUES (%s, %s, %s, %s)'
usuarios = [
      ("Jhonatan dos Santos", "js01", generate_password_hash("catiau").decode('utf-8'), True ),#gerando uma senha criptografada
      ("Camila Ferreira", "Mila", generate_password_hash("paozinho").decode('utf-8'), True),
      ("joao", "joao", generate_password_hash("1234").decode('utf-8'), False)
]
cursor.executemany(usuario_sql, usuarios)

cursor.execute('select * from jogoteca.usuarios')
print(' -------------  Usuários:  -------------')
for user in cursor.fetchall():
    print(user[1])

# inserindo jogos
jogos_sql = 'INSERT INTO jogos (nome, categoria, review) VALUES (%s, %s, %s)'
jogos = [
      ('Tetris', 'Puzzle', 'Lorem ipsum dolor sit amet. Et consectetur consequuntur id delectus distinctio id cumque dolorum eum eligendi'),
      ('God of War', 'Hack n Slash', 'Lorem ipsum dolor sit amet. Et consectetur consequuntur id delectus distinctio id cumque dolorum eum eligendi'),
      ('Mortal Kombat', 'Luta', 'Lorem ipsum dolor sit amet. Et consectetur consequuntur id delectus distinctio id cumque dolorum eum eligendi'),
      ('Valorant', 'FPS', 'Lorem ipsum dolor sit amet. Et consectetur consequuntur id delectus distinctio id cumque dolorum eum eligendi'),
      ('Crash Bandicoot', 'Hack n Slash', 'Lorem ipsum dolor sit amet. Et consectetur consequuntur id delectus distinctio id cumque dolorum eum eligendi'),
      ('Need for Speed', 'Corrida', 'Lorem ipsum dolor sit amet. Et consectetur consequuntur id delectus distinctio id cumque dolorum eum eligendi'),
]
cursor.executemany(jogos_sql, jogos)

cursor.execute('select * from jogoteca.jogos')
print(' -------------  Jogos:  -------------')
for jogo in cursor.fetchall():
    print(jogo[1])

# commitando se não nada tem efeito
conn.commit()

cursor.close()
conn.close()