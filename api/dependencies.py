from typing import Annotated
from fastapi import Path, Depends, HTTPException, status
from sqlalchemy.ext.asyncio import AsyncSession

from core.models import db, Person

from . import crud


async def person_by_id(
        person_id: Annotated[int, Path],
        session: AsyncSession = Depends(db.session_dependency)
) -> Person:
    person = await crud.get_person(session=session, person_id=person_id)
    if person is not None:
        return person

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail='not found'
    )
