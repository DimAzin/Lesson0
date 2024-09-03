import sqlite3

conn = sqlite3.connect('not_telegram.db')
cursor = conn.cursor()

# Очищаем таблицу Users
cursor.execute('DELETE FROM Users')

cursor.execute('''
CREATE TABLE IF NOT EXISTS Users (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    username TEXT NOT NULL,
    email TEXT NOT NULL,
    age INTEGER,
    balance INTEGER NOT NULL
)
''')

users = [
    ('User1', 'example1@gmail.com', 10, 1000),
    ('User2', 'example2@gmail.com', 20, 1000),
    ('User3', 'example3@gmail.com', 30, 1000),
    ('User4', 'example4@gmail.com', 40, 1000),
    ('User5', 'example5@gmail.com', 50, 1000),
    ('User6', 'example6@gmail.com', 60, 1000),
    ('User7', 'example7@gmail.com', 70, 1000),
    ('User8', 'example8@gmail.com', 80, 1000),
    ('User9', 'example9@gmail.com', 90, 1000),
    ('User10', 'example10@gmail.com', 100, 1000),
]

cursor.executemany('''
INSERT INTO Users (username, email, age, balance)
VALUES (?, ?, ?, ?)
''', users)

# Обновляем balance
cursor.execute('''
UPDATE Users
SET balance = 500
WHERE id % 2 = 1
''')

# Удаляем 3-ю запись
cursor.execute('''
DELETE FROM Users
WHERE id IN (
    SELECT id FROM Users WHERE (id + 1) % 3 = 0
)
''')

# Выбираем - возраст не равен 60
cursor.execute('''
SELECT username, email, age, balance FROM Users WHERE age != 60
''')
rows = cursor.fetchall()

for row in rows:
    print(f"Имя: {row[0]} | Почта: {row[1]} | Возраст: {row[2]} | Баланс: {row[3]}")

cursor.execute('DELETE FROM Users WHERE id = 6')

cursor.execute('SELECT COUNT(*) FROM Users')
total_users = cursor.fetchone()[0]
print(f'Всего пользователей: {total_users}')

cursor.execute('SELECT SUM(balance) FROM Users')
total_balance = cursor.fetchone()[0]
print(f'Общий баланс: {total_balance}')

if total_users > 0:
    average_balance = total_balance / total_users
else:
    average_balance = 0

print(f"Средний баланс всех пользователей: {average_balance:.2f} ккал")

conn.commit()
conn.close()