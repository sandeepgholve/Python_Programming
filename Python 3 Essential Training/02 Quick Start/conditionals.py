#!/usr/bin/python3

# Single line comment

'''
Multipline comment.
'''

a, b = 1, 2

if a < b:
    print('({}) is less than ({})'.format(a, b))
else:
    print('({}) is greater than ({})'.format(a, b))
    
print('foo' if a < b else 'bar')