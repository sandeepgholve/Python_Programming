#/usr/bin/python3

import re

# Search and Replace particular pattern using Pre Compiled Regular Expression in 2 steps
def main():
    fh= open('sample.txt')
    pattern= re.compile('(provid|reduc)es', re.IGNORECASE)
    for line in fh:
        if re.search(pattern, line):
            print(pattern.sub('####', line), end='')
            
if __name__ == "__main__" : main()