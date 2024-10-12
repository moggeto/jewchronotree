from pydantic_settings import BaseSettings

class Setting(BaseSettings):
    db_url: str = 'sqlite+aiosqlite:///'

