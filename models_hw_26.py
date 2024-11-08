from sqlalchemy import Integer, String, Text
from sqlalchemy.orm import Mapped, mapped_column

from module_26_fastapi.homework.database_hw_26 import BaseHW


class Recipe(BaseHW):
    __tablename__ = 'recipes'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)  # Название рецепта
    cooking_time: Mapped[int] = mapped_column(Integer, nullable=False)  # Время приготовления
    ingredients: Mapped[str] = mapped_column(Text, nullable=False)  # Список ингредиентов
    description: Mapped[str] = mapped_column(Text, nullable=False)  # Текстовое описание
    views: Mapped[int] = mapped_column(Integer, default=0)  # Количество просмотров
