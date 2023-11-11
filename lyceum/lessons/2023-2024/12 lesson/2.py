import sqlite3


def get_result(name_file):
    con = sqlite3.connect(name_file)
    cur = con.cursor()
    r = cur.execute('''UPDATE films set duration="42" where duration=""''').fetchall()
    con.commit()
    con.close()
