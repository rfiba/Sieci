import socket
import sys
import functions as f
import json

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server_address = ('localhost', 10000)
print ('starting up on %s port %s' % server_address)
sock.bind(server_address)

sock.listen(1)

while True:
    print ('waiting for a connection')
    connection, client_address = sock.accept()
    try:
        print('connection from', client_address)

        while True:
            data = connection.recv(4096)
            message = data.decode()

            if message == '':
                break

            print ("received ",  message)
            message = message.split(" ")
            d = f.numberToFunctionServer(message)

            data = json.dumps(d)
            if data:
                print ('sending data back to the client')
                connection.sendall(bytes(data, 'UTF-8'))
            else:
                print ('no more data from', client_address)
                break

    finally:
        connection.close()