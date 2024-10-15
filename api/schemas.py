from pydantic import BaseModel, ConfigDict


class PersonBase(BaseModel):
    name: str
    birth_date: int
    death_date: int
    tribe: str
    role: str
    description: str

class Person_create(PersonBase):
    pass

class Person(PersonBase):
    model_config = ConfigDict(from_attributes=True)
    id: int

