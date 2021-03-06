import sqlite3
from createdb import addTask
from createdb import getNextTasks
from createdb import allTasks
from createdb import clearTasks
from createdb import removeTask
from createdb import getNextWeek
from createdb import removeOldTasks
from twilio.rest import Client


if __name__ == '__main__':
    account_file = open('account.txt', 'r')

    account_sid = account_file.readline()
    auth_token = account_file.readline()

    tasks = getNextTasks()
    task_string = "Tomorrow's task:\n"
    for i in range(len(tasks)):
        task_string += str(i+1) + '. ' + tasks[i][1] + ': ' + tasks[i][3] + '\n'

    task_string+= '\nOther Tasks This Week:\n'

    week_tasks = getNextWeek()
    for i in range(len(week_tasks)):
        task_string += str(i+1) + '. ' + week_tasks[i][1] + ' ' + str(week_tasks[i][2]) + '\n'


    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to=account_file.readline(),
        from_= account_file.readline(),
        body = task_string
    )

    removeOldTasks()