import psycopg2
from psycopg2.extras import RealDictCursor

def get_connection():
    return psycopg2.connect(
        dbname='projetobanco',
        user='postgres',
        password='markim',
        host='localhost',
        port='5432'
    )

def execute_query(query, params=None, fetch=False):
    conn = get_connection()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    try:
        cursor.execute(query, params)
        if fetch:
            result = cursor.fetchall()
        else:
            result = None

        conn.commit()
        return result
    except Exception as e:
        conn.rollback()
        raise e
    finally:
        cursor.close()
        conn.close()
