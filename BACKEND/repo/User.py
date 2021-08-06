import sqlite3



def cria_usuario():
    #1o passo: criar uma conexao
    connection = sqlite3.connect("app.db")

    #2o passo: pegar o cursor
    cursor = connection.cursor()

    #3o passo: cursor.execute passando uma string de sql
    create_sql = """
    CREATE TABLE IF NOT EXISTS user (
        id INTEGER PRIMARY KEY,
        username TEXT NOT NULL,
        phone TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL,
        roles TEXT,
        access INTEGER
        
    )
    """
    return cursor.execute(create_sql)


def criar_roles():
    conection = sqlite3.connect("app.db")
    cursor = conection.cursor()

    create_sql = """
    CREATE TABLE IF NOT EXISTS roles (
        id INTEGER PRIMARY KEY,
        name TEXT
    )
    """
    return cursor.execute(create_sql)


def criar_userroles():
    conection = sqlite3.connect("app.db")
    cursor = conection.cursor()

    create_sql = """
    CREATE TABLE IF NOT EXISTS user_roles (
        id INTEGER PRIMARY KEY,     
        user_id INTEGER,
        role_id INTEGER,
        FOREIGN KEY(user_id) REFERENCES user(id),
        FOREIGN KEY(role_id) REFERENCES roles(id)
    )
    """

    return cursor.execute(create_sql)


cria_usuario()
criar_roles()
criar_userroles()