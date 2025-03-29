from fastapi import FastAPI
from routers import cs_tasks
from auth import login

app = FastAPI(title="CS Admin Tool")

app.include_router(login.router)
app.include_router(cs_tasks.router)
