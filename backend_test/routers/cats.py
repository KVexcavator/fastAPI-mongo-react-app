from fastapi import APIRouter
router = APIRouter()


# http http://localhost:8000/cats/
@router.get("/")
async def get_cats():
  return {"message": "All cats here"}