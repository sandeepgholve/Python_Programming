#!/usr/bin/python3

def main():
    # Reading file line by line
    fileHandle = open('file.txt')
    
    for line in fileHandle.readlines():
        print(line, end='')

    fh = open('file.txt')
    print('Enumerate example')        
    for index, line in enumerate(fh.readlines()):
        print(index, line, end='')
        
    s = 'this is an string.'
    for i, c in enumerate(s):
        if c == 's': print("{} is index of 's'".format(i))
        
if __name__ == "__main__" : main()