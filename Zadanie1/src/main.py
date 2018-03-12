#!/usr/bin/python
#bubblesort, data import from file

import sys
import json

print ('File name:', str(sys.argv[1]))
file = open(str(sys.argv[1]))
with open(str(sys.argv[1])) as json_data:
    d = json.load(json_data)
for element in d['input_list']:
    print (element)
print ("Number of array's elements: ", len(d['input_list']))
def sort(tab):
    swap = 1
    pom = len(tab)
    while pom >0:
        if(swap == 0):
            break;
        swap = 0
        for i in range (1, len(tab)):
            if(tab[i-1] > tab[i]):
                tmp = tab[i]

                tab[i] = tab[i-1]
                tab[i-1] = tmp
                swap = 1

        pom = pom - 1
    return;
print ("Sorted array: ")
sort(d['input_list'])
for it in d['input_list']:
    print(it)