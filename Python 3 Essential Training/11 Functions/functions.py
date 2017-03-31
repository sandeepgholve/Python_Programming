#!/usr/bin/python3

def main():
    testfunc(42, 16)
    testfunc(42)
    testfunc(1, 2, 3)
    
def testfunc(first, second = None, third = 55):
    print('This is test function: ', first, second, third)

if __name__ == "__main__" : main()