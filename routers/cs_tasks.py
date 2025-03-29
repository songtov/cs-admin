# routers/cs_tasks.py

from fastapi import APIRouter, Depends
from auth.deps import get_current_user
from models.user import User

router = APIRouter()

@router.get("/hello")
def protected_hello(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello {current_user.full_name}"}
