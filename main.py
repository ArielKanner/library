from fastapi import FastAPI
from database.book_db import BookDB
from database.member_db import MemberDB
import uvicorn
from pydantic import BaseModel

class Book(BaseModel):
    title:str
    author:str
    genre:str

app = FastAPI()

bdb = BookDB()
mdb = MemberDB()

@app.get('/books')
def get_all_books():
    return bdb.get_all_books()

@app.get('/books/{id}')
def get_book_by_id(id):
    return bdb.get_book_by_id(id)

@app.post('/books')
def create_b(data:Book):
    bdb.create_book(data)

@app.put('/books/{id}/borrow/{member_id}')
def borrow_to_member(id, member_id):
    bdb.set_available(id, 0, member_id)
    mdb.increment_borrows(member_id)

@app.put('/books/{id}/return/{member_id}')
def return_book(id, member_id):
    bdb.set_available(id, 1, member_id)
    


@app.get('/members')
def get_all_members():
    return mdb.get_all_members()

@app.get('/members/{id}')
def get_member_by_id(id):
    return mdb.get_member_by_id(id)

@app.put('members/{id}/deactive')

if __name__ == '__main__':
    uvicorn.run("main:app", host = "127.0.0.1", port = 8000)