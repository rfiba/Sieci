#!/usr/bin/python


import sys
sys.path.append('~/PycharmProjects/Sieci/kalkulator_podsieci/src')
import json
import socket
import functions

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
    b = str(a[3]).split('/')
    del a[-1]
    ip = a+b
    if(not functions.checkAddress(ip)):
        print("Err: Wrong address")
        exit(1)
    print(functions.calculateMask(ip))
    print(functions.calculateBroadcastAddress(ip))
    print(functions.calculateNetworkAddress(ip))
    print(functions.calculateRangeOfAdresses(ip))
    print(functions.calculateMaxNumberOfHost(ip))



