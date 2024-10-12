from sqlalchemy import Column, Integer, String, ForeignKey, Table
from sqlalchemy.orm import relationship, Mapped
from .base import Base


class Person(Base):
    __tablename__ = 'person'

    name: Mapped[str]
    birth_date: Mapped[int]
    death_date: Mapped[int]
    tribe: Mapped[str]
    role: Mapped[str]
    description: Mapped[str]
