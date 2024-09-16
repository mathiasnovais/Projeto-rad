import sqlite3

# Criando conexão
try:
    con = sqlite3.connect('cadastro_alunos.db')
    print("Conexão com o banco de dados realizada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao conectar com o banco de dados:", e)

# Criando a tabela de cursos
try:
    with con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS cursos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        duracao TEXT,
                        preco REAL
                    )""")
        print("Tabela cursos criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar a tabela cursos:", e)

# Criando a tabela de turmas
try:
    with con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS turmas (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        cursos_nome TEXT,
                        data_inicio DATE,
                        FOREIGN KEY (cursos_nome) REFERENCES cursos (nome) ON UPDATE CASCADE ON DELETE CASCADE
                    )""")
        print("Tabela turmas criada com sucesso!")
except sqlite3.Error as e:
    print("Erro ao criar a tabela turmas:", e)

# Criando a tabela de alunos
try:
    with con:
        cur = con.cursor()
        cur.execute("""CREATE TABLE IF NOT EXISTS alunos (
                        id INTEGER PRIMARY KEY AUTOINCREMENT,
                        nome TEXT,
                        email TEXT,
                        telefone TEXT,
                        sexo TEXT,
                        imagem TEXT,
                        data_nascimento DATE,
                        cpf TEXT,
                        turma_nome TEXT,
                        FOREIGN KEY (turma_nome) REFERENCES turmas (nome) ON DELETE CASCADE
                    )""")
        print("Tabela alunos criada com sucesso!")
except sqlite3.Error as e:
