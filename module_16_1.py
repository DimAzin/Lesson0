from fastapi import FastAPI

app = FastAPI()

# Главная страница "/"
@app.get("/")
async def main_page():
    return "Главная страница"

# Страница администратора "/user/admin"
@app.get("/user/admin")
async def admin_page():
    return "Вы вошли как администратор"

# Страница пользователей "/user/{user_id}"
@app.get("/user/{user_id}")
async def user_page(user_id: int):
    return f"Вы вошли как пользователь № {user_id}"

# Страница пользователя с параметрами в адресной строке "/user"
@app.get("/user")
async def user_info(username: str, age: int):
    return f"Информация о пользователе. Имя: {username}, Возраст: {age}"

