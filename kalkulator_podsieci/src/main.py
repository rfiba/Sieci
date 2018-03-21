#!/usr/bin/python


import sys
import json
import socket

if(len(sys.argv) == 1):
    ip = socket.gethostbyaddr(socket.gethostname())
print (ip[2])