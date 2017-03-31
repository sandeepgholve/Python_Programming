#!/usr/bin/python3

# Prime Number using Function

def isPrime(n):
    if n == 1:
        print('1 is special number')
        return False
    for x in range(2, n):
        if n % x == 0:
            print('{} is multiple of {} x {}'.format(n, x, n // x))
            return False
        
    print('{} is prime number'.format(n))


for n in range(1, 20):
    isPrime(n)
            