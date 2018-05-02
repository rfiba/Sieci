import socket
import sys
import functions as f



print ("1 - show task list\n2 - add task\n3 - remove task\n4 - show tasks with priority")
choice = input("Type number: ")
message = f.numberToFunction(choice)


sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('localhost', 10000)
print ('connecting to %s port %s' % server_address)
sock.connect(server_address)





try:
    #message = 'This is the message.  It will be repeated.'
    print ('sending %s' % message)
    sock.sendall(bytes(message, 'UTF-8'))


    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(4096)
        amount_received += len(data)
        print ("received", data.decode())

finally:
    print ('closing socket')
    sock.close()