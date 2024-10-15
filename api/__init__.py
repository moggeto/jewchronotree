from fastapi import APIRouter
from .veiws import router as person_router

router = APIRouter()
router.include_router(router=person_router, prefix='/people')