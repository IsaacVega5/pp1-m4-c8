from fastapi import APIRouter

from library_service import get_books

router = APIRouter(
  prefix="/books",
  tags=["books"],
  responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_books_list():
  result = get_books()
  return {"books": result}