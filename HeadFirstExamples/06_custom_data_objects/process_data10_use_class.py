#!/usr/bin/python3


class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    
    def top3(self):
        return str(sorted(set([sanitize(t) for t in self]))[0:3])
    
# Process all the 4 text files i.e. james.txt, juile.txt, mikey.txt, sarah.txt
def main():
    
    sarah = []
    
    try:
        sarah = get_coach_data('sarah.txt')
        print(sarah.name + "'s fastest times are: " + sarah.top3())
        sarah.append('1.1')
        print(sarah.name + "'s fastest times are: " + sarah.top3())
        sarah.extend(['1.7', '3.1'])
        print(sarah.name + "'s fastest times are: " + sarah.top3())
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
            return AthleteList(temp.pop(0), temp.pop(0), temp)
    except IOError as error:
        print('File Error: ' + str(error))
        return(None)

if __name__ == '__main__' : main()
