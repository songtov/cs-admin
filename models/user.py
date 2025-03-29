# models/user.py

from pydantic import BaseModel


class User(BaseModel):
    username: str
    full_name: str
    password: str  # 실무에서는 해싱해야 함
