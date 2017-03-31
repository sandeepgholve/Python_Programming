#!/usr/bin/python3

# Fibonacci series example using class

class Fibonacci():
    def __init__(self, a, b):
        print("In Constructor: Type {1} and Id = {0}".format(id(self), type(self)))
        self.a = a;
        self.b = b;
        
    def series(self):
        while(True):
            yield self.b
            self.a, self.b = self.b, self.a + self.b

f = Fibonacci(0, 1)
print(id(f))

for n in f.series():
    if n > 100: break;
    print(n, end=' ')