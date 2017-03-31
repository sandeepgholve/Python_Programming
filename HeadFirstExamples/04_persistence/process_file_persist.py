#!/usr/bin/python3

# Processing the sketch.txt file and separate the discussion to different
# collections

import os

man = []
other = []

try:
    data = open('sketch1.txt')
    for each_line in data:
        try:
            (role, line_spoken) = each_line.split(':', 1)
            line_spoken = line_spoken.strip()
            
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass

except IOError as error:
    print('The data file is missing: ' + str(error))
finally:
    # Check whether data object is valid and not null.
    if 'data' in locals():
        data.close()

'''
try:
    man_file = open('man_data.txt', 'w')
    other_file = open('other_data.txt', 'w')
    
    print(man, file=man_file)
    print(other, file=other_file)
except IOError:
    print('File Error')                
finally:
    man_file.close()
    other_file.close()                
'''
        