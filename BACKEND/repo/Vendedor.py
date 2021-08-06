import sqlite3


#1o passo: criar uma conexao
connection = sqlite3.connect("app.db")

#2o passo: pegar o cursor
cursor = connection.cursor()

#3o passo: cursor.execute passando uma string de sql
create_sql = """
CREATE TABLE IF NOT EXISTS Vendedor (
    id INT NOT NULL UNIQUE,
    username TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    id_loja INT NOT NULL,
    phone TEXT NOT NULL,
    password TEXT NOT NULL UNIQUE
    
    
)
"""
cursor.execute(create_sql)


#Função que registra contato no banco de dados.
#def registro_contato(nome, email, mensagem, telefone):
def cadastrar_vendedor(objeto):
    connection = sqlite3.connect("app.db")
    cursor = connection.cursor()

    try:
        sql_criar = "INSERT INTO Vendedor (username, email, phone, id_loja, passord) VALUES (?,?,?,?,?)"
        cursor.execute(sql_criar, objeto)
        connection.commit()
    
    except:
        print('Mensagem não enviada, tente outra vez mais tarde.')
        pass

    connection.close()
