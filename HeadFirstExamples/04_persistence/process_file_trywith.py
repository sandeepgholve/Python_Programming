#!/usr/bin/python3

# Processing the sketch.txt file and separate the discussion to different
# collections

# The with statement takes advantage of a Python technology called 
# context management protocol.


import os

man = []
other = []

try:
    # The use of 'with' negates the need for the 'finally' switch.
    with open('sketch.txt') as data:
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

except IOError:
    print('The data file is missing.')
