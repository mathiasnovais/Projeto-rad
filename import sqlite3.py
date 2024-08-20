import sqlite3
from sqlite3 import Error

########## CRIAR CONEXAO
def ConexaoBanco():
    caminho="C:\\Users\\Wanessa\\Documents\\banco\\agenda.db"
    con=None
    try:
        con=sqlite3.connect(caminho)
    except Error as ex:
        print(ex)
    return con

vcon = ConexaoBanco()

##### CRIAR TABELA

vsql = """CREATE TABLE tb_contatos(
             N_IDCONTATO INTEGER PRIMARY KEY AUTOINCREMENT,
             T_NOMECONTATO VARCHAR(30),
             T_TELEFONECONTATO VARCHAR(14),
             T_EMAILCONTATO VARCHAR(30)
         )"""

def criarTabela(conexao, sql):
    try:
        c = conexao.cursor()
        c.execute(sql)
        conexao.commit()  # Adicionando o commit após a execução do comando SQL
        print("Tabela criada")
    except Error as ex:
        print(ex)

criarTabela(vcon, vsql)

vcon.close()