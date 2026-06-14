import mysql.connector


class DbConnection():
    def __init__(self):
        self.user = 'root'
        self.port = 3306
        self.password = 'secret'
        self.host = '127.0.0.1'
    
    def get_connection(self):
        return mysql.connector.connect(
            user = self.user,
            port= self.port,
            password=self.password,
            host=self.host,
            database='library_d_b'
        )

    def create_tables(self):
        conn = self.get_connection()
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
        conn.commit()

        cursor.close()
        conn.close()

# db_conn = DbConnection()
# db_conn.create_tables()