"""
Format Packets in Scapy (FPIS)

a script to take a packet from a PCAP capture file and
show how to generate it in Scapy
"""


import sys


from scapy.all import *


def scapyformat(path, packetno):
    """
    use the rdpcap function to read the packets from a PCAP file

    Note:
        we subtract 1 to the packet no as they are numbered from 0 in Scapy but
        numbered from 1 in Wireshark

    Args:
        path(str): full path to the PCAP file to read from
        packetno(str): the packet number in the PCAP file

    Returns:
        scapyformat(str): string showing how to create the packet with Scapy
    """
    packets = rdpcap(path)
    scapyformat = packets[int(packetno)-1].command()
    return scapyformat


if len(sys.argv) != 3:
    print("usage ./fpis.py <full path to pcap file> <packet no>")
    sys.exit(0)
print("generating packet stand by............")
SCAPYPACKET = scapyformat(sys.argv[1], sys.argv[2])
print("\n" + SCAPYPACKET + "\n")
