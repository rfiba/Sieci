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

def close():
    exit(0)
    return

def numberToFunction(argument):
    switcher = {
        '1': showTaskList,
        '2': addTask,
        '3': removeTask,
        '4': showTaskWithPriority,
        '5': close
    }
    function = switcher.get(argument, lambda: "Invalid value")
    return function()


def showTaskListServer(message):
    with open("data.json", "r") as json_data:
        d = json.load(json_data)
        return d

def addTaskServer(message):
    with open("data.json", "r") as json_data:
         data = json.load(json_data)
    data['0'] += 1
    data[data['0']] = [message[1], message[2]]
    with open("data.json", 'w') as json_data:
        d = json.dump(data, json_data)
    return None


def removeTaskServer(message):
    with open("data.json", "r") as json_data:
        data = json.load(json_data)
    try:
        del(data[message[1]])
    except:
        return
    with open("data.json", 'w') as json_data:
        d = json.dump(data, json_data)
    return


def showTaskWithPriorityServer(message):
    tmp = {}
    with open("data.json", "r") as json_data:
         data = json.load(json_data)

    for i in data:
        if not isinstance(data.get(i), list):
            continue
        if data.get(i)[1] == message[1]:
            tmp[i] = data.get(i)
    return tmp


def numberToFunctionServer(message):
    switcher = {
        1 : showTaskListServer,
        2 : addTaskServer,
        3 : removeTaskServer,
        4 : showTaskWithPriorityServer
    }
    funct = switcher.get(message[0], lambda: "Invalid value")
    return switcher[int(message[0])](message)


