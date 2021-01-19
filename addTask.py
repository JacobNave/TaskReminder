import sqlite3
from createdb import addTask
from createdb import getNextTasks
from createdb import allTasks
from createdb import clearTasks
from createdb import removeTask
from createdb import  getNextWeek
from createdb import removeOldTasks

if __name__ == '__main__':
    user_in = ''

    while user_in != 'quit':
        user_in = input('Enter task or "quit" to quit: ')
        args = user_in.split(',')

        if user_in == 'quit':
            break
        elif len(args) < 2:
            print('Not enough arguments')
        elif len(args) == 2:
            addTask(args[0].strip(), args[1].strip())
        elif len(args) == 3:
            addTask(args[0].strip(), args[1].strip(), args[2].strip())
        else:
            print('Too many arguments')
