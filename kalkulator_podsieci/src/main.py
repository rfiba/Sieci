#!/usr/bin/python


import sys
import json
import socket



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

console = False

if(len(sys.argv) == 1):
    ip = socket.gethostbyaddr(socket.gethostname())
    ip = ip[2][0]
else:
    ip = sys.argv[1]
    console = True

a = ip.split(r'.')
if (len(a) != 4):
    print ("Err")
    exit(1);


if (console):
    b = str(a[3]).split('\\')
    del a[-1]
    print(checkAddress(a+b))
