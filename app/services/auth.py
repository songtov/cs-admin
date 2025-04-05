from datetime import datetime, timedelta

import jwt
from fastapi import HTTPException

from app.core.config import settings
from app.models.user import User
from app.repositories.user import UserRepository

class AuthService:
    def __init__(self, user_repository: UserRepository):
        self.user_repository = user_repository

    async def authenticate_user(self, username: str, password: str) -> User:
        user = await self.user_repository.get_by_username(username)
        if not user or not self.verify_password(password, user.hashed_password):
            raise HTTPException(status_code=401, detail="Invalid credentials")
        return user

    def create_access_token(self, user: User) -> str:
        token_data = {
            "sub": user.username,
            "exp": datetime.utcnow() + timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES),
        }
        return jwt.encode(token_data, settings.SECRET_KEY, algorithm=settings.ALGORITHM)

    @staticmethod
    def verify_password(plain_password: str, hashed_password: str) -> bool:
        # Implement proper password hashing here
        return plain_password == hashed_password  # This is just for example
