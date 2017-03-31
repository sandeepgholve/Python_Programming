#!/usr/bin/python3

# Python Network Programming
# Gather Remote Machine Information

import socket

def print_remote_machine_info():
    remote_host = 'www.profitbricks.co.uk'
    try:
        print("IP Address of {}: {}".format(remote_host, socket.gethostbyname(remote_host)))
    except socket.error as err_msg:
        print("{}: {}".format(remote_host, err_msg))
    
if __name__ == '__main__' : print_remote_machine_info()