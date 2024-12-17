from unittest import result
from fastapi import APIRouter, Depends

import library_service as ls
from models import BooksModel

router = APIRouter(
  prefix="/books",
  tags=["books"],
  responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_books_list():
  result = ls.get_books()
  return {"books": result}

@router.get("/{book_id}")
async def get_book_by_id(book_id: int):
  
  result = ls.get_book(book_id)
  return {"book": result}

@router.post("/")
async def create_book(book: BooksModel):
  result = ls.create_book(book.name, book.publisher, book.year, book.edition, book.authors)
  return {
    "book": result
  }

@router.put("/{book_id}")
async def update_book(book_id: str, book: BooksModel):
  result = ls.update_book(book_id, book.name, book.publisher, book.year, book.edition, book.authors)
  return {
    "book": result
  }

@router.delete("/{book_id}")
async def delete_book(book_id: str):
  result = ls.delete_book(book_id)
  return {
    "result": result
  }
