import sqlite3


def get_result(name):
    con = sqlite3.connect(name)

    cur = con.cursor()

    result = cur.execute(
        """DELETE from films where genre in (select id from genres where title='комедия')""").fetchall()

    con.commit()
    con.close()
