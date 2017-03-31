#!/usr/bin/python3


# Named parameters using **kwargs (key-word arguments)

def main():
    testfunc(one = 1, two = 2, three = 3)
    testfunc1(1, 2, 3, 4, 5, 6, one = 7, two = 8, three = 9)
    
def testfunc(**kwargs):
    print('This is test function: ', kwargs['one'], kwargs['two'], kwargs['three'])
    for k in kwargs:
        print(k , kwargs[k])

def testfunc1(first, second, third, *args, **kwargs):
    print(type(args))
    print(type(kwargs))
    print('This is test function: ', first, second, third, args, kwargs['one'], kwargs['two'], kwargs['three'])

if __name__ == "__main__" : main()