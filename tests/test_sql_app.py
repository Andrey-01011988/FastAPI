import pytest
from fastapi.testclient import TestClient

from app.main_hw_26 import app_26, get_current_session
from app.models_hw_26 import BaseHW, Recipe
from tests.database_test import engine_test, test_session


# Переопределение сессии приложения для тестирования
async def override_get_session():
    try:
        yield test_session
    finally:
        await test_session.close()


app_26.dependency_overrides[get_current_session] = override_get_session


@pytest.fixture(scope="module")
async def setup_database():
    print("Запуск фикстуры")
    async with engine_test.begin() as conn:
        # Создайте все таблицы в тестовой базе данных
        print("начало")
        await conn.run_sync(BaseHW.metadata.create_all)
        print("тестовая б/д создана")

        # Заполнение тестовыми данными
        async with test_session:
            test_recipe = Recipe(
                title="Тестовый рецепт",
                cooking_time=30,
                ingredients="что-то",
                description="где-то",
                views=0,
            )
            test_session.add(test_recipe)
            await test_session.commit()

    yield  # Здесь будут выполняться тесты

    async with engine_test.begin() as conn:
        # Удалите все таблицы после завершения всех тестов
        await conn.run_sync(BaseHW.metadata.drop_all)


@pytest.mark.asyncio
async def test_all_recipes(setup_database):
    client = TestClient(app_26)
    response = client.get("/recipes")
    assert response.status_code == 200
    assert len(response.json()) > 0  # Проверяем, что есть хотя бы один рецепт


@pytest.mark.asyncio
async def test_one_recipe(setup_database):
    client = TestClient(app_26)
    response = client.get(
        "/recipe/1"
    )  # Предполагается, что ID = 1 для тестового рецепта
    # print(response.json())
    assert response.status_code == 200
    assert response.json()["title"] == "Тестовый рецепт"


@pytest.mark.asyncio
async def test_no_recipe_in_db(setup_database):
    client = TestClient(app_26)
    response = client.get("/recipe/999")
    assert response.status_code == 404
