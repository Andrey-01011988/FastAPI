import os

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker

# URL для тестовой базы данных
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
# TEST_DATABASE_URL = "sqlite+aiosqlite:///./test.db"
TEST_DATABASE_URL = f"sqlite+aiosqlite:///{os.path.join(BASE_DIR, 'test.db')}"

# Создание асинхронного движка
engine_test = create_async_engine(TEST_DATABASE_URL, echo=True)

# Создание async_sessionmaker для тестирования
async_session = async_sessionmaker(bind=engine_test, expire_on_commit=False)

test_session = async_session()