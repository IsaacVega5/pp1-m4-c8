import sqlite3
from domain import  Books

def get_books(book_id):
    con = sqlite3.connect("tf_backend_book.sqlite3")
    cur = con.cursor()
    res = cur.execute("SELECT * FROM books WHERE id = ?", (book_id,)).fetchone()
    if res:
        return Books(res[0], res[1], res[2], res[3], res[4], res[5]).__dict__()
    else:
        return None