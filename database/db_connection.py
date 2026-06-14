import mysql.connector

def get_connection():
    return mysql.connector.connect(
        user = 'root',
        port= 3306,
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
        title VARCHAR(50) UNIQUE,
        author VARCHAR(50) NOT NULL,
        genre ENUM('fiction', 'non-fiction', 'science', 'history', 'other'),
        is_available BOOLEAN DEFAULT TRUE,
        borrowed_by_member_id INT DEFAULT NULL)
    """)
    conn.commit()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS members (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50), 
        email VARCHAR(100) NOT NULL,
        is_active BOOLEAN DEFAULT TRUE,
        total_borrows INT DEFAULT 0   
    )
    """)

    cursor.close()
    conn.close()


    


create_tables()