#!/usr/bin/python3

def main():
    x = (1, 2, 3)
    print("Tuples are immutables: ", type(x), x)
    y = [1, 2, 3]
    y.append(5)
    y.insert(0, 7)
    y.insert(10, 17)
    print("Lists are mutables: ",type(y), y)

if __name__ == "__main__" : main()