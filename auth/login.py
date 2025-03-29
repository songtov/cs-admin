# auth/login.py

from fastapi import APIRouter, HTTPException, Depends
from fastapi.security import OAuth2PasswordRequestForm
from datetime import datetime, timedelta
import jwt

from auth.users_db import fake_users_db

SECRET_KEY = "your-secret-key"
ALGORITHM = "HS256"

router = APIRouter()

@router.post("/login")
def login(form_data: OAuth2PasswordRequestForm = Depends()):
    user = fake_users_db.get(form_data.username)
    if not user or user.password != form_data.password:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    # 토큰 발급
    token_data = {
        "sub": user.username,
        "exp": datetime.utcnow() + timedelta(hours=1),
    }
    token = jwt.encode(token_data, SECRET_KEY, algorithm=ALGORITHM)
    return {"access_token": token, "token_type": "bearer"}
