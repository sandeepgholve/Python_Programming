#/usr/bin/python3

import re

# Searching for particular pattern using Regular Expression
def main():
    fh= open('sample.txt')
    for line in fh:
        if re.search('(provid|reduc)es', line):
            print(line, end='')
            
if __name__ == "__main__" : main()