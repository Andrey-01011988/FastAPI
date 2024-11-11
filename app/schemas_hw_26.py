from pydantic import BaseModel, ConfigDict


class BaseRecipe(BaseModel):
    title: str
    cooking_time: int


class RecipeIn(BaseRecipe):
    ingredients: str
    description: str


class RecipesOut(BaseRecipe):
    id: int
    views: int

    # Изменение устаревшего метода
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # class Config:
    #     from_attributes = True


class OneRecipeOut(BaseRecipe):
    id: int
    ingredients: str
    description: str

    # Изменение устаревшего метода
    model_config = ConfigDict(arbitrary_types_allowed=True)

    # class Config:
    #     from_attributes = True
