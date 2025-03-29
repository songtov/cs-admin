# auth/users_db.py

from models.user import User

fake_users_db = {
    "alice": User(username="alice", full_name="Alice Kim", password="1234"),
    "bob": User(username="bob", full_name="Bob Lee", password="abcd"),
}
