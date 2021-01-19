import sqlite3
from createdb import addTask
from createdb import getNextTasks
from createdb import allTasks
from createdb import clearTasks
from createdb import removeTask
from twilio.rest import Client


if __name__ == '__main__':
    accout_file = open('account.txt', 'r')

    account_sid = accout_file.readline()
    auth_token = accout_file.readline()

    tasks = getNextTasks()
    task_string = 'Tomorrows task:\n'
    for i in range(len(tasks)):
        task_string += str(i+1) + '. ' + tasks[i][1] + ': ' + tasks[i][3] + '\n'

    client = Client(account_sid, auth_token)

    message = client.messages.create(
        to="+12106189141",
        from_= "+16467989659",
        body = task_string
    )

    #addTask('Homework 1', '1/20/2021', 'CS 141 Homework')
    #print(getNextTasks())
