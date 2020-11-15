#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: github.com/maliozer
@license: MIT
"""


import socket

#create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

#bind the socket to the port 10000
server_address = ('localhost', 10002)

print('starting up on %s port %s' % server_address)
sock.bind(server_address)
#sock.close() to stop

sock.listen(1)

#%%
while True:
    conn, addr = sock.accept()
    data = conn.recv(2000)
    print(data.decode())
    
    if(data.decode() == 'exit -n'):
        break
