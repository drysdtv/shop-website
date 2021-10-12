import sqlite3 as sql


def createTable():
    connection = sql.connect("website.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS login (Id INTEGER PRIMARY KEY, "
                   "username TEXT UNIQUE,"
                   " email TEXT UNIQUE,"
                   " password TEXT"
                   ")")


def retrieveUser():
    con = sql.connect("website.db")
    cur = con.cursor()
    cur.execute("SELECT username, password FROM login")
    users = cur.fetchall()
    con.close()
    return users


def insertUser(username, email, password):
    con = sql.connect("website.db")
    cur = con.cursor()
    cur.execute("INSERT OR IGNORE INTO login (username, email,password) VALUES (?,?,?)", (username, email, password))
    con.commit()
    con.close()
    