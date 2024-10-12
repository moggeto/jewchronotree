from fastapi import APIRouter

router = APIRouter()



@router.get("/about")
def home_page():
    return 'сайт хронологии, даник пес'