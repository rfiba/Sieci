#!/usr/bin/python

def calculateRangeOfAdresses(address):
    broadcastAddress = calculateBroadcastAddress(address)
    networkAddress = calculateNetworkAddress(address)

    i = 3
    while i:
        if (broadcastAddress[i] -1 >= 0):
            broadcastAddress[i] -= 1
            break;
        i -= 1

    i = 3
    while i:
        if (networkAddress[i] + 1 <= 255):
            networkAddress[i] += 1
            break;

    result = []
    result.append(broadcastAddress)
    result.append(networkAddress)

    return result;

def inverse(x):
    return ~x & 0xff;

def calculateNetworkAddress(address):
    result = calculateMask(address)
    for i in range(len(result)):
        result[i] &= address[i]
    return result;

def calculateBroadcastAddress(address):
    result = calculateMask(address)

    for i in range(len(result)):
        result[i] = inverse(result[i])

    for i in range(len(result)):
        result[i] |= address[i]

    return result;

def calculateMaxNumberOfHost(address):
    return 2 ** (32 - address[4]) - 2;

def calculateMask(address):
    eights = int(address[4]/8)

    result = []
    for i in range(eights):
        result.append(255)

    tmp = (address[4] % 8)

    result.append(1)
    for i in range(7):
        result[eights] = result[eights] << 1
        if(i < tmp-1):
            result[eights] += 1

    for i in range(4-len(result)):
        result.append(0)
    return result;

def checkClass(address):
    if(len(address)):
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
            return False;

    if (length == 5 ):
        if(address[4] > 32 or address[4] < 0):
            return False;

    return True;