#!/usr/bin/python3


# Arbitrary arguments using *args

def main():
    testfunc(42, 16)
    testfunc(42)
    testfunc(1, 2, 3)
    testfunc(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    
def testfunc(first, second=22, third=33, *args):
    print('This is test function: ', first, second, third, args)

if __name__ == "__main__" : main()