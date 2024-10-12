from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .people import Base

# Инициализация базы данных
def create_db_engine(database_url='sqlite:///chronology.db'):
    engine = create_engine(database_url)
    Base.metadata.create_all(engine)
    return engine

# Создание сессии
def get_session(engine):
    Session = sessionmaker(bind=engine)
    return Session()