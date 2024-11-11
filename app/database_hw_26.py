import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
from sqlalchemy.orm import DeclarativeBase

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DATABASE_URL = f"sqlite+aiosqlite:///{os.path.join(BASE_DIR, 'hw_26.db')}"  # для работы в пакете нужно указывать абсолютный путь!!!

# engine_26 = create_async_engine("sqlite+aiosqlite:///./hw_26.db", echo=True) # работает только в папке не в пакете питона!!!
engine_26 = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionApp = async_sessionmaker(engine_26, expire_on_commit=False)


class BaseHW(AsyncAttrs, DeclarativeBase):
    pass

# current_session = async_session()
