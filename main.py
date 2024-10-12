from contextlib import asynccontextmanager

from fastapi import FastAPI
from app.pages import api_router

import uvicorn
from core.models import Base, db


@asynccontextmanager
async def lifespan(app: FastAPI):
    async with db.engine.connect() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(lifespan=lifespan)

app.include_router(api_router)

if __name__ == '__main__':
    uvicorn.run('main:app', reload=True)
