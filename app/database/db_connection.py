import mysql.connector

def get_connection():
    return mysql.connector.connect(
        user = 'root',
        port = 3306,
        password='secret',
        host='127.0.0.1',
        database='library_d_b'
        )