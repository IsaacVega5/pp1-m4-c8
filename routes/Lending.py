from fastapi import APIRouter

from library_service import get_lendings, get_lending, create_lending, update_lending_by_id
from models import BookLendingModel

router = APIRouter(
  prefix="/lending",
  tags=["lending"],
  responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_lending_list():
  result = get_lendings()
  return {"books": result}

@router.get("/{book_id}")
async def get_lending_by_book_id(book_id):
  result = get_lending(book_id)
  return {"books": result}

@router.post("/")
async def create_new_lending(lending: BookLendingModel):
  result = create_lending(lending.book_id, lending.user_id, lending.start_date, lending.end_date)
  return {
    "lending": result
  }

@router.put("/{lending_id}")
async def update_lending(lending_id, lending: BookLendingModel):
  result = update_lending_by_id(lending_id, lending.book_id, lending.user_id, lending.start_date, lending.end_date)
  return {
    "lending": result
  }