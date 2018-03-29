import socket as sock
import sys

s = sock.socket(sock.AF_INET, sock.SOCK_DGRAM)
s.bind(('', 1337))
while True:
    data, addr = s.recvfrom(1024)
    if addr[0] == sys.argv[1] and addr[1] == int(sys.argv[2]):
        print(data)
        if data == 'Hi, i am normal input!':
            s.sendto('Good job, normal input!\n', addr)
        elif data == 'This is evil input! >:)':
            s.sendto('Admin access granted', addr)
    else:
        print('Denied access from: {}'.format(addr))
        s.sendto('Unauthorized port or address!\n', addr)
