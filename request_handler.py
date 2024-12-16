import fastapi
import uvicorn

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}