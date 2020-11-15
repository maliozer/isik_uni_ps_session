#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: github.com/maliozer
@license: MIT
"""



import socket

hostname = socket.gethostname()
ip_address = socket.gethostbyname(hostname)

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = ('127.0.0.1', 10002)

print('connecting to %s port %s' % server_address)

sock.connect(server_address)
#%%

for x in range(3):
    message = 'connection done' + str(x) + 'th time from ' + str(ip_address) + '\n'
    byt = message.encode()
    sock.send(byt)