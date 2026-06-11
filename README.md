
# [Project Title]

"Library Management System"

---

## Project Description

 
"This project is a library management system that allows managing books and members. Users can add books, register members, borrow and return books, and view reports."

---

## Technologies Used

- Python
- FastAPI
- MySQL
- Docker
- [Add any other libraries or tools you used]

---

## Folder Structure


library-api/
├── main.py
├── database/
│   ├── db_connection.py
│   ├── book_db.py
│   └── member_db.py
├── routes/
│   ├── book_routes.py
│   ├── member_routes.py
│   └── report_routes.py
├── logs/
│   └── app.log
├── README.md
├── requirements.txt
└── .gitignore
```

---

## Docker Setup


```bash
docker run --name library-mysql -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=library_d_b -p 3306:3306 -d mysql:8
```

---

## Database Information

**Database Name:**  `library_d_b`

---

## Database Tables

### Table: `books`

| Column Name | Data Type | Constraints | Description |
|-------------|-----------|-------------|-------------|
| `id` | `INT` | `PRIMARY KEY` | book id |
| `title` | `VARCHAR(50)` | `NOT NULL` | book title|
| `author` | `VARCHAR(50)` | `NOT NULL` | author name|
| `genre` | `VARCHAR(50)` | `NOT NULL`| book genre|
| `is_available` | `BOOLEAN` | `NOT NULL` | |
| `id_member_by_borrowed` | `INT` | `DEFALT NULL`| id of member |


- Constraints (e.g., `PRIMARY KEY`, `NOT NULL`, `UNIQUE`, `ENUM`)
- A short description of what this column stores

---

### Table: `members`

| Column Name | Data Type | Constraints 
|-------------|-----------|-------------|-------------|
| id| `id`| `PRIMARY KEY`
| name| `VARCHAR(50)`| `NOT NULL`
| email| `EMAIL`| `NOT NULL`
| is_active| `BOOLEAN`| `NOT NULL`
| borrows_total| `INT`

---

## System Rules

1. המשתמש שולח genre/author/title — המערכת מוסיפה
   is_available=True, borrowed_by=NULL
2. ערך כל — Fiction / Non-Fiction / Science / History / Other להיות חייב 
   אחר מחזיר שגיאה
3.  המשתמש שולח email/name — המערכת מוסיפה ,True=active_is
    total_borrows=0
4.  חייב להיות ייחודי — אם קיים כבר מחזיר שגיאה
5. אם False=active_is — אי אפשר להשאיל ספר
6. אי אפשר להשאיל ספר שכבר מושאל )False=available_is)
7. חבר לא יכול להחזיק יותר מ3- ספרים בו-זמנית
8. ניתן להחזיר ספר רק אם הוא מושאל לאותו חבר שמחזיר אותו

---

## API Endpoints

### Books Endpoints


Method | Endpoint | תיאור
POST | /books| יצירת ספם 
GET| /books/{id}| לפי ספר ID 
GET | /books/{id} | לפי ספר ID
PATCH | /books/{id} | ספר עדכון
PATCH | /books/{id}/borrow/{member_id} | לחבר ספר השאלת
PATCH | /books/{id}/return/{member_id} | מחבר ספר החזרת



**What to write:**  
Fill in each row with information about your book-related endpoints:
- Method: GET, POST, PATCH, etc.
- Endpoint: The URL path (e.g., `/books`, `/books/{id}`)
- Description: What this endpoint does in simple words
- Request Body: The JSON structure needed (or write "None" if not needed)
- Response: What the endpoint returns

**Example for one row:**
| POST | /books | Creates a new book | `{"title": "...", "author": "...", "genre": "..."}` | Returns the created book with ID |

---

### Members Endpoints


Method | Endpoint | תיאור
POST | /members | יצירת חבר
GET | /members| כל החברים  
GET | /members/{id} | ID לפי חבר
PATCH | /members/{id} | חבר עדכון
PATCH |/members/{id}/deactivate | חבר השבתת
PATCH | /members/{id}/activate | חבר הפעלת




**What to write:**  
Same as Books Endpoints above, but for member-related endpoints.

---

### Reports Endpoints

Method | Endpoint | תיאור
GET | /reports/summary |כללי דוח
GET | /reports/books-by-genre | אנר'ז לפי ספרים
GET | /reports/top-member | פעיל הכי החב


**What to write:**  
Same as above, but for report-related endpoints.

---

## System Flow


1. **Server Startup:**
   - The server connects to MySQL
   - Creates tables if they don't exist
   - Starts the FastAPI server

2. **Creating a Member:**
   - User sends POST request to `/members` with name and email
   - System validates the email is unique
   - System creates member with `is_active=True` and `total_borrows=0`
   - Returns the created member

3. **Borrowing a Book:**
   - User sends PATCH request to `/books/{id}/borrow/{member_id}`
   - System checks if book exists
   - System checks if member exists and is active
   - System checks if book is available
   - System checks if member has less than 3 books
   - Updates book: `is_available=False`, `borrowed_by_member_id=member_id`
   - Increments member's `total_borrows` by 1
   - Returns success message


---

## Installation

**What to write:**  
List the step-by-step instructions for installing your project on a new computer.

**Why this section exists:**  
This helps anyone who wants to run your project get it set up correctly.

**Example structure:**

1. Clone the repository:
```bash
https://github.com/ArielKanner/library.git
```

2. Navigate to the project directory:
```bash
https://github.com/ArielKanner/library
```

3. Install dependencies:
```bash
[Write the pip install command here]
```

4. Set up the database:
```bash
docker run --name library-mysql -e MYSQL_ROOT_PASSWORD=secret -e MYSQL_DATABASE=library_d_b -p 3306:3306 -d mysql:8
```

---

## Running the Project

1. Start the FastAPI server:
```bash
uvicorn main:app --reload
```

2. Open your browser and go to:
```
http://localhost:8000/docs
```

---

## Testing the API


### Test 1: Create a Member
```
POST /members
{
  "name": "Sara Cohen",
  "email": "sara@example.com"
}
```

### Test 2: Create a Book
```
POST /books
{
  "title": "The Hitchhiker's Guide to the Galaxy",
  "author": "Douglas Adams",
  "genre": "Fiction"
}
```

### Test 3: Borrow a Book
```
PATCH /books/1/borrow/1
```

---

## Additional Notes

[Write any additional information here]

**What to write:**  
Include any extra information that might be helpful:
- Known issues or limitations
- Future improvements you'd like to make
- Special instructions or warnings
- Credits or acknowledgments

**This section is optional** — only include it if you have something important to add.