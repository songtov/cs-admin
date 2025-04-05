from fastapi import APIRouter, Depends

from app.core.dependencies import get_current_user
from app.models.user import User
from .schemas import HelloResponse

router = APIRouter(
    prefix="/cs-tasks",
    tags=["cs-tasks"],
)

@router.get("/hello", response_model=HelloResponse)
async def protected_hello(current_user: User = Depends(get_current_user)):
    return {"message": f"Hello {current_user.full_name}"}
