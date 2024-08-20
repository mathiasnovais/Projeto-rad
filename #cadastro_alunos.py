#cadastro_alunos.db
import sqlite3

# Função para conectar ao banco de dados
def connect_db():
    conn = sqlite3.connect('cadastro_alunos.db')
    return conn

# Função para criar a tabela turmas
def create_table():
    conn = connect_db()
    cur = conn.cursor()
    cur.execute('''
    CREATE TABLE IF NOT EXISTS turmas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL
    )
    ''')
    conn.commit()
    conn.close()

# Chamar a função para criar a tabela
create_table()

# Resto do seu código
def alunos():
    conn = connect_db()
    cur = conn.cursor()
    turmas = ver_turmas(cur)
    # Outras operações
    conn.close()

def ver_turmas(cur):
    cur.execute('SELECT * FROM turmas')
    return cur.fetchall()

if __name__ == "__main__":
    alunos()
