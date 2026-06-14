from pydantic import BaseModel
from database.db_connection import get_connection

class Book(BaseModel):
    title:str
    author:str
    genre:str

class BookDB:
    # def __init__(self, title, author, genre):
    def __init__(self):
        # self.title = title
        # self.author = author
        # self.genre = genre
        pass

    def create_book(self, data:Book):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = 'INSERT INTO books (title, author, genre) VALUES (%s,%s,%s)'
        values = (data.title,data.author,data.genre)

        cursor.execute(sql, values)
        conn.commit()

        cursor.close()
        conn.close()

    def get_all_books(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('select * from books')
        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return rows
    
    def get_book_by_id(self, id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('select * from books WHERE id = %s', (id,))
        row = cursor.fetchone()

        cursor.close()
        conn.close()
        return row
    
    def set_available(self, id, val, member_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        if val in [0, None]:
            sql = 'UPDATE books SET is_available = 0, borrowed_by_member_id = %s WHERE id = %s'
            values = (member_id, id)
        else:
            sql = 'UPDATE books SET is_available = 1, borrowed_by_member_id = NULL WHERE id = %s AND borrowed_by_member_id = %s'
            values = (id, member_id)
        
        cursor.execute(sql, values)
        conn.commit()

        is_changed = cursor.rowcount > 0

        cursor.close()
        conn.close()
        return is_changed
    
    def count_total_books(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT COUNT(*) FROM books')
        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return rows[0]['COUNT(*)']
    
    def count_available_books(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT COUNT(*) FROM books WHERE is_available = 1')
        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return rows[0]['COUNT(*)']
    
    def count_borrowed_books(self):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT COUNT(*) FROM books WHERE is_available = 0')
        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return rows[0]['COUNT(*)']
    
    def count_by_genre(self, genre):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT COUNT(*) FROM books WHERE genre = %s', (genre,))
        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return rows[0]['COUNT(*)']
    
    def count_active_borrows_by_member(self, member_id):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT COUNT(*) FROM books WHERE borrowed_by_member_id = %s', (member_id,))
        rows = cursor.fetchall()

        cursor.close()
        conn.close()
        return rows[0]['COUNT(*)']

bdb= BookDB()

# data = {'title': 'two', 'author': 'BLI', 'genre': 'history'}
# data = Book(**data)
# bdb.create_book(data)

print(bdb.set_available(9, 0, 67))

 