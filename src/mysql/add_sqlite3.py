import sqlite3

dbname = "TEST.db"
conn = sqlite3.connect(dbname)
cur = conn.cursor()

# "name"に"Taro"を入れる
cur.execute('INSERT INTO persons(name) values("Taro")')
# 同様に
cur.execute('INSERT INTO persons(name) values("Hanako")')
cur.execute('INSERT INTO persons(name) values("Hiroki")')

conn.commit()

cur.close()
conn.close()
