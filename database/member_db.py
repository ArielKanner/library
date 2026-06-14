from pydantic import BaseModel
from database.db_connection import DbConnection

db_conn = DbConnection()

class Member(BaseModel):
    name:str
    email:str

class MemberDB():
    def __init__(self):
        pass

    def create_member(self, data:Member):
        conn = db_conn.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT * FROM members WHERE email = %s', (data.email,))
        row = cursor.fetchone()
        if row == None:
            sql = 'INSERT INTO members (name, email) VALUES (%s,%s)'
            values = (data.name,data.email)

            cursor.execute(sql, values)
            conn.commit()

            cursor.close()
            conn.close()

    def get_all_members(self):
        conn = db_conn.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT * FROM members')
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows
    
    def get_member_by_id(self, id):
        conn = db_conn.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT * FROM members WHERE id = %s', (id,))
        row = cursor.fetchall()

        cursor.close()
        conn.close()

        return row
    
    def deactivate_member(self, id):
        conn = db_conn.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('UPDATE members SET is_active = 0 WHERE id = %s', (id,))
        conn.commit()

        cursor.close()
        conn.close()

    def activate_member(self, id):
        conn = db_conn.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('UPDATE members SET is_active = 1 WHERE id = %s', (id,))
        conn.commit()

        cursor.close()
        conn.close()
    
    def increment_borrows(self, id):
        conn = db_conn.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('UPDATE members SET total_borrows = total_borrows + 1  WHERE id = %s', (id,))
        conn.commit()

        cursor.close()
        conn.close()

    def count_active_members(self):
        conn = db_conn.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT COUNT(*) FROM members WHERE is_active = 1')
        rows = cursor.fetchall()

        cursor.close()
        conn.close()

        return rows[0]['COUNT(*)']
    
    def get_top_member(self):
        conn = db_conn.get_connection()
        cursor = conn.cursor(dictionary=True)

        cursor.execute('SELECT * FROM members ORDER BY total_borrows DESC LIMIT 1')
        row = cursor.fetchone()

        cursor.close()
        conn.close()
        return row

mem = MemberDB()
# data = {'name':'ari', 'email': 'ari@gmail'}
# data = Member(**data)
# mem.create_member(data)

# mem.deactivate_member(2)
# print(mem.get_top_member())

