from fastapi import FastAPI, Request, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Пустой список пользователей
users = []

# Шаблоны Jinja2
templates = Jinja2Templates(directory="templates")


# Модель пользователя
class User(BaseModel):
    id: int
    username: str
    age: int


# POST запрос для создания пользователя
@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int):
    if age < 0:
        raise HTTPException(status_code=400, detail="Age must be a positive number.")

    user_id = users[-1].id + 1 if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


# GET запрос для отображения всех пользователей через шаблон
@app.get("/", response_class=HTMLResponse)
async def get_user_list(request: Request):
    # Рендеринг списка всех пользователей
    return templates.TemplateResponse("users.html", {"request": request, "users": users})


# GET запрос для получения информации о конкретном пользователе
@app.get("/users/{user_id}", response_class=HTMLResponse)
async def get_user_detail(request: Request, user_id: int):
    # Поиск пользователя по ID
    user = next((user for user in users if user.id == user_id), None)
    if user is None:
        raise HTTPException(status_code=404, detail="User was not found")

    # Рендеринг информации о пользователе
    return templates.TemplateResponse("users.html", {"request": request, "user": user, "users": users})
