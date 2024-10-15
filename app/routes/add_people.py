from fastapi import APIRouter

router = APIRouter()

# Форма для добавления новой личности
# @router.post("/add")
# def add_person(name: str = Form(...), birth_date: int = Form(None), death_date: int = Form(None), tribe: str = Form(None)):
#     create_person(session, name=name, birth_date=birth_date, death_date=death_date, tribe=tribe)
#     return RedirectResponse("/", status_code=303)