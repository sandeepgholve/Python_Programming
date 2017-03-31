#!/usr/bin/python3

# Reading file using for loop

try:
    fileHandle = open('xfile.txt')
    for line in fileHandle.readlines():
        print(line, end='')
except IOError as e:
    print('Error: ({})'.format(e))
else:
    print("This is during except")