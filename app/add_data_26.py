import asyncio

from sqlalchemy import insert
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker

from app.database_hw_26 import engine_26
from app.models_hw_26 import Recipe

DATA = {
    "title": "Ленивые пельмени",
    "cooking_time": 70,
    "ingredients": "Для начинки: Фарш мясной - 300 г, Лук репчатый - 120 г, Соль - по вкусу, Перец черный молотый - по вкусу"
    "Для теста: Вода - 210 мл, Соль - 0,5 ч. л., Яйцо - 1 шт., Мука пшеничная - 450 г"
    "Для бульона: Вода - 1 л, Соль - 1 ч. л., Лавровый лист - 1 шт., Перец черный горошком - 5 шт., Куркума (по желанию) - 0,3 ч. л.",
    "description": 'Я бы не сказала, что пельмени по данному рецепту "ленивые", а значит чем-то хуже обычных. Да, делаются они быстрее, '
    "но получаются очень красивыми и аппетитными. По вкусовым качествам ничуть не уступают обычным пельменям, которые многие просто обожают.",
}


async def insert_objects(async_session: async_sessionmaker[AsyncSession]) -> None:
    async with async_session() as session:
        async with session.begin():
            await session.execute(insert(Recipe), DATA)


if __name__ == "__main__":
    current_async_session = async_sessionmaker(engine_26, expire_on_commit=False)
    asyncio.run(insert_objects(current_async_session))
