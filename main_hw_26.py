from contextlib import asynccontextmanager
from typing import List, Sequence

from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy import select, desc, update
from sqlalchemy.ext.asyncio import AsyncSession

from module_26_fastapi.homework import models_hw_26
from module_26_fastapi.homework import schemas_hw_26
from module_26_fastapi.homework.database_hw_26 import engine_26, AsyncSessionApp

# current_session = AsyncSessionApp()

@asynccontextmanager
async def lifespan(app: FastAPI):
    current_session = AsyncSessionApp()
    async with engine_26.begin() as conn:
        await conn.run_sync(models_hw_26.BaseHW.metadata.create_all)
        yield
    await current_session.close()
    await engine_26.dispose()

app_26 = FastAPI(lifespan=lifespan)

# Назначение текущей сессии
async def get_current_session():
    current_session = AsyncSessionApp()
    try:
        yield current_session
    finally:
        await current_session.close()

@app_26.get('/recipes', response_model=List[schemas_hw_26.RecipesOut])
async  def all_recipes(current_session: AsyncSession = Depends(get_current_session)) -> Sequence[models_hw_26.Recipe]:
    """
    Выводит все рецепты пользователю
    """
    recipe = models_hw_26.Recipe
    res = await current_session.execute(select(recipe).order_by(desc(recipe.views), recipe.cooking_time))
    result = res.scalars().all()
    return result

@app_26.get('/recipe/{idx}', response_model=schemas_hw_26.OneRecipeOut)
async def one_recipe(idx: int, current_session: AsyncSession = Depends(get_current_session)) -> models_hw_26.Recipe:
    """
    Выводит рецепт по id
    """
    res = await current_session.execute(select(models_hw_26.Recipe).where(models_hw_26.Recipe.id == idx))

    response = res.scalars().one_or_none()
    if response is None:
        raise HTTPException(status_code=404, detail='Recipe not found')

    update_views = update(models_hw_26.Recipe).where(models_hw_26.Recipe.id == idx).values(
    views=models_hw_26.Recipe.views + 1)

    await current_session.execute(update_views)
    await current_session.commit()

    return response

@app_26.post('/recipes', response_model=schemas_hw_26.OneRecipeOut, status_code=201)
async def add_recipe(recipe: schemas_hw_26.RecipeIn, current_session: AsyncSession = Depends(get_current_session)) -> models_hw_26.Recipe:
    """
    Добавить рецепт
    """
    new_recipe = models_hw_26.Recipe(**dict(recipe))
    async with current_session.begin():
        current_session.add(new_recipe)
    return new_recipe
