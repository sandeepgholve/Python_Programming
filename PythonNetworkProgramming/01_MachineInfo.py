#!/usr/bin/python3

# Python Network Programming
# Gather Machine Information

import socket

def print_machine_info():
    host_name = socket.gethostname()
    ip_address = socket.gethostbyname(host_name)
    
    print("Host Name: {}".format(host_name))
    print("IP Address: {}".format(ip_address))
    
if __name__ == '__main__' : print_machine_info()