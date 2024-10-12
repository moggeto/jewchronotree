from fastapi import APIRouter

router = APIRouter()


# Страница отображения таблицы личностей
@router.get("/people")
def read_people():
    return 'wtf'
