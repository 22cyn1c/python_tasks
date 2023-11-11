# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect(input())

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT * FROM films
            WHERE year >= 1997 and genre IN
             (SELECT id FROM genres WHERE title='анимация' or title='музыка')""").fetchall()

# Вывод результатов на экран
for elem in result:
    print(elem[1])

con.close()