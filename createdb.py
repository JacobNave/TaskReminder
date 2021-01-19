import sqlite3

conn = sqlite3.connect('tasks.db')

cursor = conn.cursor()

cursor.execute('''CREATE TABLE Tasks (
TaskID int NOT NULL PRIMARY KEY,
TaskName varchar(MAX) NOT NULL,
TaskDate date NOT NULL,
TaskDesc varchar(MAX)
)''')

conn.commit()
conn.close()