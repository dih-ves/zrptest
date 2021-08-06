import sqlite3

class HeroiNaoExisteException(Exception):
    pass

def heroi_existe(idHeroi):
    connection = sqlite3.connect("rpg.db")
    cursor = connection.cursor()
    sql = "SELECT * FROM Heroi WHERE id = (?)"
    cursor.execute(sql, [idHeroi])
    heroi = cursor.fetchone()
    if heroi is None:
        return False
    else:
        return True
    connection.close()

def consultar_heroi(id_heroi):
    connection = sqlite3.connect("rpg.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    sql = "SELECT * FROM Heroi WHERE id = (?)"
    cursor.execute(sql, [id_heroi])
    heroi = cursor.fetchone()
    if heroi == None:
        raise HeroiNaoExisteException
    connection.close()
    return heroi

def heroi_pronto_por_nome(nomeHeroi):
    connection = sqlite3.connect("rpg.db")
    connection.row_factory = sqlite3.Row
    cursor = connection.cursor()
    sql = "SELECT * FROM Heroi WHERE nome = (?)"
    cursor.execute(sql, [nomeHeroi])
    heroi = cursor.fetchone()
    if heroi == None:
        raise HeroiNaoExisteException
    connection.close()
    return {'id':heroi[0],'nome':heroi[1],'fisico':heroi[2], 'magia': heroi[3], 'agilidade': heroi[4], 'vida':heroi[2]*10}

def atacar_com_fisico(atacante, defensor):
    ataca = atacante['fisico']
    defensor['vida'] -= ataca

def atacar_com_magia(atacante, defensor):
    ataca = atacante['magia']
    vida_r = defensor['vida']
    if vida_r - ataca <= 0:
        defensor['vida'] = 0
    else:
        defensor['vida'] -= ataca

