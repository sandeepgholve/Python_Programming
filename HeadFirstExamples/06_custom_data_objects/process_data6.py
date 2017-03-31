#!/usr/bin/python3

# Process all the 4 text files i.e. james.txt, juile.txt, mikey.txt, sarah.txt

def main():
    
    sarah = []
    
    try:
        sarah = get_coach_data('sarah.txt')
    
        print(sarah)

        print('--------------------------------------------------------------------------------------------------------------------')
    
        (sarah_name, sarah_dob) = sarah.pop(0), sarah.pop(0)
        print(sarah_name + "'s fastest times are: " + str(sorted(set([sanitize(t) for t in sarah]))[0:3]))
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
