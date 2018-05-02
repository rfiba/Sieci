import socket
import sys
import functions as f

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
            data = connection.recv(16)
            message = data.decode()
            print ("received ",  message)
            message = message.split(" ")
            #print(message["0"])
            d = f.numberToFunctionServer(message)
            print (d)
            if d is not None:
                data = d['task']
                print ("dafad")

            if data:
                print ('sending data back to the client')
                connection.sendall(data)
            else:
                print ('no more data from', client_address)
                break

    finally:
        connection.close()