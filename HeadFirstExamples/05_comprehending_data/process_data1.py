#!/usr/bin/python3

# Process all the 4 text files i.e. james.txt, juile.txt, mikey.txt, sarah.txt

james = []
juile= []
mikey = []
sarah = []

try:
    with open('james.txt') as jaf:
        data = jaf.readline()
    james = data.strip().split(',')

    with open('juile.txt') as jul:
        data = jul.readline()
    juile = data.strip().split(',')

    with open('mikey.txt') as mik:
        data = mik.readline()
    mikey = data.strip().split(',')

    with open('sarah.txt') as sar:
        data = sar.readline()
    sarah = data.strip().split(',')

    print(james)
    print(juile)
    print(mikey)
    print(sarah)

    print('--------------------------------------------------------------------------------------------------------------------')

    print(sorted(james))
    print(sorted(juile))
    print(sorted(mikey))
    print(sorted(sarah))
except IOError:
    print("Error")