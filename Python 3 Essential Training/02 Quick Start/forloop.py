#!/usr/bin/python3

# Reading file using for loop

fileHandle = open('file.txt')
print(dir(fileHandle))
for line in fileHandle.readlines():
    print(line, end='')
