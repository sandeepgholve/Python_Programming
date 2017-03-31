#!/usr/bin/python3

def main():
    x = 42
    y = 42
    
    print(id(x), x)
    print(id(y), y)
    
    print("'is' operator checks for identity equality: ", x is y)
    
    d1 = dict(x = 42)
    d2 = dict(x = 42)
    print("---------------")
    print(d1)
    print(d2)
    print(id(d1), id(d2))
    print(' test identity equality: ', d1 is d2)
    print(' test equality: ', d1 == d2)

if __name__ == "__main__" : main()