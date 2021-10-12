import sqlite3 as sql


def createDB():
    connection = sql.connect("website.db")
    cursor = connection.cursor()
    cursor.execute("CREATE TABLE IF NOT EXISTS login (Id INTEGER PRIMARY KEY, "
                   "username TEXT UNIQUE,"
                   " email TEXT UNIQUE,"
                   " password TEXT"
                   ")")
    cursor.execute("CREATE TABLE IF NOT EXISTS cart (Id INTEGER PRIMARY KEY, "
                   "name TEXT UNIQUE,"
                   " price NUMERIC,"
                   " quantity NUMERIC"
                   ")")


def retrieveUser(username):
    con = sql.connect('website.db')
    cur = con.cursor()
    cur.execute("SELECT * FROM login where username = (?)", username)
    users = cur.fetchall()
    con.close()


def insertUser(username, email, password):
    con = sql.connect('website.db')
    cur = con.cursor()
    cur.execute("INSERT OR IGNORE INTO login (username, email, password) VALUES (?, ?, ?)", (username, email, password))
    con.commit()
    con.close()


def addCart(name, price, quantity):
    con = sql.connect("website.db")
    cur = con.cursor()
    cur.execute("insert or ignore into cart (name, price, quantity) values (?, ?, ?)", (name, price, quantity))
    con.commit()
    con.close()
