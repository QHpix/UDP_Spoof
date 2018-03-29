from scapy.all import *
from time import sleep
import sys
import socket as sock


s = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
s.bind(('', 4444))

i = 0

while True:
    s.sendto('Hi, i am normal input!', (sys.argv[1], int(sys.argv[2])))
    msg, addr = s.recvfrom(1024)
    print(msg)
    sleep(2)
