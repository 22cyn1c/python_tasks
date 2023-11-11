# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect(input())

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT * FROM films
                WHERE year <= 2000 and year >= 1995 and genre IN
                 (SELECT id FROM genres WHERE title='детектив')""").fetchall()

# Вывод результатов на экран  films_db.sqlite
for elem in result:
    print(elem[1])

con.close()