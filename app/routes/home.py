from fastapi import APIRouter

router = APIRouter()


@router.get("/")
@router.get("/home")
def home_page():
    return 'hello'
