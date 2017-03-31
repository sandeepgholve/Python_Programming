#!/usr/bin/python3

# Process all the 4 text files i.e. james.txt, juile.txt, mikey.txt, sarah.txt

def main():
    
    sarah = []
    
    try:
        sarah = get_coach_data('sarah.txt')
    
        print(sarah['Name'] + "'s fastest times are: " + sarah['Times'])
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
            data = file.readline()
            temp = (data.strip().split(','))
            return {'Name': temp.pop(0),
                    'DOB': temp.pop(0),
                    'Times': str(sorted(set([sanitize(t) for t in temp]))[0:3])
                }
    except IOError as error:
        print('File Error: ' + str(error))
        return(None)

if __name__ == '__main__' : main()
