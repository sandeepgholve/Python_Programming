#!/usr/bin/python3

def main():
    s = 'this is an string.'
    for i, c in enumerate(s):
        if c == 's': continue
        if c == 'a': break
        print(c, end='')

    print("\n-------------------------")

    for c in s:
        print(c, end='')
    else:
        print("*** this gets printed, when there is nothing to iterate in above for loop. ***")

    print("-------------------------")

    i = 0
    while (i < len(s)):
        print(s[i], end='')
        i+=1
    else:
        print("*** this gets printed, when above while condition fails. ***")
if __name__ == "__main__" : main()