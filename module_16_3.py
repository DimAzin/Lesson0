from fastapi import FastAPI, HTTPException

app = FastAPI()

# Тестовый словарь базы данных
users = {'1': 'Имя: Example, возраст: 18'}


@app.get("/users")
async def get_users():
    return users


@app.post("/user/{username}/{age}")
async def create_user(username: str, age: int):
    if age < 0:
        raise HTTPException(status_code=400, detail="Age must be a positive number.")

    max_id = max([int(user_id) for user_id in users.keys()])
    new_id = str(max_id + 1)
    users[new_id] = f"Имя: {username}, возраст: {age}"

    return f"User {new_id} is registered"


@app.put("/user/{user_id}/{username}/{age}")
async def update_user(user_id: str, username: str, age: int):
    if age < 0:
        raise HTTPException(status_code=400, detail="Age must be a positive number.")

    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found.")

    users[user_id] = f"Имя: {username}, возраст: {age}"
    return f"The user {user_id} has been updated"


@app.delete("/user/{user_id}")
async def delete_user(user_id: str):
    if user_id not in users:
        raise HTTPException(status_code=404, detail="User not found.")

    del users[user_id]
    return f"User {user_id} has been deleted"
