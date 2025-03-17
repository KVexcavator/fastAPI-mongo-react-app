import shutil
import os
from typing import Dict, Annotated
from enum import Enum
from random import randint
from fastapi import FastAPI, Path, Body, Header, Form, File, UploadFile, status, HTTPException, Depends,Request
from pydantic import BaseModel

app = FastAPI()

class AccountType(str, Enum):
    FREE = "free"
    PRO = "pro"

# http http://localhost:8000/
@app.get("/")
async def root():
    return {"message": "Hello FastAPI"}

# http POST http://localhost:8000/
@app.post("/")
async def post_root():
    return {"message": "Post request success!"}

# http http://localhost:8000/car/1
@app.get("/car/{id}")
async def car_id(id: int):
    return {"car_id": id}

# http http://localhost:8000/account/free/4
@app.get("/account/{acc_type}/{months}")
async def account(acc_type: AccountType, months: int = Path(..., ge=3, le=12)):
    return {"message": "Account created", "account_type": acc_type, "months": months}

# http "http://localhost:8000/cars/price?min_price=2000&max_price=4000"
@app.get("/cars/price")
async def cars_by_price(min_price: int = 0, max_price: int = 100000):
    return {"Message": f"Listing cars with prices between {min_price} and {max_price}"}

# http POST "http://localhost:8000/native/cars" brand="FIAT" model="500" year=2015
@app.post("/native/cars")
async def native_new_car(data: Dict = Body(...)):
    print(data)
    return {"message": data}

class InsertCar(BaseModel):
    brand: str
    model: str
    year: int

# http POST "http://localhost:8000/cars" brand="FIAT" model="500" year=2015
@app.post("/cars")
async def new_car(data: InsertCar):
    print(data)
    return {"message": data}

class UserModel(BaseModel):
    username: str
    name: str

# http POST "http://localhost:8000/car/user"    car:='{"brand": "Toyota", "model": "Corolla", "year": 2020}' user:='{"username": "johndoe", "name": "John Doe"}' code:=1234
@app.post("/car/user")
async def new_car_model(car: InsertCar, user: UserModel, code: int = Body(None)):
    return {"car": car, "user": user, "code": code}

# http GET "http://localhost:8000/headers"
@app.get("/headers")
async def read_headers(user_agent: Annotated[str | None, Header()] = None):
    return {"User-Agent": user_agent}

# Form function
# pip install python-multipart==0.0.9
# http -f POST localhost:8000/upload brand='Ferrari' model='Testarossa' picture@test_upload.jpeg

UPLOAD_DIR = "uploads"
os.makedirs(UPLOAD_DIR, exist_ok=True)

@app.post("/upload")
async def upload(
    picture: UploadFile = File(...), 
    brand: str = Form(...),
    model: str = Form(...)
):
    file_path = os.path.join(UPLOAD_DIR, picture.filename)
    with open(file_path, "wb") as buffer:
        shutil.copyfileobj(picture.file, buffer)
    return {
        "brand": brand, 
        "model": model, 
        "file_name": picture.filename,
        "saved_path": file_path
    }

# Setting status codes
# http GET "http://localhost:8000/status/code"
@app.get(
    "/status/code", 
    status_code=status.HTTP_208_ALREADY_REPORTED
)
async def raw_fa_response():
    return {"message": "fastapi response"}

# HTTP errors
# http POST http://localhost:8000/carsmodel brand="fiat" model="500L" year=2023
@app.post("/carsmodel")
async def new_car_model(car: InsertCar):
    if car.year > 2022:
        raise HTTPException(
            status.HTTP_406_NOT_ACCEPTABLE, detail="The car doesn't exist yet!"
        )
    return { "message": car}

# Dependency injection

async def pagination(
        q: str | None = None, 
        skip: int = 0, 
        limit: int = 100
):
    return {"q": q, "skip": skip, "limit": limit}

# http http://localhost:8000/items/cars
@app.get("/items/cars")
async def read_items(
    commons: Annotated[dict, Depends(pagination)]
):
    return commons

# routes
# go to folder /routers
from routers.dogs import router as dogs_router
from routers.cats import router as cats_router

app.include_router(dogs_router, prefix="/dogs", tags=["dogs"])
app.include_router(cats_router, prefix="/cats", tags=["cats"])

# Middleware

@app.middleware("http")
async def add_random_header(request: Request, call_next):
    number = randint(1,10)
    response = await call_next(request)
    response.headers["X-Random-Integer"] = str(number)
    return response

# http http://localhost:8000/mdl
@app.get("/mdl")
async def with_mdl():
    return {"message": "Hello MDL"}