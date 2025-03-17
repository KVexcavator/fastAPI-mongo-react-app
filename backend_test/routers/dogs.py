from fastapi import APIRouter
router = APIRouter()

# http http://localhost:8000/dogs/
@router.get("/")
async def get_dogs():
  return {"message": "All dogs here"}