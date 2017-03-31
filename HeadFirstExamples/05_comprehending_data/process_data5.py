#!/usr/bin/python3

# Process all the 4 text files i.e. james.txt, juile.txt, mikey.txt, sarah.txt

def main():
    
    james = []
    juile= []
    mikey = []
    sarah = []
    
    try:
        james = get_coach_data('james.txt')
        juile = get_coach_data('juile.txt')
        mikey = get_coach_data('mikey.txt')
        sarah = get_coach_data('sarah.txt')
    
        print(james)
        print(juile)
        print(mikey)
        print(sarah)

        print('--------------------------------------------------------------------------------------------------------------------')
    
        print(sorted([sanitize(each_t) for each_t in james]))
        print(sorted([sanitize(each_t) for each_t in juile]))
        print(sorted([sanitize(each_t) for each_t in mikey]))
        print(sorted([sanitize(each_t) for each_t in sarah]))
    except IOError:
        print("Error")

# Sanitize the given string and replace ':' and '-' with '.'
def sanitize(time_string):
    if '-' in time_string:
        splitter = '-'
    elif ':' in time_string:
        splitter= ':'
    else:
        return time_string
    
    (mins, secs) = time_string.split(splitter)
    
    return (mins + '.' + secs)

# Read the file data and split it and return the array
def get_coach_data(file_name):
    try:
        with open(file_name) as file:
            data= file.readline()
            return(data.strip().split(','))
    except IOError as error:
        print('File Error: ' + str(error))
        return(None)

if __name__ == '__main__' : main()
