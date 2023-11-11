import sqlite3


def get_result(name_file):
    con = sqlite3.connect(name_file)
    cur = con.cursor()
    r = cur.execute('''UPDATE films set duration = duration * 2 where genre IN
                 (SELECT id FROM genres WHERE title="фантастика")''').fetchall()

    con.commit()
    con.close()