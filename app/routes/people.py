from fastapi import APIRouter

router = APIRouter()

@router.get('/people')
def people():
    return "am israel hai"