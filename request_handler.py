import fastapi
import uvicorn
from routes import Books
from library_service import get_books

app = fastapi.FastAPI()

app.include_router(Books.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
  