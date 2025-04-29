from contextlib import asynccontextmanager
from fastapi import FastAPI
from fastapi_cors import CORS
from database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI):
  await init_db()
  yield

app = FastAPI(lifespan=lifespan)

CORS(app) 
# .env ALLOW_ORIGINS, ALLOWED_CREDENTIALS, ALLOWED_METHODS, ALLOWED_ORIGINS, and others

# http http://localhost:8000/
@app.get("/", tags=["Root"])
async def read_root() -> dict:
  return {"message": "Welcome to your beanie powered app!"}