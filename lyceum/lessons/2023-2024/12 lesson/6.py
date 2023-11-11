import sqlite3


def get_result(name_file):
    con = sqlite3.connect(name_file)
    cur = con.cursor()
    r = cur.execute('''DELETE from films where genre IN
                 (SELECT id FROM genres WHERE title="боевик") and duration >= 90''').fetchall()

    con.commit()
    con.close()