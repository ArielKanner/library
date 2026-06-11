import mysql.connector

def get_connection():
    return mysql.connector.connect(
        user = 'root',
        port = 3306,
        password='secret',
        host='127.0.0.1',
        database='library_d_b'
        )

# conn = get_connection()
# cursor = conn.cursor(dictionary=True)

# cursor.execute('CREATE TABLE IF NOT EXISTS example (id INT AUTO_INCREMENT PRIMARY KEY, email VARCHAR(255) UNIQUE, name VARCHAR(255) NOT NULL)')
# conn.commit()

# cursor.close()
# conn.close()

# from fastapi import FastAPI
# import uvicorn

# app = FastAPI()

# @app.get('/check')
# def check():
#     return 'hello'


# if __name__ == '__main__':
#     uvicorn.run('db_connection:app',host= "127.0.0.1", port= 8000)


def create_tables():
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(255) UNIQUE,
        author VARCHAR(255) NOT NULL,
        genre ENUM(Fiction | Non-Fiction | Science | History | Other),
        is_available,
        borrowed_by_member_id)
    """)
    conn.commit()

    cursor.close()
    conn.close()