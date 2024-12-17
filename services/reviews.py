
import sqlite3
import uuid

from library_service import get_book

def get_reviews():
  con = sqlite3.connect("tf_backend_book.sqlite3")
  cur = con.cursor()
  return cur.execute("SELECT * FROM book_reviews").fetchall()

def get_review(review_id):
  con = sqlite3.connect("tf_backend_book.sqlite3")
  cur = con.cursor()
  res = cur.execute("SELECT * FROM book_reviews WHERE review_id = ?", (review_id,)).fetchone()
  if res:
    return {
      "id": res[0],
      "book_id": res[1],
      "review": res[2],
      "validated": res[3]
    }
  else:
    return None

def create_review(book_id, review, validated):
  con = sqlite3.connect("tf_backend_book.sqlite3")
  cur = con.cursor()
  id = str(uuid.uuid4())
  
  book = get_book(book_id)
  if not book:
    return None
  
  cur.execute("INSERT INTO book_reviews (review_id, book_id, review, validated) VALUES (?,?, ?, ?)", (id, book_id, review, validated))
  con.commit()
  return {
    "id": id,
    "book_id": book_id,
    "review": review,
    "validated": validated
  }
  
def update_review(review_id, book_id, review, validated):
  con = sqlite3.connect("tf_backend_book.sqlite3")
  cur = con.cursor()
  cur.execute("UPDATE book_reviews SET book_id = ?, review = ?, validated = ? WHERE review_id = ?", (book_id, review, validated, review_id))
  con.commit()
  return {
    "id": review_id,
    "book_id": book_id,
    "review": review,
    "validated": validated
  }

def delete_review(review_id):
  con = sqlite3.connect("tf_backend_book.sqlite3")
  cur = con.cursor()
  cur.execute("DELETE FROM book_reviews WHERE review_id = ?", (review_id,))
  con.commit()
  return f"Review {review_id} deleted"