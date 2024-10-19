from itertools import product

from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Person, PersonCreate, PersonUpdate
from core.models import db
from .dependencies import person_by_id

router = APIRouter(tags=['People'])


@router.get('/chronology', response_model=list[Person])
async def get_people(session: AsyncSession = Depends(db.session_dependency)):
    return await crud.get_all_people(session=session)


@router.post('/add', response_model=Person)
async def add_people(person_in: PersonCreate,
                     session: AsyncSession = Depends(db.session_dependency)):
    return await crud.create_person(session=session, person_in=person_in)


@router.get('/{person_id}/', response_model=Person)
async def get_people(
        person: Person = Depends(person_by_id)
):
    return person


@router.put('/{person_id}/', response_model=Person)
async def update_person(person: Person = Depends(person_by_id),
                        person_update = PersonUpdate,
                        session: AsyncSession = Depends(db.session_dependency),
):
    return await crud.update_person(
        session=session,
        person=person,
        person_update=person_update,
    )
