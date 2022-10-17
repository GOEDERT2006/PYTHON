import sqlite3 as lite

con = lite.connect('Locadora.db')
cur = con.cursor()

with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE Cliente (ID INTEGER PRIMARY KEY AUTOINCREMENT, Nome TEXT,CPF TEXT UNIQUE,Endereco TEXT,Email TEXT,Telefone INT,DataNascimento TEXT)")