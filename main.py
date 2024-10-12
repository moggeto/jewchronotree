# from fastapi import FastAPI
# from app.pages import api_router
#
# import uvicorn
#
#
#
# app = FastAPI()
#
# app.include_router(api_router)
#
# if __name__ == '__main__':
#     uvicorn.run('main:app', reload=True)
from fastapi import FastAPI, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from core.models.database import create_db_engine, get_session
from app.crud import get_all_people, create_person, get_person_by_id, update_person, delete_person

app = FastAPI()

# Шаблоны Jinja2
templates = Jinja2Templates(directory="templates")

# Инициализация базы данных
engine = create_db_engine()
session: Session = get_session(engine)

# Страница отображения таблицы личностей
@app.get("/")
def read_people(request: Request):
    people = get_all_people(session)
    return templates.TemplateResponse("index.html", {"request": request, "people": people})

# Страница добавления новой личности
@app.get("/add")
def add_person_page(request: Request):
    return templates.TemplateResponse("add.html", {"request": request})

# Форма для добавления новой личности
@app.post("/add")
def add_person(name: str = Form(...), birth_date: int = Form(None), death_date: int = Form(None), tribe: str = Form(None)):
    create_person(session, name=name, birth_date=birth_date, death_date=death_date, tribe=tribe)
    return RedirectResponse("/", status_code=303)

# Страница редактирования личности
@app.get("/edit/{person_id}")
def edit_person(request: Request, person_id: int):
    person = get_person_by_id(session, person_id)
    return templates.TemplateResponse("edit.html", {"request": request, "person": person})

# Форма для редактирования личности
@app.post("/edit/{person_id}")
def update_person_data(person_id: int, name: str = Form(...), birth_year: int = Form(None), death_year: int = Form(None), tribe: str = Form(None)):
    update_person(session, person_id, name=name, birth_year=birth_year, death_year=death_year, tribe=tribe)
    return RedirectResponse("/", status_code=303)

# Удаление личности
@app.get("/delete/{person_id}")
def delete_person_data(person_id: int):
    delete_person(session, person_id)
    return RedirectResponse("/", status_code=303)

