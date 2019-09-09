#!/usr/bin/env python
import socket
import subprocess
import sys
from datetime import datetime

# input
remoteServer = raw_input("Hostname or IP: ")
remoteServerIP = socket.gethostbyname(remoteServer)

# scans ports in range, prints the open port numbers

try:
    for port in range(1,1025):
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        result = sock.connect_ex((remoteServerIP, port))
        if result == 0:
            print "Port: {}:     Open".format(port)
        sock.close()

# exits if error occurs
except socket.error:
    print "Connection failed"
    sys.exit()
