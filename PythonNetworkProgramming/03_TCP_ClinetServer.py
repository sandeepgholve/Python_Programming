#!/usr/bin/python3

# Simple TCP Client and Server that can send and receive 16 octets
# Documentation link: https://docs.python.org/3/library/socket.html

import socket, sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

HOST = sys.argv.pop() if len(sys.argv) == 3 else '127.0.0.1'
PORT = 1060

def recv_all(sock, length):
    data = b'' 
    while len(data) < length:
        more = sock.recv(length - len(data))
        if not more:
            raise EOFError('Socket closed {} bytes into a {}-byte message'.format(len(data), length))
        
        data += more
    return data;

if sys.argv[1:] == ['server']:
    s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    s.bind((HOST, PORT))
    s.listen(1)
    
    while True:
        print('Listening at {}'.format(s.getsockname()))
        sc, sockname = s.accept()
        print('We have accepted a connection from {}'.format(sockname))
        print('Socket connects {} and {}'.format(sc.getsockname(), sc.getpeername()))
        message = recv_all(sc, 16)
        print('The incoming sixteen-octet message says: {}'.format(repr(message)))
        sc.sendall(b'Farewell, Client')
        sc.close()
        print('Reply send, socket closed')
        
elif sys.argv[1:] == ['client']:
    s.connect((HOST, PORT))
    print('Client has been assigned socket name.', s.getsockname())
    s.sendall(b'Hi there, Server.')
    reply = recv_all(s, 16)
    print('The Server said: {}'.format(reply))
    s.close()
    
else:
    print('usage: 03_TCP_ClientServer.py server|client [host]', file=sys.stderr)
        
