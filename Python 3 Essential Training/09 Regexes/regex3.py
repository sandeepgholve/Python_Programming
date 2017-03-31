#/usr/bin/python3

import re

# Search and Replace particular pattern using Pre Compiled Regular Expression in 2 steps
def main():
    fh= open('sample.txt')
    for line in fh:
        match = re.search('(provid|reduc)es', line)
        if match:
            print(line.replace(match.group(), '####'), end='')
            
if __name__ == "__main__" : main()