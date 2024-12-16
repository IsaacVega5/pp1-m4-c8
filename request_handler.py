import fastapi
import uvicorn

from library_service import get_books

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
  
@app.get("/books/")
async def get_books_list():
  result = get_books()
  return {"books": result}