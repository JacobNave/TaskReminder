import sqlite3
import datetime

def addTask(task_name, task_date, task_description = None):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    try:
        cursor.execute('INSERT INTO Tasks ("TaskName", "TaskDate", "TaskDesc") values (?, ?, ?)', (task_name, datetime.datetime.strptime(task_date, '%m/%d/%Y').date(), task_description))
        conn.commit()
        print("Task '{}' was added!".format(task_name))
    except:
        print("Date '{}' is not a valid date. Please enter in the format day/month/year".format(task_date))

    conn.close()

#Returns tasks with tomorrow's date
def getNextTasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    tasks = cursor.execute('SELECT * FROM Tasks WHERE TaskDate = ?', (tomorrow,)).fetchall()
    return tasks

def getNextWeek():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    tomorrow = datetime.date.today() + datetime.timedelta(days=1)
    weekend = datetime.date.today() + datetime.timedelta(days=7)
    tasks = cursor.execute('SELECT * FROM Tasks WHERE TaskDate > ? AND TaskDate <= ?', (tomorrow, weekend)).fetchall()
    return tasks

def removeTask(id):
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Tasks WHERE TaskID = ?', (id,))
    conn.commit()

def allTasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    tasks = cursor.execute('SELECT * FROM Tasks').fetchall()
    return tasks

def clearTasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    cursor.execute('DELETE FROM Tasks')
    conn.commit()

def removeOldTasks():
    conn = sqlite3.connect('tasks.db')
    cursor = conn.cursor()

    today = datetime.date.today()
    cursor.execute('DELETE FROM Tasks WHERE TaskDate < ?', (today,))
    conn.commit()

#PLACEHOLDER CHANGE LATER
def checkDate():
    return True


if __name__ == '__main__':
    conn = sqlite3.connect('tasks.db')

    cursor = conn.cursor()

    #cursor.execute('DROP TABLE Tasks')

    cursor.execute('''CREATE TABLE Tasks (
TaskID INTEGER ,
TaskName VARCHAR(255) NOT NULL,
TaskDate DATE NOT NULL,
TaskDesc VARCHAR(255),
PRIMARY KEY (TaskID)
)''')

    conn.commit()
    conn.close()