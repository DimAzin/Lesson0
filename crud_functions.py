import sqlite3


# Функция для инициализации БД и создания таблицы
def initiate_db():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Создание таблицы Products
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Products (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            title TEXT NOT NULL,
            description TEXT,
            price INTEGER NOT NULL
        )
    ''')

    # Создание таблицы Users
    cursor.execute('''
            CREATE TABLE IF NOT EXISTS Users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                username TEXT NOT NULL,
                email TEXT NOT NULL,
                age INTEGER NOT NULL,
                balance INTEGER NOT NULL DEFAULT 1000
            )
        ''')

    conn.commit()
    conn.close()


# Функция для добавления продуктов (и для предзаполнения)
def add_product(title, description, price):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('''
        INSERT INTO Products (title, description, price)
        VALUES (?, ?, ?)
    ''', (title, description, price))

    conn.commit()
    conn.close()


# Функция для получения всех продуктов из базы данных
def get_all_products():
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Products')
    products = cursor.fetchall()

    conn.close()
    return products


# Функция для добавления пользователя
def add_user(username, email, age):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    # Добавление пользователя с балансом по умолчанию = 1000
    cursor.execute('''
        INSERT INTO Users (username, email, age, balance)
        VALUES (?, ?, ?, 1000)
    ''', (username, email, age))

    conn.commit()
    conn.close()


# Проверка, существует ли пользователь
def is_included(username):
    conn = sqlite3.connect('products.db')
    cursor = conn.cursor()

    cursor.execute('SELECT * FROM Users WHERE username = ?', (username,))
    user = cursor.fetchone()

    conn.close()

    # Если пользователь существует, возвращаем True
    return user is not None
