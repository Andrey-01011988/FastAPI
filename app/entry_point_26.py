import uvicorn

from app.main_hw_26 import app_26


@app_26.get("/")
async def hello():
    return "Welcome to the Cookbook"


# Запуск периодически барахлит и не обнаруживает модуль module_26_fastapi:
# (venv) uservm@uservm-VirtualBox:~/PycharmProjects/python_advanced/module_26_fastapi$ uvicorn homework.entry_point_26:app_26 --reload


if __name__ == "__main__":
    uvicorn.run(app_26, host="0.0.0.0", port=8000)
# Запускается либо из консоли либо, если раскомментировать, из файла
