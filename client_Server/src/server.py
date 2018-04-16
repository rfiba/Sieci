import socket
import sys

# Create a TCP/IP socket
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

        # Receive the data in small chunks and retransmit it
        while True:
            data = connection.recv(16)
            print ('received "%s"' % data)
            if data:
                print ('sending data back to the client')
                connection.sendall(data)
            else:
                print ('no more data from', client_address)
                break

    finally:
        # Clean up the connection
        connection.close()