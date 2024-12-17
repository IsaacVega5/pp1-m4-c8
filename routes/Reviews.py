from unittest import result
from fastapi import APIRouter, HTTPException

from services import reviews as rs
from models import BookReviewModel

router = APIRouter(
  prefix="/reviews",
  tags=["books"],
  responses={404: {"description": "Not found"}}
)

@router.get("/")
async def get_reviews_list():
  result = rs.get_reviews()
  return {"reviews": result}

@router.get("/{review_id}")
async def get_review_by_id(review_id: str):
  result = rs.get_review(review_id)
  return {"review": result}

@router.post("/")
async def create_review(review: BookReviewModel):
  result = rs.create_review(review.book_id, review.review, review.validated)
  if not result:
    raise HTTPException(status_code=404, detail="Book not found")
  return {"review": result}

@router.put("/{review_id}")
async def update_review(review_id: str, review: BookReviewModel):
  result = rs.update_review(review_id, review.book_id, review.review, review.validated)
  return {"review": result}

@router.delete("/{review_id}")
async def delete_review(review_id: str):
  result = rs.delete_review(review_id)
  return {"result": result}