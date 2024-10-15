from fastapi import APIRouter, HTTPException, status, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from . import crud
from .schemas import Person, Person_create
from core.models import db

router = APIRouter(tags=['People'])


@router.get('/chronology', response_model=list[Person])
async def get_people(session: AsyncSession = Depends(db.session_dependency)):
    return await crud.get_all_people(session=session)


@router.post('/add', response_model=Person)
async def add_people(person_in: Person_create,
                     session: AsyncSession = Depends(db.session_dependency)):
    return await crud.create_person(session=session, person_in=person_in)


@router.get('/{person_id}/', response_model=Person)
async def get_people(person_id: int,
                     session: AsyncSession = Depends(db.session_dependency)):
    person = await crud.get_person(session=session, person_id=person_id)
    if person is not None:
        return person

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND, detail='not found'
    )
