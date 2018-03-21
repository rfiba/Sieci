#!/usr/bin/python


import sys
import json
import socket

def checkAddress(address):
    if(address[len(address)-3] =='\\'):
        
    return

if(len(sys.argv) == 1):
    ip = socket.gethostbyaddr(socket.gethostname())
    ip = str(ip[2])
    ip = ip.strip('[]\'')
    print("Your ip adress:", ip)
    a = ip.split('.')
    print (a)
else:
    print( sys.argv[1])