# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect(input())

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
result = cur.execute("""SELECT * FROM films""").fetchall()

# Вывод результатов на экран
for elem in result:
    if 'Астерикс' in elem[1] and 'Обеликс' not in elem[1]:
        print(elem[1])

con.close()