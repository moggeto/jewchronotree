from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase, declared_attr

class Base(DeclarativeBase):
    __abstract__ = True
    @declared_attr
    def __tablename__(cls) -> str:
        return cls.__name__.lower()
    id: Mapped[int] = mapped_column(primary_key=True)