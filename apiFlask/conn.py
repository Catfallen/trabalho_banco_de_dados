import psycopg2

def testar_conexao():
    try:
        conn = psycopg2.connect(
            dbname='projetobanco',
            user='postgres',
            password='markim',
            host='localhost',
            port='5432'
        )
        cursor = conn.cursor()
        cursor.execute('SELECT version();')
        versao = cursor.fetchone()
        print(f'Conexão OK! Versão do PostgreSQL: {versao[0]}')
        
        cursor.close()
        conn.close()
    except Exception as e:
        print('Erro ao conectar ao banco:', e)

if __name__ == '__main__':
    testar_conexao()
