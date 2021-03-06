#!/usr/bin/python3

# Prime Number Generator

def isPrime(n):
    if n == 1:
        return False
    for x in range(2, n):
        if n % x == 0:
            return False
    else:
        return True
    
def primes(n = 1):
    while(True):
        if isPrime(n): yield n
        n += 1

for n in primes():
    if n > 100: break
    print(n)
