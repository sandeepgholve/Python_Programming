#!/usr/bin/python3

# Process all the 4 text files i.e. james.txt, juile.txt, mikey.txt, sarah.txt


def main():
    
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

        clean_james = [sanitize(each_t) for each_t in james]
        clean_juile = [sanitize(each_t) for each_t in juile]
        clean_mikey = [sanitize(each_t) for each_t in mikey]
        clean_sarah = [sanitize(each_t) for each_t in sarah]

        print('--------------------------------------------------------------------------------------------------------------------')
    
        print(sorted(clean_james))
        print(sorted(clean_juile))
        print(sorted(clean_mikey))
        print(sorted(clean_sarah))
    except IOError:
        print("Error")

def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter= ':'
    else:
        return time_string
    
    (mins, secs) = time_string.split(splitter)
    
    return (mins + '.' + secs)

if __name__ == '__main__' : main()