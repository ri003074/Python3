import sqlite3


db_name = "database.db"
conn = sqlite3.connect(db_name)

cur = conn.cursor()
try:
    cur.execute(
        "CREATE TABLE persons(id INTEGER PRIMARY KEY AUTOINCREMENT, name STRING)"
    )
except sqlite3.OperationalError:
    pass


cur.execute('INSERT INTO persons(name) values("Goro")')
conn.commit()
conn.close()
