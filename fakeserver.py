"""
Fake Server

choose your interface to listen on.
the script will then respond to any syn packets sent to the server ports with
a syn ack.
it will do this as long as the script is running.
It never forms a 3 way handshake or establishes a proper connection!


Note:
    the iptables rules stop the OS from sending a RST out
"""


import os
import sys
import random


from scapy.all import *


SERVERPORTS = [80, 22, 443, 5900]


os.system("iptables -A OUTPUT -p tcp --tcp-flags RST RST -j DROP")


def fakeserver(p):
    """
    send back a syn ack to the sender

    Args:
        p(scapy packet): the packet to respond to
    """
    spoofresponse = IP(dst=p[IP].src, ttl=64)/TCP(dport=p[TCP].sport,
    sport=p[TCP].dport, flags='SA', seq=random.randint(0,4294967295),
    ack=p[TCP].seq + 1)
    if p.haslayer(TCP) and p[TCP].flags == 2 and p[TCP].dport in SERVERPORTS:
        print('scan on port ' + str(p[TCP].dport) + ' from ' + str(p[IP].src))
        send(spoofresponse, verbose=0)


try:
    INTERFACE = input('please enter the interface to listen on: ')
    print('listening for connections to ports {} on interface {}'.format(
        SERVERPORTS, INTERFACE))
    sniff(filter='tcp', iface=INTERFACE, store=0, prn=fakeserver)
except (KeyboardInterrupt, SystemExit):
    print('quitting')
    os.system("iptables -D OUTPUT -p tcp --tcp-flags RST RST -j DROP")
    sys.exit()
