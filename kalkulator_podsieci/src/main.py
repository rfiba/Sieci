#!/usr/bin/python


import sys
import json
import socket
import functions as f

console = False

if (len(sys.argv) == 1):
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

    if(not f.checkAddress(ip)):
        print("Err: Wrong address")
        exit(1)

    classOfAddress = f.checkClass(ip)
    broadcastAddress = f.calculateBroadcastAddress(ip)
    rangeOfAddress = f.calculateRangeOfAdresses(ip)
    numberOfHost = f.calculateMaxNumberOfHost(ip)
    mask = f.calculateMask(ip)
    networkAddress = f.calculateNetworkAddress(ip)

    print ('Network address: {d[0]}.{d[1]}.{d[2]}.{d[3]}'.format(d = networkAddress))
    print ('Network class: ', classOfAddress)
    print('Mask: {d[0]}.{d[1]}.{d[2]}.{d[3]}'.format(d=mask))
    print('Mask: {d[0]:0>8b}.{d[1]:0>8b}.{d[2]:0>8b}.{d[3]:0>8b}'.format(d=mask))
    print ('Broadcast address: {d[0]}.{d[1]}.{d[2]}.{d[3]}'.format(d=broadcastAddress))
    print ('Broadcast address: {d[0]:0>8b}.{d[1]:0>8b}.{d[2]:0>8b}.{d[3]:0>8b}'.format(d=broadcastAddress))
    print ('Hosts: ', numberOfHost)
    print ('Hosts: {0:b}'.format(numberOfHost))
    print ('Range: {d[1][0]}.{d[1][1]}.{d[1][2]}.{d[1][3]} - {d[0][0]}.{d[0][1]}.{d[0][2]}.{d[0][3]}'.format(d = rangeOfAddress))
    print ('Range: {d[1][0]:0>8b}.{d[1][1]:0>8b}.{d[1][2]:0>8b}.{d[1][3]:0>8b} - {d[0][0]:0>8b}.{d[0][1]:0>8b}.{d[0][2]:0>8b}.{d[0][3]:0>8b}'.format(d=rangeOfAddress))

    with open("data.json", 'w') as json_data:
        json.dump({"numberOfHost":numberOfHost, "rangeOfAddress":rangeOfAddress,"broadcastAddress":broadcastAddress, "mask":mask, "networkAddress": networkAddress}, json_data)
else:
    ip = a
    print (ip)
    for i in range (0,4):
        ip[i] = int(ip[i])
    classOfAddress = f.checkClass(ip)
    print (classOfAddress)


