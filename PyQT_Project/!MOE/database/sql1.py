import sqlite3
import os

a = open('sql.db', 'a', encoding="utf8")
a.close()

# Устанавливаем соединение с базой данных
connection = sqlite3.connect('sql.db')
cursor = connection.cursor()

# Выбираем всех пользователей
cursor.execute("""CREATE TABLE IF NOT EXISTS sqlsound(
   button TEXT,
   namefile TEXT,
   volume INTEGER);""")

connection.commit()
connection.close()

connection = sqlite3.connect('sql.db')
cursor = connection.cursor()

cursor.execute('INSERT INTO sqlsound (button) VALUES (?)', 'Q')
cursor.execute('INSERT INTO sqlsound (button) VALUES (?)', 'W')
cursor.execute('INSERT INTO sqlsound (button) VALUES (?)', 'E')
cursor.execute('INSERT INTO sqlsound (button) VALUES (?)', 'A')
cursor.execute('INSERT INTO sqlsound (button) VALUES (?)', 'S')
cursor.execute('INSERT INTO sqlsound (button) VALUES (?)', 'D')


connection.commit()
connection.close()

connection = sqlite3.connect('sql.db')
cursor = connection.cursor()

# Выбираем всех пользователей
cursor.execute('SELECT * FROM sqlsound')
users = cursor.fetchall()

# Выводим результаты
for user in users:
    print(user)

# Закрываем соединение
connection.close()