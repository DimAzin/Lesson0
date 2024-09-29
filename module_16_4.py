from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Пустой список
users = []


class User(BaseModel):
    id: int
    username: str
    age: int


@app.get("/users", response_model=List[User])
async def get_users():
    return users


@app.post("/user/{username}/{age}", response_model=User)
async def create_user(username: str, age: int):
    if age < 0:
        raise HTTPException(status_code=400, detail="Age must be a positive number.")

    # Новый пользователь
    user_id = users[-1].id + 1 if users else 1
    new_user = User(id=user_id, username=username, age=age)
    users.append(new_user)
    return new_user


@app.put("/user/{user_id}/{username}/{age}", response_model=User)
async def update_user(user_id: int, username: str, age: int):
    if age < 0:
        raise HTTPException(status_code=400, detail="Age must be a positive number.")

    for user in users:
        if user.id == user_id:
            user.username = username
            user.age = age
            return user

    # Пользователь не найден
    raise HTTPException(status_code=404, detail="User was not found")


@app.delete("/user/{user_id}", response_model=User)
async def delete_user(user_id: int):
    for index, user in enumerate(users):
        if user.id == user_id:
            deleted_user = users.pop(index)
            return deleted_user

    # Пользователь не найден
    raise HTTPException(status_code=404, detail="User was not found")
