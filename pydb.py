import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

cur = conn.cursor()

usrname = "light"

cur.execute("SELECT * from events")

row = cur.fetchall()

print(row)