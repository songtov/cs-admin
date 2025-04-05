from contextlib import asynccontextmanager
from typing import AsyncGenerator

from fastapi import FastAPI

from app.api.v1.auth.router import router as auth_router
from app.api.v1.cs_tasks.router import router as cs_tasks_router
from app.core.config import settings
from app.core.database import init_db

@asynccontextmanager
async def lifespan(app: FastAPI) -> AsyncGenerator[None, None]:
    # Startup
    await init_db()
    yield
    # Shutdown
    # Add any cleanup code here

app = FastAPI(
    title="CS Admin Tool",
    description="A comprehensive CS administration tool",
    version="1.0.0",
    lifespan=lifespan,
)

# Include routers
app.include_router(auth_router)
app.include_router(cs_tasks_router)

@app.get("/health")
async def health_check():
    return {"status": "healthy"}
