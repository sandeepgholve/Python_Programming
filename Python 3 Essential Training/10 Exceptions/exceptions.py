#!/usr/bin/python3

def main():
    try:
        for line in readfile('aafile.txt1'): print(line.strip())
    except IOError as e:
        print('Cannot read file: ', e)
    except ValueError as ve:
        print('Value Error: ', str(ve))
    
def readfile(filename):
    if filename.endswith('.txt'):
        fh = open(filename)
        return fh.readlines()
    else: raise ValueError('Filename must end with .txt')
        

if __name__ == "__main__" : main()