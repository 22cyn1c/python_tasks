import sqlite3


def get_result(name):
    con = sqlite3.connect(name)

    cur = con.cursor()

    result = cur.execute(
        """DELETE from films where title like 'Я%' and title like '%а'""").fetchall()

    con.commit()
    con.close()
