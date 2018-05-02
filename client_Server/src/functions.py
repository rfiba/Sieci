#!usr/bin/python
import json


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
    return function()


def showTaskListServer(message):
    tmpDictionary = {}
    with open("data.json", "r") as json_data:
        d = json.load(json_data)
        print()
        for i in d:
            print(d[i])
        return #d

def addTaskServer(message):
    with open("data.json", "r") as json_data:
         data = json.load(json_data)
    print(data['0'])
    data['0'] = data['0'] + 1
    print(data['0'])
    data[data['0']] = { "name":message[1], "prirority":message[2]}
    with open("data.json", 'w') as json_data:
        d = json.dump(data, json_data)
    return {}


def removeTaskServer(message):
    with open("data.json", "r") as json_data:
         data = json.load(json_data)
    print (data.keys())
    return {}


def showTaskWithPriorityServer(message):
    return {}


def numberToFunctionServer(message):
    switcher = {
        1 : showTaskListServer,
        2 : addTaskServer,
        3 : removeTaskServer,
        4 : showTaskWithPriorityServer
    }
    funct = switcher.get(message[0], lambda: "Invalid value")
    switcher[int(message[0])](message)
    #funct(message)

    return
