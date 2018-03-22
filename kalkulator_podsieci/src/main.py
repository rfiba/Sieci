#!/usr/bin/python


import sys
import json
import socket
import re

def checkAddress(address):
    length = len(address)
    if(length != 4 | length != 5):
        return False;

    for i in range(length):
        if (address[i].isdigit() == False):
            return False;

    for i in range(length):
        address[i] = int(address[i])

    for i in range(length):
        if(address[i] > 255 or address[i] < 0):
            print (address[i])
            return False;

    if (length == 5 ):
        if(address[4] > 32 or address[4] < 0):
            return False;

    return True;

if(len(sys.argv) == 1):
    ip = socket.gethostbyaddr(socket.gethostname())
    ip = str(ip[2])
    ip = ip.strip('[]\'')
    ip += '\\32'
    print("Your ip adress:", ip)
    a = ip.split(r'.')
    print (a)
    #for i in range(a):
    b = str(a[3]).split('\\')

    del a[-1]
    print (a+b)
    print(checkAddress(a+b))
else:
    print( sys.argv[1])