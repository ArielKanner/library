from fastapi import FastAPI
from database.book_db import BookDB
from database.member_db import MemberDB
import uvicorn
from pydantic import BaseModel

class Book(BaseModel):
    title:str
    author:str
    genre:str

class Member(BaseModel):
    name:str
    email:str

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

@app.put('/members/{id}/deactivate')
def deactivate(id):
    mdb.deactivate_member(id)

@app.put('/members/{id}/activate')
def activate(id):
    mdb.activate_member(id)

@app.post('/members')
def create_m(data:Member):
    return mdb.create_member(data)




@app.get('/reports/books-by-genre')
def books_by_genre():
    return [{"Genre": "Science", "COUNT": bdb.count_by_genre('science')},
            {"Genre": "History", "COUNT": bdb.count_by_genre('history')},
            {"Genre": "Fiction", "COUNT": bdb.count_by_genre('fiction')},
            {"Genre": "Non-Fiction", "COUNT": bdb.count_by_genre('non-fiction')},
            {"Genre": "Other", "COUNT": bdb.count_by_genre('other')}
            ]

@app.get('/reports/summary')
def get_summary():
    return {"total_books": bdb.count_total_books(),
            "available_books": bdb.count_available_books(),
            "currently_borrowed": bdb.count_borrowed_books(),
            "active_members": mdb.count_active_members()
            }

@app.get('/reports/top-member')
def best_borrow():
    res = mdb.get_top_member()
    return {
            "member_id": res['id'],
            "borrowed": res['total_borrows']  
            }
    
if __name__ == '__main__':
    uvicorn.run("main:app", host = "127.0.0.1", port = 8000, reload=True)