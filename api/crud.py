from itertools import product

from sqlalchemy import select
from sqlalchemy.engine import Result
from sqlalchemy.ext.asyncio import AsyncSession
from core.models import Person
from .schemas import PersonCreate, PersonUpdate, PersonUpdatePartial


async def get_all_people(session: AsyncSession) -> list[Person]:
    statement = select(Person).order_by(Person.id)
    result: Result = await session.execute(statement)
    people = result.scalars().all()
    return list(people)


async def get_person(session: AsyncSession, person_id: int) -> Person | None:
    return await session.get(Person, person_id)


# async def create_person(session: AsyncSession, person_in: Person_create) -> Person:
#     person = Person(**person_in.model_dump())
#     session.add(person)
#     await session.commit()
#     return person
async def create_person(session: AsyncSession, person_in: PersonCreate) -> Person:
    if not person_in.name:  # Проверка, что имя заполнено
        raise ValueError("Name is required to create a person")

    person = Person(**person_in.model_dump())  # Убедитесь, что модель заполняется корректно
    session.add(person)
    await session.commit()
    return person


async def update_person(
        session: AsyncSession,
        person: Person,
        person_update: PersonUpdate | PersonUpdatePartial,
        partial: bool = False,
) -> Person:
    for name, value in person_update.model_dump(exclude_unset=partial).items():
        setattr(person, name, value)
    await person.commit()
    return person


async def delete_person(
        session: AsyncSession,
        person: Person,
) -> None:
    await session.delete(person)
    await session.commit()

# from core.models.people import Person
#
# # Создание записи
# def create_person(session, name, birth_date=None, death_date=None, tribe=None, role=None):
#     new_person = Person(name=name, birth_date=birth_date, death_date=death_date, tribe=tribe, role=role)
#     session.add(new_person)
#     session.commit()
#     return new_person
#
# # Чтение всех записей
# def get_all_people(session):
#     return session.query(Person).all()
#
# # Чтение записи по ID
# def get_person_by_id(session, person_id):
#     return session.query(Person).filter_by(id=person_id).first()
#
# # Обновление записи
# def update_person(session, person_id, **kwargs):
#     person = session.query(Person).filter_by(id=person_id).first()
#     if not person:
#         return None
#
#     for key, value in kwargs.items():
#         if hasattr(person, key):
#             setattr(person, key, value)
#
#     session.commit()
#     return person
#
# # Удаление записи
# def delete_person(session, person_id):
#     person = session.query(Person).filter_by(id=person_id).first()
#     if person:
#         session.delete(person)
#         session.commit()
#         return True
#     return False
