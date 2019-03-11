#!/usr/bin/python

import sys
import socket, pickle

HOST = '127.0.0.1'
PORT = 50007
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
sum = (2+2)
data_string = pickle.dumps(sum)
s.send(data_string)

data = s.recv(4096)
data_sum = pickle.loads(data)
s.close()
print 'Received', repr(sum)
