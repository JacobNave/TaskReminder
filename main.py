import sqlite3
from createdb import addTask
from createdb import getNextTasks
from createdb import allTasks
from createdb import clearTasks

if __name__ == '__main__':
    addTask('Quiz1', '1/20/2021', 'CS 121 Quiz 1')
    print(getNextTasks())
