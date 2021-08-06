import sqlite3


#1o passo: criar uma conexao
connection = sqlite3.connect("app.db")

#2o passo: pegar o cursor
cursor = connection.cursor()

#3o passo: cursor.execute passando uma string de sql
create_sql = """
CREATE TABLE IF NOT EXISTS Adm (
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    phone TEXT NOT NULL,
    email TEXT NOT NULL UNIQUE,
    password TEXT NOT NULL
    
    
)
"""
cursor.execute(create_sql)