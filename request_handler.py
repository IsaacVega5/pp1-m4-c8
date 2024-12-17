import fastapi
import uvicorn
from routes import Books, Reviews
from routes import Books, Lending
from library_service import get_books

app = fastapi.FastAPI()

app.include_router(Books.router)
app.include_router(Reviews.router)
app.include_router(Lending.router)

@app.get("/")
async def root():
    return {"message": "Hello World"}
  