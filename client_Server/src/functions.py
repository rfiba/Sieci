#!usr/bin/python

def showTaskList():
    return "1"

def addTask():
    taskName = input("Task's name: ")
    taskPriority = input ("Task's priority: ")
    return "2 " + taskName  + " " + taskPriority

def removeTask():
    taskId = input("Type task's id: ")
    return "3 " + taskId

def showTaskWithPriority():
    priority = input("Type priority: ")
    return "4 " + priority

def numberToFunction(argument):
    switcher = {
        '1': showTaskList,
        '2': addTask,
        '3': removeTask,
        '4': showTaskWithPriority
    }
    function = switcher.get(argument, lambda: "Invalid value")
    print (function())
    return
