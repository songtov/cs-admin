from fastapi import FastAPI

from auth import login
from routers import cs_tasks

app = FastAPI(title="CS Admin Tool")

app.include_router(login.router)
app.include_router(cs_tasks.router)
