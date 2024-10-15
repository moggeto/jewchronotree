from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.pages import api_router

import uvicorn
from core.config import settings
from core.models import Base, db
from api import router as router_v1


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)
app.include_router(router_v1, prefix=settings.api_v1_prefix)
app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
