# Импорт библиотеки
import sqlite3

# Подключение к БД
con = sqlite3.connect('music_db.sqlite')

# Создание курсора
cur = con.cursor()

# Выполнение запроса и получение всех результатов
name = input()
txt = f"""SELECT distinct t.name from artist ar
join album ab on ab.artistid = ar.artistid
join track t on t.albumid = ab.albumid
where ar.name = '{name}'
order by t.name"""
r = cur.execute(txt).fetchall()

# Вывод результатов на экран  films_db.sqlite
for elem in r:
    print(elem[0])

con.close()