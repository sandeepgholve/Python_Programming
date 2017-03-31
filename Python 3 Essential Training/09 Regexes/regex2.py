#/usr/bin/python3

import re

# Search and Replace particular pattern using Regular Expression
def main():
    fh= open('sample.txt')
    for line in fh:
        print(re.sub('(provid|reduc)es', '#####' , line), end='')
            
if __name__ == "__main__" : main()