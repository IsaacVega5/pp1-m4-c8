import sqlite3
import uuid
from domain import  Books

def get_book(book_id):
    con = sqlite3.connect("tf_backend_book.sqlite3")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if res:
        return Books(res[0], res[1], res[2], res[3], res[4], res[5]).__dict__()
    else:
        return None

def get_books():
    con = sqlite3.connect("tf_backend_book.sqlite3")
    cur = con.cursor()
    return cur.execute("SELECT * FROM books").fetchall()

def create_book(name, publisher, year, edition, authors):
    con = sqlite3.connect("tf_backend_book.sqlite3")
    cur = con.cursor()
    id = str(uuid.uuid4())
    cur.execute("INSERT INTO books (id, name, publisher, year, edition, authors) VALUES (?,?, ?, ?, ?, ?)", (id, name, publisher, year, edition, authors))
    con.commit()
    return {
        "id": id,
        "name": name,
        "publisher": publisher,
        "year": year,
        "edition": edition,
        "authors": authors
    }

def update_book(book_id, name, publisher, year, edition, authors):
    con = sqlite3.connect("tf_backend_book.sqlite3")
    cur = con.cursor()
    cur.execute("UPDATE books SET name = ?, publisher = ?, year = ?, edition = ?, authors = ? WHERE id = ?", (name, publisher, year, edition, authors, book_id))
    con.commit()
    return {
        "id": book_id,
        "name": name,
        "publisher": publisher,
        "year": year,
        "edition": edition,
        "authors": authors
    }

def delete_book(book_id):
    con = sqlite3.connect("tf_backend_book.sqlite3")
    cur = con.cursor()
    try:
        cur.execute("DELETE FROM book_lending WHERE book_id = ?", (book_id,))
        con.commit()    
    except:
        pass
    
    return f"Book {book_id} deleted"