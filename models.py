
from typing import List
from pydantic import BaseModel

class BooksModel(BaseModel):
  name: str
  publisher: str
  year: str
  edition: int
  authors: str

  
class UsersModel(BaseModel):
  id : str
  name: str
  
  users_lending : List["BookLendingModel"]

class BookLendingModel(BaseModel):
  book_id : str
  user_id : str
  start_date: str
  end_date: str
  
  book : BooksModel
  user : UsersModel

class BookReviewModel(BaseModel):
  book_id : str
  review: str
  validated: int