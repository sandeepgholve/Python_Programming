#!/usr/bin/python3

def main():
    d = { "one": 1, "two": 2, "three": 3, "four": 4, "five": 5 } 
    print("Dictionaries: ", d)
    
    for k in d:
        print(k, d[k])

    print("Sorted by Keys: ")
    for k in sorted(d.keys()):
        print(k, d[k])

    print("Dictionaries are mutable objects")
    dd = dict(
            one = 1, two = 2, three = 3, four = 4, five = "five"
        )
    
    dd["seven"] = 7
    
    for kk in sorted(dd.keys()):
        print(type(kk), kk, type(dd), dd[kk])

if __name__ == "__main__" : main()