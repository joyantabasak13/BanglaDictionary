import sqlite3
import os

resPath = os.path.dirname(os.path.dirname(__file__))
srcFile = os.path.join(os.path.normpath(resPath),'res','database','dictionary.sqlite')
try:
    sqlite_conn = sqlite3.connect(srcFile)
except sqlite3.Error as e:
    print ('conntect sqlite database failed.')
cur = sqlite_conn.cursor()

cur.execute("SELECT name FROM sqlite_master WHERE type='table'")
print(cur.fetchall())
cur.execute("SELECT sql FROM sqlite_master WHERE type='table' AND name='bn_to_bn'")
print(cur.fetchone()[0])
cur.execute("SELECT * FROM 'bn_to_bn' WHERE `word_id`<10")
rows= cur.fetchall()
for row in rows:
    for col in row:
        print(col)