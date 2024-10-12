from fastapi import APIRouter
from app.routes import home, about_us, people, cronology, add_people

api_router = APIRouter()
api_router.include_router(home.router)
api_router.include_router(about_us.router)
api_router.include_router(people.router)
api_router.include_router((cronology.router))
api_router.include_router(add_people.router)