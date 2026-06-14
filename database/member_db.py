from pydantic import BaseModel
from db_connection import get_connection

class Member(BaseModel):
    name:str
    email:str

class MemberDB():
    def __init__(self):
        pass

    def create_member(self, data:Member):
        conn = get_connection()
        cursor = conn.cursor(dictionary=True)

        sql = 'INSERT INTO members (name, email) VALUES (%s,%s)'
        values = (data.name,data.email)

        cursor.execute(sql, values)
        conn.commit()

        cursor.close()
        conn.close()

    

mem = MemberDB()
data = {'name':'avi', 'email': 'avi@gmail'}
data = Member(**data)
mem.create_member(data)
