
import sqlite3 as lite

con = lite.connect('Locadora.db')
 
#inserir





#inserindo
def inserir_info(i):
    with con:
        cur = con.cursor()
        query = 'INSERT INTO Cliente (Nome,CPF,Endereco,Email,Telefone,DataNascimento) VALUES (?,?,?,?,?,?)'
        cur.execute(query,i)


#listando
def mostrar_info():
    lista = []
    with con:
        cur = con.cursor()
        query = "SELECT * FROM Cliente"
        cur.execute(query)
        informacao = cur.fetchall()

        for i in informacao:
            lista.append(i)
    return lista

#att

def atualizar_info(i):
    with con:
        cur = con.cursor()
        query = 'UPDATE Cliente SET Nome=?, CPF=?, Endereco=?, Email=?, Telefone=?, DataNascimento=? WHERE ID=?'
        cur.execute(query,i)

def deletar_info(i):
    with con:
        cur = con.cursor()
        query = 'DELETE FROM Cliente WHERE ID=?'
        cur.execute(query,i)                    
        
          
      














