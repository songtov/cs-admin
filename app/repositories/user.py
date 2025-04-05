from typing import Optional

from sqlalchemy.ext.asyncio import AsyncSession

from app.models.user import User

class UserRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def get_by_username(self, username: str) -> Optional[User]:
        # This is a placeholder. Implement actual database query here
        # For now, we'll use the fake users db
        from auth.users_db import fake_users_db
        user_data = fake_users_db.get(username)
        if user_data:
            return User(**user_data.dict())
        return None
