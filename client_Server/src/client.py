import socket
import sys
import json
import functions as f
import ast

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print('connecting to %s port %s' % server_address)
sock.connect(server_address)

while 1:
    print ("1 - show task list\n2 - add task\n3 - remove task\n4 - show tasks with priority\n5 - exit")
    choice = input("Type number: ")
    message = f.numberToFunction(choice)
    if message == "Invalid value":
        exit(1)
        
    try:
        sock.sendall(bytes(message, 'UTF-8'))
        data = sock.recv(4096)
        data = data.decode()
        data = json.loads(data)

        if data:
            for i in data:
                if not isinstance(data.get(i), list):
                    continue
                print ("ID: " + i + " Name: " + data.get(i)[0] + " Priority: " + data.get(i)[1])
    except:
        continue
print ('closing socket')
sock.close()