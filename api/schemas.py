from pydantic import BaseModel, ConfigDict


class PersonBase(BaseModel):
    name: str
    birth_date: int
    death_date: int
    tribe: str
    role: str
    description: str


class PersonCreate(PersonBase):
    pass


class PersonUpdate(PersonCreate):
    pass


class PersonUpdatePartial(PersonCreate):
    name: str | None = None
    birth_date: int | None = None
    death_date: int | None = None
    tribe: str | None = None
    role: str | None = None
    description: str | None = None


class Person(PersonBase):
    model_config = ConfigDict(from_attributes=True)
    id: int
