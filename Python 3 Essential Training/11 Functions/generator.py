#!/usr/bin/python3 

def main():
    print('This is generator.py file')
    for i in inclusive_range(1, 20, 2):
        print(i, end = ' ')

def inclusive_range(start, stop, step):
    i = start
    while i <= stop:
        yield i
        i += step
        
if __name__ == '__main__' : main()