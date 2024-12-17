from fastapi import APIRouter

from library_service import get_lendings, get_lending, create_lending

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
async def create_new_lending(book_id, user_id, start_date, end_date):
    create_lending(book_id, user_id, start_date, end_date)
    return {"message": "Lending created successfully"}