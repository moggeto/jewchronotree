from fastapi import APIRouter

router = APIRouter()

@router.get('/chronology')
def people():
    return "there will be a tree"