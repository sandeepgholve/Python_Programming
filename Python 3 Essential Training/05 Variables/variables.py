#!/usr/bin/python3

def main():
    num = 42 / 9
    print("Division: ", type(num), num)
    num = 42 // 9
    print("Integer Division: ", type(num), num)
    num = round(42 / 9)
    print("Rounding Division: ", type(num), num)
    num = round(42 / 9, 2)
    print("Rounding Division with 2 digits: ", type(num), num)
if __name__ == "__main__" : main()