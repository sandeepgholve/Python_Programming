#!/usr/bin/python3


import pickle
from test.support import ioerror_peer_reset

class AthleteList(list):
    def __init__(self, a_name, a_dob=None, a_times=[]):
        list.__init__([])
        self.name = a_name
        self.dob = a_dob
        self.extend(a_times)
    
    def top3(self):
        return str(sorted(set([sanitize(t) for t in self]))[0:3])

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

def put_to_store(files_list):
    all_athletes = {}
    
    for each_file in files_list:
        ath = get_coach_data(each_file)
        all_athletes[ath.name] = ath
        
    try:
        with open('athlete.pickle', 'wb') as athf:
            pickle.dump(all_athletes, athf)
    except IOError as ioerr:
        print('File error (put_and_store):' + str(ioerr))
    
    return (all_athletes)

def get_from_store():
    all_athletes = {}
    
    try:
        with open('athletes.pickle', 'rb') as athf:
            all_athletes = pickle._load(athf)
    except IOError as ioerr:
        print('File error (get_from_store):' + str(ioerr))
        
    
    return (all_athletes)

