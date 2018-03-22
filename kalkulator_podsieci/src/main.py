#!/usr/bin/python


import sys
import json
import socket

def calculateMaxNumberOfHost(address):
    bits = 32 - address
    return 2 ** (32 - address) - 2

def calcMask(address):
    print(0b1 + 0b1)

def checkClass(address):
    if(len(address) == 4):
        tmp = address[0]

        tmp = tmp >> 4

        if (tmp == 0b1111): # zapytać czemu tmp & 0b1111 nie działa
            return 'E'
        if (tmp == 0b1110):
            return 'D'
        tmp >> 1
        if (tmp == 0b110):
            return 'C'
        tmp >> 1
        if (tmp == 0b10):
            return 'B'
        return 'A'
    return

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
    print("Err: Wrong address")
    exit(1);


if (console):
    b = str(a[3]).split('\\')
    del a[-1]
    ip = a+b
    if(not checkAddress(ip)):
        print("Err: Wrong address")
        exit(1)
    print(calculateMaxNumberOfHost(ip[4]))

print(checkAddress(a))
print(checkClass(a))






