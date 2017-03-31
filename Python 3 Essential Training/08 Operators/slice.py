#!/usr/bin/python3

# Use of slices or part of the Container

list = []
list = [1,2,3,4,5,6,7,8,9,10]

print(list[0], list[9])

print("Give me 0 through 5 = ", list[0:5])
print("Ranges in python as non-inclusive = ")
for i in range(0,10): print(i, end=' ')

print("Short hand for ranges")

list1 = []
list1[:] = range(100)
for i in list1: print(i, end=' ')

print("\n")
print(list1[27])

for i in list1[27:42]: print(i, end=' ')
print("")

print("third argument in slice tell how many items to step over")
for i in list1[27:42:3]: print(i, end=' ')
print("")

print("third argument in slice can also be used to replace exisiting elements")
list1[27:43:3] = (99,99,99,99,99,99)
for i in list1 : print(i, end=' ')
print("")
