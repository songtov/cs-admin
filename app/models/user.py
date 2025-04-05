from datetime import datetime
from typing import Optional

from pydantic import BaseModel, EmailStr

class User(BaseModel):
    id: Optional[int] = None
    username: str
    email: EmailStr
    full_name: Optional[str] = None
    hashed_password: str
    created_at: datetime = datetime.utcnow()
    updated_at: datetime = datetime.utcnow()

    class Config:
        from_attributes = True
