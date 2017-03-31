#!/usr/bin/python3

# Processing the sketch.txt file and separate the discussion to different
# collections

import os

man = []
other = []

try:
    data = open('sketch.txt')
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

    print(man)
    print('---------------------')
    print(other)
    data.close()

except IOError:
    print('The data file is missing.')
                
                
                