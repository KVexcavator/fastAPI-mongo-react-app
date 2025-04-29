from datetime import datetime
from typing import List, Optional
from beanie import Document, Link, PydanticObjectId
from pydantic import BaseModel, Field

class User(Document):
  username: str = Field(min_length=3, max_length=50)
  password: str
  email: str
  created: datetime = Field(default_factory=datetime.now)

  class Setting:
    name = "user"
  class Config:
    json_schema_extra = {
      "example": {
        "username": "Ivan",
        "password": "password",
        "email": "ivan@mail.local"
      }
    }

class RegisterUser(BaseModel):
  username: str
  password: str
  email: str

class LoginUser(BaseModel):
  username: str
  password: str

class CurrentUser(BaseModel):
  username: str
  email: str
  id: PydanticObjectId

class Car(Document):
  brand: str
  make: str
  year: int
  cm3: int
  price: float
  description: Optional[str] = None
  picture_url: Optional[str] = None
  pros: List[str] = []
  cons: List[str] = []
  date: datetime = datetime.now()
  user: Link[User] = None

  class Setting:
    name = "car"

class UpdateCar(BaseModel):
  price: Optional[float] = None
  description: Optional[str] = None
  pros: Optional[List[str]] = None
  cons: Optional[List[str]] = None