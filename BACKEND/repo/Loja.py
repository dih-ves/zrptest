import sqlite3


#1o passo: criar uma conexao
connection = sqlite3.connect("app.db")

#2o passo: pegar o cursor
cursor = connection.cursor()

#3o passo: cursor.execute passando uma string de sql
create_sql = """
CREATE TABLE IF NOT EXISTS Loja (
    id INTEGER PRIMARY KEY,
    nome CHAR(50) NOT NULL,
    email TEXT(50) NOT NULL UNIQUE,
    phone TEXT(25) NOT NULL,
    endereco TEXT(150) NOT NULL
    
    
)
"""
cursor.execute(create_sql)


#Função que registra contato no banco de dados.
#def registro_contato(nome, email, mensagem, telefone):
def cadastrar_loja(objeto):
    connection = sqlite3.connect("app.db")
    cursor = connection.cursor()

    try:
        sql_criar = "INSERT INTO Loja (nome, email, phone, id, endereco) VALUES (?,?,?,?,?)"
        cursor.execute(sql_criar, objeto)
        connection.commit()
    
    except:
        print('Mensagem não enviada, tente outra vez mais tarde.')
        pass

    connection.close()