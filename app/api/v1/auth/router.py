from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm

from app.core.dependencies import get_auth_service
from app.services.auth import AuthService
from .schemas import Token

router = APIRouter(
    prefix="/auth",
    tags=["auth"],
    responses={401: {"description": "Invalid credentials"}},
)

@router.post("/login", response_model=Token)
async def login(
    form_data: OAuth2PasswordRequestForm = Depends(),
    auth_service: AuthService = Depends(get_auth_service)
):
    user = await auth_service.authenticate_user(form_data.username, form_data.password)
    access_token = auth_service.create_access_token(user)
    return {"access_token": access_token, "token_type": "bearer"}
