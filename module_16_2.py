from fastapi import FastAPI, Path
from typing import Annotated

app = FastAPI()

# Главная страница "/"
@app.get("/")
async def main_page():
    return "Главная страница"

# Страница администратора "/user/admin"
@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

# Страница пользователей "/user/{user_id}" с валидацией
@app.get("/user/{user_id}")
async def user_page(
    user_id: Annotated[int, Path(
        title="Enter User ID",
        ge=1,  # Минимум 1
        le=100,  # Максимум 100
        example=1  # Пример
    )]
):
    return f"Вы вошли как пользователь № {user_id}"

# Страница пользователя с параметрами "/user/{username}/{age}" с валидацией
@app.get("/user/{username}/{age}")
async def user_info(
    username: Annotated[str, Path(
        title="Enter username",
        min_length=5,  # Минимум 5 символов
        max_length=20,  # Максимум 20 символов
        example="UrbanUser"  # Пример
    )],
    age: Annotated[int, Path(
        title="Enter age",
        ge=18,  # Минимум 18 лет
        le=120,  # Максимум 120 лет
        example=24  # Пример
    )]
):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"


