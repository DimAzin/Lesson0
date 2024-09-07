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
